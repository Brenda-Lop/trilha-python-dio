pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# Com essa sintaxe "pessoa["chave"]", se a chave não existir, uma nova é criada com o valor atribuído na declaração,
# se a chave existir e, na declaração, não houver nenhum novo valor atribuído, o valor existente é acessado/resgatado,
# se a chave existir e um novo valor for atribuído, o valor anterior é substituído pelo novo.


# Adicionando uma nova chave "telefone" ao dicionário "pessoa" acima
pessoa["telefone"] = "3333-1234"  
print(pessoa) # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Acessando o valor da chave "nome"
nome_da_pessoa = pessoa["nome"]
print("nome_da_pessoa:", nome_da_pessoa) # nome_da_pessoa: Guilherme

# Atribuindo um novo valor da chave "idade"
nova_idade = pessoa["idade"] = 33 
print("nova_idade:", nova_idade) # nova_idade: 33

print("novo dicionário pessoa", pessoa) # novo dicionário pessoa {'nome': 'Guilherme', 'idade': 33, 'telefone': '3333-1234'}


# As chaves de um dicionário devem ser valores imutáveis, como strings e números
# Listas, por exemplo, não são aceitas como chaves de um dicinário