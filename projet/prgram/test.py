import time
import random
def slowprint(sentence, x):
    for char in sentence:
        print(char, end="", flush=True)
        time.sleep(x)
    print()

class Bankai:
    def __init__(self):
        self.name = "Bankai"
        self.power = 100
        self.health = 100

class Enemy:
    def __init__(self, name="Unknown"):
        self.name = name
        self.power = 100
        self.health = 100

def attack(attacker, defender):
    player_damage = random.randint(0, 20) * attacker.power / 100
    defender.health -= player_damage
    enemy_damage = random.randint(0, 20) * defender.power / 100
    attacker.health -= enemy_damage
    print(f"{attacker.name} attacks and deals {player_damage} damage to {defender.name}!")
    print(f"{defender.name} attacks and deals {enemy_damage} damage to {attacker.name}!")


def defend(defender):
    enemy_damage = random.randint(0, 10) * defender.power / 100
    defender.health -= enemy_damage
    print(f"{defender.name} defends and receives {enemy_damage} damage from the enemy!")


def fight(power, health, chance):
    while health > 0:
        slowprint("Enter your choice:")
        slowprint("1. Attack")
        slowprint("2. Defense")
        choice = int(input())

        if choice == 1:
            player_damage = random.randint(0, 20) * power / 100
            enemy_damage = random.randint(0, 20) * power / 100
            slowprint("You attack and deal " + str(player_damage) + " damage to the enemy!")
            slowprint("The enemy attacks and deals " + str(enemy_damage) + " damage to you!")
            health -= enemy_damage
        elif choice == 2:
            enemy_damage = random.randint(0, 10) * power / 100
            slowprint("You defend and receive " + str(enemy_damage) + " damage from the enemy!")
            health -= enemy_damage



slowprint("In the continent of Aspada, 500 years ago, there lived 50 million humans under the servitude of 50 thousand beings called \"Kaidoz\", \nhybrids between humans and dragons possessing immense power.", 0.06)
slowprint("After two thousand years of enslavement and offering sacrifices to them, three wars were waged against them, all of which failed.", 0.06)
slowprint("Ten years after the last war against them, Mihawk, Sasaki, and Ryoma, the strongest men on the continent, decided to eliminate all the Kaidoz.", 0.06)
slowprint("Their power had terrorized the Kaidoz's realm, with each of them wielding a legendary weapon.", 0.06)
slowprint("Mihawk possessed a sword called Yuro, so powerful that it could cleave a whole mountain with one strike, crafted by the most skilled blacksmith in history.", 0.06)
slowprint("Sasaki had a gemstone named Anma that multiplied its wielder's power every time they received a blow.\n Legend has it that this gem was a gift from the King of Djinn to the sorcerer Tarish after he saved his daughter.\nAs for Ryoma, he had a glove called Sinistro with a hole on the palm, granting the ability to stop time and rewind it 20 seconds, increasing the wielder's strength.\nThis glove was stolen from the Timelems, creatures from the parallel world.", 0.06)
slowprint("When these weapons gathered with their powerful wielders, they managed to eradicate the Kaidoz in the Fourth Kaidoz War and sealed them in a jar placed inside a cave called \"Canavar,\" the same name as their leader,\ndue to the immense power of these weapons. However, the users of these weapons died a month later after suffering from excruciating pain.",0.06)

current_location = "home"

while True:
    print("You are at", current_location)
    
    if current_location == "home":
        direction = input("Where do you want to go? (right/north): ")
        if direction == "right":
            current_location = "doctor"
        elif direction == "left":
            current_location = "market"
        else:
            print("Please choose a valid direction")
    
    elif current_location == "market":
        direction = input("Where do you want to go? (right/north/south): ")
        if direction == "right":
            current_location = "sea2"
        elif direction == "north":
            current_location = "dam"
        elif direction == "south":
            current_location = "home"
        else:
            print("Please choose a valid direction")
    
    elif current_location == "doctor":
        print("You have reached the doctor!")
        break
    
    elif current_location == "dam":
        print("You are at the dam, you cannot go here.")
        direction = input("Where do you want to go? (right/south): ")
        if direction == "right":
            current_location = "sea3"
        elif direction == "south":
            current_location = "market"
        else:
            print("Please choose a valid direction")
    
    elif current_location == "sea2"
        print("You are at the sea, you cannot go here.")
        direction = input("Where do you want to go? (south/left): ")
        if direction == "south":
            current_location = "doctor"
        elif direction == "left":
            current_location = "market"
        else:
            print("Please choose a valid direction")
 
    elif current_location == "sea3"
        print("You are at the sea, you cannot go here.")
        direction = input("Where do you want to go? (south/left): ")
        if direction == "south":
            current_location = "sea2"
        elif direction == "left":
            current_location = "dam"
        else:
            print("Please choose a valid direction")
