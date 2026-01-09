from data_loader import dados_pokemon
from pokemon import Pokemon , Dados
import random
import pandas as pd
import time

# Escolher meu pokemon aleatório
def mostrar_opcoes():
    selecao = dados_pokemon.sample(5)
    print(f"Selecione com qual pokemon voce quer batalhar!!") # Mensagem antes de aparecer a lista de pokemons
    print(f"OPÇÃO | NOME | TIPO 1 / TIPO 2 | HP | ATAQUE | DEFESA")
    for i,(idx,pokemon_atual) in enumerate(selecao.iterrows(),1):  # Mostrar a lista de pokemons
        nome = pokemon_atual['name']
        tipo1 = pokemon_atual['type 1']
        tipo2 = pokemon_atual['type 2']
        tipo_texto = f"{tipo1} / {tipo2}" if pd.notna(tipo2) else tipo1
        hp = pokemon_atual['hp']
        ataque = pokemon_atual['attack']
        defesa = pokemon_atual['defense']
        print(f"{i} - {nome} | {tipo_texto} | {hp} | {ataque} | {defesa}")
    return selecao

pokemon_selecionado = mostrar_opcoes() # mostrar opções
# SISTEMA DE SELEÇÃO DE POKEMON.
while True:
    opcao = input(f"Digite a opção que voce quer: ")

    if opcao not in ['1','2','3','4','5']:
        print(f"Esta opção não existe, escolhar entre as opções: 1, 2, 3, 4, 5")
    else:
        indice = int(opcao) - 1
        pokemon_selecionado = pokemon_selecionado.iloc[indice]
        print(f"Voce selecionou o {pokemon_selecionado['name']}, parabens!")
        break

# SISTEMA DE ESCOLHA DE POKEMON ADVERSÁRIO (ALEATORIO)
pokemon_adversario = dados_pokemon.sample(1).iloc[0]
print("-" * 30)
print(f"UM ADVERSÁRIO APARECEU")
print(f"O computador escolheu: {pokemon_adversario['name']}")
print(f"HP: {pokemon_adversario['hp']} | ATK: {pokemon_adversario['attack']} | DEF: {pokemon_adversario['defense']}")
print("-" * 30)
print(f"\nA BATALHA SERÁ ENTRE: {pokemon_selecionado['name']} vs {pokemon_adversario['name']}\n")

# DEFINIR QUEM ATACA PRIMEIRO
if random.choice([True, False]):
    p1_dados = pokemon_selecionado
    p2_dados = pokemon_adversario
    print("Você começa!")
else:
    p1_dados = pokemon_adversario
    p2_dados = pokemon_selecionado
    print("O adversário começa!")

# LÓGICA DE BATALHA
primeiro = Pokemon(p1_dados['name'], p1_dados['type 1'], p1_dados['hp'], p1_dados['attack'], p1_dados['defense'])
segundo = Pokemon(p2_dados['name'], p2_dados['type 1'], p2_dados['hp'], p2_dados['attack'], p2_dados['defense'])

while primeiro.verificar_hp() and segundo.verificar_hp():
    time.sleep(1)
    primeiro.atacar(segundo)

    if not segundo.verificar_hp():
        Dados(segundo).anunciar_derrota()
        if segundo.nome != pokemon_selecionado['name']:
            print("PARABÉNS! Você venceu a batalha!")
        else:
            print("QUE PENA! Você foi derrotado!")
        break
    
    time.sleep(1)
    segundo.atacar(primeiro)

    if not primeiro.verificar_hp():
        Dados(primeiro).anunciar_derrota()
        if primeiro.nome != pokemon_selecionado['name']:
            print("PARABÉNS! Você venceu a batalha!")
        else:
            print("QUE PENA! Você foi derrotado!")
        break

    
