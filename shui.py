for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            i= a*100+b*10+c
            j= (a*a*a)+(b*b*b)+(c*c*c)
            if i==j:
                print("水仙花:%d"%i)
