def palindrome(inp):
    if inp == inp[::-1]:
        print('is palidrome')
    else:
        print('Not palindrome')
inpu = input('enter a string ')
palindrome(inpu)