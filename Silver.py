string1 = input('String: ')
string2 = input('String: ')

def silver1():
    vowels = 'aeiou'
    toprint = ''
    for letter in string1.lower():
        if letter not in vowels:
            toprint += letter
    return toprint

def silver2():
    toprint = ''
    for i in range(1, len(string1) + 1):
        toprint += string1[i * -1]
    return toprint

def silver3():
    if string1 < string2:
        for x in range(len(string1)):
            print(string1[x], string2[x])
    else:
        for x in range(len(string2)):
            print(string1[x], string2[x])