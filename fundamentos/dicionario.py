dicionario = {"chave": "valor"}
print(type(dicionario))

pessoa = {"nome": "Devison", "idade": 32, "cursos": ["Git", "Python"]}
print(pessoa)
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa["cursos"][0])
print(pessoa.get('cursos', "teste"))
del pessoa['idade']
print(pessoa)
pessoa['idade'] = 32
pessoa['sexo'] = "M"
print(pessoa)
pessoa['cursos'].append("Angular")
print(pessoa)
pessoa.clear()
print(pessoa)
pessoa.update({"level": "pleno"})
print(pessoa)
