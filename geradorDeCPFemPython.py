"""
Exercício Gerador de CPFs - aula 49
"""

while True:

    from random import randint
    numero = str(randint(100000000, 999999999))

    fatorMult1 = 10
    valorSoma1 = 0
    fatorMult2 = 11
    valorSoma2 = 0

    cpfCalculo = numero

    for i in cpfCalculo:
        valorSoma1 = valorSoma1 + (int(i) * fatorMult1)
        fatorMult1 -= 1
        # print(valorSoma1)

    primeiroDigito = 11 - (valorSoma1 % 11)

    if primeiroDigito > 9:
        primeiroDigito = 0

    # print(f'O valor do primeiro digito verificador é {primeiroDigito}')

    cpfCalculo = cpfCalculo + str(primeiroDigito)

    for j in cpfCalculo:
        valorSoma2 = valorSoma2 + (int(j) * fatorMult2)
        fatorMult2 -= 1
        # print(valorSoma2)

    segundoDigito = 11 - (valorSoma2 % 11)

    if segundoDigito > 9:
        segundoDigito = 0

    # print(f'O valor do segundo digito verificador é {segundoDigito}')

    cpfCalculo = cpfCalculo + str(segundoDigito)

    print(f'O CPF gerado é {cpfCalculo}')

    break
