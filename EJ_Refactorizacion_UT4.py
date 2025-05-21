from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  
        self.ingredientes = ingredientes  
        self.pasos = pasos  

# Clase para mostrar las recetas
    def mostrar(self):
        print("Ingredientes:")
        for ing in self.ingredientes:
            print(f"- {ing}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")



# Clase para recetas vegetarianas
class recetas_vegetarianas(receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")


# Clase para recetas no vegetarianas
class recetas_no_vegetarianas(receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.nombre}")


# Clase con utilidades del restaurante
class utilidades_restaurante:
    @staticmethod
    def imprimir_receta(r):
        print("====================================")
        r.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")
    
def crear_receta():
    nombre = print("Dime el nombre de la receta: ")
    ingrediente = []
    print("introduce los ingredientes, cuando hayas terminado de escribir los ingredientes escribe fin")
    while True:
        ing = input("- ")
        if ing.lower() == "fin":
            break
        ingrediente.append(ing)
    pasos = []
    print("introduce los pasos, escribe fin cuando termines de escribir los pasos")  
    while True:
        paso = input("- ")
        if paso.lower() == "fin":
            break
        pasos.append(paso)
    return nombre, ingrediente, pasos
# Función principal
def principal():

    nombre, ingrediente, pasos = crear_receta()
    tipo = input("¿Qué tipo de receta quieres crear? vegetariana/no vegetariana: ")

    if tipo == "vegetariana":
        print("-Crear receta vegetariana-")
        receta_1 = recetas_vegetarianas(nombre, ingrediente, pasos)
    elif tipo == "no vegetariana":
        print("-Crear receta no vegetariana-")
        receta_2 = recetas_no_vegetarianas(nombre, ingrediente, pasos)
    else: 
        print("Datos introducidos incorrectos")   


# Ejecutar el programa
if __name__ == "__main__":
    principal()
