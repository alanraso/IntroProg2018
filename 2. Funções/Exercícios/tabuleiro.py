def imprime_tabuleiro(n):
  linha_cheia = '#--' * n + '#'
  linha_buracos = '|  ' * n + '|'
  duas_linhas = linha_cheia + '\n' + linha_buracos + '\n'
  print(duas_linhas * n + linha_cheia)

imprime_tabuleiro(7)
