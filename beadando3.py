def harmadik(n):
    betu2=[chr(i) for i in range(97,97+n)]
    elso="--"
    for i in range(n):
        t=elso*(n-i-1)
        t2=[]
        for j in range(0,i+1):
            t2.append(betu2[n-1-j])
        for j in range(i,0,-1):
            t2.append(betu2[n-j])
        t+="-".join(t2)
        t+=elso*(n-i-1)
        print(t)
    n=n-1
    for i in range(n):
        t=elso*(i+1)
        t2=[]
        for j in range(0,n-i,1):
            t2.append(betu2[n-j])
        for j in range(n-i-1,0,-1):
            t2.append(betu2[n-j+1])
        t+="-".join(t2)
        t+=elso*(i+1)
        print(t)

harmadik(5)