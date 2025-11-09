def contagem_regressima (numero):
    while True:
        print (numero)
        numero -= 1
        if numero < 0:
            break

contagem_regressima(5)

def maior_numero (lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = [5, 10, 25, 22, 99]
maior_numero_da_lista = maior_numero(lista)
print(f"O Maior numero da lista é {maior_numero_da_lista}")