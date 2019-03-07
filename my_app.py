import types
from flask import Flask
from flask import request, abort
from owlready2 import get_ontology, destroy_entity


def init_onto():
    # TODO "It is safe to call .load() several times on the same ontology. It
    # will be loaded only once.", accoridng to the doc.  But how to re-init?
    # -> be careful to the ordering of the tests!
    onto = get_ontology("file://onto/company.owl").load()
    return onto


onto = init_onto()
app = Flask(__name__)


@app.route('/companyontology/concepts', methods=['GET'])
def download_ontology():
    pass


@app.route('/companyontology/concepts', methods=['POST'])
def add_concept():
    with onto:
        if "superclassname" in request.form:
            if onto[request.form["superclassname"]]:
                NewClass = types.new_class(request.form["classname"],
                                           (onto[request.form["superclassname"]],))
            else:
                abort(400)  # Bad Request
                print("Superclassname not found")
        else:
            NewClass = types.new_class(request.form["classname"],
                                       (onto["Company"],))

    return request.form["classname"], 201  # Created


@app.route('/companyontology/concepts/<classname>', methods=['DELETE'])
def remove_concept(classname):
    if onto[classname]:
        destroy_entity(onto[classname])
    else:
        return("Class to remove not found")
    return classname


if __name__ == '__main__':
    app.run(debug=True)
