matriz = [         #Exemplo 3x3, sempre começa com 0 1 2 
    [1, "a", 2],
    ["b", 3, 4],         
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2] #recuperar a linha com 1 [0] 
print(matriz[0][0])  # 1 # representação de linha e coluna, primeiro linha depois coluna
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
print(matriz[1][0]) # b