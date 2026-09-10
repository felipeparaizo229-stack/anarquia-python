#algoritimo calculadora
numero_1=float(input("digite o primeiro número!: "))
numero_2=float(input("digite o segundo número!: "))
print("[+]\n[-]\n[*]\n[/]")
operacoes=input(print("qual a operaçãoqu voce quer fazer:"))

if operacoes =="+":
    print("resultado=",numero_1+numero_2)

elif operacoes =="-":
    print("resultado=",numero_1+numero_2)

elif operacoes =="*":
    print("resultado=",numero_1*numero_2)

elif operacoes =="/":
    print("resultado=",numero_1/numero_2)

else:
    print("Erro de digitação!")