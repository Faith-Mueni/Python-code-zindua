def primesOfn(num):
    if num == 1:
        print (num," 1 is NOT a prime")
    elif num > 1:
        for i in range (2,num):
            if num % i == 0:
                print (num,"is prime")
        else:
            print(num,"is a Prime")


primesOfn(31)

