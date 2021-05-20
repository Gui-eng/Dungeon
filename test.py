import random

"""             Global Variables                """
#Player Status
name = "Steve"
max_health = 100
health = 100
deffence = 20
attck = 10
weapon = "Fist"
shield = "None"
potions = 3
gold = 0
"""                Class               """

class weapons(object):
    """Weapon ingame manipulates attack in game"""
    def __init__(self, weapon_name,weapon_plus_attack,weapon_durability,weapon_price):
        super(weapons, self).__init__()
        self.weapon_name = weapon_name
        self.weapon_plus_attack = int(weapon_plus_attack)
        self.weapon_durability = int(weapon_durability)
        self.weapon_price = weapon_price
class armor(object):
    """manipulates armor in game"""
    def __init__(self, armor_name,armor_plus_deff,armor_plus_health,armor_durability,armor_price):
        super(armor, self).__init__()
        self.armor_name = armor_name
        self.armor_plus_deff = int(armor_plus_deff)
        self.armor_plus_health = int(armor_plus_health)
        self.armor_durability  = int(armor_durability)

class shields(object):
    """Manipulates Shields in game"""
    def __init__(self, shield_name,shield_plus_armor,shield_durabilty,shield_price):
        super(shields, self).__init__()
        self.shield_name = shield_name
        self.shield_plus_armor = int(shield_plus_armor)
        self.shield_durabilty = int(shield_durabilty)

class monsters(object):

    monster_id = 0
    instances = []

    """Status for monsters"""
    def __init__(self,monster_id, m_name,health,attck,deff,weapon,shield,gold):
        super(monsters, self).__init__()

        self.monster_id = monster_id
        self.m_name = m_name
        self.health = int(health)
        self.attck = int(attck)
        self.deff = int(deff)
        self.weapon = weapon
        self.shield = shield
        self.gold = gold
        __class__.instances.append(self)

"""             Class Instances                 """

def monsters_var():
    global Slime, Goblin, Wolf, Hobgoblin, Skeleton
    """Monsters Variables"""
    Slime = monsters(1, 'Slime',20, 5, 5,"None", "None", 5)
    Goblin = monsters(2, 'Goblin',30, 10, 10,"None", "None", 10)
    Wolf =  monsters(3, 'Wolf', 30, 15, 5,"None", "None", 7)
    Hobgoblin = monsters(4, 'Hobgoblin',60, 35, 10,"None", "None", 50)
    Skeleton =  monsters(5, 'Skeleton',10, 10, 5,"None", "None", 10)

#Weapons Variables
Rusty_Sword = weapons("Rusty Sword", 10, 5)
Broadsword = weapons("Broadsword", 15, 10)
Bow = weapons("Bow", 20, 5)
Iron_Sword = weapons("Iron Sword", 12, 20)
Club = weapons("Club", 25, 10)

#Armor Variables
Leather_Armor = armor("Leather Armor", 10, 10, 0)
Chain_Armor = armor("Chain Armor", 15, 20, 0)

#Shield Variables
Rusty_Shield = shields("Rusty Shield", 5, 5)
Leather_Shield = shields("Leather Shield", 5, 10)
Iron_Shield = shields("Iron Shield", 10, 20)

"""   Monsters unique drops and action    """

def monster_checker():
    """Checks for monster Id to distribute its own items"""
    if random_monster.monster_id == 2:
        goblin_items()
    elif random_monster.monster_id == 4:
        hobgoblin_items()
    elif random_monster.monster_id == 5:
        skeleton_items()
    else:
        print ()
        print("the mosnter have no items")
        print()

def goblin_items():
    Goblin.weapon = Rusty_Sword.weapon_name
    Goblin.shield = Rusty_Shield.shield_name
    Goblin.attck = Rusty_Sword.weapon_plus_attack + Goblin.attck
    Goblin.deff = Rusty_Shield.shield_plus_armor + Goblin.deff

def hobgoblin_items():
    Hobgoblin.weapon = Club.weapon_name
    Hobgoblin.shield = Iron_Shield.shield_name
    Hobgoblin.attck = Club.weapon_plus_attack + Hobgoblin.attck
    Hobgoblin.deff = Iron_Shield.shield_plus_armor + Hobgoblin.deff

def skeleton_items():
    Skeleton.weapon = Rusty_Sword.weapon_name
    Skeleton.shield = Rusty_Shield.shield_name
    Skeleton.attck = Rusty_Sword.weapon_plus_attack + Skeleton.attck
    Skeleton.deff = Rusty_Shield.shield_plus_armor + Skeleton.deff

"""             Merchant functions               """

def buy():
    print()
    print ("Welcome to dungeon store!")
    print()
    print ("What would you like to do?")
    print ("[V] to view catalogue")
    print ("[Q] to quit")
    choice = str(input("please type and enter here:"))
    if choice == 'v' or choice == 'V':
        view_catalogue()
    elif choice == 'q' or choice == 'Q':
        player_action()

choice = "Something"
def view_catalogue():
    global choice
    print(name + "'s gold: " + gold)
    print()
    print("****************************")
    print("          Weapons           ")
    print("[RSW] Rusty Sword for 20 gold")
    print("[BSW] Broadsword for 50 gold")
    print("[BOW] Bow for 10 gold")
    print("[ISW] Iron Sword for 30 gold")
    print("[CLB] Club for 100 gold")
    print("****************************")
    print()
    print("****************************")
    print("          Shields           ")
    print("[RSH] Rusty Shield for 20 gold")
    print("[LSH] Leather_Shield for 50 gold")
    print("[ISH] Iron Shield for 100 gold")
    print("****************************")
    print()
    print("****************************")
    print("          Armors            ")
    print("[LAR] Leather armor for 40 gold")
    print("[CAR] Chain Armor for 100 gold")
    print("****************************")
    print()
    choice = str(input("Please enter your choice here or type and enter [Q] to go back: "))

def buy_handle():
    global gold, choice
    if choice ==
        pass
"""             Functions               """


#Random Monsters Variables
def gen_random_monster():
    """Radom monster Generator"""
    global random_index,random_monster
    random_index = random.randrange(len(monsters.instances))
    random_monster = monsters.instances[random_index]

def get_name():
    """A function to get player name
    note: this will be only be called once!
    """
    global name
    name = str(input("Please enter your name: "))
    print ("So your name is: " + name)
    choice =  str(input("if Yes type [Y] na if no type [N]: "))
    if choice == 'Y' or choice == 'y':
        return name
    elif choice == 'N' or choice == 'n':
        get_name()
    else:
        print("Please enter a valid answer!")
        get_name()

def fountain():
    global health,max_health
    print("Restoring Health...")
    health = max_health
    print("Health Restored!")
    get_stats()
    player_action()

def apply_potion():
    global health,max_health,potions
    if potions <= 0:
        print ("You don't have enough potions!")
    else:
        print (name + " used a potion!")
        potions = potions - 1
        health = health + 50
        if health >= max_health:
            health = max_health
        get_stats()


def get_stats():
    """Show Player Status"""
    print (name + "'s health is: " + str(health))
    print (name + "'s deffence is: " + str(deffence))
    print (name + "'s attack is: " + str(attck))
    print ()
    #prints player's items
    print (name + "'s weapon is: " + str(weapon))
    print (name + "'s shield is: " + str(shield))
    print (name + "'s potion count is: " + str(potions))
    print (name + "'s gold is: " + str(gold))
    print ()


def get_m_stats():
    """Show Monster Status"""
    print ("Name: " + str(random_monster.m_name))
    print ("Health: " + str(random_monster.health))
    print ("Attack: " + str(random_monster.attck))
    print ("Deffence: " + str(random_monster.deff))
    print()
    #prints monster's items
    print ("Weapon: " + random_monster.weapon)
    print ("Shield: " + random_monster.shield)
    print ()

def player_fight():
    """Player fight action if he/she choose [A]"""
    global attck
    deffence = random_monster.deff
    get_percentage = deffence / 100
    get_final_percentage = attck * get_percentage
    get_final_damage = int(attck - get_final_percentage)
    print()
    print (str(name) + " attacked " + str(random_monster.m_name) + " for " + str(get_final_damage) + " Damage!")
    print()
    random_monster.health = random_monster.health - get_final_damage
    get_m_stats()

def monster_fight():
    """Mosnter automatic fighting sequence"""
    global health,deffence
    attack = random_monster.attck
    get_percentage = deffence / 100
    get_final_percentage = attack * get_percentage
    get_final_damage = int(attack - get_final_percentage)
    print (str(random_monster.m_name) + " attacked " + str(name) + " for " + str(get_final_damage) + " Damage!")
    print()
    health = health - get_final_damage
    get_stats()

def fight_choice():
    """Players gets to select what to do while in the dungeon"""
    global health,gold
    fight = True;
    while fight:
    #Checks for health status for both players and monsters
        if health <= 0:
            health = 0
            print ("Game Over")
            break
        if random_monster.health <=0:
            random_monster.health == 0
            print()
            print(random_monster.m_name + ' is defeated ')
            print("You get " + str(random_monster.gold) + " gold!")
            gold = gold + random_monster.gold
            player_action()
            break
    #Handles decicion
        print("What would you like to do? ")
        choice = str(input("type and enter [A] to attack and [R] to run [P] to use a potion: "))
        if choice == 'A' or choice == 'a':
            #an exchange of attack sequence between the player and the monster
            player_fight()
            monster_fight()
            fight_choice()
        elif choice == 'R' or choice == 'r':
            player_action()
            break

        elif choice == 'P' or choice == 'p':
            apply_potion()
            fight_choice()
        else:
            print("Please enter a valid choice!")
            fight_choice()

def regen_monster():
            #regenerate monster instances after fight
            monsters_var()


def fight_action():
    """Fighting aspect of the game"""

    #generate monster instances
    monsters_var()

    #Generate random monster
    gen_random_monster()

    #Check for monster name if it has an item
    monster_checker()

    print ("A " + str(random_monster.m_name) + " appeard out of nowhere!")
    print ()

    #prints monster status
    get_m_stats()
    fight_choice()

def player_action():
    """Gets players decision every time
        it finished a move or just started the game
    """
    print()
    print ("What would you like to do?")
    print ("[E] to explore the dungeon.")
    print ("[Q] to quit")
    print ("[F] to fountain of joy")
    print ("[B] to buy")
    choice = str(input("there isn't much to choose so choose [E]: "))
    print()

    if choice == 'E' or choice == 'e':
       #init monster fighting sequence
       fight_action()
       return
    elif choice == 'q' or choice == 'Q':
        #quits game
        exit()
    elif choice == 'f' or choice == 'F':
        #go to fountain() to regenerate health
        fountain()
    elif choice == 'B' or choice == 'b':
        buy()
    else:
        print ("Please enter a valid choice")
        player_action()

def start_game():
    choice = str(input("Please type and enter [P] if you want to play and [Q] if you want to quit: "))
    if choice == 'q' or choice == 'Q':
        exit()
    elif choice == 'p' or choice == 'P':
        print()
        #getting player name
        get_name()
        #Get player to decide if he/she will play the game
        player_action()
    else:
        print("Please enter a valid choice")
        start_game()

"""             Main Executioner              """

def main():
    print("Welcome to dungeon!")
    print()
    start_game()



main()
