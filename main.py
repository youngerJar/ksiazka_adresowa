from audioop import add
from calendar import c
from re import S
from tkinter import N
from unicodedata import name


class Address:
    def __init__(self, name, surname, company_name, position, adres):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.adres = adres
        for name in self.name:
            print(self.name,self.surname,",","adres korespodencyjny:",adres)
            break
    def __str__(self):
        return f'{self.name} {self.surname} {self.adres}'
    def __repr__(self):
        return f"Address(name={self.name} surname={self.surname}, company_name={self.company_name}, adres={self.adres}"
    def __eq__(self, other):
        return all(
            (
                self.name== other.name,
                self.surname == other.surname,
                self.company_name == other.company_name,
                self.adres == other.addres
            )
        )
    def get_make(self):
        return self.name
    lambda self: self.name

Flower = Address(name="Jan", surname="Kowalski", company_name="Kwiatuszki",position="Dyrektor",adres="Kwiatuszki@o2.pl")
Mug = Address(name="Krzysztof", surname="Jezyna", company_name="Jezynka", position="Menager", adres="Jezynki@io.pl")
Desk= Address(name="Sławomir",surname="Allworks", company_name="Desk For You", position="Dyrektor", adres="Deskforyou@o2.pl")
Storczyk = Address(name="Eugeniusz",surname="Kos", company_name="Storczyki",position="Menager",adres="storczyki@121.pl")
people = [Flower, Mug, Desk, Storczyk]

by_name= sorted(people, key=lambda self: self.name)
by_surname= sorted(people, key=lambda self: self.surname)
print(by_name)
print("po nazwisku", by_surname)





