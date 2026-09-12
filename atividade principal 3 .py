nome=input("Nome do Cliente: ")
velocidade=int(input("Velocidade contratada em MBPS:"))
if velocidade < 50:
    print("\nPlano Básico!")
elif 50 <= velocidade <= 199:
    print("\nPlano Intermedíario!")
elif 200 <= velocidade <= 499:
    print("\nPlano Avançado!")
elif velocidade > 500:
    print("\nPlano Ultra!")
else:
    print("\nErro na Digitação!")