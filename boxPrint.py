def boxprint(symbol, width, height):

    if (len(symbol) != 1):
        raise Exception('"symbol" needs to be a string of length of 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)

    print(symbol * width)

    
boxprint('*', 15, 5)
boxprint('O', 5, 15)
#boxprint('xx', 5, 5)
boxprint('x', 1, 1)
