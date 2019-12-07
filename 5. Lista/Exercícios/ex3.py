numeros = []
dig = int(input('Digite um inteiro: '))

while dig != 0:
  numeros.append(dig)
  dig = int(input('Digite um inteiro: '))

for num in numeros:
  if num % 2 == 0:
    print(num)
