def splitList(listIn):
	for i in range(1, len(listIn)-1):
		list1 = listIn[:i]
		list2 = listIn[i:]
		return list1, list2

listIn = [1,2,3,4]
list1, list2 = splitList(listIn)
print(list1)
print(list2)



	