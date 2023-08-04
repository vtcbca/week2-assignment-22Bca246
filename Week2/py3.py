
#3.Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

def pali(a):
    if(a.isdigit()):
        ans=str(a)
        if(ans==ans[::-1]):
            print(f"The number {a} is a palindrome number!!")
        else:
            print(f"The number {a} is not a palindrome number!!")
    else:
        print(f"The given input {a} is not valid number!!")

number=input("Enter a number!!:")
pali(number)
