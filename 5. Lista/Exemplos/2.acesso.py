# Como acessar os elementos de uma lista?
# Para uma lista de tamanho n, índices de 0 a n-1

# Exemplo: lista de tamanho 8: índices de 0 a 7
lista = [40, 5, 8, 5, 1000, 678, 7, 25]

# Primeiro elemento: índice 0
# Para acessar, usar colchetes
print(lista[0]) # 40

# Quarto elemento: índice 3
print(lista[3]) # 123

# Último elemento: índice 7
print(lista[7]) # 25

# Trocando um elemento: índice 4
lista[4] = 21
print(lista[4])
print(lista)

# Tupla - Bem similar, porém imutável (não posso modificar)
tupla = (1, 2, 3, 4)
print(tupla)
print(type(tupla))
# tupla[0] = 2 # Vai dar erro!
