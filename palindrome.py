def ispalindrome(s):
 return s == s[::-1]

 s ='mam'
ans =ispalindrome(s)

if ans:
     print("yes")
else:
   print("no")

num =7

# factorail =1
#
# if num < 0:
#     print("enter positive number")
# elif num == 0:
#     print("fcatorail of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorail =factorail * i
#         print(factorail)
#
