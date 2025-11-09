linguagens = ["python", "js", "c", "java", "csharp"] #função buildIN ordena interaveis IGUAK SORT SÓ QUE FUNÇÃO

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

