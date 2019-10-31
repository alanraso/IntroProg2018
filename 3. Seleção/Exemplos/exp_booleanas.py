# Expressão numérica
num = 3 + 5 * 6 + 7 / (6 + 1) - 45

# --------------------
# Expressões booleanas
# --------------------
print('Expressões booleanas')
comparacao = 3 > 1
print(comparacao)
print(type(comparacao))

comparacao = 3 < 1
print(comparacao)
print(type(comparacao))

# É possível usar variáveis
print('Usando variável')
num = 40
comp = num > 60
print(comp)
print(type(comp))

# Comparadores
print('Comparadores')
num = 40
comp_maior = num > 40
comp_menor = num < 40
comp_menor_igual = num <= 40
comp_maior_igual = num >= 40
comp_igual = num == 40  # Não confundir com o =
comp_diferente = num != 40

# Operadores

num = 40

# and  - "e" - Uma coisa e outra
print('and - Uma coisa e outra')
op_e = num > 20 and num < 60
print(op_e)
op_e = num > 50 and num < 60
print(op_e)
op_e = num > 20 and num < 30
print(op_e)
op_e = num > 50 and num < 30
print(op_e)

# or  - "ou" - Uma coisa ou outra
print('or - Uma coisa ou outra')
op_or = num > 20 or num < 60
print(op_or)
op_or = num > 50 or num < 60
print(op_or)
op_or = num > 20 or num < 30
print(op_or)
op_or = num > 50 or num < 30
print(op_or)

# not  - o oposto
print('not - o oposto')
print(num < 5)
print(not num < 5)

# Expressoes booleanas VS. valores
print('' and 3)
print('' or 3)

print(0 and 'Ola')
print(0 or 'Ola')

print(1 and 3)
print(1 or 3)