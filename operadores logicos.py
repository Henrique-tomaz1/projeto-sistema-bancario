#AND É IGUAL E
#OR É IGUAL OU

# OPERADOR DE NEGAÇÃO
#NOT = NEGAÇÃO INVERTER A VERDADE,

#PARENTESES
#servem para delimitar a precedencia 

#na condição AND para ser true tem que ser true 
#no OR para ser true apenas um tem que ser true

print(True and True and True)
print(True and False and True)
print(True or True and False)
print (True or True and True)


saldo = 1000
saque = 250
limite = 200
conta_especial = True



exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print (exp3)