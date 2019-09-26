a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

maior = a

if b > maior:
  meio = maior
  maior = b
else:
  meio = b

if c > maior:
  menor = meio
  meio = maior
  maior = c
elif c > meio:
  menor = meio
  meio = c
else:
  menor = c

print(menor, meio, maior)
