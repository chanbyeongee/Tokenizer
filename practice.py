list = [1,2,3,4,5]
list2= [2,3,4,5,6]
list3 = [3,4,5,6,7]
list4 = [4,5,6,7,8]

for (i,j),(k,l) in zip(enumerate(list3),enumerate(list4)) :
    list3[i] += 1

print(list3)
