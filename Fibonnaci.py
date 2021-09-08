num =int(input("how many terms ??"))

n1,n2= 0,1
count= 0
if num <= 0:
    print(" please enter positive number")
elif num ==1:
    print("fibonnaci upto ", num)
    print (n1)
else:
    while count < num:
        print(n1)
        ans= n1+n2
        n1=n2
        n2 = ans
        count +=1

