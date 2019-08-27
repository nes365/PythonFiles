def typer(x):
    '''
    Returns datatype for x (limited use)
    '''
    if type(x) == int:
        print('This is an integer')
    elif type(x) == str:
        print('This is a string')
    else:
        print('This is neither an integer nor a string')

print(typer(200))
