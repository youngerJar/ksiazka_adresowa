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
        
for firm in range(5):
    print(fake.first_name(), fake.last_name(),fake.email())


