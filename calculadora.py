print("calculadora")
print("1 soma")
print("2 subtração")
print("3 multiplicação")
print("4 divição")

resposta=int(input("escolha uma opção "))
n1=int(input("digita o primeiro numero "))
n2=int(input("digita o segundo numero "))

if resposta==1:
    print(n1+n2)
if resposta==2:
    print(n1-n2)
if resposta==3:
    print(n1*n2)
if resposta==4:
    print(n1/n2)
 
    input("deseja continuar?")
    