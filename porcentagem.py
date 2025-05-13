# Cálculo de Porcentagem de um Número.
# • O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
# valor total e 15 como porcentagem, o programa deverá calcular
# que 15% de 200 é 30.
# • Exemplo de fórmula:
# valor_parte = valor_total * (porcentagem / 100)

valor=float(input("digita uma valor?"))
taxa_porcentagem= float(input("digita a taxa?"))

resultado= valor * (taxa_porcentagem/100)
print(resultado)