#f strings
#.format
# %d para numero inteiro e %s para str

nome = "Henrique"
idade = 28
profissao = "Estudante"
linguagem = "Python"
saldo = 45.4545

#print("Olá, me chamo %s. Eu tenho %d anos de idad, trabalho com %s e estou matriculado no curso de %s."(nome, idade, profissao, linguagem))

#print("olá, me chamo {}. eu tenho {}. anos de idade, trabalho com {}. e estou matriculado no curso {}.".format(nome, idade, profissao, linguagem))
#print("olá, me chamo {2}. eu tenho {3}. anos de idade, trabalho com {1}. e estou matriculado no curso {0}.".format(nome, idade, profissao, linguagem))

#print(f"Olá, me chama, {nome}. Eu tenho {idade}. anos de idade, trabalho como {profissao} e estou amtriculado no curso {linguagem}")


#pi = 3.14159
#print(f'Valor de PI: {pi:.2f}') #usar para separar espaço nesse caso tem alterção de 2 casa apos os dois pontos
#print(f'Valor de PI: {pi:10.2f}')# nesse caso tera 10 casas apos os dois pontos

dados = {'nome': 'Henrique', 'idade': 28} 


print('nome: %s idade: %d' %(nome, idade))
print('nome: {} idade: {}' .format(nome, idade))
print('nome: {0} idade: {1}' .format(nome, idade))
print('nome: {nome} idade: {idade}' .format(nome=nome, idade=idade))
print('nome: {name} idade: {age}' .format(name=nome, age=idade))
print('nome: {nome} idade: {idade}.'.format(**dados))
print(f'nome: {nome} idade: {idade}')
print(f'nome: {nome} idade: {idade} Saldo: {saldo:10.2f}')