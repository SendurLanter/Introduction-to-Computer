e=0
phi=0

#算最大公因數
def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        (g, y, x) = gcd(b % a, a)
        return (g, x-(b//a)*y, y)

#算反模數
def inverse(a, m):
    g, x, y = gcd(a, m)
    if g == 1:
        return x % m

#讀檔
with open('cryptan.txt','r') as f:
	e=int(f.readline())
	phi=int(f.readline())

#算出d
d=inverse(e,phi);
#寫答案
with open('cryptan_result.txt','w') as f:
	f.write(str(d))