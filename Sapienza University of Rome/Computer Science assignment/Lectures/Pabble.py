
def wingame(game):
    if (game[0] % 2) != 0 and (game[1] % 2) != 0:
        print("Remove one from both")
        game[0] = game[0]-1
        game[1] = game[1]-1
        print(game, "This is a winning situation")
    elif (game[0] % 2) == 0 and (game[1] % 2) == 0:
        print("This is a lose situation")
    elif (game[0] % 2) == 0 and (game[1] % 2) != 0:
        print("Remove one from the right pabble")
        game[1] = game[1]-1
        print(game, "This is a winning situation")
    elif (game[0] % 2) != 0 and (game[1] % 2) == 0:
        print("Remove one from the left pabble")
        game[0] = game[0]-1
        print(game, "This is a winning situation")
    elif game[0]*game[1]==0:
        if (game[1] % 2) == 0:
            print("Remove one from the right pabble")
            game[1]=game[1]-1
            print(game, "'This is a winning situation")
        elif (game[0] % 2) == 0:
            print("Remove one from the left pabble")
            game[0]=game[0]-1
            print(game, "This is a winning situation")

        else:
            print("This os a lose situations")
play = "y"
while play == "y":
    game = [int(input("How many stones the first stack has?")),int(input("How many stones the second stack has?"))]
    wingame(game)
    play == input("Do u wanto to play again? (y or n)")