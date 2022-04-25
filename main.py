from calendar import c
from re import S
from tkinter import N
from unicodedata import name


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
    def __str__(self):
        return f'{self.name} {self.surname} {self.adres}'

Flower = address(name="Jan", surname="Kowalski", company_name="Kwiatuszki",position="Dyrektor",adres="Kwiatuszki@o2.pl")
Mug = address(name="Krzysztof", surname="Jezyna", company_name="Jezynka", position="Menager", adres="Jezynki@io.pl")
Desk= address(name="Sławomir",surname="Allworks", company_name="Desk For You", position="Dyrektor", adres="Deskforyou@o2.pl")
Storczyk = address(name="Eugeniusz",surname="Kos", company_name="Storczyki",position="Menager",adres="storczyki@121.pl")

