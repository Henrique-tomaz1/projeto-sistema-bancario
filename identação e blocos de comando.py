def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor Sacado!")
        print("Retire seu Dinheiro na boca do caixa.")
    if saldo <= valor:
        print("seu saldo é inferior ao valor solitado.")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")



sacar(200)