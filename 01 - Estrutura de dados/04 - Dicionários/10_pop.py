contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# .pop() - remove o par chave:valor referente à chave passada como argumento e retorna o mesmo
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# Definindo valor de retorno default no caso da chave não existir
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
