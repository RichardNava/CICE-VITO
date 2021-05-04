
#! Ejercicio 5: Crear una clase de tipo municipality/municipio
#!      Debe tener tantas propiedas como claves en el diccionario

class Municipality:
#! Ejercicio 11: Crea un contador de modo que cada vez que se cree una nueva instancia, el mencionado contador aumente en 1
    count = 0

    def __init__(self, density, mun_name, surface):
        self.mun_name = mun_name
        self.density = density
        self.surface = surface

        Municipality.count += 1

#! Ejercicio 7: Modificar el tipo de impresión (print) para que se vea así --> nombre: valor densidad: float con tres decimales superficie: float con tres decimales
    def __str__(self):
        return f'''Nombre: {self.mun_name}, Densidad: {round(self.density,3)}, Surface: {self.surface}'''

    def __repr__(self): #? Dunder que se utilizapor defecto en los iterables de un objeto
        return f'''Municipality({self.mun_name}, {self.density}, {self.surface}'''

#! Ejercicio 9: Considerando que en cada objeto tenemos la superficie y densidad ambas por km2, crear un MÉTODO (una función dentro del objeto) que devuelva la población total del municipio dado

    def population(self):
        return self.density*self.surface