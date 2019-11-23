def primo(n):
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      return False
  return True

n = int(input('Digite um inteiro: '))
cont = 0

for k in range(2, n + 1):
  if primo(k):
    cont += 1

print(f'Entre 1 e {n} existem {cont} números primos.')
