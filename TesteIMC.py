peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura * altura)

print("Seu IMC é: {:.2f}".format(IMC))
