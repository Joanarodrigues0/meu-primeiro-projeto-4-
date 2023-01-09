# Variaveis

# Numeros
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 # Float
# Valores boleanos
estar_aberto = True # verdadeiro e False # falso
# Strings - basicamento um texto
nome_do_curso = 'Logica da Programação'

# Como variaveis seriam usadas em um problema real?
# Problema 1 
# Escreve um programa que retonrne o valor hora de um funcionario com base no seu salario mensal e horas trabalhadas por mes?
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_horas = salario_mensal / horas_trabalhadas_por_mes
 print valor_hora
'''
salario_mensal = input('Qaul é o seu salario mensal?')
horas_trabalhada_por_mes = input('Qauntas horas trabalha por mes?')
valor_hora = int(salario_mensal) / int(horas_trabalhada_por_mes)
print(valor_hora)