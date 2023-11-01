#Python Program to check uncommon lists in a given two lists
list1 = []
num = int(input("Enter the number of elements in list1: "))
for i in range(num):
    ele = input("Enter an element for list1: ")
    list1.append(ele)
print(list1)

list2 = []
num2 = int(input("Enter the number of elements in list2: "))
for i in range(num2):
    ele2 = input("Enter an element for list2: ")
    list2.append(ele2)
print(list2)    

new_list=[]
for i in list1:
    if i not in list2:
        new_list.append(i)
for i in list2:
    if i not in list1:
        new_list.append(i)     

print("Your uncommon elements in the lists are:", new_list)           




