n = int(input('Digite o numero: '))
d = int(input('Digite o digito: '))

cont = 0

if n % 10 == d:
  cont += 1

if n // 10 % 10 == d:
  cont += 1

if n // 100 == d:
  cont += 1

print('O digito', d, 'ocorre', cont, 'vezes')