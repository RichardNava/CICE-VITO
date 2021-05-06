
#! Ejercicio 14: Crear una clase país attr--> name, capital, population
#! Ejercicio 15: Convertir TODOS los países en un objeto y luego podamos acceder a un atributo de clase y nos indique la población total

class Country:
    populationTotal = 0

    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        Country.populationTotal += population

    def __str__(self):
        return f'''Nombre: {self.name}, Capital: {self.capital}, Población: {self.population}'''

    def __repr__(self): #? Dunder que se utilizapor defecto en los iterables de un objeto
        return f'''Country({self.name}, {self.capital}, {self.population}'''