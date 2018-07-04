# nota < 3 - reprovado, 3 < nota < 5 - recuperação, nota > 5 - aprovado

# 1
nota = int(input('Digite a nota: '))

if nota < 3:
  print('Reprovado!')
else:
  if nota < 5:
    print('Em recuperação!')
  else:
    print('Aprovado!')

# 2
nota = int(input('Digite a nota: '))

if nota < 3:
  print('Reprovado!')
elif nota < 5:
  print('Em recuperação!')
else:
  print('Aprovado!')