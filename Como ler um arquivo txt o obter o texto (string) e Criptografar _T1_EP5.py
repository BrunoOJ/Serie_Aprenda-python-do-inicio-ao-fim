'''
PYTHON_STRING_T1_EP5 - Ler arquivo txt para obter o texto (string)

'''

diretorio = "texto_string.txt"
texto = open(diretorio,'r', encoding='utf-8').readline()
print(texto)

tabela = str.maketrans("abcdefghijklmnopqrstuvwxyz", "qwertyuiop123456789asdfghj")
texto_cript = texto.translate(tabela)
print(texto_cript)

##arq = open("texto_criptografado.txt", 'w')
##arq.write(texto_cript)
##arq.close()
##
##
##diretório = "texto_criptografado.txt"
##texto = open(diretório,'r').readline()
##print(texto)
##
##tabela = str.maketrans("qwertyuiop123456789asdfghj", "abcdefghijklmnopqrstuvwxyz")
##texto_descript = texto.translate(tabela)
##print(texto_descript)


