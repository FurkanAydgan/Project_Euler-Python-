for a in range(1,1000):
    for b in range(1,1000-a):
       c=1000-a-b
       if c*c==a*a + b*b:
           if b>a:
            print(a*b*c)
            print(a,b,c)
            break

