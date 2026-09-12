print ("////////SISTEMA DE CADASTRO BIBLIOTECA CENTRAL\\\\\\\\")

print("opção 01-cadastro do livro")
print("opção 02- cadastra aluno")
print("opção 03-realizar emprestimo")
print("opção 04-sair")

opcao=int(input("digite a opção escolhida:"))
if opcao==1:
    print("======CADASTRO DO LIVRO======")
    quantidade_de_livros=int(input(print("quantos livros você quer cadastrar?:")))
for i in range (1,quantidade_de_livros+1):
    print("====livro-",i,"=====")
    codigo_do_livro=int(input("digite o codigo do livro: "))
    titulo_do_livro=str(input("qual o titulo do livro?: "))
    nome_do_autor=str(input("digite o nome do autor: "))
    ano_de_publiucacao=int(input("digite o ano de publicação: "))
    
    if codigo_do_livro == "":
        print("erro de digitação")
    elif titulo_do_livro =="":
        print("erro de digitação")
    elif nome_do_autor == "":
        print("erro de digitação")
    elif ano_de_publiucacao =="":
        print("erro de digitação")
    print(f"-----cadastro do livro {i}-----\nCodigo:{codigo_do_livro}\nTítulo:{titulo_do_livro}\nNome do Autor{nome_do_autor}\nquantidade_disponivel{quantidade_de_livros}\nAno de Publicação{ano_de_publiucacao}")

if opcao==2:
    print("**********************")
    print("--CADASTRO DO ALUNO--")
    print("**********************")











