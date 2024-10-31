#crud

#create
print("created new list")
newList = ["elemento1","elemento2","elemento3","elemento4"]
#read
print("show complete List")
print(newList)
print("show position list")
print("position 1",newList[0])
print("position 3",newList[2])
#update
print("add append element")
newList.append(input("new element?: "))
#remove
print("remove element of list")
newList.remove("elemento2")
print(newList)

size = len(newList)
print("size of list: ",size)
