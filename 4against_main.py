from tabulate import tabulate
import numpy as np
from random import *

def rolld6(x=1):
    roll_tot = 0
    for i in range(x):
        roll_tot = roll_tot + randrange(1, 7)
    return roll_tot

def rolld66():
    roll_tot = randrange(1, 7) + 10*randrange(1, 7)
    return roll_tot

#salas que são corredores
corr = np.array([11, 12, 13, 14, 26, 32, 33, 42, 45, 51, 53, 55, 63, 65])

#variáveis de progresso
xp = 0
boss_xp = 0
fountain = 0
lady = 0

#bolsa de moedas e inventário
gold = 0
inv = []
quest = "Não há missão."

#definindo os jogadores
class Player:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.lv = 1
        self.hp = 0
        self.atk = 0
        self.dfc = 0
        self.clues = 0
        self.inv = []

class Warrior(Player):
    def __init__(self):
        Player.__init__(self)
        self.hp = 7

def levelup(p):
    p.hp += 1



player = {
    1: Player(),
    2: Player(),
    3: Player(),
    4: Player()
}

def combat(monsters):
    print("Combate com " + monsters + " iniciado!")
    action = input("O que fazem?")
    if action == "a":
        print(monsters + "mortos!")
    elif action == "f":
        print("Vocês fogem dos monstros!")
    return "Combate finalizado!"

traps_table = {
    1: "Dart lv2",
    2: "Poison gas lv3",
    3: "Trapdoor lv 4",
    4: "Bear trap lv4",
    5: "Spears from wall lv5",
    6: "Giant stone block lv5"
    }

magic_treasure_table = {
    1: "Varinha da Sonolência",
    2: "Anel do Teleporte",
    3: "Ouro de tolo",
    4: "Arma mágica",
    5: "Poção de Cura",
    6: "Cajado de Bola de Fogo"
    }

random_spell_table = {
    1: "Bênção",
    2: "Bola de fogo",
    3: "Raio elétrico",
    4: "Sonolência",
    5: "Escape",
    6: "Proteção"
    }

def special_feature_table():
    roll = rolld6()
    global fountain
    if roll == 1:
        if fountain == 0:
            fountain = fountain + 1
            return "Encontram uma fonte, cada jogador ganha +1HP"
        else:
            return "Encontram mais uma fonte."
    return {
    2: "Blessed Temple: one +1ATK vs first undead or demon",
    3: "Armory: change weapons",
    4: "Cursed Altar: one -1DEF until slayed boss or Blessed Temple",
    5: "Statue: if touched, 50% chance of boss, 50% 3d6*10 gold",
    6: "Puzzle Room: d6 to solve, if failed -1HP, if solved Treasure"
    }[roll]

boss_table = {
    1: "Mummy, lv5",
    2: "Orc Brute, lv5",
    3: "Ogre, lv5",
    4: "Medusa, lv4",
    5: "Chaos Lord, lv6",
    6: "Small dragon, lv6"
    }

def quests_table():
    roll = rolld6()
    global quest
    if roll == 1:
        quest = """CORTEM AS CABEÇAS! \n 
            O grupo precisa matar o boss """ + boss_table[rolld6()] + """ e trazer sua cabeça de volta para a sala onde foi dada a missão."""
    elif roll == 2:
        quest = """TRAGAM-ME OURO! \n
            To complete the quest, the party must bring d6 x 50 worth of treasure to this room. If they already have that amount available, the amount required to complete the quest is doubled."""
    elif roll == 3:
        quest = """EU QUERO ELE VIVO! \n
            As 1, above, but the party must subdue the boss, tie him up with a rope, and take him to the creature’s room to complete the quest. To subdue a monster, you must either use the Sleep spell or fight with -1 on all Attack rolls (striking with the flat of the blade or trying to knock out the boss instead of killing him)"""
    elif roll == 4:
        quest = """ME TRAGAM AQUILO! \n
            Roll on the magic items table to determine what the object is. Every time the party kills a boss, there is a 1 in 6 chance that he will have that object in addition to his treasure, if any. To complete the quest, the party must bring the object in the room where the quest started."""
    elif roll == 5:
        quest = """QUE REINE A PAZ! \n
            To complete the quest, the party must complete at least three encounters in the adventure in a non violent way. This includes reactions such as bribing, getting help from monsters, performing another quest (not this one!), or defeating a monster with the Sleep spell and then tying him up with a rope."""
    elif roll == 6:
        quest = """MATEM TODOS OS MONSTROS! \n
            To complete the quest, all the dungeon rooms must be laid out and all the occupants slain, with the exception of the creature who sent the party on this quest. As soon as these conditions are met, the party can claim their reward."""
    return quest

weird_monsters_table = {
    1: "Minotaur, lv5",
    2: "Iron Eater, lv3",
    3: "Chimera, lv5",
    4: "Catoblepas, lv4",
    5: "Giant Spider lv5",
    6: "Invisible Gremlins"
    }

minions_table = {
    1: "1d6+2 skeletons or 1d6 zombies, lv3",
    2: "1d6+3 goblins, lv3",
    3: "1d6 hobgoblins, lv4",
    4: "1d6+1 orcs, lv4",
    5: "1d3 trolls, lv5",
    6: "2d6 Fungi Folk, lv3"
    }

def vermin_table():
    roll = rolld6()
    chance = randint(0,1)

    if roll == 1 and chance == 0:
        return "Apareceram alguns ratos, porém fugiram"
    elif roll == 1 and chance == 1:
        num = rolld6(3)
        print("Aparecem " + str(num) + " ratos!")
        monsters = "ratos"
        #"3d6 rats lv1. 1 in 6 chance of -1HP infection"
        return combat(monsters)
    elif roll == 2 and chance == 0:
        return "Apareceram alguns morcegos, porém fugiram"
    elif roll == 2 and chance == 1:
        num = rolld6(3)
        print("Aparecem " + str(num) + " morcegos!")
        monsters = "morcegos"
        #"3d6 bats lv1, Spells -1"
        return combat(monsters)
    else:
        return {
            3: "2d6 goblins lv3",
            4: "1d6 giant centipedes lv3",
            5: "1d6 vampire frogs lv4",
            6: "1d6 skeletal rats"
            }[roll]

def special_events_table():

    roll = rolld6()
    global lady
    #print("Roll do special events", roll)
    if roll == 3:
        if lady == 0:
            lady = lady + 1
            a = input("Uma misteriosa mulher vestida de branco passa-te a bufa, aceitas? \n")
            if a == "s":
                return quests_table()
            else:
                return "Você negou a bufa da velha! Sem quest pra você."

    elif roll == 2:
        sub_roll = rolld6()
        if sub_roll < 4:
            return vermin_table()
        elif sub_roll == 4:
            return minions_table[rolld6()]
        elif sub_roll == 5:
            return weird_monsters_table[rolld6()]
        elif sub_roll == 6:
            return boss_table[rolld6()]

    else:
        return {
            1: "Ghost: lv4 fear save, if failed -1HP",
            3: "Ghost: lv4 fear save, if failed -1HP",
            4: traps_table[rolld6()],
            5: "Healer: 10 gold per life healed, once per game",
            6: "Alchemist"                                 
            }[roll]

def treasure_table():
    roll = rolld6()
    #print("Roll do treasure table", roll)
    global gold
    global inv
    if roll == 1:
        val = rolld6()
        gold = gold + val
        return "Vocês acharam " + str(val) + " moedas!"
    elif roll == 2:
        val = rolld6(2)
        gold = gold + val
        return "Vocês acharam " + str(val) + " moedas!"
    elif roll == 3:
        spell = random_spell_table[rolld6()]
        inv.append("Pergaminho com " + spell)
        return "Vocês acharam um pergaminho com um feitiço de " + spell + "!"
    elif roll == 4:
        val = rolld6(2)*5
        inv.append("Gema (" + str(val) + "g)")
        return "Vocês acharam uma gema no valor de " + str(val) + " moedas!"
    elif roll == 5:
        val = rolld6(3)*10
        inv.append("Jóia (" + str(val) + "g)")
        return "Vocês acharam uma jóia no valor de " + str(val) + " moedas!"
    elif roll == 6:
        treasure = magic_treasure_table[rolld6()]
        inv.append(treasure)
        return "Vocês encontram o item " + treasure

def contents_table():

    roll = rolld6(2)
    #print("Roll do contents table", roll)
    if (room in corr) and (roll in np.array([4, 8, 10, 12])):
        return "Corredor vazio"
    elif roll == 2: return treasure_table()
    elif roll == 3: return treasure_table() + "\n" + traps_table[rolld6()]
    elif roll == 4: return special_events_table()
    elif roll == 5: return special_feature_table()
    elif roll == 6: return vermin_table()
    elif roll == 7 or roll == 8: return minions_table[rolld6()]
    elif roll == 9: return "Está vazia"
    elif roll == 10: return weird_monsters_table[rolld6()]
    elif roll == 11: return "Boss + 1d6 progress"
    elif roll == 12: return boss_table[6]

epic_rewards_table = {
    1: "The Book of Skalitos",
    2: "The Gold of Kerrak Dar",
    3: "Enchanted weapon",
    4: "Shield of Warning",
    5: "Arrow of slaying",
    6: "Holy Symbol of healing"
    }

def empty_room_search_table():
    roll = rolld6()

    if roll in np.array([2, 3, 4]):
        return "Ainda não tem nada"
    return{
    1: "Wandering Monsters",
    5: "Clue, secret door, or hidden treasure",
    6: "Clue, secret door, or hidden treasure" 
    }[roll]

#INÍCIO DO JOGO

def create_character(pn):
    global gold
    pn.name = input("Nome: ")
    print("Tipo:")
    print("1: Guerreiro \n2: Clérigo \n3: Ladino \n4: Mago \n5: Bárbaro \n6: Elfo \n7: Anão \n8: Hobbit")
    pn.type = input("")

    if pn.type == 1:
        gold = gold + rolld6(2)
        pn.hp = pn.lv+6
        pn.atk = pn.lv
        print("Equipamentos iniciais:")
        print("1: Escudo + Arma Padrão \n2: Arma de duas mãos \n3:Arco")
        inv = input("")
        if inv == 1:
            pn.inv.append("Escudo", "Arma Padrão")
        elif inv == 2:
            pn.inv.append("Arma de duas mãos")
        elif inv == 3:
            pn.inv.append("Arco")
        pn.inv.append("Armadura leve")
        print("\n")

    elif pn.type == 2:
        gold = gold + rolld6()
        pn.hp = pn.lv+4
        print("Equipamentos iniciais:")
        print("1: Escudo + Arma Padrão \n2: Arma de duas mãos \n3:Arco")
        inv = input("")
        if inv == 1:
            pn.inv.append("Escudo", "Arma Padrão")
        elif inv == 2:
            pn.inv.append("Arma de duas mãos")
        elif inv == 3:
            pn.inv.append("Arco")
        pn.inv.append("Armadura leve")
    print("\n")


for i in range(1,5):
    print("PERSONAGEM %s:" % i)
    create_character(player[i])

print("Sala inicial:", randrange(1,7))

i = input("")

while i != "f":

    if i == "i":
        print("\nDINHEIRO")
        print("Vocês têm", gold, "moedas. \n")
        print("INVENTÁRIO")
        for char in inv:
            print(char)
    elif i == "p":
        room = rolld66()
        print("Próxima sala:", room)
        print(contents_table())
    elif i == "q":
        print("Sua missão atual é:", quest)
    i = input("")

print("Fim do jogo, obrigado por jogar!")