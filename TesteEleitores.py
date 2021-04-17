eleitores = int(input("Digite o numero de eleitores da cidade: "))
v_brancos = int(input("Digite a QTD de Votos Brancos: "))
v_nulos = int(input("Digite a QTD de Votos Nulos: "))
v_validos = int(input("Digite a QTD de votos válidos: "))

percbrancos = float(v_brancos/eleitores*100)
percnulos = float(v_nulos/eleitores*100)
percvalidos = float(v_validos/eleitores*100)

print("Os votos brancos representam: {:.2f}%".format(percbrancos))
print("Os votos nulos representam: {:.2f}%".format(percnulos))
print("Os votos validos representam: {:.2f}%".format(percvalidos))
