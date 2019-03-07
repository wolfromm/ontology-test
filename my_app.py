from flask import Flask
from owlready2 import get_ontology


onto = get_ontology("file://onto/company.owl").load()
app = Flask(__name__)


@app.route('/companyontology/concepts', methods=['GET'])
def download_ontology():
    pass


@app.route('/companyontology/concepts', methods=['POST'])
def add_concept():
    pass


@app.route('/companyontology/concepts/<classname>', methods=['DELETE'])
def remove_concept(classname):
    pass


if __name__ == '__main__':
    app.run(debug=True)
