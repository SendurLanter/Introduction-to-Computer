N=0
d=0
cipher=''

#讀檔
with open('private_key.txt','r') as f:
	N=int(f.readline())
	d=int(f.readline())

#讀檔
with open('secret.txt','r') as f:
	cipher=f.readlines()
	for a in cipher:
		#算反模數, 解密
		decrypted = pow(int(a), d, N)
		#第一個字,因為字串加密的規則是a*256+b
		A=int(decrypted/256)
		#第二個字,因為字串加密的規則是a*256+b
		B=decrypted%256
		with open('message.txt','a') as f:
			f.write(chr(A))
			if B!=0:
				f.write(chr(B))