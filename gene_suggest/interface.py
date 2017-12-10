"""
Interface to the data source. Provides methods to access
data at the source.

"""

import os

from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

# The default ENSEMBL database
DEFAULT_URL = ('mysql+pymysql://anonymous@ensembldb.ensembl.org:3306/'
               'ensembl_website_90')


def get_connection(url=None, env_var='DBURL'):
    """Create a connection to the sql database with sqlalchemy.

    Either pass the URL of the database to connect to, or it will be taken
    from an environment variable. If the environment variable is empty then
    fallback to a default

    Parameters
    ----------
    url : str or None
        sqlalchemy style URL that follows RFC-1738 and encodes all the
        information about the database. Has the form:
            dialect+driver://user:pass@host:port/database
        e.g.
            mysql+pymysql://anonymous@dbexample.org:1234/main_dbase
        If url is None, the URL is pulled from an environment variable.
    env_var : str or None
        Name of the environment variable to check for a url if none
        has been passed as the url argument.

    Returns
    -------
    engine : Engine
        The database engine initialised with the url.
    meta : MetaData
        The metadata associated with the database.
    session : scoped_session
        A session to interact with the database.
    """

    # Grab a url from the environment if not specified explicitly
    if url is None:
        url = os.getenv(env_var, DEFAULT_URL)

    # Use sqlalchemy to interact with the database
    # The ORM adds overhead but allows for fast prototyping
    # and makes expanding the scope much easier than dealing
    # with handwritten sql.
    # More importantly, it is much safer than trying to escape
    # user data manually!
    Session = scoped_session(sessionmaker())
    engine = create_engine(url, pool_recycle=360)  #, echo=True)  # show sql
    meta = MetaData(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    # enough parts to interact with the database
    return engine, meta, session


def get_suggestions(query, species=None, limit=None):
    """Generate auto-completion suggestions based on the query string.

    Matches query as a case insensitive string at the start of
    a gene name, and only for the selected species, if requested.

    Connects automatically to the database.

    Parameters
    ==========
    query : str
        A partial query as input by the user, e.g. `brc`
    species : str
        The name of the target species, e.g. `homo_sapiens`.
        Defaults to all species.
    limit : int
        The maximum number of suggestions to return, e.g. 10.
        Defaults to all results.

    Returns
    =======
    suggestions : list of str
        A list of the suggested auto-completions. List is empty of none
        are found, and will not return more than limit total.
    """
    # auto-connect to the database
    engine, meta, session = get_connection()
    # autoload inspects the schema and builds the ORM from that
    # ensures there is never a mismatch between the code and the
    # target database, and works with multiple database structures.
    gene_autocomplete = Table('gene_autocomplete', meta, autoload=True,
                              autoload_with=engine)
    # shorter names
    display_label = gene_autocomplete.columns.display_label
    species_c = gene_autocomplete.columns.species

    if species is not None:
        # query based on label and species
        c_query = session.query(display_label, species_c)
        # == may not be case insensitive, so use ilike
        c_query = c_query.filter(species_c.ilike(species))
    else:
        # query only on labels, needed for distinct to work
        c_query = session.query(display_label)
    # Case insensitive at beginning of label
    c_query = c_query.filter(display_label.ilike('{}%'.format(query)))

    if limit is not None:
        c_query = c_query.limit(limit)

    # only return unique solutions
    c_query = c_query.distinct()

    # convert query to results
    suggestions = [row.display_label for row in c_query]

    return suggestions

