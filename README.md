## 🎮 Definição do Projeto

Criar um jogo de batalha em Python, executado no terminal (sem interface gráfica), baseado em dados de pokémons armazenados em um arquivo CSV.

## 📁 Fonte de Dados (CSV)

- Os pokémons serão armazenados em um arquivo CSV.
- Cada linha do CSV representa um pokémon.
- O arquivo contém os atributos necessários para a batalha, como:
    - Nome do pokémon
    - Dano (ataque)
    - Defesa
    - HP

## 🤖 Jogador Máquina (IA simples)

A máquina:
- Escolhe seu pokémon aleatoriamente.
- Utiliza uma função de sorteio (randint) para essa escolha.
- Não há tomada de decisão estratégica:
- O comportamento da máquina é totalmente automático.

## 🧑 Jogador Humano

O jogador:
- Recebe 5 pokémons aleatórios como opções.
- Escolhe 1 pokémon entre esses 5 para a batalha.
- A escolha é feita via entrada pelo terminal.

## 🎲 Sistema de Sorteio

O sistema de sorteio:
- Seleciona pokémons de forma aleatória a partir do CSV.
- É usado tanto para:
    - Gerar as 5 opções do jogador
    - Escolher o pokémon da máquina

## ⚔️ Sistema de Batalha

A batalha ocorre entre:

- 1 pokémon do jogador
- 1 pokémon da máquina
- A luta acontece sem interface gráfica, apenas por texto.

## 🧮 Cálculo de Dano

O dano causado em cada ataque é baseado em:
    - Dano (ataque) do pokémon atacante
    - Defesa do pokémon defensor

Regra definida:

- A defesa do defensor é dividida por 2 para reduzir o dano recebido.
- A defesa atua como um redutor de dano, não como bloqueio total.

🔁 Fluxo da Batalha

- A batalha ocorre em turnos.
- A cada turno:
    - Um pokémon ataca
    - O outro recebe dano
    - O combate continua até que:
    - Um dos pokémons seja derrotado (HP chega a zero ou menos)
🖥️ Interface

- Não existe interface gráfica.
- Toda a interação ocorre via:
    - print para exibir informações
    - input para escolhas do jogador