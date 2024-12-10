"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = ("Que horas são agora?")

horas_int = int(input(horas))
if 0 <= horas_int <= 11:
    print("Bom dia!")
elif 12 <= horas_int <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")