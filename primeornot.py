a=int(input("enter any number:"))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(" {} is not prime number".format(a))
            break
        else:
            print(" {} is prime number".format(a))
