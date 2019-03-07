import types
from flask import Flask
from flask import request, abort
from owlready2 import get_ontology, destroy_entity


def init_onto():
    # TODO Read the docs / code of owlready to understand how to do a
    # re-initialization of the ontology. Meanwhile, be careful to the ordering
    # of the tests!
    onto = get_ontology("file://onto/company.owl").load()
    return onto


onto = init_onto()
app = Flask(__name__)


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


@app.route('/companyontology/concepts', methods=['GET'])
def download_ontology():
    # TODO Check how to avoid this tmp file
    onto.save(file="onto/company-tmp.owl")
    with open("onto/company-tmp.owl") as f:
        owl_txt = f.read()
    return owl_txt


if __name__ == '__main__':
    app.run(debug=True)
