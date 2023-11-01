#Python – Convert List to List of dictionaries
list1=[]
num= int(input("Enter your range of elements:"))
for i in range(1,num+1):
    ele=input("Enter your elements within your range have mentioned: ")
    list1.append(ele)
print(list1)

new_dict=["key","value"]
length=len(list1)
new_list=[]
for i in range(0,length,2):
    new_list.append({new_dict[0] : list1[i], new_dict[1] : list1[i+1]})
print("The dictionary from the given list is :", new_list)




