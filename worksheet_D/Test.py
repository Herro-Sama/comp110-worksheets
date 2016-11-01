Board = [[0,0,0],[0,0,0],[0,0,0]]

def get_state(Board, x, y):
    available = Board[y-1] [x-1]
    if available == 1:
        return 'X'
    if available == 2:
        return 'O'
    return ' '

def set_state(Board, x, y, player):
    if player == 'X':
        available = 1
    else:
        available = 2
    Board[y-1] [x-1] = available

def is_winner(Board):
    if Board[1] [1] !=0:
        if Board[0] [0] == Board[1] [1]:
            if Board [2] [2] == Board[1] [1]:
                return True

        if Board [2] [0] == Board[1] [1]:
            if Board [0] [2] == Board[1] [1]:
                return True

    for i in xrange (0,3):
        if Board [0] [i] != 0:
            if Board [0] [i] == Board [1] [i]:
                if Board [0] [i] == Board [2] [i]:
                    return True

        if Board [i] [0] != 0:
            if Board [i] [0] == Board [i] [1]:
                if Board [i] [0] == Board [i] [2]:
                    return True


    return False

def print_row(Board,x):
    output = get_state(Board, x, 1)
    output += '|' + get_state(Board,x, 2)
    output += '|' + get_state(Board,x, 3)
    print output

def print_board(Board):
    print_row(Board, 1)
    print '_____'
    print_row(Board, 2)
    print '_____'
    print_row(Board, 3)

ongoing = True
CurrentPlayer = 'X'
spaces = 9
while ongoing:
    print_board(Board)
    print CurrentPlayer + "'s turn"
    print "Row?"
    x = int(raw_input())
    print "Column?"
    y = int(raw_input())
    current = get_state(Board, x, y)
    if current != ' ':
        print "That space is occupied!"
    else:
        set_state(Board, x, y, CurrentPlayer)
        spaces -= 1

        if is_winner(Board):
            print CurrentPlayer + " wins!"
            ongoing = False

        if spaces == 0:
           print "Stalemate!"
           ongoing = False

        else:
            if CurrentPlayer == 'X':
                CurrentPlayer = 'O'
            else:
                CurrentPlayer = 'X'