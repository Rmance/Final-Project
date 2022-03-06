#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/1/2022

#Purpose: Creating a game
#-------------------------------------------------------------------------------

import random

print("Welcome Gamer - To the Celestial Adventure")

game_on = True
while game_on:
    ans = str(input("Would you like to begin?"))
    if (ans == 'yes'):
        print("Let's begin! Let's name your dragon!")
        name = str(input("What shall their name be?"))
        game_on = False

    elif(ans == 'no'):
        print("Thanks for playing")
        quit()

    else:
        print("Invalid Input")

print("Before we begin our adventure, we have to get", name,
"battle ready")
print("The enemies are known as Nightmares, and for your tutorial fight")
print("You'll be facing off against three")
print("These are your movesets for", name)

Alist = ['A.Fireball', 'B.Super Claws', 'C.Tail Slasher']
print(Alist)
enemy = 3

ehealth = random.randint(150,200)

def Attack(move):
    if move == 'a' or move == 'A':
        attackDamage = 150
        return attackDamage
    elif 'b' == move or move == 'B':
        attackDamage = 75
        return attackDamage
    elif move == 'c' or move == 'C':
        attackDamage = 50
        return attackDamage
    else:
        print("Move invalid - skipping turn")
        attackDamage = 0
        return attackDamage

def E_health(hits, nightmare, player, hearts):

    print(name, "has done", hits, "damage")
    print("Enemy", nightmare, "had", hearts, "health")
    ouch = hearts - hits

    if ouch > 0:
        print("Enemy", nightmare, "has", ouch, "left")
        return 0 and ouch

    elif ouch <= 0:
        print("Enemy", nightmare, "has been defeated")
        return 1


while enemy != 0:
    attck = str(input())
    if 'a' == attck or attck == 'A':
        print("You're using Fireball")
    elif 'b' == attck or attck == 'B':
        print("You're using Super Claws")
    elif attck == 'c' or attck == 'C':
        print("You're using Tail Slasher")
    else:
        print("Invalid move")

    dam = Attack(attck)
    remain = E_health(dam, enemy, name, ehealth)
    enemy = enemy - remain

print("You defeated them!")