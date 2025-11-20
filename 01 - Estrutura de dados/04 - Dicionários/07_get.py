contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Acessando uma chave que não existe
# contatos["chave"]  # KeyError - não é a melhor forma de acessar uma chave que não sabemos se existe

# Usando o .get() é possível receber None caso a chave não exista 
resultado = contatos.get("chave")  # None 
print(resultado)

# Ou, ainda melhor, atribuir um valor de retorno caso ela não exista, no caso abaixo "{}""
resultado = contatos.get("chave", {})  # {}
print(resultado)

# Mesmo usando um valor de retorno default, o método .get() retorna o valor correto caso ele exista
resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
