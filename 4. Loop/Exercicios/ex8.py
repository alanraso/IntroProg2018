def quadrado_perfeito(n):
  for i in range(0, n // 2 + 1):
    if i ** 2 == n:
      return True
  return False

soma = 0
for n in range(0, 1000):
  if quadrado_perfeito(n):
    soma += n

print(soma)