salarios = []
for i in range (0, 3):
    salarios.append(input())
int(salarios[0])
salario = int(salarios[1]) * float(salarios[2])
print(f'''NUMBER = {salarios[0]} ''')
print(f'''SALARY = U$ {salario:.2f} ''')