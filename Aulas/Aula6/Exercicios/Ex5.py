def quadrado_perfeito(n):
  for i in range(0, n+1):
    if i*i == n:
      return True
  return False

n = int(input('Entre com um inteiro: '))
mensagem = 'Os quadrados perfeitos de 1 a ' + str(n) + ' são: '

for i in range(1, n+1):
  if quadrado_perfeito(i):
    mensagem += str(i) + ' '

print(mensagem)