import random

def guess_the_number():
    print('-' * 100)
    print('\t\t\t\t\tWELCOME TO GUESS THE NUMBER GAME')
    print('-' * 100)
    secret_num= random.randint(1,10)
    count=0
    guess_num= int(input('Guess a number between 1 and 10 inclusive: '))
    while guess_num !=secret_num and count<2:
        if guess_num<secret_num:
            print('Your guess is low')
            count+=1
        else:
            print('Your guess is high')
            count+=1

        guess_num= int(input('Guess a number 1 and 10 inclusive: '))

    if guess_num==secret_num:
        print('-' * 50)
        print("\nCONGRATULATIONS! YOUR GUESS IS CORRECT.")
        print('-' * 50)
        restart = input("Do want to play Again?(y/n): ")
        game_status(restart)
        
    else:
        print('-' * 50)
        print("\nTHE NUMBER IS "+str(secret_num)+" BETTER LUCK NEXT TIME!")
        print('-' * 50)
        restart = input("Do want to play Again?(y/n): ")
        game_status(restart)



def printsampleBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-+-+-+')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-+-+-+')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def tic_tac_toe_game():
    print('-' * 100)
    print('\t\t\t\t\tWELCOME TO TIC-TAC-TOE GAME AKA ZERO-KATTA')
    print('-' * 100)
    turn = 'X'
    count = 0
    sampleBoard = {'7': '(7)' , '8': '(8)' , '9': '(9)' ,
            '4': '(4)' , '5': '(5)' , '6': '(6)' ,
            '1': '(1)' , '2': '(2)' , '3': '(3)' }

    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

    board_keys = []

    for key in theBoard:
        board_keys.append(key)
    printsampleBoard(sampleBoard)

    print('\nInstructions: This is the Tic-Tac-Toe Board and you can place your move on the positions numbering between 1-9.\nChoose a place which is not yet taken by other player')
    print("\nNow, that you have understood the game rules. Let's start the game")
    print('-' * 100)
    place_not_filled=[1,2,3,4,5,6,7,8,9]
    while count<9:
        printBoard(theBoard)
        move = input("\nIt's your turn " + turn + ", Choose a place from numbers: "+str(place_not_filled)+'\n')
        if move!='1' and move!='2'and move!='3'and move!='4'and move!='5'and move!='6'and move!='7'and move!='8'and move!='9':
            print("\nChoose a valid place from numbers: "+str(place_not_filled))
            continue
            
        if theBoard[move] == ' ':
            theBoard[move] = turn
            place_not_filled.remove(int(move))
            count += 1
        else:
            print("\nThat place is already filled. Choose a place from numbers: "+str(place_not_filled)+'\n')
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    game_status(restart)

def game_status(restart):
    if restart == 'y' or restart == 'Y':
        start_game()
    else:
        print('-'*100)
        print('\t\t\t\tHOPE YOU HAD A GREAT TIME AT THE GAMING ZONE\n\t\t\t\t\t\tSEE YOU NEXT TIME')
        print('-'*100)


def start_game():
    
    print('-'*100)
    print("""\t\t\t\t\tWELCOME TO THE GAMING ZONE \n\n\t\t\t\t\tPROJECT MADE BY ISHITA PAHUJA""")
    print('-'*100)

    print('Press 1 to play GUESS THE NUMBER \n\nPress 2 to play TIC-TAC-TOE AKA ZERO KATTA')

    game_choice=int(input("\nENTER YOUR CHOICE:"))

    if game_choice==1 or game_choice==2:
        if game_choice==1:
            guess_the_number()
        elif game_choice==2:
            tic_tac_toe_game()
    else:
        print('\nPlease choose a valid option between 1 and 2')
        game_choice=int(input("ENTER YOUR CHOICE:"))
        if game_choice==1:
            guess_the_number()
        elif game_choice==2:
            tic_tac_toe_game()
    
    

start_game()
