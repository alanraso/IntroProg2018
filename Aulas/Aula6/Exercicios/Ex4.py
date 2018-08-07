# Escrever primeiro sem a função para fins didático

def vogal(caractere):
  return caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u'

frase = input('Digite a frase:\n')
frase_a = ''

for char in frase:
  if vogal(char):
    frase_a += 'a'
  else:
    frase_a += char

print(frase_a)

