idade=int(input("Digite sua idade: "))
curso=(input("Você tem curso técnico(s/n): "))

if idade >= 18 and curso == "s":
    print("Você e maior de idade e possue formação")

elif idade >= 18 and curso == "n":
    print("Você e maior de idade, no entanto n possue formação")
elif idade < 18 and curso == "s":
    print("Voçê e menor de idade, mas possue formação")
elif idade < 18 and curso == "n":
    print("Você e menor de idade, e não possue formação")
else:
    print("Erro na digitação!")

          