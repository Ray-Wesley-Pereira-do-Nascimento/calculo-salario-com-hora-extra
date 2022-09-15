"""Um trabalhador trabalha 40 horas por semana. Escreva um algoritmo que leia o número de horas
   trabalhadas em cada semana de um mês, o salário por hora e escreva o salário total do mês do
   funcionário (considere que o mês possua 4 semanas exatas). Considere que o trabalhador que trabalhar
   mais de 40 horas numa semana, recebe hora extra de 50% nas horas trabalhadas a mais.
   O número de horas por semana não pode ser negativo e não pode ultrapassar 50 horas por semana.
"""


horas1 = -1
horas2 = -1
horas3 = -1
horas4 = -1
hora_extra1 = 0
hora_extra2 = 0
hora_extra3 = 0
hora_extra4 = 0
while horas1 < 0 or horas1 > 50:
  horas1 = int(input(f'Digite a quantidade de horas da 1 semana: '))
  if horas1 < 0 or horas1 > 50:
     print('Quantidade de horas inválida! Digite novamente ou contate o RH.')
  elif horas1 > 40 and horas1 <= 50:
     hora_extra1 = horas1 - 40
while horas2 < 0 or horas2 > 50:
   horas2 = int(input(f'Digite a quantidade de horas da 2 semana: '))
   if horas2 < 0 or horas2 > 50:
    print('Quantidade de horas inválida! Digite novamente ou contate o RH.')
   elif horas2 > 40 and horas2 <= 50:
     hora_extra2 = horas2 - 40
while horas3 < 0 or horas3 > 50:
    horas3 = int(input(f'Digite a quantidade de horas da 3 semana: '))
    if horas3 < 0 or horas3 > 50:
     print('Quantidade de horas inválida! Digite novamente ou contate o RH.')
    elif horas3 > 40 and horas3 <= 50:
      hora_extra3 = horas3 - 40
while horas4 < 0 or horas4 > 50:
   horas4 = int(input(f'Digite a quantidade de horas da 4 semana: '))
   if horas4 < 0 or horas4 > 50:
    print('Quantidade de horas inválida! Digite novamente ou contate o RH.')
   elif horas4 > 40 and horas4 <= 50:
      hora_extra4 = horas4 - 40

hora_extra = (hora_extra1 + hora_extra2 + hora_extra3 + hora_extra4)  * 0.5
salario_hora = float(input('Digite o salário por hora: '))
total_horas = horas1 + horas2 + horas3 + horas4
total_salario = (hora_extra + total_horas) * salario_hora
print(f"Total Horas Extras: {hora_extra}")
print(f'Total de Horas: {total_horas}')
print(F'O salário total do mês é de R${total_salario:.2f}')
