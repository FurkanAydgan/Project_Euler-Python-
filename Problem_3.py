sayi=600851475143
bolen=1

while sayi>1:
    bolen+=1
    while sayi%bolen==0:
        sayi=sayi/bolen

print(bolen)