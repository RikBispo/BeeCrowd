n1,n2,n3,n4 = map(float, input().split())
n1,n2,n3,n4 = round(n1,1), round(n2,1), round(n3,1), round(n4,1)
media1 = round(((n1*2) + (n2*3) + (n3*4) + n4)/10,1)
print('Media:',media1)
if media1 >= 7:
    print('Aluno aprovado.')
if media1 < 5:
    print('Aluno reprovado.')
if media1 >= 5 and media1 < 7:
    print('Aluno em exame.')
    n5 = round(float(input()),1)
    media2 = round((media1+n5)/2,1)
    print('Nota do exame:',n5)
    if media2 >= 5:
        print('Aluno aprovado.')
        print('Media final:',media2)
    else:
        print('Aluno reprovado.')
        print('Media final:',media2)
