"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = int(input('Digite um numero e direi se ele é par ou ímpar: '))

if numero % 2 == 0:
    print(f'{numero} é par.')
else:
    print(f'{numero} é ímpar.')