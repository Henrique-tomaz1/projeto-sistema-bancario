

#colocar tudo em função


def menu ():
    menu_texto = """ 
###### Seja bem vindo####

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

#  Depositar

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato +=f"deposito:\t R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        
        else:
            print("\n@@@ Operação falhou! O Valor infomrado é invalido!@@@")
            
            return saldo, extrato
        

def sacar(*, Saldo, valor, extrato, limite, numero_saques, limite_saques):
 while True:
#     opcao = input(menu)

#     if opcao == "1":
#         valor = float(input("Qual valor deseja depositar? "))

        if valor > 0:

            saldo += valor
            extrato += f"Deposito realizado {valor:.2f}\n"

    elif opcao == "2":
        saque = float(input("Qual valor deseja sacar? "))
            
        excedeu_limite = saque > saldo

        excedeu_saque = numero_saque <= 0

        Excedeu_valor_maximo_saque = saque > saque_maximo

        if excedeu_limite:
            print(f"Você excedeu seu limite, seu saldo é R${saldo:.2f}")
        
        elif excedeu_saque:
            print("Você excedeu o numero de saques! ")
        
        elif Excedeu_valor_maximo_saque:
            print("você excedeu o valor maximo de saque! ")

        elif saque > 0:
            saldo -= saque
            numero_saque -= 1
            extrato += f'Saque de R$ {saque}\n'

        else:
            print("OPção falhou, tente novamente mais tarde!")

    elif opcao == "3":
        print("\n ############ Extrato ##########\n")
        print(f'{extrato}\n seu saldo atual é {saldo}\n')
        print("############### Obrigado! #########")

    elif opcao == "4":
        print("Obrigado, volte sempre")
        break

    else:
        print("Opção invalida, tente novamente.")
    

        







