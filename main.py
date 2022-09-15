"""Um trabalhador trabalha 40 horas por semana. Escreva um algoritmo que leia o número de horas
   trabalhadas em cada semana de um mês, o salário por hora e escreva o salário total do mês do
   funcionário (considere que o mês possua 4 semanas exatas). Considere que o trabalhador que trabalhar
   mais de 40 horas numa semana, recebe hora extra de 50% nas horas trabalhadas a mais.
   O número de horas por semana não pode ser negativo e não pode ultrapassar 50 horas por semana.
"""


horas = [-1, -1, -1, -1]
salario_semana = [0, 0, 0, 0]

valor_hora = float(input("Digite o valor do salário por hora: "))
for n_semana in range(4):
  while horas[n_semana] < 0 or horas[n_semana] > 50:
   horas[n_semana] = int(input(f"Digite a quantidade de horas trabalhadas na semana {n_semana + 1}: "))
   if horas[n_semana] < 0 or horas[n_semana] > 50: print("Quantidade de horas inválida. Digite novamente: ")
   else:
     if horas[n_semana] <= 40:
       salario_semana[n_semana] = valor_hora * horas[n_semana]
     else:
       salario_semana[n_semana] = valor_hora * 40
       salario_semana[n_semana] += (horas[n_semana] - 40) * (valor_hora + valor_hora * 0.5)
salario_mes = 0
for n_semana in range(4):
  salario_mes += salario_semana[n_semana]
print(f"O salário do mês é de R$ {salario_mes}")

