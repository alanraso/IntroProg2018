def imprime_separando(palavra, delimitador, n):
  padrao = palavra + delimitador
  print(padrao * (n - 1) + palavra)

imprime_separando('Ola', '/', 4)
imprime_separando('Pão', ',', 10)
