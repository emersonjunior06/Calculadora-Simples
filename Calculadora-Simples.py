'''

Bom esse codigo eu estou criando por pura zueira 

'''

# Calculadora SIMPLES

# Introdução

print('Olá tudo bem, bom eu fiz essa calculadora de forma intuitiva, e simples')
print('-----------------------------------------------------------------------') \

print('VAMOS COMEÇAR') \

print('-----------------------------------------------------------------------') \

print('ESOLHA ABAIXO O OPERADOR LOGICO DESEJADO: ') \

print('(+) é adição, (-) é subtração, (*) multiplicação, (/) divisão.')

print('-----------------------------------------------------------------------') \


# Resposta de Operador Logico (adição(+), subtração(-), Multiplicação(*), Divisão(/).)


while True:

    operadoresMatematicos = input('DIGITE O OPERADOR LOGICO: ')
    if operadoresMatematicos not in ['+', '-', '*', '/']:
        print('Você não escreveu um operador matemático válido.')
        continue
    print('-----------------------------------------------------------------------') \
    
    quantidades_de_numeros_a_calcular = int(input('Quantos numeros você vai usar para os operadores logícos: '))# Quantos numeros iremos usar para os operadores logícos.

    resultado = 0 

# For e in para fazer as perguntas de quantos numeros a ser usados.

    

    if operadoresMatematicos == '+':
        print('Operador escolhido foi MATEMATICA (+)')
        for cont in range(1,quantidades_de_numeros_a_calcular + 1):
            n = int(input(f'Escreva o {cont}° numero: '))

            resultado += n

    elif operadoresMatematicos == '-':
        
        print('Operador escolhido foi SUBTRAÇÂO (-)')
        n = int(input('Escreva o 1° número: '))
        resultado = n
        for cont in range(2,quantidades_de_numeros_a_calcular + 1):
            n = int(input(f'Escreva o {cont}° numero: '))

            resultado -= n

    elif operadoresMatematicos == '*':
        print('Operador escolhido foi MULTIPLICAÇÂO (*)')
        resultado = 1
        for cont in range(1,quantidades_de_numeros_a_calcular + 1):
            n = int(input(f'Escreva o {cont}° numero: '))

            resultado *= n 

    elif operadoresMatematicos == '/':
        print('Operador escolhido foi DIVISÃO (/)')
        n = int(input('Escreva o 1° número: '))
        resultado = n
        for cont in range(2,quantidades_de_numeros_a_calcular + 1):
            n = int(input(f'Escreva o {cont}° numero: '))

            resultado /= n

    print(f'RESULTADO: {resultado}')


# Abaixo vemos algo para perguntar se o usuario vai querer fazer o codigo 

    continuar = input("Deseja fazer mais algum cálculo? (s/n): ")
    if continuar.lower() != 's':
        break


#for cont in range(1,quantidades_de_numeros_a_calcular):
