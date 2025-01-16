import time
import os
import subprocess
import random
from Arts import *

def clear():
    input("Press Enter to clear the screen...")
    if os.name == 'nt':  # Windows
        subprocess.run('cls')
    else:  # Unix/Linux/MacOS
        subprocess.run('clear', shell=True)


def lucky():
    return random.randrange(0, 100)


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
        self.defence = 30


Bankai = Bankai()


class jhon:
    def __init__(self, name="jhon"):
        self.name = name
        self.power = 100
        self.health = 100
        self.defence = 30


jhon = jhon()


class prince:
    def __init__(self, name="prince of suduma"):
        self.name = name
        self.power = 50
        self.health = 120
        self.defence = 30


prince = prince()


class Ares:
    def __init__(self, name="Ares"):
        self.name = name
        self.power = 870
        self.health = 1200
        self.defence = 50


Ares = Ares()


class haouari:
    def __init__(self, name="El-haouari"):
        self.name = name
        self.power = 223
        self.health = 250
        self.defence = 70


haouari = haouari()


class enemy:
    def __init__(self, name="the enemy"):
        self.name = name
        self.power = 250
        self.health = 300
        self.defence = 40


enemy = enemy()


class strenemy:
    def __init__(self, name="strong enemy"):
        self.name = name
        self.power = 600
        self.health = 500
        self.defence = 30


strenemy = strenemy()


class martin:
    def __init__(self, name="martin"):
        self.name = name
        self.power = 600
        self.health = 450
        self.defence = 20


martin = martin()


class elder:
    def __init__(self, name="the elder"):
        self.name = name
        self.power = 600
        self.health = 1000
        self.defence = 30


elder = elder()


class lizard:
    def __init__(self, name="the lizard"):
        self.name = name
        self.power = 20000
        self.health = 30000
        self.defence = 48


lizard = lizard()

class monsterY:
    def __init__(self, name="The monster of Yskina"):
        self.name = name
        self.power = 30000
        self.health = 100000
        self.defence = 34
monsterY = monsterY()


class Bankai0:
    def __init__(self, name="Bankai with form of Kaidoz"):
        self.name = name
        self.power = 1500
        self.health = 1000
        self.defence = 50


Bankai0 = Bankai0()


class Bankai1:
    def __init__(self, name="Bankai with the first form of Kaidoz"):
        self.name = name
        self.power = 10000
        self.health = 30000
        self.defence = 50


Bankai1 = Bankai1()


class Bankai2:
    def __init__(self, name="Bankai with the second form of Kaidoz"):
        self.name = name
        self.power = 30000
        self.health = 40000
        self.defence = 50


Bankai2 = Bankai2()


class Bankai3:
    def __init__(self, name="Bankai with the third form of Kaidoz"):
        self.name = name
        self.power = 50000
        self.health = 100000
        self.defence = 50


Bankai3 = Bankai3()


class Bankai4:
    def __init__(self, name="Bankai with the third form of Kaidoz"):
        self.name = name
        self.power = 800000
        self.health = 1000000
        self.defence = 50


Bankai4 = Bankai4()


class suduma:
    def __init__(self, name="suduma"):
        self.name = name
        self.power = 100000
        self.health = 100000
        self.defence = 85


class kaidos:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidos = kaidos()

class kaidosbi:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidosbi = kaidosbi()

class kaidosvir:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidosvir = kaidosvir()

class kaidosst:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidosst = kaidosst()

class kaidosbu:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidosbu = kaidosbu()

class kaidossu:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidossu = kaidossu()

class kaidoswi:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidoswi = kaidoswi()

class kaidosro:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidosro = kaidosro()

class kaidossa:
    def __init__(self, name="kaidos"):
        self.name = name
        self.power = 300000
        self.health = 150000
        self.defence = 40


kaidossa = kaidossa()


class canavar:
    def __init__(self, name="canavar"):
        self.name = name
        self.power = 500000
        self.health = 800000
        self.defence = 60


canavar = canavar()


def wronganswer(damage):
    Bankai.health -= damage
    print("Wrong answer")
    print(f"your health now is {Bankai.health}")
    if Bankai.health <= 0:
        print("Game over! Your health reached zero.")
        exit()


def gard(damage):
    Bankai.health -= damage
    print("What do you think you're doing? He is the guard.")
    print(f"your health now is {Bankai.health}")
    if Bankai.health <= 0:
        print("Game over! Your health reached zero.")
        exit()


def attack(attacker, defender):
    player_damage = lucky() * attacker.power / 100
    defender.health -= player_damage
    enemy_damage = lucky() * defender.power / 100
    attacker.health -= enemy_damage
    print(f"{attacker.name} attacks and deals {player_damage} damage to {defender.name}!")
    print(f"{defender.name} attacks and deals {enemy_damage} damage to {attacker.name}!")


def defend(attacker, defender):
    attacker_damage = lucky() * attacker.power / 100
    defender_damage = lucky() * defender.power / 100
    defender.health -= attacker_damage * (1 - defender.defence / 100)
    attacker.health -= defender_damage * (1 - attacker.defence / 100)
    print(f"{defender.name} defends and receives {attacker_damage} damage from the enemy!")
    print(f"{attacker.name} also receives {defender_damage} damage while defending!")


def fight(attacker, defender, newhealth, newpower, oldhealth):
    while defender.health > 0:
        while attacker.health > 0 and defender.health > 0:
            print("Enter your choice:")
            print("1. Attack")
            print("2. Defense")
            choice = int(input())

            if choice == 1:
                attack(attacker, defender)
            elif choice == 2:
                defend(defender, attacker)
            else:
                print("Invalid choice. Please choose 1 or 2.")

        if attacker.health <= 0:
            print(f"{defender.name} has {defender.health} health remaining.")
            print("You lose. Restarting the fight...")
            print(f"Your health increased. Your new health is {newhealth}")
            print(f"Your power increased. Your new power is {newpower}")
            attacker.health = newhealth
            attacker.power = newpower
            defender.health = oldhealth
        else:
            print(f"You beat {defender.name} and your health now is {attacker.health}")
            break


def fightl(attacker, defender):
    while attacker.health > 0 and defender.health > 0:
        print("Enter your choice:")
        print("1. Attack")
        print("2. Defense")
        choice = int(input())

        if choice == 1:
            attack(attacker, defender)
        elif choice == 2:
            defend(defender, attacker)
    if attacker.health > 0:
        print(f"you beat {defender.name} and your health now is {attacker.health}")
    else:
        print(f"{defender.name} and his health is {defender.health}")
        print("You lose")
        print("You've let your emotions take control of you. Now you're a monster resembling the Kaidoz.")


# the part of the story of the game
print(rockstar)
time.sleep(5)
subprocess.run('cls')
print(present)
time.sleep(3)
subprocess.run('cls')
print(castel)
print(cannavar)
time.sleep(5)
subprocess.run('cls')

slowprint(
    "In the continent of Aspada, 500 years ago, there lived 50 million humans under the servitude of 50 thousand beings called \"Kaidoz\", \nhybrids between humans and dragons possessing immense power.", 0.06)
print(
    "After two thousand years of enslavement and offering sacrifices to them, three wars were waged against them, all of which failed.")
print(
    "Ten years after the last war against them, Mihawk, Sasaki, and Ryoma, the strongest men on the continent, decided to eliminate all the Kaidoz.")
print("Their power had terrorized the Kaidoz's realm, with each of them wielding a legendary weapon.")
print(
    "Mihawk possessed a sword called Yuro, so powerful that it could cleave a whole mountain with one strike, crafted by the most skilled blacksmith in history.")
print(
    "Sasaki had a gemstone named Anma that multiplied its wielder's power every time they received a blow.\n Legend has it that this gem was a gift from the King of Djinn to the sorcerer Tarish after he saved his daughter.\nAs for Ryoma, he had a glove called Sinistro with a hole on the palm, granting the ability to stop time and rewind it 20 seconds, increasing the wielder's strength.\nThis glove was stolen from the Timelems, creatures from the parallel world.")
print(
    "When these weapons gathered with their powerful wielders, they managed to eradicate the Kaidoz in the Fourth Kaidoz War and sealed them in a jar placed inside a cave called \"Canavar,\" the same name as their leader,\ndue to the immense power of these weapons. However, the users of these weapons died a month later after suffering from excruciating pain.")
clear()
# the first part of the game
slowprint("chapter One: Exiting Shtorm City", 0.06)
print("Our story begins with a person named Kyoku Bankai.")
print(
    "From a remote village in the city of Shturm, he was raised by his mother and grandfather. \nHis grandfather taught him the martial arts, and he became very strong. \nAfter his grandfather passed away, his mother continued to take care of him.\nThis motivated him to keep learning combat skills so he could protect his mother.")
print("Years later, her mother's condition worsened and she developed a rare disease.")
current_location = "home"

choice = input(
    "What do you want to do? (1. Let's go to the market, 2. Let's go to the doctor, 3. Let's watch my mum die): ")

while choice != 2:
    if choice == 1:
        print("It's not the appropriate time to go shopping; we should save my mum.")
        current_location = "home"
        choice = int(input())
    elif choice == 2:
        print("He must now bring the doctor to his mother. Let's go to the doctor.")
        current_location = "home"
    elif choice == 3:
        print("Your mum has died. Thank you for wasting your money watching your mum die without playing.")
        exit()
    else:
        print("Invalid choice. Please try again.")
        choice = int(input())

while current_location != "doctor":
    print("You are at", current_location)

    if current_location == "home":
        direction = input("Where do you want to go? (doctor/market): ").lower()
        if direction == "doctor":
            current_location = "doctor"
            print("You have reached the doctor! let take the doctor to my mom.")
            break
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "market":
        direction = input("Where do you want to go? (sea/dam/home): ").lower()
        if direction == "sea":
            current_location = "sea2"
        elif direction == "dam":
            current_location = "dam"
        elif direction == "home":
            current_location = "home"
        else:
            print("Please choose a valid direction")

    elif current_location == "dam":
        print("You are at the dam, you cannot go here.")
        direction = input("Where do you want to go? (sea/market): ").lower()
        if direction == "sea":
            current_location = "sea3"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "sea2":
        print("It's not the appropriate time to swim; we should save my mum.")
        direction = input("Where do you want to go? (doctor/market): ").lower()
        if direction == "doctor":
            current_location = "doctor"
            print("You have reached the doctor! let take the doctor to my mom.")
            break
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "sea3":
        print(
            "It's not the appropriate time to swim; we should save my mum. Let's go back to the dam to go to the doctor.")
        current_location = "dam"

while current_location != "home":
    print("You are at", current_location)

    if current_location == "doctor":
        direction = input("Where do you want to go? (home/sea1/sea2): ").lower()
        if direction == "home":
            current_location = "home"
            print("The doctor sees your mother and gives a list of medicine ingredients:")
            print(
                "1. Chamomile herb (rosenbelle)\n2. Black elderberry herb (winterland)\n3. Ginseng herb (bummer)\n4. Echinacea herb (savana)\n5. Ginkgo Biloba herb (canavar)")
            break
        elif direction == "sea1" or direction == "sea2":
            print(
                "It's not the appropriate time to swim; we should save my mum. Let's go back to the dam to go to the doctor.")
        else:
            print("Please choose a valid direction")

clear()

print("you face a group of bandits.\ndo you wanna fight them")
choice = 1
while choice != 2:
    print("1.run\n2.fight")
    choice = int(input())
    if choice == 1:
        Bankai.health = Bankai.health - 1
        print("you get attacked by them.")
        print(f"your health now is {Bankai.health}")
        if Bankai.health == 0:
            exit()
    elif choice == 2:
        print("Great you defeated them; they were weak, but be careful, for the upcoming battles will not be easy.")
        break
    else:
        print("Invalid choice. Please try again.")

clear()
# the second part of the game
slowprint("chapter two: In the most beautiful city", 0.06)
def kill_jinbi():
    print(
        "He sat with his friend in his house and they talked about the old days and about their friend Martin, who was also one of his grandfather's students.")
    print("The night was dark, and as they were talking, they heard a scream outside.")
    goto_jinbi = False
    while not goto_jinbi:
        print("Do you want to go out to see what happened?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            print(
                "Bankai went to see, and he found the old man Jinbei lying on the ground, saying to three people wearing the official attire of the kingdom of Suduma, one of whom was its prince.")
            print(
                "The old man said, 'I know what you want from this marriage. You want to conquer the kingdom of Rosenbelle as you did with other kingdoms. I won't allow you to kill the king or his son.' The prince raised his sword in the air and struck him down.")
            print(
                "Bankai returned to John and told him what he had seen. He wasn't surprised by this evil, as it's a custom of the Suduma kingdom to do anything for the purpose of occupying other kingdoms. Now Bankai wants to save the kingdom of Rosenbelle.")
            goto_jinbi = True
        elif choice == "2":
            print("The scream is still outside. I think you should go to see what happened.")
        else:
            print("Invalid choice. Please try again.")


def market_rose():
    print(
        "He asked some of the merchants in the city if anyone knew the chamomile herb. No one knew its whereabouts, but a blacksmith directed him to an old man named Jinbi who knew a lot about herbs.")
    print(
        "Bankai went to the place of that old man, and he told him that he wouldn't tell him where it is until he answered his riddle. He said: \"He does not walk, yet he always comes. He has no eyes, yet he always cries. What is he?\"")
    while True:
        print("What is the correct answer:")
        print("1. Candle\n2. Cloud\n3. Moon")
        print("Warning: wrong answer takes 10 points of health.")
        choice = input()
        if choice == "1" or choice == "3":
            wronganswer(10)
        elif choice == "2":
            print("Great! Your answer is correct.")
            print(
                "It is located in the king's palace and grows once every year, but you must wait three days to speak with him because his daughter's wedding will be held tomorrow.")
            return True
        else:
            print("Invalid choice. Please try again.")

current_location = "start"
visit_john = False
visit_market = False

while visit_john == False or visit_market == False:
    print("You are at", current_location)

    if current_location == "start":
        direction = input("Where do you want to go? (john/market): ").lower()
        if direction == "john":
            current_location = "john"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")
    elif current_location == "john":
        if not visit_john:
            print(
                "Bankai meets John, his childhood friend and one of his grandfather's students, who managed to defeat him in his childhood.\n And john told john about the reason why he is here.")
            visit_john = True
        else:
            pass
        if not visit_market:
            print("John: We should go to the market now to get the chamomile herb.")
            choice = 0
            while choice != 1:
                choice = int(input("Do you wanna go to the market: \n1. Yes\n2. No\n"))
                if choice == 1:
                    current_location = "market"
                elif choice == 2:
                    print("John: But you should go to save your mum.")
                else:
                    print("Invalid choice. Please try again.")
        else:
            kill_jinbi()
    elif current_location == "market":
        if visit_market == False:
            visit_market = market_rose()
            direction = input("Where do you want to go? (john/start): ").lower()
            if direction == "john":
                current_location = "john"
            elif direction == "start":
                current_location = "start"
            else:
                print("Please choose a valid direction")
        else:
            print("We were here. What are you doing?")
            direction = input("Where do you want to go? (john/start): ").lower()
            if direction == "john":
                current_location = "john"
            elif direction == "start":
                current_location = "start"
            else:
                print("Please choose a valid direction")
clear()
while current_location != "castel":
    if current_location == "start":
        direction = input("What is your next direction: \njohn\nsea\ncastle\n").lower()
        if direction == "sea":
            current_location = "sea"
        elif direction == "castle":
            current_location = "castle"
        elif direction == "john":
            current_location = "john"
        else:
            print("Please choose a valid direction")

    elif current_location == "sea":
        print("It's not the appropriate time to swim; we should save my mum.")
        current_location = "start"

    elif current_location == "market":
        direction = input("What is your next direction: \ncastel\nstart\nsea\n").lower()
        if direction == "castel":
            current_location = "castel"
        elif direction == "start":
            current_location = "start"
        elif direction == "sea":
            current_location = "sea"
        else:
            print("Please choose a valid direction")

    elif current_location == "john":
        direction = input("What is your next direction: \ncastel\nstart\n").lower()
        if direction == "castel":
            current_location = "castel"
        elif direction == "start":
            current_location = "start"
        else:
            print("Please choose a valid direction")

    elif current_location == "castel":
       break
    else:
        print("Please choose a valid direction")
clear()
print("Gatekeeper: This place is not meant for people like you. Go away from here.")
choice = 0
while choice != 2:
    choice = int(input("what do you want :\n1. fight him\n2. go to the window\n3. resign\n"))
    if choice == 1:
        gard(10)
    elif choice == 3:
        exit()
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")

current_location = "window"

print(
    "Bankai entered the castle through the back window without being seen by anyone. Now he has to search for the person who wants to assassinate the king and his daughter.")

if Bankai.health >= 70:
    print("Hint : they are in the basement.")

location_count = {"wedding": 0, "kitchen": 0, "the store": 0, "basement": 0, "window": 0, "door": 0}
print("Warning : if you go to the same place 3 times the guards will know that you're intruder ")
current_location = "window"
clear()
while current_location != "basement":
    if current_location in location_count:
        location_count[current_location] += 1
        if location_count[current_location] > 3:
            print("You have gone to the same place more than 3 times. You lose!")
            exit()

    if current_location == "wedding":
        print("You are in the wedding now. And there is nothing here.")
        direction = input("Where do you want to go? (window/kitchen): ").lower()
        if direction == "window":
            current_location = "window"
        elif direction == "kitchen":
            current_location = "kitchen"
        else:
            print("Please choose a valid direction")

    elif current_location == "window":
        print("You are at the window now. And there is nothing here.")
        direction = input("Where do you want to go? (wedding/kitchen/the store): ").lower()
        if direction == "wedding":
            current_location = "wedding"
        elif direction == "kitchen":
            current_location = "kitchen"
        elif direction == "the store":
            current_location = "the store"
        else:
            print("Please choose a valid direction")

    elif current_location == "kitchen":
        print("You are in the kitchen now. And there is nothing here.")
        direction = input("Where do you want to go? (door/wedding/basement/window): ").lower()
        if direction == "door":
            current_location = "door"
            print("The guard caught you. You lose!")
            exit()
        elif direction == "wedding":
            current_location = "wedding"
        elif direction == "basement":
            current_location = "basement"
        elif direction == "window":
            current_location = "window"
        else:
            print("Please choose a valid direction")
    elif current_location == "the store":
        print("You are in the store now. And there is nothing here.")
        direction = input("Where do you want to go? (basement/window): ").lower()
        if direction == "basement":
            current_location = "basement"
        elif direction == "window":
            current_location = "window"
        else:
            print("Please choose a valid direction")
    elif current_location == "basement":
        break

clear()
if current_location == "basement":
    print("You are at the Basement now and you find the prince of sudumma")
    print("Now you should fight him")
    fight(Bankai, prince, 100, 100, 120)

print(
    "Bankai saved the kingdom of Rosenbelle. \nAt first, everyone was in shock. As for the attendees from the kingdom of Suduma, it was a small delegation, and not many military figures were present to avoid arousing suspicion among the inhabitants of Rosenbelle. \nTherefore, the king of Suduma ordered the prince's body to be taken and the delegation to withdraw.")
print(
    "After this incident, the king invited Bankai to hear his story and was impressed by his bravery and determination to save his mother. \nThe king gave him the chamomile herb, and Bankai left the kingdom of Rosenbelle accompanied by his friend John.")
choice = int(input("Do you wanna see a doctor before you go to Winterland ?\n1. Yes\n2. No\n"))
if choice == 1:
    Bankai.health = 100
elif choice == 2:
    pass
else:
    print("Invalid choice.")
clear()
#the part 3 of the game
slowprint("chapter three: Coldest city", 0.06)
current_location = "start"

def grave():
    winter = False
    print(
        "Bankai and John went to the cemetery where prominent figures are buried to search for Rasputin's tomb.\nThey found the guard at the cemetery gate, who did not allow them to enter.")
    while winter == False:
        choice = int(input("What do you want to do now?\n1. fight\n2. search another way to get in\n"))
        if choice == 1:
            gard(10)
        elif choice == 2:
            current_location = "door"
            river = False
            while not winter:
                if current_location == "door":
                    direction = input("What is your next direction: \nleft side\nback\nriver\n").lower()
                    if direction == "left side":
                        current_location = "left side"
                    elif direction == "back":
                        current_location = "back"
                    elif direction == "river":
                        current_location = "river"
                elif current_location == "back":
                    print("we can't resign now we should save your mum.")
                    current_location = "door"
                elif current_location == "river":
                    if not river:
                        Bankai.health = 500
                        print("wow you get increase in your health")
                        current_location = "door"
                    else:
                        current_location = "door"
                        print("now there is nothing we to do here let's go back to the door")
                elif current_location == "left side":
                    print(
                        "They coincidentally met the king of the Winterland kingdom, the youngest king of the continent of Espada.\nHe shook Bankai's hand firmly and asked, 'Are you Bankai?' \nBankai answered, 'Yes.'\nThe king said, 'Thank you very much for what you did in the kingdom of Rosenbelle. I did not want their princess to marry the prince of Suduma.I hated him, and I also wanted to marry her myself.'")
                    print(
                        "The king asked why they had come to the cemetery and how they knew about Suduma's plan.\nBancai told him about his story, his mother, and the death of the old man Jinbei.\nThe king said to them, 'Come, you will enter with me into the cemetery.\nI also want to go there to visit my father's grave.\nHe died in the Third Kaidos War twelve years ago, so I became the king of Winterland at the age of six.'")
                    print("And after a series of conversations, they parted ways.")
                    print(
                        "The king asked why they had come to the cemetery and how they knew about Suduma's plan.\nBankai told him about his story, his mother, and the death of the old man Jinbei.\nThe king said to them, 'Come, you will enter the cemetery with me.\nI also want to go there to visit my father's grave.\nHe died in the Third Kaidos War twelve years ago, so I became the king of Winterland at the age of six.'\nAfter a series of conversations, they parted ways.\n\nBankai asked his friend John if the former king of the kingdom took the throne a year after Rasputin's death and died twenty-three years later, doesn't that mean the current king is the son of the prince who tried to kill Rasputin?\n\nJohn replied, 'No, Rasputin didn't die.\nHe only faked his death and was the one who killed the former king of Winterland in the Third Kaidos War as revenge for attempting to kill him.\nHe disappeared afterward.\n\nNot only that, but even the legends from the Kaidos War did not die from any illness.\nIt's just a myth to prevent anyone from searching for the legendary weapons.\nDo you remember Jinbei, who died in the kingdom of Rosenbelle at the hands of the prince of Suduma?'\n\nBankai: 'Yes, what about him?'\n\nJohn: 'He was Ryoma, the user of the Sinestro Glove, and he weakened due to overusing his power, making it easy for the prince of Suduma to kill him.\nThe same happened with the others.\nAlso, Bankai, I want to tell you something about Mihawk, the strongest among them.\nHe is your father.'\n\nBankai couldn't comprehend what his friend said at first and asked in shock, 'How did you know all this?'\n\nJohn replied, 'My father told me this.'\n\nBankai went to Rasputin's fake grave and took the black elderberry herb.\n\nBankai and John spent the night in Winterland.\nBankai couldn't sleep because he was thinking about his father, Mihawk, and why he never returned.\nIn the morning, they set off to their next destination, the city of Bummer.")
                    winter = True
                    break
        if winter == True:
            break
        else:
            print("Invalid choice. please try again")

puzzle = False
winter = False
while winter == False or puzzle == False:

    if current_location == "graveyard":
        if not puzzle:
            print("There is nothing we can do here.")
            direction = input("What is your next direction: \ncastle\nsea\nstart\n").lower()
            if direction == "sea":
                current_location = "sea"
            elif direction == "start":
                current_location = "start"
            elif direction == "castle":
                current_location = "castle"
            else:
                print("Please choose a valid direction")
        else:
            grave()
            break

    elif current_location == "sea":
        print("It's not the appropriate time to swim; we should save my mum.")
        current_location = "start"

    elif current_location == "start":
        print("You are at the start.")
        direction = input("What is your next direction: \nmarket\nsea\ngraveyard\n").lower()
        if direction == "market":
            current_location = "market"
        elif direction == "sea":
            current_location = "sea"
        elif direction == "graveyard":
            current_location = "graveyard"

    elif current_location == "market":
        print("You are at the market.")
        if not puzzle:
            print(
                "After a long search, Bankai finally found the black elderberry herb, but it came at a high price. \nSo he asked the seller if there was another way to obtain this herb.")
            print(
                "The seller : \"Yes, there is a way.\nIt grows above the Devil's Head Hole, where the demon died from the city's cold.\"")
            print("what is the correct answer")
            while puzzle == False:
                choice = int(input(
                    "1. Napoleon's tomb\n2. Queen Elizabeth's tomb\n3. Pharaoh's tomb\n4. Ramses II\n5. Rasputin's tomb\n"))
                if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                    wronganswer(15)
                elif choice == 5:
                    print("It's the correct answer")
                    print("so now we should go to the graveyard")
                    puzzle = True
                else:
                    print("Invalid choice Please try again")
        direction = input("What is your next direction: \nstart\ncastle\n").lower()
        if direction == "castle":
            current_location = "castle"
        elif direction == "start":
            current_location = "start"
        else:
            print("Please choose a valid direction")

    elif current_location == "castle":
        direction = input("What is your next direction: \ngraveyard\nmarket\n").lower()
        if direction == "graveyard":
            current_location = "graveyard"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")
    else:
        print("Please choose a valid direction")
clear()

#the part 4 of the game
slowprint("chapter four: When the vikings rises", 0.06)
print(
    "After what happened in the kingdom of Winterland, Bankai and John arrived in the city of Bummer.\nThis city was completely different from the ones they had been in before. It was not as beautiful as the kingdom of Rosenbelle or Winterland. It was inhabited by people resembling Vikings.\nIt is the only city that rejected royal rule, and here, the strong rule.")

current_location = "start"
while current_location != "hal":
    if current_location == "start":
        direction = input("What is your next direction: \nsea\nmarket\nrestaurant\n").lower()
        if direction == "sea":
            current_location = "sea"
        elif direction == "market":
            current_location = "market"
        elif direction == "restaurant":
            current_location = "restaurant"
        else:
            print("Please choose a valid direction")

    elif current_location == "sea":
        print("It's not the appropriate time to swim; we should save my mum.")
        current_location = "start"

    elif current_location == "market":
        print("I heard people talking about a competition in a place called Hal.")
        direction = input("What is your next direction: \nsea\narena\nstart\nhal\n").lower()
        if direction == "sea":
            current_location = "sea"
        elif direction == "arena":
            current_location = "arena"
        elif direction == "start":
            current_location = "start"
        elif direction == "hal":
            current_location = "hal"
        else:
            print("Please choose a valid direction")

    elif current_location == "arena":
        print("I heard people talking about a competition in a place called Hal.So first let's go to market")
        direction = input("What is your next direction: \nsea\nmarket\n").lower()
        if direction == "sea":
            current_location = "sea"
        elif direction == "market":
            current_location = "market"
        else:
            print("Please choose a valid direction")

    elif current_location == "restaurant":
        print("I heard people talking about a competition in a place called Hal.")
        direction = input("What is your next direction: start\nhal\n").lower()
        if direction == "start":
            current_location = "start"
        elif direction == "hal":
            current_location = "hal"
        else:
            print("Please choose a valid direction")

    elif current_location == "hal":
        print(
            "We have arrived at Hal. This is where the competition we heard about will take place.\nThe herb is inside. We have to win now.")
        break
    else:
        print("Please choose a valid direction")
clear()
print("Bankai and John registered for this competition. Participants from other kingdoms also joined.")
print(
    "The rules of the competition are simple: there are 32 fighters and 5 rounds.\nEach fighter who wins advances to the next match.\nAnyone who falls to the ground, exits the ring, or surrenders loses.\nAll weapons are allowed.")
print(
    "The draw results revealed that Bankai and John were in completely different brackets, meaning they wouldn't face each other until the final. \nhey were happy with this outcome, but their joy didn't last long.\nBankai discovered that he would face the champion of the previous seven competitions, named El-Haouari, in his first round.\nAs for John, he would face one of the strongest individuals from the kingdom of Suduma, named Ares, if he made it to the semifinals.\nAres was a formidable warrior, his strength comparable to one of the three legends.\nHe wore iron armor similar to that of knights, which earned him the nickname 'The Armored.' Only his red eyes were visible from his face.")
print(
    "Before the competition began, Bankai looked at the list of contestants and found a familiar name—yes, it was their third friend, Martin, who had also been a student of his grandfather.\nHe went to look for him in the competitors' waiting room and found him.\nYes, it was indeed Martin, their childhood friend. Finally, the trio was reunited once again.")
clear()
print("Round One")
fight(Bankai, haouari, 500, 300, 250)
print("John and Martin easily defeated their opponents.")
print(
    "The audience was surprised by what happened as El-Haouari, the legend of Hal, lost in the first round to a wanderer whose goal was neither the money nor the title of the Hal competition, but only that herb.")
clear()
print("Round Two")
fight(Bankai, enemy, 500, 300, 250)
print(
    "The fights were easy for both Banنai and John; they each won, attracting even more attention.\nHowever, two contestants from the kingdoms of Shturm and Rosenbelle easily defeated our men.")
clear()
print("Round Tree")
fight(Bankai, strenemy, 750, 500, 500)
print(
    "During the break, John and Bankai were with their friend Martin, reminiscing about their adventures and childhood days.\nSuddenly, Ares, who would face John in the next round, approached them.\nAfter learning that John was Bancai's friend who had killed their prince a few days ago, Ares said to him, 'You must withdraw and let me face Bancai.\nOtherwise, I will kill your friend in the final round, and then I will kill your sick friend.' At first, John refused, but Ares whispered something in his ear.\nJohn's face turned pale, and he agreed to it.")
clear()
print("Round Four")
fight(Bankai, enemy, 750, 500, 250)
print(
    "Bankai won his match as usual, but on John's side, he saw his friend withdraw as soon as he entered the arena.\nBankai thought John withdrew because he was afraid of suffering the same fate as their friend Martin, or to protect him and prevent Ares from killing him when they face off in the final.\nHowever, John had a secret that no one knew, not even his friend Bancai.\nAres said to him, 'You made the right choice,' drew his sword, and killed John with it.\nJohn fell to the ground, and Bankai rushed to him, screaming, 'John!' The doctors couldn't do anything; John was dead.")
print(
    "Ares looked at Bankai and said, 'Don't let your tears hinder you in our next battle.' At that moment, Bankai screamed in despair, transforming all his sorrow into rage.\nBankai didn't wait for the referees to announce the start of the match; he started it himself.\nHe pushed John's body away from the arena and began their fight.")
clear()
print("Round Five")
print(
    "The fight began with Bankai's weak strikes that did nothing but amuse Ares.\n'Is this the one who managed to defeat El-Haouari?' Ares raised his hand to the sky, then struck Bankai with a blow that knocked him to the ground.\nAres said, 'I told you not to let your sorrow be an obstacle, or else you will die from the next strike.'")
fightl(Bankai, Ares)
fight(Bankai1, Ares, 1500, 1000, 1200)
print(
    "Bankai stood up, looking at the crowd, who watched him with pity.\nHe saw his friend Martin crying silently, sitting in shock at the loss of their friend John.\nThe voices around him faded until Bankai lost consciousness.\nOne of the referees came to declare Bankai's defeat and Ares's victory, whose laughter filled the arena.\nSuddenly, Bankai's body moved, surprising everyone.\nEven the referee stepped back in astonishment.\nBankai stood up, his eyes white, with a tattoo extending from his right eye to his neck, covering part of his right hand.\nA black aura emanated from his body; it was his grief.\nThis appearance terrified everyone; it resembled the form of the Kaidoz.")
print(
    "Finally, Bankai allowed his true power to emerge.\nAres prepared to continue the fight, but Bankai struck him down, attempting to rise but unable to due to the strength of the black aura.\nThe referees intervened, but Ares stopped them.\nHe removed his armor, revealing his face for the first time, freeing himself from the constraints that limited his abilities in combat.\nThe fight between Bankai and Ares continued for a long time until Ares surrendered, and Bankai emerged victorious.")
print(
    "After the fight, Bankai collapsed, remaining in a coma for three days.\nWhen he woke up, the doctor couldn't understand his condition during the fight and advised him to see a doctor in the city of Savana, hoping for treatment.")
print(
    "Bankai went with his friend Martin to their friend's grave, then went to claim his prize and took the Ginseng herb he had come for.\nFinally, he packed his belongings and left the city, saddened and heartbroken by the loss of his friend.")
clear()
#the part 5 of the game
slowprint("chapter five: hottest city", 0.06)
print(
    "At night, Bankai arrived in the kingdom of Savana, the warmest of the kingdoms, this time with his friend Martin and without their friend John.\nTheir goal now was to find the Echinacea herb.\nAt first, Bankai was surprised by the warm welcome from the citizens of Savana and the large table filled with food.\nHe thought it was a festival or celebration until one of the residents approached him and said, \"Are you the Bankai who won the Hal competition? Everyone is talking about your strength and how you defeated Ares.\"\nBankai looked at the attendees and saw El-Haouari, whom he had defeated in the first round of the competition.\nHe went to talk to him, but El-Haouari refused and simply said, \"I pity you for entering this kingdom.\"\nBankai was puzzled by this remark and returned to his place with Martin.")
print(
    "Some people started talking in front of him in an unfamiliar language, their native tongue.\nFortunately, Martin understood what they were saying.\nMartin said, \"We need to leave. They want you to be the sacrifice for their monster.\"\n\nBankai: \"What sacrifice? What monster?\"\n\nMartin: \"It's a lizard-like monster that appears every year to eat a strong person, and they want you to be their sacrifice.\"\n\nBankai: \"Why?\"\n\nMartin: \"Because you're not from this kingdom, you're strong, and there are also some other requirements that I don't know about.\"\n\nBankai: \"Does that black thing that appeared during my last fight have anything to do with it?\"\n\nMartin: \"I think so.\"")
choice = int(
    input("What is your tool you will take from the table: \n1. spoon \n2. Knife\n3. Lighter\n4. nothing\n5. Apple\n"))
clear()
print(
    "Bankai and his friend quickly got up from the table to leave, but the king arrived with a senior elder who asked them where they were going, as the festivities hadn't started yet.\nBankai didn't want the locals to know that he had discovered their plan, so he sat down, pondering a way to escape.\nHe thought that the only solution might be to fight the monster.\nWithin seconds, Bankai was struck on the head and lost consciousness.\nHis friend tried to intervene but couldn't.\nWhen Bankai woke up, he found himself bound inside a stable along with the elder.\nHis friend lay on the ground, knocked out by a few blows that proved too much for him, still recovering from his fight in the Hal tournament's second round.")
if choice == 2 or choice == 3:
    print(f"Fortunately, Bankai had a tool that he had taken from the table before losing consciousness.")
    print("So, Bankai cut the rope without the sheikh noticing.")
else:
    print(f"Unfortunately, Bankai had a useless tool that he had taken from the table before losing consciousness.")
    print("so now can't do any thingti cut the rope")
    print("The elder struck Bankai with a powerful blow.")
    Bankai.health -= 100
    print("The elder accidentally cut the rope while striking Bankai.")
print("Now Bankai is free so he should fight the elder")
fight(Bankai0, elder, 1500, 1000, 1000)
print("Martin: Oh no, Bankai, that elder didn't die, he transformed into a lizard now.")
clear()
fightl(Bankai0, lizard)
fightl(Bankai1, lizard)
fight(Bankai2, lizard, 40000, 30000, 30000)
print(
    "During Bankai's fight against the elder, he transformed just as he had during the Hal competition.\nAgain, he couldn't control his power and defeated the elder, transforming into a lizard.\nHe then took the elder's severed head to the citizens of Savana, freeing them from the monster they had feared.\nThe people celebrated this victory, but Bankai soon fainted from his exertion.\nHowever, he quickly recovered, and the citizens gave him and his friend the Echinacea herb they had come for.\nNow, only one element remained: the Ginkgo Biloba herb in the Canavar Cave.\nBut before proceeding, Bankai needed to visit a doctor to understand the reason behind his mysterious power.")
current_location = "barn"
clear()
while current_location != "doctor":
    print("You are at", current_location)

    if current_location == "barn":
        direction = input("Where do you want to go? (doctor/diner place): ").lower()
        if direction == "doctor":
            current_location = "doctor"
        elif direction == "diner place":
            current_location = "diner place"
        else:
            print("Please choose a valid direction")
    elif current_location == "diner place":
        direction = input("Where do you want to go? (castle/barn): ").lower()
        if direction == "castle":
            current_location = "castle"
        elif direction == "barn":
            current_location = "barn"
        else:
            print("Please choose a valid direction")
    elif current_location == "doctor":
        print("You have reached the doctor!")
        break
    elif current_location == "sea":
        print("You have reached the doctor!")
        current_location = "start"
    elif current_location == "start":
        direction = input("Where do you want to go? (sea/barn): ").lower()
        if direction == "sea":
            current_location = "sea"
        elif direction == "barn":
            current_location = "barn"
        else:
            print("Please choose a valid direction")
    elif current_location == "castle":
        direction = input("Where do you want to go? (doctor/diner place): ").lower()
        if direction == "doctor":
            current_location = "doctor"
        elif direction == "diner place":
            current_location = "diner place"
        else:
            print("Please choose a valid direction")
    else:
        print("Please choose a valid direction")

print("Doctor: What disease did your mother suffer from?\nBankai: The doctor in Sturorm didn't want to tell me the name of the disease.\nDoctor: The medicine needs Ginseng herb, and also what else? Tell me everything about your journey.\nAfter Bankai told him about the other ingredients and how he managed to obtain them, the doctor understood his condition.\nDoctor: You are the son of the legend Mihawk, then. I see. Your mother is afflicted with Anarogia, one of the diseases that emerged after the Kaidoz war.\nAs for your power, it's a curse upon you to control it. You need to take the Sinestro glove and insert a stone into the hole in its palm.\nLuckily, I have that stone, but you will find the glove in the Yaskeena Cave located between Savana and Canavar Forest.\nYou won't find anyone to ask in Canavar, so I'll tell you where to find the last herb, Ginko Biloba.\nIt's in the Canavar Cave in the middle of the forest, inside the waterfall.\nBut be warned, your fight there will be the toughest, as its guardian won't spare you.\nAlso, as you know, the Kaidoz jar they sealed is there.\nThen he asked Bankai to leave and told his friend to stay to say a few words.\nDoctor to Martin: Keep your eyes on your friend, and don't let him fight until he finds the glove; he might die while fighting.\nYou have to fight in his place. He gave him medicine and continued, saying: Drink this medicine to heal your wounds; you are stronger than you think.\nDon't suppress your power and defend your friend with it.\nAfter these words, Martin felt that John's death was because of him.\nIf he had been stronger, he would have defeated Ares in the second round, and John wouldn't have fought in the semi-final.\nBut soon the remorse vanished, for now, he had to save his friend's mother.")
clear()
#the fifth part of the game
current_location = "start"
print("you should go to Yaskina cave to get the sinestro golve  ")

Yaskina = False
Canavar = False

while not Yaskina or not Canavar:

    if current_location == "start":
        direction = input("Where do you want to go? (mushroom/yaskina)").lower()
        if direction == "mushroom":
            current_location = "mushroom"
        elif direction == "yaskina":
            current_location = "yaskina"
        else:
            print("Please choose a valid direction")
    elif current_location == "mushroom":
        choice = 0
        while choice != 1 or choice != 2:
            choice = int(input("Do you wanna eat the mushroom:\n1. Yes\n2. No\n"))
            if choice == 1:
                print("Ooh this mushroom decrease you health.")
            elif choice == 2:
                pass
                break
            else:
                print("Invalid choice please try again")
        direction = input("Where do you want to go? (canavar/start)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "start":
            current_location = "start"
        else:
            print("Please choose a valid direction")
    elif current_location == "yaskina":
        print("You meet the guard of the cave he is a giant monster")
        print("Martin wanna fight the monster by himself")
        time.sleep(1)
        print("Martin couldn't beat the monster and he need your help")
        print("Now you should fight the monster by yourself")
        fightl(Bankai, monsterY)
        fight(Bankai3, monsterY, 100000, 50000, 100000)
        Yaskina = True
        direction = input("Where do you want to go? (canavar/start)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "start":
            current_location = "start"
        else:
            print("Please choose a valid direction")

    elif current_location == "canavar":
        if Yaskina == False:
            print("There nothing we can do here i think we should go to Yaskina cave first as the doctor said")
            direction = input("Where do you want to go? (yaskina/mushroom)").lower()
            if direction == "yaskina":
                current_location = "yaskina"
            elif direction == "mushroom":
                current_location = "mushroom"
            else:
                print("Please choose a valid direction")
        else:
            print(
                "The monster was finally defeated, and Bankai took the gauntlet.\nWhen he placed the stone into the hole in the palm of his hand, a lightning bolt struck his hand, causing him great pain.\nHowever, he felt an immense power surge through him, doubling his strength.\nAfter taking hits from that monster, he now feels that he can defeat any being.\nThat is what he believes.")
            print(
                "In their journey to find the final element, they faced many challenges on their way to the cave.\nThey fought some monsters from the Kingdom of Bits, a realm inhabited entirely by biological monsters.\nThe Kingdom of Suduma conducts experiments on them after having killed their king and seized their lands.\nOnly a few humans remain in that place, hiding in the forest of Canavar, while some have migrated to other kingdoms, with their total number not exceeding two hundred.\nBankai encountered some of the residents, giving them food and protecting some from the Bits monsters that were chasing them.\n")
            print(
                "Eventually, Bankai reached a river and followed it to its source at a waterfall inside the cave.\nFinally, they arrived at the Canavar Cave, where everything would end, and they would save the mother (or so he believes).\n")
            print(
                "Upon entering the cave, he found it very spacious with no guards at the entrance, suggesting they were inside.\nAfter walking a bit, they came across three diverging paths.\nOne of these paths leads to the jar containing the Kaidos monsters; it is unguarded but anyone who enters it will be cursed and never leave the cave alive.\nAnother path leads to the herb the hero seeks, and the third path leads to an endless circular loop from which no one can escape.\n")
            print(
                "1. The first path is marked, 'The path that ascends to the yellow sky is the path that restores life to the dead.'\n")
            print("2. The second path is marked, 'He who sees the unseen will find the key to enter the illusion.'")
            print(
                "3. The third path is marked, 'He who seeks salvation, let him follow the lone star in the sea of darkness.'")
            choice = 0
            while choice != 1 or choice != 2:
                choice = int(input("Do you wanna hear the discussion between Bankai and Martin :\n1. Yes\n2. No"))
                if choice == 1:
                    print("Martin said: What will you choose, Bankai?")
                    print("Bankai: I don't know. If we choose the wrong path, we might die.")
                    print("Martin said: The first path brings the dead back to life. Don’t you think it’s the one since the herb is medicinal and heals those who were about to die? What does the phrase 'yellow sky' mean?")
                    print("Bankai: I’m not sure, but it might refer to the Kaidos monsters.")
                    print("Martin said: What about the second path? I think the 'key to the illusion' refers to the vicious circle.")
                    print("Bankai: But it could also mean the Kaidos monsters.")
                    print("Martin said: Or it might refer to the disease we want to cure your mother from.")
                    print("Bankai: What does 'salvation' mean in the phrase for the third path?")
                    print("Martin said: I think it means our way out of this problem and finding the herb.")
                    print("Bankai: Or maybe it talks to those inside who couldn’t get out, implying that their salvation is impossible. I think it’s the final loop.")
                    print("Martin said: Or maybe it means the salvation of the Kaidos monsters from their prison.")
                    break
                elif choice == 2:
                    pass
                    break
                else:
                    print("Invalid choice please try again")
            if choice == 1:
                print("Martin said, 'What will you choose, Bankai?' Bankai replied, 'I don’t know. If we choose the wrong path, we might die.' Martin said, 'The first path revives the dead. Don’t you think that might be it since the herb is medicinal and can heal someone who is about to die? What does the term 'yellow sky' mean?' Bankai responded, 'I’m not sure, but it might refer to the Kaidos monsters.' Martin said, 'What about the second path? I think the key to enter the illusion might refer to the endless loop.' Bankai replied, 'But it could also mean the Kaidos monsters.' Martin said, 'Or perhaps it refers to the disease we want to cure your mother from.' Bankai asked, 'What does salvation mean in the context of the third path?' Martin replied, 'I think it’s our way out of this predicament and finding the herb.' Bankai said, 'Or maybe it’s telling those inside that their salvation is impossible, meaning it’s the endless loop.' Martin concluded, 'Or perhaps it means the salvation of the Kaidos monsters from their prison.'")
            else:
                pass
            while choice != 1 or choice != 2 or choice != 3:
                choice = int(input("So what is your choice : \n1. First path\n2. Second path\n3. Third path"))
                if choice == 1:
                    print("Your choice was successful. The first path was the correct answer")
                    Canavar = True
                    break
                elif choice == 2:
                    print(
                        "Your choice was wrong. This path leads to the Kaidos monsters, and now they are free. You have lost")
                    exit()
                elif choice == 3:
                    print(
                        "Your choice was wrong. This path leads to the endless loop, and now you cannot escape from it. You have lost.")
                    exit()
                else:
                    print("Invalid choice please try again.")

            print("Bankai took the herb and was overjoyed; their journey was finally over.\nAt last, he would save his mother.\n")
            print("However, his friend Martin felt something strange.\n")
            print("Didn't that doctor from the Kingdom of Savana tell them that the cave had strong guards?\nHe hadn't seen any guards since they entered the cave, but he didn't want to worry Bankai now.\nThey needed to get out of there.\n")
            print("He hadn't seen any guards since they entered the cave, but he didn't want to worry Bankai now.\nThey needed to get out of there.\n")
            print("Bankai and his friend moved from the spot, and when they reached the place where they had chosen one of the three paths, they found a man with huge muscles lying on the ground.\nBeside him were two men: one holding a knife who looked strong, and the other holding a large jar.\nThey turned towards him, and one of them said, 'Finally, your silly journey is over. Your end is now.'\nBankai recognized them; it was Ares and his friend John.")

clear()
#the last part of the game
slowprint("chapter six: the last war", 0.06)
print("While Bankai and Martin were in shock, Ares smashed the jar, releasing a scream that pushed Bankai and Martin backward.\nAll the imprisoned Kaidos emerged from it, and smoke filled the entire continent of Espada.\nThe kings of the kingdoms in the continent of Espada saw this and ordered their armies to prepare for war, as the thing they had feared had come to pass.")
print("King of the Kingdom of Shturm: \"This is our son; we must save him no matter the cost.\"")
input("Press Enter to continue...")
print("King of the Kingdom of Rosenbelle: \"Now we will show our strength to protect those who shielded our kingdom. We will repay Bankai by eradicating all the Kaidos. I know the Kingdom of Suduma is involved in this; today, that kingdom will fall.\"")
input("Press Enter to continue...")
print("King of the Kingdom of Winterland: \"In a war like this, my father died. Today, I will avenge him and return to marry you, Princess of Rosenbelle.\"")
input("")
print("The residents of Bummer moved towards the Canavar Forest without a leader, acting with complete savagery.")
input("")
print("King of the Kingdom of Savana: \"We are grateful for what Bankai did for us. He saved many lives from the lizard monster. We must thank him in our own way.\"")
input("")
print("King of the Kingdom of Suduma: \"This is my chance to conquer the other kingdoms. I knew you wouldn't disappoint me, John.\"")
input("")
print("Back in the cave, the man who had been lying on the ground stirred. Bankai wondered who this man could be.")
print("Martin said, \"I recognize you now. You are the legendary Mihawk.\"")
input("")
print("Bankai exclaimed, \"You are my father!\"")
input("")
print("Mihawk replied, \"Are you Bankai?\"")
input("")
print("The family was finally reunited, but this was not the time for conversation. They now faced a major problem: the Kaidos on one side and Ares and John on the other.")
input("")
print("Mihawk, severely injured, retreated as he could barely stand.")
input("")
print("\"After the union of the kingdoms, they managed to eliminate several of the Kaidos creatures, but they couldn't eradicate them all. Now, you must fight them.\"")
print("On the other side, the fight between Martin and Ares was intense.\n")
print("Ares was surprised by Martin's strength; he wasn't like this in the competition.")
print("\"In the end, Martin emerged victorious.\nJohn and Bankai were also surprised by what had happened.\nBankai continued the fight, suddenly stopping time.\nThis was the power of the glove; Bankai could now control it.\nHe became a formidable force, stopping time, striking his opponent, then allowing time to resume, receiving a blow that doubled his strength.\nHe defeated John, incapacitating him but not killing him, as he was his friend and knew he had his own secrets.\nMartin said, 'Stop the time and prevent the jar from breaking.'\nBankai replied, 'It's impossible for us to kill all the Kaidos. If we prevent it, it won't change anything. It's not just John who wants this, but all the villains in this world, especially the Kingdom of Suduma.'\nAs they spoke, the King of Suduma sneaked up and struck Bankai's hand, causing the stone to fall.\nAs Bankai was about to stop time to kill him, he was blindsided by a blow from Ares.\nMartin retaliated, killing Ares.\"")
print("Finally, Ares died, but as Bankai tried to retrieve the glove, the king killed his friend, John, and his men from the Kingdom of Suduma joined the fight.\nUnfortunately, more than 20 seconds had passed since John's death, and it was futile to turn back time to save him.\nJohn had truly died this time, and the grief was overwhelming.\nBankai had seen his friend die twice, and this time, he held a secret in his heart.\nWhy did he collaborate with Suduma? What did this king threaten him with?\nIn a moment of anger and sorrow, with the glove not in his hand, Bankai reached a level he had never reached before.\nThe tattoos that had appeared during the Hal competition resurfaced.\nIt was the curse that had been cast on him, but this time, the curse had become even greater.\nHis power was truly incomparable.\nBlinded by anger, Martin and Mihawk took cover to avoid being killed.\nMihawk was surprised by his son's strength; he was stronger than the three combined.\nBankai rose from the ground, his voice changing to a powerful tone with a slight wave.\nThe king and 82 of the soldiers who had come with him were killed.\nBankai's power surpassed not only the three legends but even the strength of the jinn.\nHe emerged from the cave, finding the other kingdoms fighting the Kaidos creatures and winning.\nThey all fled because they knew if they crossed his path, they would be killed.")
print("Your strength has doubled with the stone and the glove. Now, you can move to any kingdom instantly due to your speed.")
fight(Bankai4, kaidos, 1000000, 800000, 150000)
clear()

print("you kill 11000 of the kaidos")
current_location = "canavar"
defeat = 0
beatsa = False
beatsu = False
beatbi = False
beatvir = False
beatsh = False
beatro = False
beatwi = False
beatbu = False
while defeat < 8:
    if current_location == "canavar":
        print(" you beat the kaidos here let's go to another place")
        direction = input("Where do you want to go? (savana/suduma/bits/visors/shturm/rosenbell/winterland/bummer)").lower()
        if direction == "savana":
            current_location = "savana"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "savana":
        if beatsa == False:
            fight(Bankai4, kaidossa, 1000000, 800000, 150000)
            print("you kill 5000 of the kaidos")
            beatsa = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/bits/visors/shturm/rosenbell/winterland/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "bits":
        if beatbi == False:
            fight(Bankai4, kaidosbi, 1000000, 800000, 150000)
            print("you kill 5000 of the kaidos")
            defeat += 1
            beatbi = True
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/savana/visors/shturm/rosenbell/winterland/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "visors":
        if beatvir == False:
            fight(Bankai4, kaidosvir, 1000000, 800000, 150000)
            print("you kill 7000 of the kaidos")
            beatvir = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/bits/savana/shturm/rosenbell/winterland/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "winterland":
        if beatwi == False:
            fight(Bankai4, kaidoswi, 1000000, 800000, 150000)
            print("you kill 4000 of the kaidos")
            beatwi = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/bits/visors/shturm/rosenbell/savana/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "rosenbell":
        if beatro == False:
            fight(Bankai4, kaidosro, 1000000, 800000, 150000)
            print("you kill 1000 of the kaidos")
            beatro = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/bits/visors/shturm/savana/winterland/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "bummer":
        if beatbu == False:
            fight(Bankai4, kaidosbu, 1000000, 800000, 150000)
            print("you kill 6000 of the kaidos")
            beatbu = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/bits/visors/shturm/rosenbell/savana/winterland)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "winterland":
            current_location = "winterland"
        else:
            print("Please choose a valid direction")
    elif current_location == "shturm":
        if beatsh == False:
            fight(Bankai4, kaidosst, 1000000, 800000, 150000)
            print("you kill 3000 of the kaidos")
            beatsh = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/suduma/bits/visors/winterland/rosenbell/savana/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "suduma":
            current_location = "suduma"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
    elif current_location == "suduma":
        if beatsu == False:
            suduma = suduma()
            fight(Bankai4, kaidossu, 1000000, 800000, 150000)
            print("you kill 8000 of the kaidos")
            print("The Suduma army won't let you rest; you must fight them now.")
            fight(Bankai4, suduma, 1000000, 800000, 100000)
            beatsu = True
            defeat += 1
        print(" you beat the kaidos here let's go to another place")
        direction = input(
            "Where do you want to go? (canavar/winterland/bits/visors/shturm/rosenbell/savana/bummer)").lower()
        if direction == "canavar":
            current_location = "canavar"
        elif direction == "winterland":
            current_location = "winterland"
        elif direction == "bits":
            current_location = "bits"
        elif direction == "visors":
            current_location = "visors"
        elif direction == "shturm":
            current_location = "shturm"
        elif direction == "rosenbell":
            current_location = "rosenbell"
        elif direction == "savana":
            current_location = "savana"
        elif direction == "bummer":
            current_location = "bummer"
        else:
            print("Please choose a valid direction")
clear()
print("You have defeated both the Kaidos and the Suduma army. Now, only the leader of the Kaidos, Canavar, remains.")
print(dragon)
subprocess.run('cls')
print("Your last battle will strat soon.")
time.sleep(5)
fight(Bankai4, canavar, 1000000, 800000, 800000)
print("finally you beat the last kaidos.")
print("\"The battle between Bankai and the Kaidos continued for three days.\nMeanwhile, the Kingdom of Suduma withdrew after losing their king and more than 10,000 soldiers.\nThe Fifth Kaidos War, known as the Last Kaidos War, finally ended.\nIt was a conflict between the Kaidos creatures and the Kingdom of Suduma against a single person: Bankai.\"")
print("\"When Bankai delivered his final blow, sending Canavar flying through the air, he realized it was over.\nHis anger and sorrow faded, and the curse lifted.\nHis friend Martin, his father Mihawk who was being treated, and the kings of the other kingdoms came to him as he collapsed on the ground.\"")
print("Bankai: 'Why did you leave us, Father?'")
input("")
print("Mihawk: 'I was assigned the task of guarding the Kaidos jar.'")
input("")
print("Bankai: 'So, you can come back with us now, Father?'")
input("")
print("Mihawk: 'Yes, I will return home with you.'")
input("")
print("Bankai: 'I wish I knew why John helped the Kingdom of Suduma and what Ares told him. I know it wasn't for his own benefit; he wanted to save someone.'")
input("")
print("Bankai handed his bag to Mihawk.\nBankai: 'Take this to the doctor and tell my mother my story. She will definitely enjoy it.'")
print("Mihawk: 'Why don't you tell her yourself?'")
print("Bankai: 'You know, Father, in the end, John and I are alike. We want to save others, and our own lives don't matter. I never considered John my enemy, and neither did he, even during our fight in the cave.'")
print("Mihawk: 'Our time together was short, but I admired you and your friends. I'm sorry I didn't fulfill the role of a good father.'")
print("Bankai took his last breath. I don't think he heard his father's final words, but he died holding his father's hand tightly, like a little child. And thus, Bankai's story ended here.")

#the end of the game
print("In the Kingdom of Shturm:\nThe mother was cured of her illness, and a statue of Bankai was erected to honor his contribution to saving humanity from the threat of the Kaidos and the Kingdom of Suduma.\nMihawk retired from swordsmanship and had a second child, who showed the same courage as his older sibling.")
input("")
print("In the Kingdoms of Rosenbelle and Winterland:\nThe princess married the King of Winterland, and they had a child named Raja, after his grandfather King Raja, who died in the Kaidos war.")
input("")
print("In the Kingdom of Bummer:\nIt became a kingdom again after restoring the monarchy and crowning Hawari as king, since his mother was from that kingdom and they acknowledged his heroism.\nThe rules of the Hal competition were revised: weapons and lethal violence were banned, turning it into a clean competition.")
input("")
print("In the Kingdom of Savana:\nMartin opened a martial arts training hall to teach children what he had learned from Bankai's grandfather.")
input("")
print("In the Kingdom of Bits:\nThe citizens returned to rebuild their land.\nA medicine was developed that restored the Bits monsters to their human forms.")
input("")
print("In the Kingdom of Visors:\nNot a new kingdom, but one that had been taken over by Suduma, it regained its sovereignty after the fall of the Kingdom of Suduma.")
input("")
print("And thus ends our story about the hero Bankai and his journey to save his mother, which transformed into a quest to save the world.")
subprocess.run('cls')
slowprint("\t\t\t\t\t\tThe game made by :", 0.06)
time.sleep(1)
slowprint("\t\t\t\t\t\tBenChetioui Ahmed Ayoub", 0.06)
time.sleep(1)
slowprint("\t\t\t\t\t\tDaouadi faycal Wassim", 0.06)
time.sleep(1)
slowprint("\t\t\t\t\t\tElbah Abderaouf Fadi", 0.06)
time.sleep(1)
slowprint("\t\t\t\t\t\tBerkani Ahmed", 0.06)
time.sleep(1)
subprocess.run('clear', shell=True)
slowprint("Thank you for playing The game", 0.06)
print(castel)
print(cannavar)