# 1. Faça uma que recebe o peso em (kG) e a altura (m) como entrada e calcula o MMC
# 2. Faça um programa que pergunta altura e peso e imprime o MMC

def mmc(altura, peso):
    return  peso/(altura**2)

def main():
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    print('Seu mmc eh: ', mmc(altura, peso))

main()
