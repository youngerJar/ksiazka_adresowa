from faker import Faker
fake = Faker("pl_PL")

class card:
    def __init__(self,first_name, last_name, email, tel_priv,phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tel_priv = tel_priv
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"

    def __repr__(self):
        return f"card(first_name= {self.first_name} last_name= {self.last_name}, email={self.email}"

    def contact(self):
        return f"Wybieram numer prywatny : {self.tel_priv} i dzwonię do  {self.first_name} {self.last_name}"

    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])

class BusinessContact(card):
    def __int__(self,position, company_name,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company

    def workcontact(self):
        return f"Wybieram numer firmowy : {self.tel_priv} i dzwonię do {self.first_name} {self.last_name}"

    def create_contacts(self):
        x = input("Wybierz rodzaj wizytówki: Biznesowa czy Prywatna ")
        y = int(input("Ilość Wizytówek: "))


        if x =="Prywatna":
            print("Super więc już zabieram się za przygotowanie dla Ciebie tylu wizytówek: ", y, "szt")
            return f"{fake.first_name()} {fake.last_name()}, Twój numer to: {fake.phone_number()}," \
                   f" a Twój adres e-mail to: {fake.email()}"


        if x =="Biznesowa":
            print("Super więc już zabieram się za przygotowanie dla Ciebie tylu wizytówek: ", y, "szt")
            print(fake.company())
            return f"{fake.first_name()} {fake.last_name()}, Twój numer służbowy to: {fake.phone_number()}" \
                   f" służbowy e-mail {fake.email()}. Twoje stanowisko: {fake.job()}"


print(BusinessContact.create_contacts(BusinessContact))
person1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),
              email=fake.email(), tel_priv=fake.phone_number(),phone=fake.phone_number())
print("-"*20)
print(fake.company())
print(person1.contact())
print(person1.workcontact())
print(person1.label_length())





