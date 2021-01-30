string1 = input('String: ')
string2 = input('String: ')

def bronze1():
    for letter in string1:
        print(letter)

def bronze2():
    print(string1[0], string2[-1])

def bronze3():
    print(len(string1))

def bronze4():
    if string1 < string2:
        print(string1)
    else:
        print(string2)

def bronze5():
    for x in range(1, 11, 1):
        print(x)
    print('- -')
    for x in range(10, 0, -1):
        print(x)