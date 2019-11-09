def maior(a, b, c):
  maior = a
  if b > maior:
    maior = b
  if c > maior:
    maior = c
  return maior

print(maior(4, 10, 2))
print(maior(13, 2, 6))

# Forma mais legal
def maior_2(a, b):
  if a > b:
    return a
  return b

def maior_3(a, b, c):
  return maior_2(a, maior_2(b, c))
