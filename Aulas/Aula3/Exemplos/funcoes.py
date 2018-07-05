# Função simples (exlicar identação)
def imprime_oi():
  print('oi')

imprime_oi()

# Função com parâmetro
def imprime_duas_vezes(palavra):
  print(palavra)
  print(palavra)

imprime_duas_vezes('Ola')

# Função mais parâmetros
def imprime_com_virgula(p1, p2, p3):
  print(p1 + ',' + p2 + ',' + p3)

imprime_com_virgula('alo', 'ola', 'ole')

# Função com retorno
def converte_para_segundos(horas):
  return horas*60*60

segundos = converte_para_segundos(3)
print(segundos)

# Como fica o print e o type delas?
print(converte_para_segundos)
print(converte_para_segundos(3))
print(type(converte_para_segundos))
print(type(converte_para_segundos(3)))

# E os tipos de parametros?
imprime_duas_vezes('Palavraaa')
imprime_duas_vezes(4)
imprime_duas_vezes(4.0)
imprime_duas_vezes(True)
