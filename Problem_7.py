import math
prime_count=0
def prime_check(x):
    is_prime=True
    if x==2:
        return True
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i==0:
                is_prime=False
                break
        return is_prime

j=2

while True:
    if prime_check(j):
        prime_count+=1
    if prime_count==10001:
        print(j)
        break
    j+=1