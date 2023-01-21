import random
import time
import termcolor
import os

# Create Default Board
board = {}
for a in range(0, 9):
    board[a] = f"{a}"
# Create all cases of winning
wining_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal cases
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical cases
                [0, 4, 8], [2, 4, 6]]  # Diagonal cases


def update_board(x=None, o=None):
    """
    Print X or O on game board according to values of x and o.
    :param x: Position of X on board
    :param o: Position of O on board
    :return: None
    """
    os.system("clear")
    x_char = termcolor.colored('X', 'blue')
    o_char = termcolor.colored('O', 'red')
    if x is not None:
        board[x] = x_char
    if o is not None:
        board[o] = o_char

    print(f"{board[0]}|{board[1]}|{board[2]}\n------\n{board[3]}|{board[4]}|{board[5]}\n------"
          f"\n{board[6]}|{board[7]}|{board[8]}\n------")


def check_unoccupied_places(*places):
    """
    Check places that are empty or not then return those one that are empty.
    This function returns [] when there is no empty place among places param on board.
    :param places: Positions of board that are wanted to check.
    :return: List of Empty Places
    """

    empty_places = []
    for c in places:
        if board[c] == str(c):
            empty_places.append(c)
    return empty_places


def get_winning_move(player):
    """
    Gets a move that can make player (Computer or User) winner
    :param player: Determines player (X or O).
    X is used for User and O is used for Computer.
    :return: Position number that can make player winner of game.
    It returns None when there is no way to win.
    """

    selected = []
    lt = []  # List of every two elements (as tuple) of selected list.
    # Set color variable due to player value. Used for termcolor module.
    if player == "X":
        color = "blue"
    else:
        color = "red"
    # Fetch position numbers that player selected so far in the game and then put them into selected list.
    for i in board:
        if board[i] == termcolor.colored(player, color):
            selected.append(i)
    # Find cases of every two elements of selected list.
    # Ex) selected = [1,2,3] => lt = [(1,2),(1,3),(2,3)]
    for j in selected:
        k = 1
        while selected.index(j) + k <= len(selected) - 1:
            lt.append((j, selected[selected.index(j) + k]))
            k += 1
    # Get winning move due to all win cases.
    for case in wining_cases:
        for i in lt:
            if set(case).intersection(set(i)) == set(i):
                return list(set(case).difference(set(i)))[0]
    return None


def check_winner(player):
    """
    Due to player's moves, check that if player can win or not.
    :param player: Determines player (X or O).
    X is used for User and O is used for Computer.
    :return: Return 1 if player won the game.
    """

    selected = []
    # Set color variable due to player value. Used for termcolor module.
    if player == "X":
        color = "blue"
    else:
        color = "red"
    # Fetch position numbers that player selected so far in the game and then put them into selected list.
    for i in board:
        if board[i] == termcolor.colored(player, color):
            selected.append(i)
    # Check that if player can win the game.
    for case in wining_cases:
        if set(case).intersection(set(selected)) == set(case):
            return 1
    return 0


def make_computer_move():
    if player_char["Computer"] == "O":
        if get_winning_move("O") is not None and check_unoccupied_places(get_winning_move("O")):
            update_board(o=get_winning_move("O"))
        elif get_winning_move("X") is not None and check_unoccupied_places(get_winning_move("X")):
            update_board(o=get_winning_move("X"))
        elif check_unoccupied_places(0, 2, 6, 8):
            update_board(o=random.choice(check_unoccupied_places(0, 2, 6, 8)))
        elif check_unoccupied_places(4):
            update_board(o=random.choice(check_unoccupied_places(4)))
        elif check_unoccupied_places(1, 3, 5, 7):
            update_board(o=random.choice(check_unoccupied_places(1, 3, 5, 7)))
    elif player_char["Computer"] == "X":
        if get_winning_move("X") is not None and check_unoccupied_places(get_winning_move("X")):
            update_board(x=get_winning_move("X"))
        elif get_winning_move("O") is not None and check_unoccupied_places(get_winning_move("O")):
            update_board(x=get_winning_move("O"))
        elif check_unoccupied_places(0, 2, 6, 8):
            update_board(x=random.choice(check_unoccupied_places(0, 2, 6, 8)))
        elif check_unoccupied_places(4):
            update_board(x=random.choice(check_unoccupied_places(4)))
        elif check_unoccupied_places(1, 3, 5, 7):
            update_board(x=random.choice(check_unoccupied_places(1, 3, 5, 7)))


def check_input(choice):
    if not choice.isdigit():
        return termcolor.colored("Please Enter a number", "red")
    if not 0 <= int(choice) <= 8:
        return termcolor.colored("Please Enter a number between 0 to 8", "red")
    if not check_unoccupied_places(int(choice)):
        return termcolor.colored("Please select an unoccupied position", "red")
    return None


def determine_player_character():
    global player_char
    player_char = {"Computer": "", "User": ""}
    while True:
        char = input("Select your character: (X or O) \n").upper()
        if char == "X":
            player_char["User"] = "X"
            player_char["Computer"] = "O"
            break
        elif char == "O":
            player_char["User"] = "O"
            player_char["Computer"] = "X"
            break
        else:
            continue


def main():
    os.system("clear")
    print(termcolor.colored("<< Welcome to Tic-tac-toe Game >>", "green"))
    time.sleep(3)
    os.system("clear")
    determine_player_character()
    # Determine randomly whether the computer or the player goes first.
    turn = random.choice([0, 1])  # 0 => Player (X) , 1 => Computer (O)
    if turn == 1:
        make_computer_move()
        print("Computer did its move, now it's your turn.")
    else:
        update_board()
        print("It's your turn :)")
    while True:
        choice = input()
        if check_input(choice) is None:
            if player_char["User"] == "X":
                update_board(x=int(choice))
            else:
                update_board(o=int(choice))

        else:
            print(check_input(choice))
            continue
        if check_winner(player_char["User"]) == 1:
            print("User won :)")
            break

        make_computer_move()
        if check_winner(player_char["Computer"]) == 1:
            print("Computer won :)")
            break
        if not check_unoccupied_places(0, 1, 2, 3, 4, 5, 6, 7, 8):
            print("Tie")
            break


main()
