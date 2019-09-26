print('Print de vaiável (int):')
a = 58
print(a)
print('') # Para pular linha

print('Print composto: texto + variável:')
print('A variável a vale', a)
print('')

print('Print composto: texto + duas variáveis (string):')
b = 21
print('As variáveis a tem b os valores, respectivamente:', a, b)
print('')

print('Print composto: Usando soma de strings:')
print('As variáveis a tem b os valores, respectivamente: ' +  str(a) + ' ' + str(b)) # Tenho que transformar a em string
print('')

print('Print de variáveis usando f-string:')
print(f'A variável a tem o valor {a}')
print(f'As variáveis a tem b os valores, respectivamente: {a} {b}')
print('')

print('Print pulando linha: usar o caractere especial \\n')
print('Texto da linha 1 \nTexto da linha 2 (as duas linhas num mesmo print)')
