
arr = [1,5,9,4,5,6,1,2,3]

print("duplicate array is given")

for i in range (0,len(arr)):
    for j in range (i +1, len(arr)):
        if arr[i]==arr[j]:
            print(arr[i])