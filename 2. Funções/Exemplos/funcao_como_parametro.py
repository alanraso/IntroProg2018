# Parâmetro pode ser uma outra função!
def imprime_oi():
  print('Oi')

def executa_duas_vezes(tarefa):
  tarefa()
  tarefa()

executa_duas_vezes(imprime_oi)
