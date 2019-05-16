def elso(n):
    t=[0,7,4]
    l=[]
    for i in t:
        for i1 in t:
            for i2 in t:
                if(i!=i1 and i1!=i2 and i!=i2):
                    l.append(str(i)+str(i1)+str(i2))
    l.sort()
    for i in l:
        if n>int(i):
            print(i)

elso(1000)
