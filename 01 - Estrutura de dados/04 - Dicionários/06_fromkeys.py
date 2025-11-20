
# Criando novas chaves sem valores
# Usando dict.fromkeys() cria-se um dicionário novo, mas é possível
# alterar um dicinário existente usando nome-do-dicionario.fromkeys(["chave1", "chave2"])
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# Criando novas chaves com valor padrão
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
