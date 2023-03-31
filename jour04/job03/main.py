import random

number = int(input('Entrez un nombre: '))
lastQueen = []
test = list(range(1, number + 1))
restart = False

# IMPOSSIBLE DE FAIRE UNE FONCTION QUI TEST SANS BOUCLE
def deplacementPossilble(lastQueen, queenColumn):
    i = 0
    # print(lastQueen, queenColumn)
    for movement in reversed(lastQueen):
        gap = movement - queenColumn
        if gap == i + 1 or gap == -i - 1:
            return False
        i += 1
    return True
    

def queen(n):
    global lastQueen
    global test
    global restart
    if (n == 0):
        restart = True
        return 'Impossible de placer la reine'
    queenColumn = random.choice(test)
    if queenColumn not in lastQueen and deplacementPossilble(lastQueen, queenColumn):
        string = ' . ' * (queenColumn - 1) + ' X ' + ' . ' * (number - queenColumn)
        lastQueen.append(queenColumn)
        test.remove(queenColumn)
    else:
        # print('recommence', queenColumn, lastQueen)
        return queen(n - 1)
    return string
        

def print_board(n):
    if n == 0:
        return 1
    else:
        print(queen(n))
        return print_board(n - 1)
    

print_board(number)
while restart:
    restart = False
    lastQueen = []
    test = list(range(1, number + 1))
    print('-' * 50)
    print()
    print_board(number)
    print()
print('-' * 50)
print('Solution trouvée:')
print(lastQueen)