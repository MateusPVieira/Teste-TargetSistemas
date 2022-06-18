import math
"""
O código previne a entrada de valores inválidos.
Confere quantos algorismos o valor iserido possui para gerar somente a parte necessária da sequência de Fibonacci.
Em seguida confere se o valor esta dentro do array de valores gerados e retorna uma mensagem de acordo com o resultado.
"""

def input_value():
    while True:
        inputedValue = input('Digite um número: ')
        try:
            inputedValue = int(inputedValue)
        except:
            print('Digite um valor válido!')
        else:            
            if inputedValue < 0:
                print('Digite um valor maior ou igual a 0!')
            else:
                number_size(inputedValue)
                break

        

def number_size(number):
    if number > 0:
        digits = int(math.log10(number))+1
    elif number == 0:
        digits = 1
    fibonacci_sequence(number, digits)


def fibonacci_sequence(number, digits):
    fibNumbers = [0, 1]
    n = 1
    while True:
        nextNumber = fibNumbers[n-1] + fibNumbers[n]
        fibNumbers.append(nextNumber)
        print(nextNumber)
        n += 1
        if(int(math.log10(nextNumber))+1 > digits):
            break
    is_fibonacci(number, fibNumbers)



def is_fibonacci(number, fibNumbers):
    print(fibNumbers)
    if number in fibNumbers:
        print(f'{number} está na sequência de fibonacci')
    else:
        print(f'{number} não está na sequência de fibonacci')


input_value()