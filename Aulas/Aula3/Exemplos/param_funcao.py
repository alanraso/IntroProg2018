def imprime_oi():
  print('oi')

def imprime_com_virgula(p1, p2, p3):
  print(p1 + ',' + p2 + ',' + p3)

# Tipo pode ser função!
def executa_duas_vezes(tarefa):
  tarefa()
  tarefa()

executa_duas_vezes(imprime_oi)
# executa_duas_vezes(4)
# executa_duas_vezes('palavra')
# executa_duas_vezes(imprime_com_virgula) -> mostrar o erro