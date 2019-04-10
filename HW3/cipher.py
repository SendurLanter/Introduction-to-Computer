plain=''
N=0
e=0

#讀檔
with open('plain.txt','r') as f:
	plain=f.readline()

#讀檔
with open('public_key.txt','r') as f:
	N=int(f.readline())
	e=int(f.readline())

#兩個字一組,循環所有要加密的字
for i in range(int(len(plain)/2)):
	try:
		#正常case,一次加密兩個字
		buf=str((ord(plain[2*i])*2**8+ord(plain[2*i+1])))
		#算模數
		cipher = pow(int(buf), e, N)
		#寫入加密過的字,我是一次加密2個字,因為如果要加密的字串太長,不管long都一定會overflow,全部一起加密不合理
		with open('secret.txt','a') as f:
			f.write(str(cipher))
			f.write('\n')
	except:
		#處理index超過的case,代表只剩一個字
		buf=str(ord(plain[i]))
		cipher = pow(int(buf), e, N)
		with open('secret.txt','a') as f:
			f.write(str(cipher))
			f.write('\n')

