import math
import random
from time import sleep

global player_xp
player_lvl = 0
player_xp = 0
player_dmg= 25 + 15 * player_lvl
player_hp = 100
player_crit = 0.1
player_gold = 0


enemies = [
    {
        "type": "Homeless Man",
        "hp": 85,
        "xp": 110,
        "suicide": 0,
        "gold": 5,
        "attacks": [
            
            {
                "name": "Needle Injection",
                "dmg": 20,
                "crit": 0.4,
            },
            {
                "name": "Can Smack",
                "dmg": 25,
                "crit": 0.2,
            }
        ]
    },
    {
         "type": "Rabies Raccoon",
         "hp": 40,
         "xp": 60,
         "suicide": 0,
         "gold": 20,
         "attacks": [
             {
                 "name": "Bite",
                 "dmg": 30,
                 "crit": 0.3,
             },
             {
                 "name": "Scratch",
                 "dmg": 15,
                 "crit": 0.2,
             }
         ]
    },
    {
         "type": "Puffin' Dragon",
         "hp": 180,
         "xp": 220,
         "suicide": 0,
         "gold": 80,
         "attacks": [
             {
                 "name": "Blow Smoke",
                 "dmg": 5,
                 "crit": 0.9,
             },
             {
                 "name": "Cough",
                 "dmg": 69,
                 "crit": 0.2,
             }
         ]
    },
    {
         "type": "Greedy Dwarf",
         "hp": 80,
         "xp": 65,
         "suicide": 0,
         "gold": 60,
         "attacks": [
             {
                 "name": "Robbery",
                 "dmg": 20,
                 "crit": 0.4,
             },
             {
                 "name": "Pickaxe Swing",
                 "dmg": 32,
                 "crit": 0.2,
             }
         ]
    },
    {
         "type": "Giant Cyclops",
         "hp": 120,
         "xp": 85,
         "suicide": 0,
         "gold": 50,
         "attacks": [
             {
                 "name": "Sit-On",
                 "dmg": 50,
                 "crit": 0.2,
             },
             {
                 "name": "Stare",
                 "dmg": 0,
                 "crit": 100,
             }
         ]
    },
    {
         "type": "Garden Gnome",
         "hp": 25,
         "xp": 12,
         "gold": 20,
         "suicide": 1,
         "attacks": [
             {
                 "name": "Nibble Ankle",
                 "dmg": 5,
                 "crit": 0.2,
             },
             {
                 "name": "Break",
                 "dmg": 0,
                 "crit": 0.2,
                 
             }
         ]
    }
    ]






def delay_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.04)
    print()

def speedy_delay_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.01)
    print()

def Title_Art():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("██████╗ ██████╗  █████╗ ██╗    ██╗██╗")
    print("██╔══██╗██╔══██╗██╔══██╗██║    ██║██║")    
    print("██████╔╝██████╔╝███████║██║ █╗ ██║██║")   
    print("██╔══██╗██╔══██╗██╔══██║██║███╗██║██║")    
    print("██████╔╝██║  ██║██║  ██║╚███╔███╔╝███████╗")
    print("╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝")

    delay_print("  -THE LAST STAND OF TYLER DURDEN'T-\n\n")
    sleep(0.6)

def start_game():
    delay_print("Starting the game...")
    sleep(1)
    delay_print("You find yourself in a dark maosoleum, with the sounds of creatures all around you.")
    delay_print("There's nothing you can do... EXPECT BRAAAAAAAWL!\n")
    battle()

def shakespear_title():
    insult = [
    "artless", "bawdy", "beslubbering", "bootless", "churlish",
    "cockered", "clouted", "craven", "currish", "dankish",
    "dissembling", "droning", "errant", "fawning", "fobbing",
    "froward", "frothy", "gleeking", "goatish", "gorbellied",
    "impertinent", "infectious", "jarring", "loggerheaded",
    "lumpish", "mammering", "mangled", "mewling", "paunchy",
    "pribbling", "puking", "puny", "qualling", "rank",
    "reeky", "roguish", "ruttish", "saucy", "spleeny",
    "spongy", "surly", "tottering", "unmuzzled", "vain",
    "venomed", "villainous", "warped", "wayward", "weedy",
    "yeasty"
]
    return random.choice(insult)

def battle():
    global player_xp, player_gold, player_hp, player_dmg, traverse, xp_slider
    current_enemy = random.choice(enemies)
    delay_print(f"A {shakespear_title()} {current_enemy.get("type")} arises before your feet.")
    while True:
        if player_hp <= 0:
            player_gold = 0
            delay_print("You died and lost your gold...")
            delay_print("Returning to titlescreen.")
            sleep(2)
            player_hp = 100
            First_Title_Screen()
        else:
            delay_print(f"{current_enemy.get("type")} HP: {current_enemy.get("hp")}\n")
            current_enemy_attack = random.choice(current_enemy.get("attacks"))
            delay_print(f"{current_enemy.get("type")} attacks you with {current_enemy_attack['name']}!")
            delay_print(f"It deals {current_enemy_attack["dmg"]} DMG!\n")
            player_hp -= current_enemy_attack["dmg"]
            delay_print(f"Your HP: {player_hp}\n")
            delay_print("Retaliate with...?")
            delay_print("[1] Attack")
            delay_print("[2] Heavy Attack (W.I.P.)")
            delay_print("[3] Run\n")
            choice = input("> ")
            if choice == '1':
                strike = player_dmg + player_dmg * player_crit
                current_enemy["hp"] -= strike
                delay_print(f"You strike the enemy with your fist and deal {strike} damage!")
                if current_enemy["hp"] <= 0:
                    delay_print(f"{current_enemy.get('type')} was slain...\n")
                    delay_print(f"You gained {current_enemy.get('xp')} XP!")
                    delay_print(f"You gained {current_enemy.get('gold')} Gold!\n")
                    player_xp += current_enemy["xp"]
                    player_gold += current_enemy["gold"]
                    xp_sequence()
                    delay_print("Would you like to traverse deeper? y/n")
                    traverse = input("> ")
                    if traverse == "y":
                        battle()
                    elif traverse == "n":
                        print("Returning to titlescreen.")
                        sleep(1)
                        player_hp = 100
                        First_Title_Screen()
                    else:
                        print("Invalid input. Please try again")
                        battle()
            elif choice == '2':
                delay_print("Heavy Attack is a work in progress. u dumbass.\n")
                battle()
            elif choice == '3':
                delay_print(f"You run away leaving the {current_enemy.get("type")} in the dust.")
                sleep(2)
                First_Title_Screen()
            else:
                delay_print("Invalid choice. Please try again.")
                battle()


def xp_sequence():
    global player_xp, player_lvl, xp_slider
    if player_xp >= 160:
        player_xp -= 160
        player_lvl += 1
        delay_print(f"You leveled up!")
    else:
        return

            

def Tavern():
    global player_lvl, player_xp, player_gold, player_dmg, player_crit, player_hp, xp_slider
    speedy_delay_print("================================")
    speedy_delay_print("       THE RUSTY DRAGON")
    speedy_delay_print("================================")
    speedy_delay_print("  The smell of roasted meat")
    speedy_delay_print("  and skunked ale fills the air.")
    speedy_delay_print("")
    speedy_delay_print("  What would you like to do?\n")
    speedy_delay_print("[1] Buy a drink (15 Gold)")
    speedy_delay_print("[2] Talk to @£?#!")
    speedy_delay_print("[3] Talk to the bartender")
    speedy_delay_print("[4] Leave the tavern\n")
    title_choice = input("> ")
    if title_choice == '1':
        if player_gold >= 15:
            player_gold -= 15
            delay_print("You buy a drink and feel it's warmth flow through your body.")
            delay_print("You feel a bit more powerful...")
            player_dmg += 5
            delay_print(f"Gold: {player_gold}")
            sleep(2)
            Tavern()
        else:
            delay_print("You don't have enough gold to buy a drink.")
            sleep(2)
            Tavern()
    elif title_choice == '2':
        delay_print("You walk up to the shady looking character.")
        delay_print("He looks at you with a sinister grin and opens his coat to reveal a collection of knives and other sharp objects.")
        delay_print("He says, 'I can make you stronger... for a price.'")
        if player_gold >= 50:
            delay_print("You pay him 50 gold and he hands you a small vial of liquid.")
            delay_print("You drink it and feel a surge of power coursing through your veins.")
            player_dmg += 10
            player_crit += 0.05
            player_gold -= 50
            delay_print(f"Gold: {player_gold}")
            sleep(2)
            Tavern()
        else:
            delay_print("You don't have enough gold to pay him. He looks disappointed and walks away.")
            sleep(2)
            Tavern()
    elif title_choice == '3':
        if player_gold >= 300:
            player_gold -= 120
            delay_print("'You better be careful with that sweet wad of cash hanging around in here.'")
            print(f"Gold: {player_gold} - 120")
            player_gold -= 120
            sleep(2)
            First_Title_Screen()
        else:
            delay_print("The bartender tells you to leave. He doesn't like your face.")
        sleep(2)
        First_Title_Screen()
    elif title_choice == '4':
        delay_print("You leave the tavern...")
        sleep(2)
        First_Title_Screen()
    






def First_Title_Screen():
    global player_xp, player_dmg, player_gold, player_crit, player_lvl, xp_slider
    Title_Art()
    if player_xp == 0:
        xp_slider = "#---------"
    elif player_xp > 20:
        xp_slider = "##--------"
    elif player_xp > 40:
        xp_slider = "###-------"     
    elif player_xp > 60:
        xp_slider = "####------"
    elif player_xp > 80:
        xp_slider = "#####-----"
    elif player_xp > 100:
        xp_slider = "######----"
    elif player_xp > 120:
        xp_slider = "#######---"
    elif player_xp > 140:
        xp_slider = "########--"     
    elif player_xp > 160:
        xp_slider = "#########-"
    player_hp = 100
    speedy_delay_print(f"Player Stats:\nHP: {player_hp}, DMG: {player_dmg}, Crit Chance: {player_crit*100}%, Gold: {player_gold}")
    delay_print(f"Xp: {xp_slider}, Lvl: {player_lvl}\n")
    delay_print("Where to go?")
    delay_print("[1] Start Game")
    delay_print("[2] Tavern")
    delay_print("[3] Exit\n")
    choice = input("> ")
    if choice == '1':
        start_game()
    elif choice == '2':
        Tavern()
    elif choice == '3':
        delay_print("Exiting the game. Bye bye!")
        exit()
    else:
        delay_print("Invalid choice. Please try again.")
        First_Title_Screen()

First_Title_Screen()




