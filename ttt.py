cell_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_board():
    print("---------")
    print("|" + " " + cell_list[0] + " " + cell_list[1] + " " + cell_list[2] + " " + "|")
    print("|" + " " + cell_list[3] + " " + cell_list[4] + " " + cell_list[5] + " " + "|")
    print("|" + " " + cell_list[6] + " " + cell_list[7] + " " + cell_list[8] + " " + "|")
    print("---------")


print_board()


def main_game():
    count = 0

    while True:
        move = input("Enter coordinates: ").split()
        for x in move:
            if x == "X" or x == "O":
                count += 1
        if count % 2 == 0:
            turn = 'X'
        else:
            turn = 'O'

        if move[0].isalpha() or move[1].isalpha():
            print("You should enter numbers!")
            continue

        cell_list_col, cell_list_row = move
        cell_list_x = int(cell_list_col) - 1
        cell_list_y = 3 - int(cell_list_row)
        move = (cell_list_y * 3) + cell_list_x

        if int(cell_list_col) > 3 or int(cell_list_row) > 3 or int(cell_list_col) == 0 or int(cell_list_row) == 0:
            print("Coordinates should be from 1 to 3!")
            continue

        if cell_list[move] == ' ':
            cell_list[move] = turn
            count += 1
            print_board()
        else:
            print("This cell is occupied! Choose another one!")

        if count >= 5:
            if cell_list[0] == cell_list[1] == cell_list[2] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[3] == cell_list[4] == cell_list[5] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[6] == cell_list[7] == cell_list[8] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[6] == cell_list[3] == cell_list[0] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[7] == cell_list[4] == cell_list[1] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[8] == cell_list[5] == cell_list[2] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[0] == cell_list[4] == cell_list[8] != ' ':
                print_board()
                print(turn + ' wins')
                break
            elif cell_list[8] == cell_list[4] == cell_list[0] != ' ':
                print_board()
                print(turn + ' wins')
                break

        if count == 9:
            print_board()
            print("Draw")
            break


main_game()
