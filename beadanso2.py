import sys
def masodik(n,fi):
    f=open(fi,'w')
    v=0
    i=1
    while v==0:
        sum=0
        for i1 in range(1,i+1):
            sum+=i1

        i+=1
        if(n<sum):
            v=1
        else:
            f.write(str(sum)+"\n")
    f.close()

masodik(int(sys.argv[1]),str(sys.argv[2]))