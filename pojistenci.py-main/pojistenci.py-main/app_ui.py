from insurance_register import InsuranceRegister
from insured_person import InsuredPerson

class AppUI:
    def __init__(self):
        self.register = InsuranceRegister()

    def run(self):
        while True:
            self.show_menu()
            choice = input("Zvolte možnost: ").strip()
            if choice == "1":
                self.add_person_ui()
            elif choice == "2":
                self.list_all_ui()
            elif choice == "3":
                self.find_person_ui()
            elif choice == "4":
                print("Ukončuji aplikaci.")
                break
            else:
                print("Neplatná volba.\n")

    def show_menu(self):
        print("\n----------------------------")
        print("Evidence pojištěných osob")
        print("----------------------------")
        print("1. Přidat nového pojištěného")
        print("2. Zobrazit všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Konec")

    def input_nonempty(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            else:
                print("Tento údaj nesmí být prázdný!")

    def pause(self):
        input("\nData byla uložena. Pokračujte stisknutím tlačítka enter...")

    def add_person_ui(self):
        print("\nZadejte údaje pojištěného:")
        first_name = self.input_nonempty("Jméno: ")
        last_name = self.input_nonempty("Příjmení: ")
        while True:
            try:
                age = int(self.input_nonempty("Věk: "))
                break
            except ValueError:
                print("Věk musí být číslo!")
        phone = self.input_nonempty("Telefon: ")

        person = InsuredPerson(first_name, last_name, age, phone)
        self.register.add_person(person)
        print("Pojištěný byl úspěšně přidán.")
        self.pause()

    def list_all_ui(self):
        print("\nSeznam všech pojištěných:")
        people = self.register.list_all()
        if people:
            for person in people:
                print(person)
        else:
            print("Žádní pojištění nejsou evidováni.")
        self.pause()

    def find_person_ui(self):
        print("\nZadejte jméno a příjmení hledaného pojištěného:")
        first_name = self.input_nonempty("Jméno: ")
        last_name = self.input_nonempty("Příjmení: ")
        matches = self.register.find_person(first_name, last_name)
        if matches:
            print("Nalezeno:")
            for person in matches:
                print(person)
        else:
            print("Pojištěný nebyl nalezen.")
        self.pause()

