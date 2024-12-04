#Calculadora de IMC

nome = (input('Qual seu nome? '))
altura = float(input('Qual sua altura? '))
peso = float(input('Qual sua peso? '))

#Apresentação
imc = peso / (altura ** 2)

print ({nome}, 'tem', {altura}, 'de altura.')
print ('Pesa', peso ,'quilos e seu IMC é ')
print(imc)