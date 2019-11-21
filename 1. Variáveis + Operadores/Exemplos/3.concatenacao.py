a = 'abc'
b = 'cde'
c = 2

## Concatenando strings
print('Concatenando:')

# print(a + 2) # Erro: Só pode concatenar strings
print(a + '2')
print(a + b)
# print(a + c) # Erro: Só pode concatenar strings
print(a + str(c))
print('O valor de c é: ' + str(c))
print('O valor de c é:', c)

## "Multiplicando" strings
print('------------------')
print('Multiplicando:')

print(a * 3)
# print(a * b) # Dá erro

## f-strings
print('------------------')
print('f-strings:')

print(f'O valor de a é {a} e o valor de c é {c}')
print(f'O valor de a é {a}.\nO valor de c é {c}.') # \n => quebra linha
