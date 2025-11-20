frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

carros = ("gol",) 
print(isinstance(carros, tuple)) # True

carros = ("gol") 
print(isinstance(carros, tuple)) # False - para ser uma tupla, é preciso terminar com ,

carros = ("gol") 
print(isinstance(carros, str)) # True - aqui "gol" é apenas uma string