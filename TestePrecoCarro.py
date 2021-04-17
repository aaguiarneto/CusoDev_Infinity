precofabrica = float(input("Informe o preço de Fabrica: "))

precovenda = (precofabrica + (precofabrica * 28/100) + (precofabrica * 45/100))

print("O preço para o consumidor é: {:.2f}".format(precovenda))
