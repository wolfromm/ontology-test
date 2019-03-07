# Ontology-test

Quick Rest API to modify an ontology.


## REST API

| Http Method | URI | Action |
| --- | --- | --- |
| POST | http://[host]/companyontology/concepts/[classname, superclassname] | Add a concept |
| DELETE | http://[host]/companyontology/concepts/[classname] | Delete a concept |
| GET | http://[host]/companyontology/concepts/ | Retrieve the ontology in OWL |


## Tests

For the tests we've created a simple ontology with these classes:

Company
-- Bank
---- PrivateBank
---- InvestmentBank
-- Airline

and 10 individuals (AirFrance, Qantas, UBSWealthManagement,...).

Cf. `` for the corresponding OWL file and `` for the generation with `owlready2`.
