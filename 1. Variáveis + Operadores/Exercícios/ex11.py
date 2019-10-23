# 13. Numa sorveteria, o vendedor estimou seu gasto mensal com energia
# elétrica, água, limpeza e outras despesas como sendo em média cerca
# de R$ 1800,00 / mês. Supondo que ele lucre R$2,00 por bola de sorvete
# que ele vender, escreva um programa que recebe como entrada o lucro
# desejado pelo sorveteiro em 1 ano e imprime na tela quantas bolas de
# sorvete ele deve vender para isso.

gasto_anual = 1800 * 12
lucro = float(input('Olá, sorveteiro! Digite o lucro desejado: '))
bolas_sorvete = (lucro + gasto_anual) / 2
print(f'Você deve vender {bolas_sorvete} bolas de sorvete para obter esse lucro em 1 ano.')
