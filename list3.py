# Python – Convert Lists of List to Dictionary
list1=[]
num= int(input("Enter your range of elements:"))
for i in range(1,num+1):
    ele=input("Enter your elements within your range have mentioned: ")
    list1.append(ele)
print(list1)
new_dict= dict()
for i in list1:
    new_dict[tuple(i[:2])]= tuple(i[2:])
print(" The converted lists of lists into dictionary is :",str(new_dict) )   