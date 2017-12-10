"""
API testing.

Define a query and the expected response.

"""

# TODO: use a fixed db source that will not change and works offline

from gene_suggest.interface import get_suggestions


def test_live_db():
    """Test that the system works with the live database."""
    # Details for the database have been provided in the instructions
    # test that the output is as expected for the live system

    test_query = 'brc'
    expected_suggestions = ['BRCA1', 'BRCA2', 'BRCC3', 'BRCC3P1']

    results = get_suggestions(test_query)

    # Ensure all expected suggestions are present
    # results may not always be the same if database is changed
    for suggestion in expected_suggestions:
        assert suggestion in results

    for result in results:
        assert test_query.lower() in result.lower()


def test_query_with_species():
    """Test that using species gives different results."""
    # make the same query with and without a species argument
    # results should be a subset
    test_query = 'ab'
    test_species = 'homo_sapiens'

    results_all = get_suggestions(test_query)
    results_species = get_suggestions(test_query, species=test_species)

    assert all([result in results_all for result in results_species])
    assert len(results_species) < len(results_all)


def test_query_with_limit():
    """Test that limit will give only up to the maximum number
    of results"""
    test_query = 'ag'
    test_limit = 10
    test_limit_big = 10**6  # all results

    results_all = get_suggestions(test_query)
    results_limit = get_suggestions(test_query, limit=test_limit)
    results_limit_big = get_suggestions(test_query, limit=test_limit_big)

    # with limit is a subset
    assert len(results_limit) == test_limit
    assert len(results_limit) < len(results_all)
    assert all([result in results_all for result in results_limit])
    # high limit should be the same as no limit
    assert sorted(results_limit_big) == sorted(results_all)


#TODO test failure
# pytest raises

