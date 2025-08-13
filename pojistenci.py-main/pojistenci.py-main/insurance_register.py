from insured_person import InsuredPerson

class InsuranceRegister:
    def __init__(self):
        self.people = []

    def add_person(self, person: InsuredPerson):
        self.people.append(person)

    def list_all(self):
        return self.people

    def find_person(self, first_name, last_name):
        return [p for p in self.people if p.first_name.lower() == first_name.lower() and p.last_name.lower() == last_name.lower()]
