'''
PYTHON_NUMEROS_T1_EP7 - Como utilizar as operações matemática no python .

'''
# Soma
num1 = 10
num2 = 3
resp = num1 + num2
print("Soma: ", resp)


# Subtração
num1 = 10
num2 = 3
resp = num1 - num2
print("Subtração: ", resp)


# Multiplicação
num1 = 10
num2 = 3
resp = num1 * num2
print("Multiplicação: ",resp)


# Divisão - retorna um número float
num1 = 10
num2 = 3
resp = num1 / num2
print("Divisão: ",resp)


# Divisão de inteiros (descarta a parte decimal).
num1 = 10
num2 = 3
resp = num1 // num2
print("Divisão: ", resp)


# Retorna o resto da divisão inteira.
num1 = 10
num2 = 3
resp = num1 % num2
print("Resto da divisão: ",resp)


# divmod(): Retorna o quociente e o resto da divisão entre dois números.
dividendo = 10
divisor = 3
quociente_e_resto = divmod(dividendo, divisor)
print("Quociente e Resto: ", quociente_e_resto)


# Exponenciação.
base = 10
expoente = 3
resp = base ** expoente
print("Exponenciação: ",resp)


# pow(): Retorna o resultado de elevar um número à potência de outro número.
base = 10
expoente = 3
resp = pow(base, expoente)
print("Potência: ",resp)

