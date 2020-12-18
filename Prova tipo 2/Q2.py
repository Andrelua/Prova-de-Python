"""
[Questão criada por Pedro Vinicius (adaptada)] Crie um programa que leia o nome de n jogadores, o time que joga, 
a quantidade de partidas que eles jogaram, a quantidade de gols feitos em cada partida e o total de gols. Essas informações 
serão armazenadas em um dicionário. O programa apresentará no final todas as informações dos jogadores e um ranking com os 
top 3 com mais gols.
"""

jogadores = {}
while True:
    valor = []
    gols = 0
    quantGols = 0
    
    nome = input("Qual o nome do jogador ?")
    time = input("Qual o time do jogador ?")
    partidas = int(input("Qual a quantidade de partidas ele jogou ?"))
    
    for i in range(partidas):
        quantGols = int(input(f"Quantos gols ele fez na {i+1}º partida ?"))
        gols += quantGols
    
    valor.append([gols, partidas, time])
    jogadores[nome] = valor
    
    jog = input("Mais algum jogador(Y/N)? ")
    if jog == "N":
        break


golacos = []
for chave, valor in jogadores.items():
    nome = chave
    golacos.append([valor, nome])
    
ordem = sorted(golacos)

i = -1
for y in range(len(ordem)):
    print(f"{y+1}º Lugar - Jogador {ordem[i][1]} do time {ordem[i][0][0][2]} com {ordem[i][0][0][0]} gols em {ordem[i][0][0][1]} jogo(s).")
    i -= 1
    