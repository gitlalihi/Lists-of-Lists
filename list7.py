#Python program to Pair elements with Rear element in Matrix Row
list1=[]
num= int(input("Enter your number of rows:"))
for i in range(num):
    row=input(f"Enter elements for row{i+1}")
    ele=[e for e in row.split()]
    list1.append(ele)

print(" Your original list is")
for row in list1:
    print(row)

new_list = []
for x in list1:
    new_list.append([(ele, x[-1]) for ele in x[:-1]])

print("Your modified list  after pairing elements is :")
for row in new_list :
    print(row)    