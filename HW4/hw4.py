import struct

def readParameters():
	
	with open("input2",'rb') as fin:
		(m,) = struct.unpack("i",fin.read(4)) 
		(n,) = struct.unpack("i",fin.read(4))
		v = [[0]*(m+1) for i in range(n)]
		h = [[0]*(m) for i in range(n+1)]
		for i in range(n):
			for j in range(m+1):
				(v[i][j],) = struct.unpack("d",fin.read(8))
		for i in range(n+1):
			for j in range(m):
				(h[i][j],) = struct.unpack("d",fin.read(8))
	return m, n, v, h

#(A,E,)
def main():
	(m, n, v, h) = readParameters()
	print(m)
	print(n)
	print(v)
	print(h)

	table=dict()
	def shortest(A1,A2,E1,E2,path):
		
		if (A1+1,A2) == (E1,E2):
			path.append((E1,E2))
			print(path)
			print('yes')
			return v[A1][A2]
		if (A1,A2+1) == (E1,E2):
			path.append((E1,E2))
			print(path)
			print('yes')
			return h[A1][A2]

		else:
			mini=9999999999
			if A1-1>=0:
				if (A1-1,A2) not in path:
					path1=path.copy()
					path1.append( (A1-1,A2) )
					
					if str(A1-1)+','+str(A2) in table:
						memory=table[str(A1-1)+','+str(A2)]
					else:
						memory=shortest(A1-1,A2,E1,E2,path1)
						table[str(A1-1)+','+str(A2)]=memory
					
					buf = v[A1-1][A2] + table[str(A1-1)+','+str(A2)]
					if buf < mini:
						print('fucyoy')
						mini = buf
			if A1+1<=100:
				if (A1+1,A2) not in path:
					path2=path.copy()
					path2.append((A1+1,A2))
					
					if str(A1+1)+','+str(A2) in table:
						memory=table[str(A1+1)+','+str(A2)]
					else:
						memory=shortest(A1+1,A2,E1,E2,[(A1+1,A2)])
						table[str(A1+1)+','+str(A2)]=memory
					
					buf = v[A1][A2] + table[str(A1+1)+','+str(A2)]
					if buf < mini:
						mini = buf

			if A2+1<=100:
				if (A1,A2+1) not in path:
					path4=path.copy()
					path4.append((A1,A2+1))
					
					if str(A1)+','+str(A2+1) in table:
						memory=table[str(A1)+','+str(A2+1)]
					else:
						memory=shortest(A1,A2+1,E1,E2,[(A1,A2+1)])
						table[str(A1)+','+str(A2+1)]=memory
					
					buf = h[A1][A2] + memory
					if buf < mini:
						mini = buf
			
			if A2-1>=0:
				if (A1,A2-1) not in path:
					path3=path.copy()
					path3.append((A1,A2-1))
					
					if str(A1)+','+str(A2-1) in table:
						memory=table[str(A1)+','+str(A2-1)]
					else:
						memory=shortest(A1,A2-1,E1,E2,path3)
						table[str(A1)+','+str(A2-1)]=memory

					buf = h[A1][A2-1] + memory
					if buf < mini:
						mini = buf


			#print(path,'\n')
			#print(len(table))
			return mini

	def prefind(A1,A2,E1,E2,path):

		if (A1+1,A2) == (E1,E2):
			path.append((E1,E2))
			print(path)
			print('yes')
			return v[A1][A2]
		if (A1,A2+1) == (E1,E2):
			path.append((E1,E2))
			print(path)
			print('yes')
			return h[A1][A2]

		else:
			mini=9999999999

			if A1+1<=100:
				if (A1+1,A2) not in path:
					path2=path.copy()
					path2.append((A1+1,A2))
					
					if str(A1+1)+','+str(A2) in table:
						memory=table[str(A1+1)+','+str(A2)]
					else:
						memory=prefind(A1+1,A2,E1,E2,[(A1+1,A2)])
						table[str(A1+1)+','+str(A2)]=memory
					
					buf = v[A1][A2] + memory
					if buf < mini:
						mini = buf

			if A2+1<=100:
				if (A1,A2+1) not in path:
					path4=path.copy()
					path4.append((A1,A2+1))
					
					if str(A1)+','+str(A2+1) in table:
						memory=table[str(A1)+','+str(A2+1)]
					else:
						memory=prefind(A1,A2+1,E1,E2,[(A1,A2+1)])
						table[str(A1)+','+str(A2+1)]=memory
					
					buf = h[A1][A2] + memory
					if buf < mini:
						mini = buf

			return mini

	for i in range(101):
		for j in range((101)):
			prefind(100-i,100-j,100,100,[(100-i,100-j)])
	print(len(table))
	print(shortest(0,0,100,100,[(0,0)]))

	'''
	dp=list()
	for i in range(10):
		dp.append([])
		for j in range(10):
			dp[i].append(0)
	for i in range(1,10):
		dp[i][0] = v[i-1][0] + dp[i-1][0]
	for j in range(1,10):
		dp[0][j] = h[0][j-1] + dp[0][j-1]
	for i in range(1,10):
		for j in range(1,10):
			dp[i][j] = min( dp[i][j-1]+h[i][j-1] , dp[i-1][j]+v[i-1][j] )
	i=9
	j=9
	ans=list()
	while 1:
		
		if dp[i-1][j] < dp[i][j-1]:
			i-=1
			ans.append('d')
		else:
			j-=1
			ans.append('r')
		if i==-1 or j==-1:
			break
	ans.reverse()
	print(str(ans))

	print(dp[-1][-1])
	print(len(dp))
	print(len(v))'''

	'''mini=99999
		print(path)
		if A1-1>=0 and ((A1-1,A2) not in path):
			path1=path
			path1.append((A1-1,A2))
			mini = v[A1-1][A2] + shortest(A1-1,A2,E1,E2,path1)
		
		if A2-1>=0 and ((A1,A2-1) not in path):
			path2=path
			path2.append((A1,A2-1))
			
			buf = h[A1][A2-1] + shortest(A1,A2-1,E1,E2,path2)
			if buf < mini:
				mini = buf 
		
		if A2+1<300 and ((A1,A2+1) not in path):
			path3=path
			path3.append((A1,A2+1))
			buf = h[A1][A2+1] + shortest(A1,A2+1,E1,E2,path3)
			if buf < mini:
				mini = buf
		
		if A1+1<200 and ((A1+1,A2) not in path):
			path4=path
			path4.append((A1+1,A2))
			buf = v[A1+1][A2] + shortest(A1+1,A2,E1,E2,path4)
			if buf < mini:
				mini = buf
		

		return mini'''

		#path.append((AN1,AN2))
		#print(AN1,AN2)
		#print(path)
		#return mini + shortest(AN1,AN2,E1,E2,path)

	

	'''
	for i in 
	graph=dict()
	# yours code
	for i in range(n):
		for j in range(m):
			graph[str(i)+' '+str(j)]=[str(i-1)+' '+str(j),str(i+1)+' '+str(j),str(i)+' '+str(j-1),str(i)+' '+str(j+1)]
	#print(graph)
	i=0
	j=0
	path=''
	history=[]
	'''
	'''
	while 1:
		if i==199 and j==299:
			break
		else:
			pass
		'''
	'''def determine(source , destination):
		result = list()
		def BFS(source , destination , path , history , cost):
			print('why')
			if destination in graph[source]:
				print('h')
				path+=destination
				result.append(cost)
				return 

			else:
				print(history)
				if '-' not in graph[source][0]:
					if graph[source][0] not in history:
						try:
							a=graph[source][0].split()
							history.append(graph[source][0])
							BFS(graph[source][0] , destination ,path+'u',history,cost+v[int(a[0])][int(a[1])])
							print('fukx')
						except:
							print('0')
				if '-' not in graph[source][1]:
					if graph[source][1] not in history:
						try:
							b=graph[source][1].split()
							history.append(graph[source][1])
							BFS(graph[source][1] , destination ,path+'d',history,cost+v[int(b[0])][int(b[1])])
							print('fukx')
						except:
							print('1')
				if '-' not in graph[source][2]:
					if graph[source][2] not in history:
						try:
							c=graph[source][2].split()
							history.append(graph[source][2])
							BFS(graph[source][2] , destination ,path+'l',history,cost+h[int(c[0])][int(c[1])])
							print('fukx')
						except:
							print('2')
				if '-' not in graph[source][3]:
					if graph[source][3] not in history:
						try:
							d=graph[source][3].split()
							print(d[0])
							print(graph[source][3])
							history.append(graph[source][3])
							BFS(graph[source][3] , destination ,path+'r',history,cost+h[int(d[0])][int(d[1])])
							print('fukx')
						except:
							print('3')
				print('no')

		BFS(source , destination , '' ,['0 0'], 0)
		print(result)
		return min(result)
	print( determine( '0 0' , '2 2' ) )'''

	return 0
	
if __name__ == "__main__":
	main()