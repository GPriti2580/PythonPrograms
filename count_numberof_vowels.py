from pip._vendor.distlib.compat import raw_input

string = raw_input("enter string")

vowels = 0

for i in string :
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ):
        vowels = vowels+1

#print("number of vowles")
print(vowels)