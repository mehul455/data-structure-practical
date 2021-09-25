import array as a

a1 = a.array('i',[35, 24, 20, 3, 45, 29])
a1.insert(5, 50)
a1.pop(0)
a1[2] = 25
a1.reverse() 
for x in a1:
    print(x, end=" ")