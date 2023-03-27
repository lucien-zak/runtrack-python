def drawRectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('|' + ('-' * width) + '|')
        else:
            print('|' + (' ' * width) + '|')

drawRectangle(10, 5)