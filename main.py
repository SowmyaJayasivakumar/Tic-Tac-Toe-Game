from helpers import create_board,check_turn,check_win
import os

spot = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

complete = False
turn = 0
prev_turn = -1
playing = True
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    create_board(spot)

    if prev_turn == turn:
        print("Invalid spot selected. please pick another.")
    prev_turn = turn

    print(f"Player {str((turn%2)+1)}'s turn : Pick ur spot or press 'q' to quit.")
    choice = input()
    
    if choice == 'q':
        playing = False
        break
    elif str.isdigit(choice) and int(choice) in spot:
        if not spot[int(choice)] in {'X','O'}:
            turn += 1
            spot[int(choice)] = check_turn(turn)
        else:
            print("Spot already taken. Choose another spot.")
            continue
    else:
        print("Invalid input. Please enter a valid spot number or 'q' to quit.")
        continue

    if check_win(spot):
        playing = False
        complete = True

    if turn > 8:
        playing = False
        print("No more moves")
        break

    os.system('cls' if os.name == 'nt' else 'clear')
    create_board(spot)

    if complete:
        if check_turn(turn) == 'X':
            print('Player 1 Wins!')
        else:
            print('Player 2 Wins!')
    else:
        print("Tie")

print("Thanks for playing")