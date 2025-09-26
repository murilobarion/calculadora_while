'''

Calculadora com While

'''


while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = False

    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numero_validos = True

    except:
        numero_validos = False

    if numero_validos == False:
        print('\nUm dos números nao são válidos \n')
        continue

    operador_permitido = "+-/*"

    if operador not in operador_permitido:
        print('Operador Inválido')
        continue

    if len(operador) >1:
        print('Digite apenas um operador')
        continue


    print('Realizando sua conta. Confira os resultados abaixo:\n ')
    if operador == '+':
        print(numero_1_float + numero_2_float)

    elif operador == '-':
        print(numero_1_float - numero_2_float)

    elif operador == '*':
        print(numero_1_float * numero_2_float)

    elif operador == '/':
        print(numero_1_float / numero_2_float)



    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

print('Você saiu')