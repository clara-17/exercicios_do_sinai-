from colorama import init,Fore
init(autoreset=True)

nome=input('qual é nome do aluno?' )
nota1=(int(input('primeira nota?')))
nota2=(int(input('segunda nota?')))
nota3=(int(input("terceira nota?")    
))

media=(nota1+nota2+nota3)/3
print("media:" , media)


if media>=5: 
    print(Fore.GREEN+'aluno aprovado')
else:
    print(Fore.RED+"aluno reprovado")
