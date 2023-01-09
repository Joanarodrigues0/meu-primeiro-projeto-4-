''''
# Crie um programa que ao, iniciar o valor aleatorio entre 1 a 10 e permite que o usuario chute um numero ate que o valor aleatorio no inicio programa seja chutado corretamente
o programa deve informar que o chute foi acima, abaixo ou igual ao valor aletorio citado no inicio do programa.
Metodo 5Q's para um montar um algoritimo:
Analise criticamente o problema e descruba;
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/inestigue mais ate voce compreender completamnete o problema)
5 Q's:
1- Quais são os dados de entrada necessario?
valor aleatorio entre 1  10
CHUTE DO USUARIO
2- O que devemos fazer com estes dados?
comparar p chute do usuario com o valor aleatorio que foi gerado no inicio do programa e informar que o chute foi acima, abaixo ou igual ao valor que foi dito no ninico do programa
3- Quais são as retrições desse problema?
um valor aleatorio entre 1 a 10
4- Qual é o resultado esperado?
resultado esperado é que chute foi acima, abaixo ou igual 
5- Qual é a sequencia de passos a ser feita para chegar ao resultado esperado?
input valor_aletorio de 1 a 10
input churte
if chute > valor_aleatorio
print "chute foi maior que o valor gerado"
if chute < valor_aleatorio
print "chute foi menor que o valor gerado "
if chute = valor_aleatorio
print "voce acertoul"
'''
import random

valor_aletorio = random.range(1,10)
chute = int(input('chute um  entre 1 a 10'))
if chute > valor_aleatorio:
  print("Chute foi maior que o valor gerado")
elif chute < valor_aleatorio:
  print('Chute foi menor que o valor gerado')
elif chute == valor_aleatorio:
  print("voce acertou')


  