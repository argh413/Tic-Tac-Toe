import random
from time import sleep
from termcolor import colored
from os import system

# Create Default Board
board = {}
for a in range(0, 9):
    board[a] = str(a)
# Create all cases of winning
wining_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal cases
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical cases
                [0, 4, 8], [2, 4, 6]]  # Diagonal cases

player_char = {"Computer": "", "User": ""}


def update_board(x=None, o=None):
    """
    Prints X or O on game board according to values of x and o params.
    :param x: Position of X on board
    :param o: Position of O on board
    :return: None
    """
    system("clear")  # Clear the console
    x_char = colored('X', 'blue')  # Set color of X
    o_char = colored('O', 'red')  # Set color of O
    if x is not None:
        board[x] = x_char
    if o is not None:
        board[o] = o_char

    print(colored("You -> {0} | Computer -> {1}".format(player_char["User"], player_char["Computer"]), "cyan"))
    print(f"{board[0]}|{board[1]}|{board[2]}\n------\n{board[3]}|{board[4]}|{board[5]}\n------"
          f"\n{board[6]}|{board[7]}|{board[8]}\n------")


def check_unoccupied_places(*places):
    """
    Checks if places are occupied or not then return those one that are unoccupied.
    This function returns [] when there is no empty place among places param on board.
    :param places: Positions of board that are wanted to check.
    :return: List of unoccupied places
    """

    unoccupied_places = []
    for c in places:
        if board[c] == str(c):
            unoccupied_places.append(c)
    return unoccupied_places


def get_selected_places(player):
    """
    Gets the places that player selected.
    :param player: Determines player (X or O)
    :return: List of player's selected places
    """
    selected = []
    # Set color variable due to player value. Used for termcolor module.
    if player == "X":
        color = "blue"
    else:
        color = "red"
    # Fetch position numbers that player selected so far in the game and then put them into selected list.
    for i in board:
        if board[i] == colored(player, color):
            selected.append(i)
    return selected


def get_winning_move(player):
    """
    Gets a move that can make player (Computer or User) winner
    :param player: Determines player (X or O).
    :return: Position number that can make player winner of game.
    It returns None when there is no way to win.
    """
    selected = get_selected_places(player)
    lt = []  # List of every two elements (as tuple) of selected list.
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
    Due to player's moves, checks that if player can win or not.
    :param player: Determines player (X or O).
    :return: Return 1 if player won the game.
    """
    selected = get_selected_places(player)
    # Check that if player can win the game.
    for case in wining_cases:
        if set(case).intersection(set(selected)) == set(case):
            return 1
    return 0


def make_computer_move():
    """
    Makes a move for computer due to scenario of the game.
    :return: selected position on board by computer
    """
    position = None
    if player_char["Computer"] == "O":
        if get_winning_move("O") is not None and check_unoccupied_places(get_winning_move("O")):
            position = get_winning_move("O")
            update_board(o=position)
        elif get_winning_move("X") is not None and check_unoccupied_places(get_winning_move("X")):
            position = get_winning_move("X")
            update_board(o=position)
        elif check_unoccupied_places(0, 2, 6, 8):
            position = random.choice(check_unoccupied_places(0, 2, 6, 8))
            update_board(o=position)
        elif check_unoccupied_places(4):
            position = random.choice(check_unoccupied_places(4))
            update_board(o=position)
        elif check_unoccupied_places(1, 3, 5, 7):
            position = random.choice(check_unoccupied_places(1, 3, 5, 7))
            update_board(o=position)
    elif player_char["Computer"] == "X":
        if get_winning_move("X") is not None and check_unoccupied_places(get_winning_move("X")):
            position = get_winning_move("X")
            update_board(x=position)
        elif get_winning_move("O") is not None and check_unoccupied_places(get_winning_move("O")):
            position = get_winning_move("O")
            update_board(x=position)
        elif check_unoccupied_places(0, 2, 6, 8):
            position = random.choice(check_unoccupied_places(0, 2, 6, 8))
            update_board(x=position)
        elif check_unoccupied_places(4):
            position = random.choice(check_unoccupied_places(4))
            update_board(x=position)
        elif check_unoccupied_places(1, 3, 5, 7):
            position = random.choice(check_unoccupied_places(1, 3, 5, 7))
            update_board(x=position)

    return position


def check_input(choice):
    """
    Checks if selected position is valid or not.
    :param choice: Selected position by user
    :return: Return error message if selected position is invalid
    Return None if selected position is OK
    """
    if not choice.isdigit():
        return colored("Please Enter a number", "red")
    if not 0 <= int(choice) <= 8:
        return colored("Please Enter a number between 0 to 8", "red")
    if not check_unoccupied_places(int(choice)):
        return colored("Please select an unoccupied position", "red")
    return None


def determine_player_character():
    """
    Determines player character (X or O) for User and Computer.
    :return: None
    """
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
    system("clear")
    print(colored("<< Welcome to Tic-tac-toe Game >>", "green"))
    sleep(3)
    system("clear")
    determine_player_character()
    # Determine randomly whether the computer or the player goes first.
    turn = random.choice([0, 1])  # 0 => User , 1 => Computer
    if turn == 1:
        computer_move = make_computer_move()
        print(f"Computer selected {computer_move} on board, now it's your turn.")
    else:
        update_board()
        print("It's your turn.")
    while True:
        choice = input("Select an unoccupied position :  ")
        if check_input(choice) is None:
            if player_char["User"] == "X":
                update_board(x=int(choice))
            else:
                update_board(o=int(choice))

        else:
            print(check_input(choice))
            continue
        if check_winner(player_char["User"]) == 1:
            print(colored("You won!", "magenta"))
            break

        computer_move = make_computer_move()
        if computer_move is not None:
            print(f"Computer selected {computer_move} on board.")
        if check_winner(player_char["Computer"]) == 1:
            print(colored("Computer won!", "magenta"))
            break
        # if check_unoccupied_places return [] for all positions on board, the game ends in tie.
        if not check_unoccupied_places(0, 1, 2, 3, 4, 5, 6, 7, 8):
            print(colored("Tie!", "magenta"))
            break


main()
