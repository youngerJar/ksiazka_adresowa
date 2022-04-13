from calendar import c
from re import S
from tkinter import N


class address:
    def __init__(self, name, surname, company_name, position, adres):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.adres = adres
        for name in self.name:
            print(self.name,self.surname,",","adres korespodencyjny:",adres)
            break

Flower = address(name="Jan", surname="Kowalski", company_name="Kwiatuszki",position="Dyrektor",adres="Kwiatuszki@o2.pl")
Mug = address(name="Krzysztof", surname="Jerzyna", company_name="Jerzynka", position="Menager", adres="Jerzynki@io.pl")

