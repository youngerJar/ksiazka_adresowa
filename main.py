import faker.providers.date_time
from faker import Faker
fake = Faker("pl_PL")

class card:
    def __init__(self,first_name, last_name, email,tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tel_priv = tel_priv

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"

    def __repr__(self):
        return f"card(first_name= {self.first_name} last_name= {self.last_name}, email={self.email}"

    def contact(self):
        return f"Wybieram numer prywatny : {self.tel_priv} i dzwonię do  {self.first_name} {self.last_name}"

    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])

class BusinessContact(card):
    def __int__(self,position, company_name, tel_work,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.tel_work = tel_work

    def workcontact(self):
        return f"Wybieram numer firmowy : {self.tel_work} i dzwonię do {self.first_name} {self.last_name}"


person1= card(first_name=fake.first_name(),last_name=fake.last_name(),email= fake.email(),tel_priv=fake.phone_number())

print(person1.contact())
