""" Assignment No -15  -Write a Python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a)	Insertion sort
b)	Shell Sort and display top five scores
"""
def InsertSort(arr,n):
        for i in range(1,len(arr)):
            a= arr[i]
            j=i
            while((a<arr[j-1]) and (j>0)):
                arr[j] = arr[j-1]
                j=j-1
                
            arr[j] = a
        print("Using Insert Sort Algorithm",arr)

def ShellSort(arr,n):
    gap = len(arr)//2
    while gap > 0: 
        for i in range(gap,len(arr)):
            a = arr[i]
            j=i
            while(a<arr[j-gap] and j >= gap): 
                arr[j] = arr[j-gap] 
                j=j-gap
  
            arr[j] = a 
        gap= gap//2
    print("Using Shell Sort Algorithm",arr)
    print("Top Five Scores are...")
    for i in range (len(arr)-1,len(arr)-6,-1):
            print(arr[i])

#Driver Code
print("\nHow many students are there?")
n = int(input())
array = []
i=0
for i in range(n):
    print("\n Enter percentage marks")
    item = float(input())
    array.append(item)

print(array)

InsertSort(array,n)
ShellSort(array,n)


