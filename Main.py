import random
import string


def addtwo(x, y):
    sumofxy = x + y
    print("Your 2 numbers add up to "+ str(sumofxy) +"!")


def findmax(x, y):
    if x > y:
        print(str(x) + " is greater than " + str(y) + "!")
    elif x < y:
        print(str(y) + " is greater than " + str(x) + "!")
    else:
        print("The 2 numbers are equal!")


def factorial(num):
    total = num
    temp = num
    num -= 1

    while num != 0:
        total *= num
        num -= 1

    print(str(temp) + " factorial is equal to " + str(total))

def simpleintrest(p, t, r):
    total = (p*t*r)/100
    print("An initial value of " + str(p) + " at a rate of " + str(r) + " for " + str(t) + " years, "
          "will give you a total of " + str(total))


# birth every 9 secs, death every 10, new immagrant every 47
#525600 mins, 31,536,000 seconds
def calcUSPopulation(startPopulation):
    t_secs = 31536000
    birth = t_secs/9
    death = t_secs/10
    new_imm = t_secs//47

    startPopulation += birth - death + new_imm

    print(int(startPopulation))


def calcGramsAndKg(gramWeight):
    gram = gramWeight % 1000
    kilo = gramWeight // 1000

    print("gramWeight is " + str(kilo) + " kilograms and " + str(gram) + " grams")


#Celsius = (Fahrenheit - 32) * (5/9)
def calcFahrenheit(celsiusTemp):
    fahr = celsiusTemp*(9/5) + 32
    return int(fahr)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def printifsmall(alpha):
    #for i in alpha:
    #    if i <= 5:
     #       print(i)

    # or
    print([i for i in alpha if i <= 5])


def rockpapersci():
    moves = ["Rock", "Paper", "Scissors"]
    quit = 0
    p1score = 0
    p2score = 0

    while quit == 0:
        play1 = input("player one move: ")
        print("\n\n\n\n\n\n\n\n")
        play2 = input("player two move: ")

        if play2 == "":
            play2 = random.choice(moves)

        if play1 == play2:
            print("Draw!")
        elif play1.lower() == "rock":
            if play2.lower() == "paper":
                print("Player 2 wins!")
                p2score += 1
            elif play2.lower() == "scissors":
                print("Player 1 wins!")
                p1score += 1
        elif play1.lower() == "paper":
            if play2.lower() == "rock":
                print("Player 1 wins!")
                p1score += 1
            elif play2.lower() == "scissors":
                print("Player 2 wins!")
                p2score += 1
        elif play1.lower() == "scissors":
            if play2.lower() == "rock":
                print("Player 2 wins!")
                p2score += 1
            elif play2.lower() == "paper":
                print("Player 1 wins!")
                p1score += 1
        else:
            print("invalid input. Try again")
            continue

        contplay = input("Enter 1 to play again, and 2 to quit: ")

        if contplay == "1":
            quit = 0
        elif contplay == "2":
            quit = 1
            if p1score>p2score:
                winner = "Player 1"
            else:
                winner = "Player 2"
            print(winner + " wins! With a score of " + str(p1score) + " vs " + str(p2score))
            print("Thanks for playing!")


def passgen():
    pass_len = 0
    password = ""
    l_symbol = ["!", "$", "&", "?", "%", "~", "@", "#", "^","*","_","-", "+", "=", "<", ">",",","."]
    word_lst = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon',
                'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla',
                'watermelon', 'xigua', 'yam', 'zucchini', 'almond', 'basil', 'cinnamon', 'dill', 'endive', 'fennel',
                'garlic', 'hazelnut', 'iceberg', 'jalapeno', 'kale', 'lettuce', 'mint', 'nutmeg', 'oregano', 'parsley',
                'quinoa', 'radish', 'spinach', 'thyme', 'upland', 'violet', 'wheat', 'xanthan', 'yucca', 'zebra']
    str_lvl = 0

    while str_lvl != "-1":
        str_lvl = input("How strong should the password be? 1(easy), 2(medium), 3(hard): ")
        if str_lvl == "3":
            while pass_len < 12:
                rand_choice = random.randint(1,10)

                if 1 <= rand_choice <= 4:
                    password += random.choice(string.ascii_letters)
                    pass_len += 1
                elif rand_choice == 5:
                    password += random.choice(l_symbol)
                    pass_len += 1
                elif 8 <= rand_choice <= 10:
                    password += str(random.randint(0,9))
                    pass_len += 1
                elif 6 <= rand_choice <= 7:
                    password += random.choice(string.ascii_letters)
                    pass_len += 1
                else:
                    continue
                str_lvl = "-1"
        elif str_lvl == "2":
            password += random.choice(word_lst)
            password += str(random.randint(0, 9))
            password += str(random.randint(0, 9))
            password += random.choice(l_symbol)
            password += random.choice(l_symbol)
            str_lvl = "-1"
        elif str_lvl == "1":
            password += random.choice(word_lst)
            password += random.choice(word_lst)
            password += str(random.randint(0, 9))
            password += str(random.randint(0, 9))
            str_lvl = "-1"
        else:
            print("Please enter a valid input!")

    print("Your new password is: " + password)

passgen()


