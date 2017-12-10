"""
API testing.

Define a query and the expected response.

"""

# TODO: use a fixed db source that will not change

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


#TODO test failure
# pytest raises

