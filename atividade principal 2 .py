produto=input("Nome do produto: ")
quat=int(input("Quantidade disponível(unidade): "))
if quat == 0:
    situacao="Produto Esgotado"
elif 5<= quat <= 1:
    situacao="Estoque Crítico"
elif 6 <= quat <= 20:
    situacao="Estoque Baixo"
elif quat > 20:
    situacao="Estoque Normal"
else:
    print("Erro na Digitação da quantidade!Preste atenção...")
print("NOME DO PRODUTO:\n",produto,"\nQUANTIDADE DISPONÍVEL:\n",quat,"\nSITUAÇÃO DO ESTOQUE:\n",situacao,)