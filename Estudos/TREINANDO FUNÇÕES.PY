# def calcular_total(numeros):
#     return sum(numeros)

# def retorna_antecessor_e_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero +1

#     return antecessor, sucessor

# calcular_total([10, 20, 34])
# retorna_antecessor_e_sucessor(10)

# def hello_word(nome, idade):

#     return f"Hello Word, welcome {nome}, você tem {idade}"

# saudacao = hello_word("Henrique","28")
# print(saudacao)


# def somar_numeros(num1, num2):
#     return num1 + num2

# soma_total = somar_numeros(1,2)

# print(f"A soma dos numeros é {soma_total}")

# def media_notas(num1, num2, num3):
#     return (num1 + num2 + num3) / 3

# media_final = media_notas(5,3,5)

# print(f"a média das notas é {media_final:.2f}")

# def maior_idade(idade):
#     if idade >= 18:
#         return True
#     else:
#         return False
    
# idade = maior_idade(17)

# if idade:
#     print("Maior de idade")
# else:
#     print("Menor de idade")

# def filtrar_numeros(*numeros):
#     filtrado = list(filter(lambda x: x == 10, numeros))
#     if filtrado:
#         return True
#     else:
#         return False

# resultado = filtrar_numeros(1,10,24,35)

# if resultado:
#     print("Possui o numero 10")
# else:
#     print("Não possui o numero 10")

# def caixa(valor):
#     preco_final = 0.00
#     if valor >= 100:
#         preco_final = valor * 0.85

#     elif 50 <= valor <= 99.99:
#         preco_final = valor *0.90

#     else:
#         preco_final = valor

#     return preco_final

# total_caixa = caixa(90)
# print(f"O valor para pagamento deve ser de {total_caixa:.2f}")


def adicionar_antesdepois(happy):
    def wharper():
        print("antes do parabéns")
        happy()
        print("Depois do parabéns")
    return wharper

@adicionar_antesdepois
def happy():
    print("parabéns")
    
happy()
