from owlready2 import onto_path, get_ontology, Thing

onto_path.append("onto/")
onto = get_ontology("http://test.org/company.owl")


# Creation of the classes
with onto:
    class Company(Thing):
        pass

    class Bank(Company):
        pass

    class InvestmentBank(Bank):
        pass

    class PrivateBank(Bank):
        pass

    class Airline(Company):
        pass

# Creation of the individuals
airfrance = Airline("AirFrance")
qantas = Airline("Qantas")
ubswm = PrivateBank("UBSWealthManagement")
goldmansachs = InvestmentBank("GoldmanSachs")
creditsuisse = Bank("CreditSuisse")

onto.save()
