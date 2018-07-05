despesa_anual = 12*1800
lucro_desejado = float(input('Olá sorveteiro, digite o lucro desejado (em R$): '))
bolas_de_sorvete = (lucro_desejado + despesa_anual)/3
print('Você deve vender',  int(bolas_de_sorvete), 'bolas de sorvete.')
