def chess_knight_move(coords):

    try:
        numlst = coords.split('-')
    except:
        print('ERROR')
        exit()

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    if len(numlst) <= 5:
        try:
            li1 = letters.index(numlst[0][0])
            ni1 = numbers.index(numlst[0][1])

            li2 = letters.index(numlst[1][0])
            ni2 = numbers.index(numlst[1][1])
        except:
            print("ERROR")
            exit()

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
