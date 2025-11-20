contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy() # Cria uma cópia - não modifica o dicionário original
print("primeira copia:", copia)
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print("segunda cópia", copia["guilherme@gmail.com"])  # {"nome": "Gui"}
