# Ontology-test

Quick Rest API to modify an ontology.


## REST API

| Http Method | URI | Action |
| --- | --- | --- |
| POST | http://[host]/companyontology/concepts/[classname, superclassname] | Add a concept |
| DELETE | http://[host]/companyontology/concepts/[classname] | Delete a concept |
| GET | http://[host]/companyontology/concepts/ | Retrieve the ontology in OWL |

To add a concept (ie. class), we have to give the name of the new class. The new class will be a subclass of the `Company` class.

It's also possible to indicate that the new class is a subclass of another class. In this case the superclassname should be given.


## Tests

For the tests we've created a simple ontology with these classes:

```
Company
-- Bank
---- PrivateBank
---- InvestmentBank
-- Airline
```

and 10 individuals (AirFrance, Qantas, UBSWealthManagement,...).

See `onto/company.owl` for the corresponding OWL file generated by `create-test-ontology.py` using the library `owlready2`.

You can run the tests to check how the app is working:

> pytest

Or use curl :

> curl http://localhost:5000/companyontology/concepts
> curl -X POST -F 'classname=RetailBank' -F 'superclassname=Bank' http://localhost:5000/companyontology/concepts
> curl -X DELETE http://localhost:5000/companyontology/concepts/Airline

Or [Postman](https://www.getpostman.com/).
