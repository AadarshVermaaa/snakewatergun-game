import random
# snake water gun
game_tools = ["snake", "water", "gun"]
game = True
lives = 5
cpu_score = []
player_score = []
while game:
    if lives == 1:
        game = False
    random_choice = random.choice(game_tools)
    gamer_input = int(input(
        "FOR\n\tSNAKE PRESS 1\n\tWATER PRESS 2\n\tGUN PRESS 3\n\t"))
    print("CPU CHOICE ==",random_choice)
    print("YOUR CHOICE ==",gamer_input)
    lives = lives- 1
    print(f"\t\tLives Left[{lives}]\t\t")
    if gamer_input == 1 and random_choice == game_tools[0]:
        print("ITS A DRAW")
        print("[No Score]")
        
    elif gamer_input == 1 and random_choice == game_tools[1]:
        print("YOU WIN THIS CHANCE")
        player_score.append(1)

    elif gamer_input == 1 and random_choice == game_tools[2]:
        print("YOU LOOSE THIS CHANCE")
        cpu_score.append(1)

    elif gamer_input == 2 and random_choice == game_tools[0]:
        cpu_score.append(1)
        print("YOU LOOSE THIS CHANCE")
    
    elif gamer_input == 2 and random_choice == game_tools[1]:
        print("ITS A DRAW")
        print("[No Score]")
    
    elif gamer_input == 2 and random_choice == game_tools[2]:
        print("YOU WIN THIS CHANCE")
        player_score.append(1)

    elif gamer_input == 3 and random_choice == game_tools[0]:
        print("YOU WIN THIS CHANCE")
        player_score.append(1)
    
    elif gamer_input == 3 and random_choice == game_tools[1]:
        print("YOU LOOSE THIS CHANCE")
        cpu_score.append(1)
    
    elif gamer_input == 3 and random_choice == game_tools[2]:
        print("ITS A DRAW")
        print("[No Score]\n\n")
    else:
        print("invalid input")
        

print("Your Score --- [",len(player_score),"]")
print("CPU Score --- <",len(cpu_score),">")
if len(cpu_score) < len(player_score):
    print("[YOU WIN CONGRATS]")
elif len(cpu_score) == len(player_score):
    print("[DRAW]")
else:
    print("[YOU LOOSE]")
