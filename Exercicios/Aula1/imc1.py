# 1. Faça uma que recebe o peso em (kG) e a altura (m) como entrada e calcula o IMC
# 2. Faça um programa que pergunta altura e peso e imprime o IMC

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso/(altura*altura)

print('Seu imc eh: ', imc)
