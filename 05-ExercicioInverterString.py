def string_inverter(string):
    c = 0
    newstring = ""
    
    while c < len(string):
        newstring+=(string[(len(string) - 1) - c])
        c +=1 

    print(f'a string "{string}" invertida é: ')
    print(f'{newstring}')
    


string_inverter(input('Insira uma string: '))

