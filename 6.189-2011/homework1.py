#MIT 6.189
#homework 1

#Ex 1.0
#Python Istalled

def ex11():
    #ex 1.1
    print "hello world"


def ex12():
    #ex 1.2
    a = '  |  |  \n'
    b = '--------\n'
    print a,b,a,b,a

def ex13():
    #ex 1.3
    a = "Hello World!\n"
    b = "...and goodbye."
    print a,b

def ex14():
    #ex 1.4
    #Part III:
    print 1+2*3
    print (1+2)*3

def ex15():
    #ex 1.5
    first = raw_input('Enter your first name: ')
    last = raw_input('Enter your last name: ')
    print 'Enter your Date of Birth:\n'
    month = raw_input('Month? ')
    day = raw_input('Day? ')
    year = raw_input('Year? ')
    print first, last, "was born on", month, day+',', year+'.'

def ex17():
    #ex 1.7
    #rock, paper, scissors

    message = "ROCK PAPER SCISSORS EXTREME EDITION 2014"
    border = "*" * len(message)

    print "\n", border, "\n", message, "\n", border, "\n" 
    p1,p2 = '','' 

    while p1 not in ['r','p','s']:
        p1 = raw_input('Player 1, PLEASE CHOOSE: (r)ock, (p)aper, or (s)cissors? ')
        # clears screen
        print '\n' * 100

    while p2 not in ['r','p','s']:
        p2 = raw_input('Player 2, PLEASE CHOOSE: (r)ock, (p)aper, or (s)cissors? ')

    print "Player 1:", p1, "\n", "Player 2:", p2
    print "\nLET'S GET IT ON!!\n\n"

    outcomes = [['r','p','s'], ['s','r','p'], ['p','s','r']] 
    for outlist in outcomes:
        if p1 == outlist[1]:
            if p2 == outlist[1]:
                print "TIE!\n"
            if p2 == outlist[0]:
                print "PLAYER 1 IS CH-CH-CH-CHAMPION!\n"
            if p2 == outlist[2]:
                print "PLAYER 2 IS CH-CH-CH-CHAMPION!\n"
    play = ''
    if raw_input('Play again? (y/N): ') in ['y','Y','Yes','yes','YES']:
        ex17()
    else:
        print "\n*******************\n"+"Thanks for playing!\n"+"*******************"

def ex18():
    #ex 1.8

    #part 1
    print "\nPart 1: 1/n, where n is integers 1-10"
    for n in range(1,11):
        print 1.0/n

    #part 2
    print "\nPart 2: Countdown"
    user_input = raw_input('Input to countdown from: ')
    if user_input.isdigit():
        user_input = int(user_input)
        while user_input > 0:
            print user_input
            user_input -= 1
        print "BLASTOFF!!"
    else:
        print "invalid input... program will now restart"

    #part 3
    print "\nPart 3: Base - Exponent Calcultor"
    base = input("give a number for the base: ")
    exp = input("give a number for the exponent: ")
    print str(base)+"^"+str(exp),"=", base**exp

    #part 4
    print "\nPart 4: Divisible by 2"
    number = input("Enter an integer: ")
    if number % 2 == 0:
        print "I LOVE YOU!"
    else:
        print "I HATE YOU!"

ex18()
                
            
    
