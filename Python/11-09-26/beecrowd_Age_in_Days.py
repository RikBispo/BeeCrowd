idade = int(input())
if idade < 30:
    print(f'''0 ano(s)
0 mes(es)
{idade} dia(s)''')
if idade >= 30 and idade < 365:
    dias = idade % 30 #vai pegar o resto da divisão por 30, sobrando os dias
    meses = int(idade/30)
    print(f'''0 ano(s)
{meses} mes(es)
{dias} dia(s)''')
else:
    anos = int(idade/365)
    meses = int(((anos*365) - idade)/30)
    dias = ((anos*365) - idade)%30
    print(f'''{anos} ano(s)
{meses} mes(es)
{dias} dia(s)''')