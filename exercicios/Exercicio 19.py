# Um professor quer 
# sortear um de seus 4 alunos para sortear o quadro, faça um programa que ajude ele.

from random import choice

nomes = ['Rafael', 'lucas', 'antonio', 'gabriel']
nome_aleatorio = choice(nomes)
print(nome_aleatorio)