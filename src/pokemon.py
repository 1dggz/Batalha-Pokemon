class Pokemon:
    def __init__(self,nome,tipos,hp,attack,defense):
        self.nome = nome
        self.tipos = tipos
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)  
    
    def atacar(self,alvo): # Ataque
        print(f"{self.nome} atacou {alvo.nome}!!") 
        alvo.receber_dano(self.attack)
    
    def receber_dano(self,ataque_inimigo): # Calcular a lógica de defesa e o dano que sofreu
        dano_recebido = ataque_inimigo - (self.defense // 2)
        if dano_recebido > 0:
            self.hp = max(0, self.hp - dano_recebido)
        print(f"{self.nome} recebeu {dano_recebido} de dano! HP atual: {self.hp}")
    
    def verificar_hp(self): # Verificar se esta vivo ainda
        if self.hp == 0:    
            return False
        return True
    
class Dados:
    def __init__(self,infos_pokemon):
        self.pokemon = infos_pokemon

    def status(self):
        return f'Meu nome é {self.pokemon.nome} e meu HP atual é {self.pokemon.hp}.'
    
    def anunciar_derrota(self):
        print(f"\n[{self.pokemon.nome.upper()}] não aguento mais e desmaiou!")
        print(f"Fim de combate para ele...")
        