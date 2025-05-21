from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  
        self.ingredientes = ingredientes  
        self.pasos = pasos  

# Clase para mostrar las recetas
    @abstractmethod
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

# Función principal
def principal():
    receta_1 = recetas_vegetarianas("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta_2 = recetas_no_vegetarianas("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades_restaurante.imprimir_receta(receta_1)
    utilidades_restaurante.imprimir_receta(receta_2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in receta_1.ingredientes:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in receta_2.ingredientes:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
