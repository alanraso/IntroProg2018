def vogal(c):
  return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

palavra = input('Digite uma palavra: ')
contador = 0

for c in palavra:
  if vogal(c):
    contador += 1
  
print(f'Tem {contador} vogais.')
