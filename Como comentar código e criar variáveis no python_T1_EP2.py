
########### - COMENTARIOS NO CÓDIGO - 

# Comentar uma linha
# Para comentar uma única linha utiliza Hastag(#)




'''
Comentar múltiplas linhas (Docstring)

Esse texto é um comentário. Ele apresenta várias linhas
por isso, utilizamos três aspas simples('''       ''')
ou três aspas duplas ("""      """) no início e no final.

'''

#-------------------------------------------------------------------------
############## - PORQUE UTILIZAR VARIÁVEIS NO PYTHON - ####
# Sem variáveis
print("----- Trecho de código sem variáveis-----")
print("Calculando a soma de 3 e 5 diretamente:", 3 + 5)
print("Calculando o dobro de 7 diretamente:", 2 * 7)
print("Imprimindo 'Hello, World!' diretamente:", "Hello, World!")

print() ## pula uma linha em branco
print() ## pula uma linha em branco

# Com variáveis

print("----- Trecho de código com variáveis-----")
num1 = 5
num2 = 5
num3 = 7
num4 = 25
resultado_soma = num1 + num2
dobro = 2 * num3
mensagem = "Hello, World!"
print("Calculando a soma de 3 e 5 diretamente:", resultado_soma)
print("Calculando o dobro de 7 diretamente:", dobro)
print("Imprimindo 'Hello, World!' diretamente:", mensagem)

# Nomes de variáveis premitido

teste_2 = 0
teste_teste = 0

# Nomes de variáveis que não pode

1teste = 0
teste 1 = 0

#-------------------------------------------------------------------------


#### - TIPOS DE VARIÁVEIS - ########
'''
Em Python, existem vários tipos de variáveis que podem ser usados para armazenar
diferentes tipos de dados.
'''
'''
Inteiro (int): Variáveis do tipo inteiro são usadas para armazenar números inteiros,
positivos ou negativos. Por exemplo:
'''
idade = 25
print("Variável int: ",idade)
'''
Flutuante (float): Variáveis do tipo flutuante são usadas para armazenar números
decimais (utiliza ponto e não virgula). Por exemplo:
'''
altura = 1.75
print("Variável float: ",altura)
'''
String (str): Variáveis do tipo string são usadas para armazenar sequências de
caracteres (entre aspas simples (' ') ou aspas duplas (" "). Por exemplo:
'''
nome = "Se inscreva no canal"
print("Variável str: ",nome)
'''
Booleano (bool): Variáveis do tipo booleano são usadas para armazenar
valores True (verdadeiro) ou False (falso). São frequentemente usadas
em expressões condicionais. Por exemplo:
'''
tem_carro = True
print("Variável bool: ",tem_carro)
'''
Lista (list): Variáveis do tipo lista são usadas para armazenar uma coleção
ordenada de valores, que podem ser de tipos diferentes. Por exemplo:
'''
numeros = [1, 2, 3, 4, 5]
print("Variável list: ",numeros)
'''
Tupla (tuple): As tuplas são semelhantes às listas, mas são imutáveis, ou seja,
seus elementos não podem ser alterados após a criação. Por exemplo:
'''
coordenadas = (3, 4)
print("Variável tuple: ",coordenadas)
'''
Dicionário (dict): Variáveis do tipo dicionário são usadas para armazenar
pares de chave-valor. Cada chave está associada a um valor. Por exemplo:
'''
pessoa = {"nome": "Maria", "idade": 30}
print("Variável dict: ",pessoa)
'''
Conjunto (set): Variáveis do tipo conjunto são usadas para armazenar coleções
não ordenadas de valores únicos. Por exemplo:
'''
numeros_unicos = {1, 2, 3, 4, 5}
print("Variável set: ",numeros_unicos)
'''
Nenhum (None): O tipo None é usado para representar a ausência de valor ou
uma variável vazia. Pode ser útil para inicializar variáveis. Por exemplo:
'''
valor = None
print("Variável None: ",valor)


#-------------------------------------------------------------------------

## - APLICAÇÃO PRÁTICA - ####

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
print("O nome digitado foi:", nome)
print("A idade digitada foi:", idade)
#-------------------------------------------------------------------------



