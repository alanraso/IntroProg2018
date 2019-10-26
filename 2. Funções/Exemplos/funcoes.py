# Função sem parâmetro
def imprime_oi():
  print('oi')

imprime_oi()

# Função com parâmetro
def imprime_duas_vezes(palavra):
  print(palavra + palavra)

imprime_duas_vezes('Oi')

# Função com mais parâmetros
def imprime_com_virgula(p1, p2, p3):
  print(f'{p1},{p2},{p3}')

imprime_com_virgula('A', 'B', 'C')

# Função que retorna um valor
def converte_para_segundos(horas):
  print(type(horas))
  return horas * 60 * 60

a = converte_para_segundos(3)
b = converte_para_segundos(2)
print(a)
print(b)

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
