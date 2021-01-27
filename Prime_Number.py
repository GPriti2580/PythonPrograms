
#------------WAP to check number is prime or not_______

num = int(input("enter a number"))

if num > 1 :
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"number is not prime number")
            break

        else:
            print(num,"number is prime number")
