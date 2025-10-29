linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]   #vai ordenar alfabeticamente padrão
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"] #vai ordenar ordem alfabetica espelhada
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]  #ordenar por tamanho da palavra menor p/maior
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"] #ordenar por tamanho maior p/ menor 
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)