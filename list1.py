#Python – Remove empty List from List
list1=[]
num= int(input("Enter your range of elements:"))
for i in range(1,num+1):
    ele=input("Enter your elements within your range have mentioned: ")
    list1.append(ele)
print(list1)

new_list=[ele for ele in list1 if ele !=[]]
print("Your modified list after removing empty list is:" ,new_list)    