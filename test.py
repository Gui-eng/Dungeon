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
p_armor = "None"
potions = 3
gold = 0
kills = 20

is_fountain_visible = False
"""                Class               """

class weapons():
    """Weapon ingame manipulates attack in game"""
    def __init__(self, weapon_name,weapon_plus_attack,weapon_durability,price,letters):
        super(weapons, self).__init__()
        self.weapon_name = weapon_name
        self.weapon_plus_attack = int(weapon_plus_attack)
        self.weapon_durability = int(weapon_durability)
        self.price = int(price)
        self.letters = letters

    def prices(self):
        print ()
        print (self.weapon_name + " price is: " + str(self.price) + " gold")
        print ()
        print (self.weapon_name + " Specs as follows:")
        print ("Plus attack: " + str(self.weapon_plus_attack))
        print (self.weapon_name + "'s durability: " + str(self.weapon_durability))
        print()
        weapons.buy_decide(self)

    def buy_decide(self):
        print("Do you want to buy the " + self.weapon_name + "?")
        choice = str(input("[Y] for Yes and [N] for no: "))
        if choice == 'y' or choice == 'Y':
            weapons.buy_confirm(self)
        elif choice == 'n' or choice == 'N':
            view_catalogue()
        else:
            print ("please enter a valid answer")
            weapons.buy_decide(self)

    def buy_confirm(self):
        global attck,weapon,gold
        if gold < self.price:
            print()
            print("Not enough gold")
            print()
            view_catalogue()
        else:
            print (name + " bought " + self.weapon_name)
            gold = gold - self.price
            print (name + " total gold " + str(gold))
            weapon = self.weapon_name
            attck = attck + self.weapon_plus_attack
            get_stats()
            print("Would you like to purchase more?")
            view_catalogue()

class armor(object):
    """manipulates armor in game"""
    def __init__(self, armor_name,armor_plus_deff,armor_plus_health,armor_durability,price):
        super(armor, self).__init__()
        self.armor_name = armor_name
        self.armor_plus_deff = int(armor_plus_deff)
        self.armor_plus_health = int(armor_plus_health)
        self.armor_durability  = int(armor_durability)
        self.price = price

    def prices(self):
        print ()
        print (self.armor_name + " price is: " + str(self.price) + " gold")
        print ()
        print (self.armor_name + " Specs as follows:")
        print ("Plus deffence: " + str(self.armor_plus_deff))
        print ("Plus health: " + str(self.armor_plus_health))
        print (self.armor_name + "'s durability: " + str(self.armor_durability))
        print()
        armor.buy_decide(self)

    def buy_decide(self):
        print("Do you want to buy the " + self.armor_name + "?")
        choice = str(input("[Y] for Yes and [N] for no: "))
        if choice == 'y' or choice == 'Y':
            armor.buy_confirm(self)
        elif choice == 'n' or choice == 'N':
            view_catalogue()
        else:
            print ("please enter a valid answer")
            armor.buy_decide(self)

    def buy_confirm(self):
        global deffence,p_armor,max_health,gold
        if gold < self.price:
            print()
            print("Not enough gold")
            print()
            view_catalogue()
        else:
            print (name + " bought " + self.armor_name)
            gold = gold - self.price
            print (name + " total gold " + str(gold))
            p_armor = self.armor_name
            deffence = deffence + self.armor_plus_deff
            max_health = max_health + self.armor_plus_health
            get_stats()
            print("Would you like to purchase more?")
            view_catalogue()
class shields(object):
    """Manipulates Shields in game"""
    def __init__(self, shield_name,shield_plus_deff,shield_durabilty,price):
        super(shields, self).__init__()
        self.shield_name = shield_name
        self.shield_plus_deff = int(shield_plus_deff)
        self.shield_durabilty = int(shield_durabilty)
        self.price = price

    def prices(self):
        print ()
        print (self.shield_name + " price is: " + str(self.price) + " gold")
        print ()
        print (self.shield_name + " Specs as follows:")
        print ("Plus deffence: " + str(self.shield_plus_deff))
        print (self.shield_name + "'s durability: " + str(self.shield_durabilty))
        print()
        shields.buy_decide(self)

    def buy_decide(self):
        print("Do you want to buy the " + self.shield_name + "?")
        choice = str(input("[Y] for Yes and [N] for no: "))
        if choice == 'y' or choice == 'Y':
           shields.buy_confirm(self)
        elif choice == 'n' or choice == 'N':
            view_catalogue()
        else:
            print ("please enter a valid answer")
            shields.buy_decide(self)

    def buy_confirm(self):
        global deffence,p_armor,health,gold,shield
        if gold < self.price:
            print()
            print("Not enough gold")
            print()
            view_catalogue()
        else:
            print (name + " bought " + self.shield_name)
            gold = gold - self.price
            print (name + " total gold " + str(gold))
            shield = self.shield_name
            deffence = deffence + self.shield_plus_deff
            get_stats()
            print("Would you like to purchase more?")
            view_catalogue()
class monsters(object):

    monster_id = 0
    instances = []

    """Status for monsters"""
    def __init__(self,monster_id, m_name,health,attck,deff,weapon,shield,gold,max_health):
        super(monsters, self).__init__()

        self.monster_id = monster_id
        self.m_name = m_name
        self.health = int(health)
        self.attck = int(attck)
        self.deff = int(deff)
        self.weapon = weapon
        self.shield = shield
        self.gold = gold
        self.max_health = max_health
        __class__.instances.append(self)

    def monster_regen(self):
        self.health = self.max_health

"""             Class Instances                 """

def monsters_var():
    global Slime, Goblin, Wolf, Hobgoblin, Skeleton
    """Monsters Variables"""
    Slime = monsters(1, 'Slime',20, 5, 5,"None", "None", 5, 20)
    Goblin = monsters(2, 'Goblin',30, 10, 10,"None", "None", 10, 30)
    Wolf =  monsters(3, 'Wolf', 30, 15, 5,"None", "None", 7, 30)
    Skeleton =  monsters(5, 'Skeleton',10, 10, 5,"None", "None", 10, 10)
    Hobgoblin = monsters(4, 'Hobgoblin',60, 35, 10,"None", "None", 50, 60)


#Weapons Variables
Rusty_Sword = weapons("Rusty Sword", 10, 5, 20, "RSW")
Broadsword = weapons("Broadsword", 15, 10, 50, "BSW")
Bow = weapons("Bow", 7, 5, 10, "BOW")
Iron_Sword = weapons("Iron Sword", 12, 20, 30, "ISW")
Club = weapons("Club", 25, 10, 100, "CLB")

#Armor Variables
Leather_Armor = armor("Leather Armor", 10, 10, 0, 40)
Chain_Armor = armor("Chain Armor", 15, 20, 0, 100)

#Shield Variables
Rusty_Shield = shields("Rusty Shield", 5, 5, 20)
Leather_Shield = shields("Leather Shield", 5, 10, 50)
Iron_Shield = shields("Iron Shield", 10, 20, 100)

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
    Goblin.deff = Rusty_Shield.shield_plus_deff + Goblin.deff

def hobgoblin_items():
    Hobgoblin.weapon = Club.weapon_name
    Hobgoblin.shield = Iron_Shield.shield_name
    Hobgoblin.attck = Club.weapon_plus_attack + Hobgoblin.attck
    Hobgoblin.deff = Iron_Shield.shield_plus_deff + Hobgoblin.deff

def skeleton_items():
    Skeleton.weapon = Rusty_Sword.weapon_name
    Skeleton.shield = Rusty_Shield.shield_name
    Skeleton.attck = Rusty_Sword.weapon_plus_attack + Skeleton.attck
    Skeleton.deff = Rusty_Shield.shield_plus_deff + Skeleton.deff

is_hobgoblin_available = False

def hobgoblin_appear():
    global is_hobgoblin_available
    if kills >= 20:
        is_hobgoblin_available = True
        print ("[H] to fight hobgoblin")

"""             Merchant functions               """
p_price = 20
def pots():
        global gold,potions
        print ()
        print("Do you want to buy potion? for 20 gold")
        print ()
        print("Potion: gives player +50 health")
        choice = str(input("Type and enter [Y] for yes and [N] for no: "))
        if choice == 'y' or choice == 'Y':
            if gold < p_price:
                print("not enough gold!")
            else:
                print(name + " bought 1 potion/s" )
                gold = gold - p_price
                potions = potions + 1
                get_stats()
                print("Would you like to purchase more?")
                view_catalogue()
        elif choice == 'n' or choice == 'N':
            view_catalogue()
        else:
            print("Please enter a valid choice!")
            pots()
def buy():
    print()
    print ("Welcome to dungeon store!")
    print()
    print(name + "'s gold: " + str(gold))
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
    print(name + "'s gold: " + str(gold))
    print()
    print("****************************")
    print("          Weapons           ")
    print("****************************")
    print("[RSW] Rusty Sword for 20 gold")
    print("[BSW] Broadsword for 50 gold")
    print("[BOW] Bow for 10 gold")
    print("[ISW] Iron Sword for 30 gold")
    print("[CLB] Club for 100 gold")
    print("****************************")
    print()
    print("****************************")
    print("          Shields           ")
    print("****************************")
    print("[RSH] Rusty Shield for 20 gold")
    print("[LSH] Leather_Shield for 50 gold")
    print("[ISH] Iron Shield for 100 gold")
    print("****************************")
    print()
    print("****************************")
    print("          Armors            ")
    print("****************************")
    print("[LAR] Leather armor for 40 gold")
    print("[CAR] Chain Armor for 100 gold")
    print("****************************")
    print()
    print("****************************")
    print("        Consumables         ")
    print("****************************")
    print("[POT] potion for 20 gold")
    print("****************************")
    print()
    choice = str(input("Please enter your choice here or type and enter [Q] to go back: "))
    if choice == 'q' or choice == 'Q':
        player_action()
    elif choice == 'RSW' or choice == 'rsw':
        weapons.prices(Rusty_Sword)
    elif choice == 'BSW' or choice == 'bsw':
        weapons.prices(Broadsword)
    elif choice == 'BOW' or choice == 'bow':
        weapons.prices(Bow)
    elif choice == 'ISW' or choice == 'isw':
        weapons.prices(Iron_Sword)
    elif choice == 'CLB' or choice == 'clb':
        weapons.prices(Club)
    elif choice == 'LAR' or choice == 'lar':
        armor.prices(Leather_Armor)
    elif choice == 'CAR' or choice == 'car':
        armor.prices(Chain_Armor)
    elif choice == 'RSH' or choice == 'rsh':
        shields.prices(Rusty_Shield)
    elif choice == 'LSH' or choice == 'lsh':
        shields.prices(Leather_Shield)
    elif choice == 'ISH' or choice == 'ish':
        shields.prices(Iron_Shield)
    elif choice == 'POT' or choice == 'pot':
        pots()
    else:
        print ("Please enter a valid choice!")
        view_catalogue()

"""             Boss Fight              """
monsters_var()
hobgoblin_items()
def fight_choice_boss():
    """Players gets to select what to do while in the dungeon"""
    global health,gold, kills
    fight = True;
    while fight:
    #Checks for health status for both players and monsters
        if health <= 0:
            health = 0
            print ("Game Over")
            break
        if  Hobgoblin.health <=0:
            Hobgoblin.health == 0
            monsters.monster_regen(Goblin)
            print()
            print(Hobgoblin.m_name + ' is defeated ')
            print("You get " + str(Hobgoblin.gold) + " gold!")
            gold = gold + Hobgoblin.gold
            kills = kills + 1
            print("Congratulations!")
            exit()
            break
    #Handles decicion
        get_m_stats_boss()
        print("What would you like to do? ")
        choice = str(input("type and enter [A] to attack and [R] to run [P] to use a potion: "))
        if choice == 'A' or choice == 'a':
            #an exchange of attack sequence between the player and the boss
            player_fight_boss()
            monster_fight_boss()
            fight_choice_boss()
        elif choice == 'R' or choice == 'r':
            print("You died while running!")
            exit()
        elif choice == 'P' or choice == 'p':
            apply_potion()
            fight_choice_boss()
        else:
            print("Please enter a valid choice!")
            fight_choice()

def player_fight_boss():
    """Player fight action if he/she choose [A]"""
    global attck
    deffence = Hobgoblin.deff
    get_percentage = deffence / 100
    get_final_percentage = attck * get_percentage
    get_final_damage = int(attck - get_final_percentage)
    print()
    print (str(name) + " attacked " + str(Hobgoblin.m_name) + " for " + str(get_final_damage) + " Damage!")
    print()
    Hobgoblin.health = Hobgoblin.health - get_final_damage
    get_m_stats_boss()

def monster_fight_boss():
    """Mosnter automatic fighting sequence"""
    global health,deffence
    attack = Hobgoblin.attck
    get_percentage = deffence / 100
    get_final_percentage = attack * get_percentage
    get_final_damage = int(attack - get_final_percentage)
    print (str(Hobgoblin.m_name) + " attacked " + str(name) + " for " + str(get_final_damage) + " Damage!")
    print()
    health = health - get_final_damage
    get_stats()

def get_m_stats_boss():
    """Show Monster Status"""
    print ("Name: " + str(Hobgoblin.m_name))
    print ("Health: " + str(Hobgoblin.health) + "/" + str(Hobgoblin.max_health))
    print ("Attack: " + str(Hobgoblin.attck))
    print ("Deffence: " + str(Hobgoblin.deff))
    print()
    #prints monster's items
    print ("Weapon: " + Hobgoblin.weapon)
    print ("Shield: " + Hobgoblin.shield)
    print ()
"""             Functions               """

def random_fountain():
    global is_fountain_visible
    x = random.random()
    chance = int(x * 100)
    if chance <= 37:
        is_fountain_visible = True
        print ("[F] to fountain of joy")
    else:
        is_fountain_visible = False




#Random Monsters Variables
def gen_random_monster():
    """Radom monster Generator"""
    global random_index,random_monster
    random_index = random.randrange(0,4)
    random_monster = monsters.instances[random_index]

def get_name():
    """A function to get player name
    note: this will be only be called once!
    """
    global name
    name = str(input("Please enter your name: "))
    print ("So your name is: " + name)
    choice =  str(input("if Yes type [Y] and if no type [N]: "))
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
    print (name + "'s health is: " + str(health) + "/" + str(max_health))
    print (name + "'s deffence is: " + str(deffence))
    print (name + "'s attack is: " + str(attck))
    print ()
    #prints player's items
    print (name + "'s weapon is: " + str(weapon))
    print (name + "'s armor is:" + str(p_armor))
    print (name + "'s shield is: " + str(shield))
    print (name + "'s potion count is: " + str(potions))
    print (name + "'s gold is: " + str(gold))
    print ()
    print (name + "'s kills:" + str(kills))
    print()

def get_m_stats():
    """Show Monster Status"""
    print ("Name: " + str(random_monster.m_name))
    print ("Health: " + str(random_monster.health) + "/" + str(random_monster.max_health))
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
    global health,gold, kills
    fight = True;
    while fight:
    #Checks for health status for both players and monsters
        if health <= 0:
            health = 0
            print ("Game Over")
            break
        if random_monster.health <=0:
            random_monster.health == 0
            monsters.monster_regen(random_monster)
            print()
            print(random_monster.m_name + ' is defeated ')
            print("You get " + str(random_monster.gold) + " gold!")
            gold = gold + random_monster.gold
            kills = kills + 1
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



def fight_action():
    """Fighting aspect of the game"""

    #generate monster instances
    monsters_var()

    #Generate random monster
    gen_random_monster()

    #Check for monster name if it has an items
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
    random_fountain()
    hobgoblin_appear()
    print ("[B] to buy")
    print ("[S] to view stats")
    print ("[U] to use potion")
    choice = str(input("Please type and enter here: "))
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
        if is_fountain_visible:
            fountain()
    elif choice == 'h' or choice == 'H':
        #Fights the boss of te game
        if is_hobgoblin_available:
            fight_choice_boss()
    elif choice == 'B' or choice == 'b':
        buy()
    elif choice == 's' or choice == 'S':
        get_stats()
        player_action()
    elif choice == 'U' or choice == 'u':
        apply_potion()
        player_action()
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
