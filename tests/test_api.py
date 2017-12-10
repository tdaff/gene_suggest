"""Test API from other side of flask."""

from flask import url_for
# All tests use flask app fixture, defined in conftest.py


def test_api_query(app, client):
    """Test query through flask API"""
    test_query = 'brc'
    expected_suggestions = ['BRCA1', 'BRCA2', 'BRCC3', 'BRCC3P1']

    url = url_for('query_gene_suggest', query=test_query)
    assert '/gene_suggest/{}'.format(test_query) in url

    res = client.get(url)
    assert res.status_code == 200
    for suggestion in expected_suggestions:
        assert suggestion in res.json['gene_suggest']


def test_api_query_species(app, client):
    """Test limiting by species through API"""
    test_query = 'ab'
    test_species = 'homo_sapiens'

    url_all = url_for('query_gene_suggest', query=test_query)
    url_species = url_for('query_gene_suggest', query=test_query,
                          species=test_species)

    assert url_species != url_all
    assert 'species={}'.format(test_species) in url_species

    res_species = client.get(url_species)
    assert res_species.status_code == 200
    res_all = client.get(url_all)
    assert res_all.status_code == 200

    assert all([result in res_all.json['gene_suggest']
                for result in res_species.json['gene_suggest']])
    assert (len(res_species.json['gene_suggest']) <
            len(res_all.json['gene_suggest']))


def test_api_query_limit(app, client):
    """Test limiting by number through API"""
    test_query = 'ag'
    test_limit = 10

    url_all = url_for('query_gene_suggest', query=test_query)
    url_limit = url_for('query_gene_suggest', query=test_query,
                        limit=test_limit)

    assert url_limit != url_all
    assert 'limit={}'.format(test_limit) in url_limit

    res_limit = client.get(url_limit)
    assert res_limit.status_code == 200
    res_all = client.get(url_all)
    assert res_all.status_code == 200

    assert len(res_limit.json['gene_suggest']) == test_limit
    assert (len(res_limit.json['gene_suggest']) <
            len(res_all.json['gene_suggest']))
    assert all([result in res_all.json['gene_suggest']
                for result in res_limit.json['gene_suggest']])


def test_404_error(app, client):
    """Non existing URL."""
    test_url = 'nothing_here'

    res = client.get(test_url)
    assert res.status_code == 404
