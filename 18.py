
with open("18.txt","r") as dosya:
    liste = []
    for satir in dosya:
        list=[]
        satir=satir.strip("\n")
        satirlist=satir.split(" ")
        for sayi in satirlist:
            list.append(int(sayi))
        liste.append(list)

for i in range(len(liste)-1,-1,-1):
    for j in range(0,i):
        liste[i-1][j]+=max(liste[i][j],liste[i][j+1])

print(liste[0])

