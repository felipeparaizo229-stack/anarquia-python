#liberação de acesso ao laboratorio 
nome_do_aluno=(input(print("digite o nome do aluno:")))
idade=int(input(print("digite sua idade: ")))

cadastro=str(input("voce possui cadastro ativo (s/n)"))

if idade <14 and cadastro == "n":
    print("aceso negado!")

if idade >14 and cadastro == "s":
    situacao="Aceso permitido somente com acompanhamnto!"

if 14<=idade<=17 and cadastro == "s":
    situacao="acesso permitido!"

if idade >=18 and cadastro == "s":
    situacao="acesso permitido!"

print("olá aluno",nome_do_aluno,"sua situação atual e de:",situacao,)
