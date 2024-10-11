def create_board(spot):
    board = (f"|{spot[1]}|{spot[2]}|{spot[3]}|\n"
             f"|{spot[4]}|{spot[5]}|{spot[6]}|\n"
             f"|{spot[7]}|{spot[8]}|{spot[9]}|")
    
    print(board)

def check_turn(turn):
    if turn % 2==0:
        return 'O'
    else:
        return 'x'


def check_win(spot):
    # horizontal cases
    if (spot[1]==spot[2]==spot[3]) or (spot[4]==spot[5]==spot[6]) or (spot[7] == spot[8] == spot[9]):
        return True

    #vertical cases
    elif (spot[1]==spot[4]==spot[7]) or (spot[2]==spot[5]==spot[8]) or (spot[3]==spot[6]==spot[9]):
        return True
    
    #diagonal cases
    elif (spot[1]==spot[5]==spot[9]) or(spot[3]==spot[5]==spot[7]):
        return True
    
    else:
        return False

