# a battle game, play against a bot
# starter pack: hp = 30/100
# equipped with different weapons, each accounts different points
# choose in turn
# lose: hp = 0

import random
import time

print("hi! welcome to my new battle game!")
time.sleep(1)
player = input("enter your name: ")

while True:
    # intro: player, bot
    bot_list = ("spongebob tripants", "garfarm", "male-efficient")
    bot = random.choice(bot_list)

    print("\nhi", player, ", you will play against", bot, "\n")
    time.sleep(0.7)

    # intro: weapon - points
    weapon = {'stick': 1, 'hands': 3, 'chair': 5, 'keyboard': 7, 'words': 10}
    print("you can choose from these weapons:", weapon, "\n")

    # gameplay
    hp = {player: 50, bot: 50}

    while True:
        time.sleep(1)
        player_move = input("choose your weapon: ").lower()
        print(player, "chooses", player_move)
        if player_move in weapon:
            hp[bot] -= weapon.get(player_move)
        else:
            pass

        bot_move = random.choice(list(weapon.keys()))
        print(bot, "chooses", bot_move)
        hp[player] -= weapon.get(bot_move)

        time.sleep(0.5)
        print(hp, "\n")

        if hp[player] == 0 or hp[player] < 0 or hp[bot] == 0 or hp[bot] < 0:
            break

    # announce the winner
    if hp[player] > hp[bot]:
        print("and the winner is", player, "! congrats!")
    elif hp[player] == hp[bot]:
        print("it's a tie!")
    else:
        print("you lost to a bot!")

    time.sleep(0.7)
    if input("\nnice game! want another round? y/n: ").lower() != "y":
        print("thanks for playing!")
        break
