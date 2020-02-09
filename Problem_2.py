

sayi1=1
sayi2=2
ctoplam=0

toplam=sayi1 + sayi2

while toplam<4000000:
    if toplam%2==0:
         ctoplam+=toplam
    sayi1=sayi2
    sayi2=toplam
    toplam=sayi1+sayi2

ctoplam+=2
print(ctoplam)