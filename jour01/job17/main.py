for i in range (101):
    output = str(i) + ' : '    
    if i % 3 == 0 and i != 0:
        output += 'Fizz'
    if i % 5 == 0 and i != 0:
        output += 'Buzz'
    print(output)
