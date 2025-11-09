saldo = 0
limite = 300
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo+= valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print ("\n Deposito Realizado com Sucesso!")
    else: 
        print("\n Deposito falhou")