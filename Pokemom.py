import random
from Player import Player


def pokemom():

    # Asking user for difficulty
    difficulty = input("Enter a difficulty level(Easy, Medium, Hard):\n").lower()
    user = Player()
    comp = Player(difficulty)
    player_move = True

    print("It is time to battle! You and your opponent each have 100 health.\n----------------------------------------")

    # Checks to see if game should continue
    while user.health > 0 and comp.health > 0:
        if player_move:
            # Ask for user input on their move.
            move = int(input("Your turn. Choose a move(number):\n1. Normal Strike\n2. Lucky Strike\n3. Heal\n"))
            dmg = choose_move(user, move)
            if dmg < 0:
                # dmg is negative when the move is heal
                user.health = user.health - dmg
                print("You have healed for " + str(-1 * dmg) + " health.")
            else:
                # dmg is positive when move is a damaging move
                comp.health = comp.health - dmg
                print("You have inflicted " + str(dmg) + " damage upon your opponent.")
        else:
            dmg = comp_move(comp)
            if dmg < 0:
                comp.health = comp.health - dmg
                print("Your opponent have healed for " + str(-1 * dmg) + " health.")
            else:
                user.health = user.health - dmg
                print("Your opponent has inflicted " + str(dmg) + " damage upon you.")
        print_status(user, comp)
        player_move = not player_move

    # End game
    if user.health <= 0:
        print("Game over. You have lost.")
    else:
        print("Congratulations! You have won.")


def comp_move(player):
    # Randomly selects a move for the computer. If health is less than 35, heal is more likely to be used.
    if player.health > 35:
        rand_move = random.randrange(1, 4)
    else:
        rand_move = random.randrange(1, 5)
    if rand_move == 1:
        print("Your opponent chose to use normal strike.")
    elif rand_move == 2:
        print("Your opponent chose to use lucky strike.")
    else:
        print("Your opponent chose to use heal.")
    return choose_move(player, rand_move)


def choose_move(player, n):
    # Selects the health value of the move depending on the player object.
    if n == 1:
        return player.normal_strike()
    elif n == 2:
        return player.lucky_strike()
    else:
        return player.heal()


def print_status(user, comp):
    # Prints the health of both players.
    if user.health < 0:
        h1 = 0
        h2 = comp.health
    elif comp.health < 0:
        h2 = 0
        h1 = user.health
    else:
        h1 = user.health
        h2 = comp.health
    print("--------------------------------------------------------------------------------")
    print("You have " + str(h1) + " health and your opponent has " + str(h2) + " health.\n")


pokemom()
