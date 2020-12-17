"""
[Questão criada por Myllena Laís (adaptada)] Um novo funcionário de supermercado quer saber em 
qual corredor se encontra um produto. No sistema existem os seguintes produtos: 
Arroz - corredor 1, Feijão - corredor 1, Óleo de soja - corredor 2, Sal - corredor 3, 
Açúcar - corredor 3, Café- corredor 4, Molho de tomate -corredor 5, Macarrão- corredor 6. 
O funcionário precisa encontrar em qual corredor está o produto para ajudar o cliente em sua compra. 
Use tupla para criar esse programa. 
"""

produtos = (["Arroz", 1],["Feijão", 1],["Óleo de soja", 2],["Sal", 3],["Açúcar", 3],["Café", 4],["Molho de tomate", 5], ["Macarrão", 6])

while True:
    print("BEM-VINDO(A) AO SISTEMA DO SUPERMERCADO")
    corredor = int(input("Qual corredor deseja pesquisar ?"))
    print("Os produtos desse corredor são:")
    for i in range(len(produtos)):
        if corredor == produtos[i][1]:
            print(f"Produto: {produtos[i][0]}.")
    
    saida = input("Mais alguma coisa (Y/N)? ")
    if saida == "N":
        break

print("Até a próxima, volte sempre.")