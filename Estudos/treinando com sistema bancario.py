menu_inicial = """"
########### SEJA BEM VINDO ###########

       SELECIONE O TIPO DE CONTA

[1] NORMAL
[2] UNIVERSITARIA

#######################################
"""

tipo_conta = input(menu_inicial)


if tipo_conta == "1":
    print("\nVocê selecionou a conta normal (Com cheque especial)")

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    nome_conta = "normal"


elif tipo_conta == "2":
    print("\n Você selecionou a conta universitaria")

    saldo = 0
    limite = 0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    nome_conta = "universitaria"

else:
    print("Informação invalida, tente novamente...")

menu_operacoes = f"""

########## CONTA {nome_conta} ##########


[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


while True:
    opcao = input(menu_operacoes)

    if opcao == "1":
        valor = float(input("Qual o valor que deseja depositar? "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo_disponivel = saldo + limite

        excedeu_saldo = valor > saldo_disponivel

        excedeu_saque = numero_saques >= limite_saques

        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente, seu saldo é {saldo_disponivel}")

        elif excedeu_saque:
            print("Operação falhou! Seu numero maximo de saques foi excedido\n Seu limite de saque é",limite_saques)
        
        elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            limite_saques = limite_saques -1
        
        else:
            print("Operação falhou! O valor informado é invalido.")
        

    elif opcao == "3":  
        print ("\n==============Extrato============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")

    elif opcao == "4":
        print("\n        Banco Toju Agradece pela parceria")
        print("\n                  Volte sempre                 ")
        break

    else:
        print ("Operação inválida, por favor selecione novamente a opção desejada!") 