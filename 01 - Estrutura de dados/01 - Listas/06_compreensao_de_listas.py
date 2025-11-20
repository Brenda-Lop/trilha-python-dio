# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)



# Forma extensa de fazer loop
lista = []

for n in range(10):
    if n % 2 == 0:
        if n > 6:
             lista.append(n**2)
        else:
            lista.append(n)
    
print(f"LISTA: {lista}") # LISTA: [0, 2, 4, 6, 64]


# Forma curta (list comprehension)
resultado_curto = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(f"RESULTADO_CURTO: {resultado_curto}") # [0, 2, 4, 6, 64]