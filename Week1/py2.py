#2.Write a python script to enter any number and print the sum of its digit.

def sumofdigit(k):
    r=k
    ram=0
    sum=0
    while(k!=0):
        ram=k%10
        sum=sum+ram
        k//=10
    print(f"The sum of digit of number {r} is {sum}!")  

num=int(input("Enter a number:"))
sumofdigit(num)
