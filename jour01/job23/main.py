TRIANGE_BASE = '_'
TRIANGE_RIGHT = '\\'
TRIANGE_LEFT = '/' 

def drawTriangle(base):
    for i in range(base):
        if i == base - 1:
            print((' ' * (base - i)) + TRIANGE_LEFT + (TRIANGE_BASE * (i + i)) + TRIANGE_RIGHT)
        else: 
            print((' ' * (base - i)) + TRIANGE_LEFT + (' ' * (i + i)) + TRIANGE_RIGHT)

drawTriangle(9)