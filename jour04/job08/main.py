f = open('jour04/job08/maze.mz', 'r')
# print(f.read())
finding = True

def maze(f):
    if f.readline():
        print(f.readline())
        maze(f)
    else:
        return 1

maze(f)