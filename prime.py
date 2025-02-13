from xmlrpc.client import MAXINT


def printPrime(p_list): # Print all prime numbers
    for i in range(len(p_list)):
        print("Prime " + str(i + 1) + ": " + str(p_list[i]))


def findprime(n = 200000):
    p_list = [2,3,5,7]
    denom = [3,7]
    prime = len(p_list)
    num = 8

    while prime < n or num == MAXINT - 1:
        p_test = True
        if num % 2 == 0:
            p_test = False
        if num % 5 == 0:
            p_test = False
        else:
            for i in denom:
                if num % i == 0:
                    p_test = False
        if p_test:
            p_list.append(num)
            denom.append(num)
            prime+= 1
            print("Prime " + str(prime) + ": " + str(num))
        num += 1


findprime()