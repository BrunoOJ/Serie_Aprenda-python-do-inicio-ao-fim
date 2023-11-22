'''
PYTHON_NUMEROS_T1_EP8 - Como utilizar as converões numéricas e arredondamentos
no python.

'''

# int(): Converte float para inteiro.
num_float = 10.5
num_int = int(num_float)
print(num_int)


# float(): Converte inteiro para float.
num_int = 5
num_float = float(num_int)
print(num_float)


# complex(): Converte inteiros para número complexo.
num1_int = 3
num2_int = 4
num_complex = complex(num1_int, num2_int)
print(num_complex)


# round(): Arredonda o número para o inteiro mais próximo ou para uma quantidade específica de casas decimais.
num_float = 3.7345
print(round(num_float))    
print(round(num_float, 1))
print(round(num_float, 3))


