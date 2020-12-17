"""
[Questão criada por Nicolas Mathias (adaptada)] Josemar trabalha numa revendedora de carros usados a cada 
carro vendido ele ganha 1,5 % de comissão. Utilizando lista composta guarde o nome e preço dos carros. Para 
vender o carro mostre uma tabela com os carros e os preços. Quando o carro for vendido deve modificar a lista
de carros para vendido. A venda acaba quando os carros acabarem ou quando a pessoa não quiser continuar. No final 
mostre: quantidade de carros vendidos e quanto Josemar lucrou no final em reais. Para essa questão use pelo menos 
duas funções.
"""


def calculoComis(comissao):
    comissao = comissao * 0.015
    print(f"A comissão final foi de: R${comissao}.")


def loja():
    
    comis = 0
    
    carros = [["Gol",30000, "Não Vendido"],["Celta",15000, "Não Vendido"],["Creta",80000, "Não Vendido"],["Vectra",40000, "Não Vendido"],["Onix",35000, "Não Vendido"],["Fusca",10000, "Não Vendido"],["Ka",36000, "Não Vendido"]]
    
    print("BEM-VINDO(A) A LOJA DO SENHOR JOSEMAR.")
    
    y = len(carros)

    print("CARROS DISPONÍVEIS: ")
    for i in range(len(carros)):
        print(f"{i+1} - {carros[i][0]} - R${carros[i][1]} - {carros[i][2]}")
    
    carrosVend = 0
    while y != 0:
        carro = input("Qual desses carros o senhor deseja (nome) ?")
        
        for i in range(len(carros)):
            if carro == carros[i][0]:
                comis += carros[i][1]
                carros[i][2] = "Vendido"
                carrosVend += 1
            if (carros[i][2] == "Vendido") or (carros[i][2] == "Não Vendido"):
                print(f"{i+1} - {carros[i][0]} - R${carros[i][1]} - {carros[i][2]}")
        
        saida = input("Quer compra mais algum carro ? (Y/N)")
        if saida == "N":
            break
        
        y -= 1
        if y == 0:
            print("Não tem mais carros a serem vendidos, até a próxima!!")
    
    calculoComis(comis)
    print(f"O total de carros vendidos foram: {carrosVend}")

loja()