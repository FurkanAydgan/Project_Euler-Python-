def check_polindrom(x):
    str_number=str(x)
    reverse_number=str_number[::-1]
    if str_number==reverse_number:
        return True
    else:
        return False


big_polindrome=0
for i in range(100,1000):
    for j in range(100,1000):
        if check_polindrom(i*j)  and i*j>big_polindrome:
            big_polindrome=i*j
            a=i
            b=j

print(big_polindrome)
print(a,b)


