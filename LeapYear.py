#year = 2001
#year = int(input("input Year"))

#if(year % 4) == 0:

   # if(year % 100) == 0:
       # if(year % 400) == 0:
            #print("{0} is a leap year".format(year))
        #else:
         #   print("{0} is a not leap year".format(year))
    #else:
     #  print("{0} is a leap year".format(year))
#else:
 #   print("{0} is not a leap year".format(year))




#-----leap year using function----

Input = [2000,  2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

def verify_leap(year):
    return(((year % 4 == 0)and
            (year % 100 != 0)) or
            (year % 400 == 0))



answer = 0

for i in  Input:
    if verify_leap(i):
        answer = answer+1



print("leap year  count is",answer)
