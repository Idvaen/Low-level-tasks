"""Can knight move in chess YES or NO"""


import sys


def chess_knight_move(coords: str) -> str:
    """Chess knight moves"""
    try:
        numlst = coords.split('-')
    except TypeError:
        print('ERROR')
        sys.exit(1)

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    if len(numlst) <= 5:
        try:
            li1 = letters.index(numlst[0][0])
            ni1 = numbers.index(numlst[0][1])

            li2 = letters.index(numlst[1][0])
            ni2 = numbers.index(numlst[1][1])
        except ValueError:
            print("ERROR")
            sys.exit(1)

        if letters[li1-2] == letters[li2] and numbers[ni1-1] == numbers[ni2]:
            print("YES")
        elif letters[li1-2] == letters[li2] and numbers[ni1+1] == numbers[ni2]:
            print("YES")
        elif letters[li1-1] == letters[li2] and numbers[ni1-2] == numbers[ni2]:
            print("YES")
        elif letters[li1-1] == letters[li2] and numbers[ni1+2] == numbers[ni2]:
            print("YES")
        elif letters[li1+1] == letters[li2] and numbers[ni1-2] == numbers[ni2]:
            print("YES")
        elif letters[li1+1] == letters[li2] and numbers[ni1+2] == numbers[ni2]:
            print("YES")
        elif letters[li1+2] == letters[li2] and numbers[ni1-1] == numbers[ni2]:
            print("YES")
        elif letters[li1+2] == letters[li2] and numbers[ni1+1] == numbers[ni2]:
            print("YES")
        else:
            print("NO")


if __name__ == "main":
    print(chess_knight_move("2 6 8"))
