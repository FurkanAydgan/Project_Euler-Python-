def facts(x):
    factorial=1
    for i in range(1,x+1):
        factorial*=i
    return factorial


steps=facts(40)/(facts(20)*facts(20))

print(int(steps))
