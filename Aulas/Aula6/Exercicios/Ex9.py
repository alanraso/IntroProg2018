def primo(n):
  if n == 1:
    return False

  for i in range(2, n):
    if n % i == 0:
      return False

  return True

soma = 0

for i in range(1, 1000):
  if primo(i):
    soma += i

print(soma) # 76127