#Python program to select Random value from list of lists using random module
import random
list1=[]
num= int(input("Enter the number of lists:"))
for i in range(num):
    sublist=[]
    ele=int(input(f"Enter the number of elements in your list {i+1}"))
    for j in range (ele):
        ele= input(f"Enter an element for your list{i+1}")
        sublist.append(ele)
    list1.append(sublist)    

print("List of lists:", list1)
randomsublist = random.choice(list1)
random_element = random.choice(randomsublist)
print("Your randomly chosen list from your given lists of lists:", randomsublist)
print("Your randomly chosen element from the selected list:", random_element)

    