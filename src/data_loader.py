import pandas as pd 

def carregar_dados():
    pokemons = pd.read_csv('./data/Pokemon.csv',sep=';')
    pokemons.columns = pokemons.columns.str.strip() # Remove espaçoes em brancos extras dos nomes das colunas.
    return pokemons 
dados_pokemon = carregar_dados()


