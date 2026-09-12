import sys as sys
var1,var2,var3,var4 = map(float, input().split())
media = ((var1*2)+(var2*3)+(var3*4)+var4)/(2+3+4+1)
round(media,1)
print(media)
if media >= 7:
    print('Aluno aprovado.')
    sys.exit()
if media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    var5 = float(input())
    mediafinal = (media + var5)/2
    round(mediafinal,1)
    if mediafinal >= 5:
        print('Aluno aprovado.')
        print(mediafinal)
    else:
        print('Aluno reprovado')
        print(mediafinal)