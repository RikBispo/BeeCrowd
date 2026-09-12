ano, mes, dia = 0,0,0
idade = int(input())
if idade < 30:
    dia = idade
if idade > 29 and idade < 365:
    mes = int(idade/30)
    dia = idade%30
if idade > 364:
    ano = int(idade/365)
    mes = int((idade%365)/30)
    dia = (idade%365)%30
print(f'''{ano} ano(s)
{mes} mes(es)
{dia} dia(s)''')