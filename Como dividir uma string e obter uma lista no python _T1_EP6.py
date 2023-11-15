'''
PYTHON_STRING_T1_EP6 - Como dividir uma string e obter uma lista no python.

'''



# partition(sep): Divide a string em uma tupla (antes, separador, depois) com base no separador especificado.
texto = "Python é uma linguagem de programação"
print(texto.partition("é"))

### rsplit([sep[, maxsplit]]): Divide a string em uma lista de substrings usando o separador especificado, começando pela direita.
##texto = "maçã, laranja, banana"
##frutas = texto.rsplit(", ")
##print(frutas)
##
### split(): Divide a string em uma lista de substrings com base em um separador.
##texto = "maçã, laranja, banana"
##frutas = texto.split(", ")
##print(frutas)
##
### splitlines([keepends]): Divide a string em uma lista de linhas, mantendo ou não os caracteres de quebra de linha.
##texto = """linha 1 
##linha 2 
##linha 3
##"""
##linhas = texto.splitlines()
##print(linhas)
##
##
### replace(): Substitui um determinado caractere ou sequência de caracteres por outro.
##texto = "Olá, mundo!"
##novo_texto = texto.replace("mundo", "Planeta Terra")
##print(novo_texto)
