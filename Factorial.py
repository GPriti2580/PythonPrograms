num =5

factorial =1

if num < 0:
    print("factorail does not exist in negative number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial *i
        print("factorail",factorial)