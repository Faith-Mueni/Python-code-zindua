def primesOfN(num):
    for j in range (1,num):
        if j > 1:
            for i in range (2,j):
                if j % i == 0:
                    break
            else:
                print(j," is a prime number")

primesOfN(100)



