'''
Crie um programa que recebe um numero e imprima o fatorial daquele numero.
Metodo 5Q's para um montar um algoritimo:
Analise criticamente o problema e descruba;
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/inestigue mais ate voce compreender completamnete o problema)
5 Q's:
1- Quais são os dados de entrada necessario?
numero
2- O que devemos fazer com estes dados?
Calcular o fatorial que foi passado ao programa e exibir na tela
3- Quais são as retrições desse problema?
O numero deve ser um valor inteiro
o numero deve ser um valor positivo
4- Qual é o resultado esperado?
É que o fatorial do numero providenciado seja exibido na tela
5- Qual é a sequencia de passos a ser feita para chegar ao resultado esperado?
input = numero
if numero = 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
 fatorial = fatorial * numero
 print(fatorial)
'''
numero = int(input('Digite um numero'))
if numero > 0:
  fatorial = 1 
for item in range(1,numero +1):
    fatorial = fatorial * item
print(fatorial)