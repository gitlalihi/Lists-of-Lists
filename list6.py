#Python – Reverse Row sort in Lists of List
list1=[]
num= int(input("Enter your number of rows:"))
for i in range(num):
    row=input(f"Enter elements for row{i+1}")
    ele=[e for e in row.split()]
    list1.append(ele)
print(list1)
sort_list=[sorted(i,reverse=True) for i in list1]
for row in list1:
    print(row)
print("The reversed row sort in your lists of lists is :" ,list1)    