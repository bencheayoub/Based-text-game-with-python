import time
import os
import subprocess
import random

def clear():
    input("Press Enter to clear the screen...")
    if os.name == 'nt':  # Windows
        subprocess.run('cls')
    else:  # Unix/Linux/MacOS
        subprocess.run('clear', shell=True)

def lucky():
   return random.randrange(0,100)

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

class prince:
    def __init__(self, name="prince of suduma"):
        self.name = name
        self.power = 50
        self.health = 120
        self.defence = 30

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
    enemy_damage = lucky() * attacker.power / 100
    defender.health -= enemy_damage * defender.defence / 100
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
            defend(defender, attacker)
    if attacker.health > 0:
        print(f"you beat {defender.name} and your health now is {attacker.health}")
    else:
        print(f"{defender.name} and his health is {defender.health}")
        print("You lose")
        exit()

# the part of the story of the game

print("In the continent of Aspada, 500 years ago, there lived 50 million humans under the servitude of 50 thousand beings called \"Kaidoz\", \nhybrids between humans and dragons possessing immense power.")
print("After two thousand years of enslavement and offering sacrifices to them, three wars were waged against them, all of which failed.")
print("Ten years after the last war against them, Mihawk, Sasaki, and Ryoma, the strongest men on the continent, decided to eliminate all the Kaidoz.")
print("Their power had terrorized the Kaidoz's realm, with each of them wielding a legendary weapon.")
print("Mihawk possessed a sword called Yuro, so powerful that it could cleave a whole mountain with one strike, crafted by the most skilled blacksmith in history.")
print("Sasaki had a gemstone named Anma that multiplied its wielder's power every time they received a blow.\n Legend has it that this gem was a gift from the King of Djinn to the sorcerer Tarish after he saved his daughter.\nAs for Ryoma, he had a glove called Sinistro with a hole on the palm, granting the ability to stop time and rewind it 20 seconds, increasing the wielder's strength.\nThis glove was stolen from the Timelems, creatures from the parallel world.")
print("When these weapons gathered with their powerful wielders, they managed to eradicate the Kaidoz in the Fourth Kaidoz War and sealed them in a jar placed inside a cave called \"Canavar,\" the same name as their leader,\ndue to the immense power of these weapons. However, the users of these weapons died a month later after suffering from excruciating pain.")
time.sleep(5)
subprocess.run('clear', shell=True)


slowprint("Part One: Exiting Storm City", 0.06)
slowprint("Our story begins with a person named Kyoku Bankai.", 0.06)
slowprint("His mother's condition worsened until he summoned a doctor, who diagnosed her with a rare illness.", 0.06)
print("From a remote village in the city of Sturm, he was raised by his mother and grandfather. \nHis grandfather taught him the martial arts, and he became very strong. \nAfter his grandfather passed away, his mother continued to take care of him.\nThis motivated him to keep learning combat skills so he could protect his mother.")
time.sleep(5)

# the first part of the game
clear()

choice = int(input(
    "What do you want to do? (1. Let's go to the market, 2. Let's go to the doctor, 3. Let's watch my mum die): "))

while choice != 2:
    if choice == 1:
        slowprint("It's not the appropriate time to go shopping; we should save my mum.", 0.06)
        current_location = "home"
        choice = int(input())
    elif choice == 2:
        slowprint("He must now bring the doctor to his mother. Let's go to the doctor.", 0.06)
        current_location = "doctor"
    elif choice == 3:
        slowprint("Your mum has died. Thank you for wasting your money watching your mum die without playing.", 0.06)
        exit()
    else :
        slowprint("Invalid choice. Please try again.", 0.06)
        choice = int(input())


while current_location != "doctor":
    print("You are at", current_location)

    if current_location == "home":
        direction = input("Where do you want to go? (doctor/market): ")
        if direction == "doctor":
            current_location = "doctor"
            print("You have reached the doctor! let take the doctor to my mom.")
            break
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
        direction = input("Where do you want to go? (home/sea1/sea2): ")
        if direction == "home":
            current_location = "home"
            print("The doctor sees your mother and gives a list of medicine ingredients:")
            print("1. Chamomile herb (rosenbelle)\n2. Black elderberry herb (winterland)\n3. Ginseng herb (bummer)\n4. Echinacea herb (savana)\n5. Ginkgo Biloba herb (canavar)")
            break
        elif direction == "sea1" or direction == "sea2":
            print("It's not the appropriate time to swim; we should save my mum. Let's go back to the dam to go to the doctor.")
        else:
            print("Please choose a valid direction")

clear()

print("you face a group of bandits.\ndo you wanna fight them")
choice = 1
while choice != 2:
    print("1.run\n2.fight")
    choice = int(input())
    if choice == 1:
        Bankai.health = Bankai.health-1
        print("you get attacked by them.")
        print(f"your health now is {Bankai.health}")
        if Bankai.health == 0:
            exit()
    elif choice == 2:
        print("Great you defeated them; they were weak, but be careful, for the upcoming battles will not be easy.")
        break
    else :
        print("Invalid choice. Please try again.")

# the second part of the game
jhon = jhon()
prince = prince()
def kill_jinbi():
    print("He sat with his friend in his house and they talked about the old days and about their friend Martin, who was also one of his grandfather's students.")
    print("The night was dark, and as they were talking, they heard a scream outside.")
    goto_jinbi = False
    while not goto_jinbi:
        print("Do you want to go out to see what happened?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            print("Bankai went to see, and he found the old man Jinbei lying on the ground, saying to three people wearing the official attire of the kingdom of Suduma, one of whom was its prince.")
            print("The old man said, 'I know what you want from this marriage. You want to conquer the kingdom of Rosenbelle as you did with other kingdoms. I won't allow you to kill the king or his son.' The prince raised his sword in the air and struck him down.")
            print("Bankai returned to John and told him what he had seen. He wasn't surprised by this evil, as it's a custom of the Suduma kingdom to do anything for the purpose of occupying other kingdoms. Now Bankai wants to save the kingdom of Rosenbelle.")
            goto_jinbi = True
        elif choice == "2":
            print("The scream is still outside. I think you should go to see what happened.")
        else:
            print("Invalid choice. Please try again.")

def market_rose():
    print("He asked some of the merchants in the city if anyone knew the chamomile herb. No one knew its whereabouts, but a blacksmith directed him to an old man named Jinbi who knew a lot about herbs.")
    print("Bankai went to the place of that old man, and he told him that he wouldn't tell him where it is until he answered his riddle. He said: \"He does not walk, yet he always comes. He has no eyes, yet he always sees. What is he?\"")
    while True:
        print("What is the correct answer:")
        print("1. Candle\n2. Cloud\n3. Moon")
        print("Warning: wrong answer takes 10 points of health.")
        choice = input()
        if choice == "1" or choice == "3":
            wronganswer(10)
        elif choice == "2":
            print("Great! Your answer is correct.")
            print("It is located in the king's palace and grows once every year, but you must wait three days to speak with him because his daughter's wedding will be held tomorrow.")
            return True
        else:
            print("Invalid choice. Please try again.")

current_location = "start"
visit_john = False
visit_market = False

while not visit_john and not visit_market:
    print("You are at", current_location)

    if current_location == "start":
        direction = input("Where do you want to go? (john/market): ").lower()
        if direction == "john" and not visit_john:
            current_location = "john"
            print("Bankai meets John, his childhood friend and one of his grandfather's students, who managed to defeat him in his childhood.")
            visit_john = True
            if not visit_market:
                print("John: We should go to the market now to get the chamomile herb.")
                choice = 0
                while choice not in ["1", "2"]:
                    choice = input("1. Yes\n2. No\n")
                    if choice == "1":
                        if not visit_market:
                            current_location = "market"
                            visit_market = market_rose()
                            if visit_market:
                                kill_jinbi()
                        elif visit_market:
                            kill_jinbi()
                    elif choice == "2":
                        print("John: But you should go to save your mum.")
                    else:
                        print("Invalid choice. Please try again.")
            else:
                kill_jinbi()

        elif direction == "market":
            if not visit_market:
                current_location = "market"
                visit_market = market_rose()
                if visit_market:
                    kill_jinbi()
            else:
                print("We were here. What are you doing?")
        else:
            print("Please choose a valid direction")

current_location = "john"

while current_location != "castle":
    direction = input("What is your next direction :\ncastle\nmarket\nstart\n")
    if direction == "castle":
        print("You are in the castle now.")
        current_location = "castle"
        break
    elif direction == "market":
        print("You are in the market now what is your next direction")
        direction = input("Where do you want to go? (castle/start): ")

        if direction == "start":
            current_location = "start"
        elif direction == "castle":
            current_location = "castle"
        else:
            print("Please choose a valid direction")
    elif direction == "start":
        direction = input("Where do you want to go? (sea/castle/start): ")
        if direction == "sea":
            current_location = "sea"
        elif direction == "market":
            current_location = "market"
        elif direction == "john":
            current_location = "john"
        else:
            print("Please choose a valid direction")
    elif direction == "sea":
        print("It's not the appropriate time to swim; we should save my mum.")
        current_location = "start"
    elif direction == "john":
        print("You are at john's home now what is your next direction")
        current_location = "john"
    else:
        print("Please choose a valid direction")



print("Gatekeeper: This place is not meant for people like you. Go away from here.")
choice = 0
while choice != 2:
    choice = int(input("what do you want :\n1. fight him\n2. go to the window\n3. resign"))
    if choice == 1:
        gard(10)
    elif choice == 3:
        exit()
    elif choice == 2:
        break
    else :
        print("Invalid choice. Please try again.")

current_location = "window"

print("Bankai entered the castle through the back window without being seen by anyone. Now he has to search for the person who wants to assassinate the king and his daughter.")

if Bankai.health >= 70:
    print("Hint : they are in the basement.")

location_count = {"wedding": 0, "kitchen": 0, "the store": 0, "basement": 0, "window": 0, "door": 0}
print("Warning : if you go to the same place 3 times the guards will know that you're intruder ")
current_location = "window"

while current_location != "basement":
    if current_location in location_count:
        location_count[current_location] += 1
        if location_count[current_location] > 3:
            print("You have gone to the same place more than 3 times. You lose!")
            exit()

    if current_location == "wedding":
        print("You are in the wedding now. And there is nothing here.")
        direction = input("Where do you want to go? (window/kitchen): ")
        if direction == "window":
            current_location = "window"
        elif direction == "kitchen":
            current_location = "kitchen"
        else:
            print("Please choose a valid direction")

    elif current_location == "window":
        print("You are at the window now. And there is nothing here.")
        direction = input("Where do you want to go? (wedding/kitchen/the store): ")
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
        direction = input("Where do you want to go? (door/wedding/basement/window): ")
        if direction == "door":
            current_location = "door"
            print("The guard caught you. You lose!")
            exit()

if current_location == "basement":
    print("")
    print("Now you should fight him")
    fight(Bankai, prince)

print("Bankai saved the kingdom of Rosenbelle. \nAt first, everyone was in shock. As for the attendees from the kingdom of Suduma, it was a small delegation, and not many military figures were present to avoid arousing suspicion among the inhabitants of Rosenbelle. \nTherefore, the king of Suduma ordered the prince's body to be taken and the delegation to withdraw.")
print("After this incident, the king invited Bancai to hear his story and was impressed by his bravery and determination to save his mother. \nThe king gave him the chamomile herb, and Bancai left the kingdom of Rosenbelle accompanied by his friend John.")
choice = int(input("Do you wanna see a doctor before you go to Winterland ?\n1. Yes\n2. No\n"))
if choice == 1:
    Bankai.health = 100
elif choice == 2:
    pass
else:
    print("Invalid choice.")

current_location = "start"
winter = False
puzzle = False

def grave():
    print("Bankai and John went to the cemetery where prominent figures are buried to search for Rasputin's tomb.\nThey found the guard at the cemetery gate, who did not allow them to enter.")
    while not winter:
        choice = input("What do you want to do now?\n1. fight\n2. search another way to get in")
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
                    print("now there is nothing we to do here let's go back to the door")
                elif current_location == "left side":
                    print("They coincidentally met the king of the Winterland kingdom, the youngest king of the continent of Espada.\nHe shook Bankai's hand firmly and asked, 'Are you Bankai?' \nBankai answered, 'Yes.'\nThe king said, 'Thank you very much for what you did in the kingdom of Rosenbelle. I did not want their princess to marry the prince of Suduma.I hated him, and I also wanted to marry her myself.'")
                    print("The king asked why they had come to the cemetery and how they knew about Suduma's plan.\nBancai told him about his story, his mother, and the death of the old man Jinbei.\nThe king said to them, 'Come, you will enter with me into the cemetery.\nI also want to go there to visit my father's grave.\nHe died in the Third Kaidos War twelve years ago, so I became the king of Winterland at the age of six.'")
                    print("And after a series of conversations, they parted ways.")
                    print("The king asked why they had come to the cemetery and how they knew about Suduma's plan.\nBankai told him about his story, his mother, and the death of the old man Jinbei.\nThe king said to them, 'Come, you will enter the cemetery with me.\nI also want to go there to visit my father's grave.\nHe died in the Third Kaidos War twelve years ago, so I became the king of Winterland at the age of six.'\nAfter a series of conversations, they parted ways.\n\nBankai asked his friend John if the former king of the kingdom took the throne a year after Rasputin's death and died twenty-three years later, doesn't that mean the current king is the son of the prince who tried to kill Rasputin?\n\nJohn replied, 'No, Rasputin didn't die.\nHe only faked his death and was the one who killed the former king of Winterland in the Third Kaidos War as revenge for attempting to kill him.\nHe disappeared afterward.\n\nNot only that, but even the legends from the Kaidos War did not die from any illness.\nIt's just a myth to prevent anyone from searching for the legendary weapons.\nDo you remember Jinbei, who died in the kingdom of Rosenbelle at the hands of the prince of Suduma?'\n\nBankai: 'Yes, what about him?'\n\nJohn: 'He was Ryoma, the user of the Sinestro Glove, and he weakened due to overusing his power, making it easy for the prince of Suduma to kill him.\nThe same happened with the others.\nAlso, Bankai, I want to tell you something about Mihawk, the strongest among them.\nHe is your father.'\n\nBankai couldn't comprehend what his friend said at first and asked in shock, 'How did you know all this?'\n\nJohn replied, 'My father told me this.'\n\nBankai went to Rasputin's fake grave and took the black elderberry herb.\n\nBankai and John spent the night in Winterland.\nBankai couldn't sleep because he was thinking about his father, Mihawk, and why he never returned.\nIn the morning, they set off to their next destination, the city of Bummer.")

        else:
            print("Invalid choice. please try again")

while not winter and not puzzle:

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
            print("After a long search, Bankai finally found the black elderberry herb, but it came at a high price. \nSo he asked the seller if there was another way to obtain this herb.")
            print("The seller : \"Yes, there is a way.\nIt grows above the Devil's Head Hole, where the demon died from the city's cold.\"")
            print("what is the correct answer")
            while not puzzle:
                choice = int(input("1. Napoleon's tomb\n2. Queen Elizabeth's tomb\n3. Pharaoh's tomb\n4. Ramses II\n5. Rasputin's tomb\n"))
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
#the part 4 of the game
