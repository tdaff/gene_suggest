"""
Flask app serves the API.

"""

from flask import Flask
from flask import render_template, jsonify, request

from gene_suggest.interface import get_suggestions

# Flask
app = Flask(__name__)


# Demo page
@app.route('/')
def view_demo():
    """Simple page with interactive demo."""
    return render_template('demo.html', url='localhost')  # TODO: fix url?


# Current version of the API
@app.route('/gene_suggest/<string:query>', methods=['GET'])
# Fixed, versioned API for legacy systems in the future
@app.route('/v1.0/gene_suggest/<string:query>', methods=['GET'])
def query_gene_suggest(query=''):
    """Return suggested completions from the partial gene name.

    Parameters
    ----------
    query: str
        The partial query as input by the user.

    Returns
    -------
    gene_suggest: json
        The list of suggestions as serialised JSON.

    """

    species = request.args.get('species', default=None, type=str)
    limit = request.args.get('limit', default='', type=int)

    suggestions = get_suggestions(query, species, limit)
    return jsonify(suggestions)


# Have main handle any extra arguments from
# environment at runtime
def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
