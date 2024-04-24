import time
import random

def slowprint(sentence, x):
    for char in sentence:
        print(char, end="", flush=True)
        time.sleep(x)
    print()

print("In the continent of Aspada, 500 years ago, there lived 50 million humans under the servitude of 50 thousand beings called \"Kaidoz\", \nhybrids between humans and dragons possessing immense power.", 0.06)
print("After two thousand years of enslavement and offering sacrifices to them, three wars were waged against them, all of which failed.", 0.06)
print("Ten years after the last war against them, Mihawk, Sasaki, and Ryoma, the strongest men on the continent, decided to eliminate all the Kaidoz.", 0.06)
print("Their power had terrorized the Kaidoz's realm, with each of them wielding a legendary weapon.", 0.06)
print("Mihawk possessed a sword called Yuro, so powerful that it could cleave a whole mountain with one strike, crafted by the most skilled blacksmith in history.", 0.06)
print("Sasaki had a gemstone named Anma that multiplied its wielder's power every time they received a blow.\n Legend has it that this gem was a gift from the King of Djinn to the sorcerer Tarish after he saved his daughter.\nAs for Ryoma, he had a glove called Sinistro with a hole on the palm, granting the ability to stop time and rewind it 20 seconds, increasing the wielder's strength.\nThis glove was stolen from the Timelems, creatures from the parallel world.", 0.06)
print("When these weapons gathered with their powerful wielders, they managed to eradicate the Kaidoz in the Fourth Kaidoz War and sealed them in a jar placed inside a cave called \"Canavar,\" the same name as their leader,\ndue to the immense power of these weapons. However, the users of these weapons died a month later after suffering from excruciating pain.",0.06)



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


def fight(attacker, defender):
    while attacker.health > 0 and defender.health > 0:
        print("Enter your choice:")
        print("1. Attack")
        print("2. Defense")
        choice = int(input())

        if choice == 1:
            attack(attacker, defender)
        elif choice == 2:
            defend(defender)


slowprint("Part One: Exiting Storm City", 0.06)
slowprint("Our story begins with a person named Kyoku Bankai.", 0.06)
slowprint("His mother's condition worsened until he summoned a doctor, who diagnosed her with a rare illness.", 0.06)

choice = int(input(
    "What do you want to do? (1. Let's go to the market, 2. Let's go to the doctor, 3. Let's watch my mum die): "))

if choice == 1:
    slowprint("It's not the appropriate time to go shopping; we should save my mum.", 0.06)
    current_location = "home"
elif choice == 2:
    slowprint("He must now bring the doctor to his mother. Let's go to the doctor.", 0.06)
    current_location = "doctor"
else:
    slowprint("Your mum has died. Thank you for wasting your time watching your mum die without playing.", 0.06)
    exit()



while True:
    print("You are at", current_location)

    if current_location == "home":
        direction = input("Where do you want to go? (doctor/market): ")
        if direction == "doctor":
            current_location = "doctor"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "market":
        direction = input("Where do you want to go? (sea/dam/home): ")
        if direction == "sea":
            current_location = "sea2"
        elif direction == "dam":
            current_location = "dam"
        elif direction == "home":
            current_location = "home"
        else:
            print("Please choose a valid direction")

    elif current_location == "doctor":
        print("You have reached the doctor!")
        slowprint("The doctor sees your mother and gives a list of medicine ingredients:", 0.06)
        slowprint(
            "1. Chamomile herb (rosenbelle)\n2. Black elderberry herb (winterland)\n3. Ginseng herb (bummer)\n4. Echinacea herb (savana)\n5. Ginkgo Biloba herb (canavar)",
            0.06)
        break

    elif current_location == "dam":
        print("You are at the dam, you cannot go here.")
        direction = input("Where do you want to go? (sea/market): ")
        if direction == "sea":
            current_location = "sea3"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "sea2":
        print("It's not the appropriate time to swim; we should save my mum.")
        direction = input("Where do you want to go? (doctor/market): ")
        if direction == "doctor":
            current_location = "doctor"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "sea3":
        print(
            "It's not the appropriate time to swim; we should save my mum. Let's go back to the dam to go to the doctor.")
        current_location = "dam"
