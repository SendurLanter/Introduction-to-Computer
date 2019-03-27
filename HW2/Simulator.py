import struct
class Simulator:
	def __init__(self):
		print("");

	def loadMemory(self, path):
		print("loadMemory");
		
		#存指令用的list
		self.instruction=list()
		#存register用的list
		self.register=list()
		#存address cells值的list
		self.data=list()

		####全都10進位運算,最後再轉hex
		for i in range(16):
			self.register.append(0)
		
		#instruction 以string形式存
		with open(path,'rb') as f:
			for e in range(128):
				self.instruction.append(f.read(2).hex())

		#address cells中的數值以10進位int存
		with open(path,'rb') as f:
			for i in range(256):
				self.data.append(int(f.read(1).hex(),16))

	def loadMemory2(self, path):
		print("loadMemory");
		#TODO
		self.instruction=list()
		self.register=list()
		self.data=list()

		####全都10進位運算,最後再轉hex
		for i in range(16):
			self.register.append(0)

		#instruction 以string形式存 
		#開的是bounus,存方式不一樣
		with open("input/bonus.txt",'r') as f:
			for e in f.readlines():
				self.instruction.append(e[0:-1])
		print(self.instruction)
		#address cells中的數值以10進位int存
		with open(path,'rb') as f:
			for i in range(256):
				self.data.append(int(f.read(1).hex(),16))
	
	def storeMemory(self, path):
		print("storeMemory");
		#TODO

		#將output的格式存成跟input一樣
		with open(path,'wb') as f:
			i=0
			j=0
			for e in self.data:
				#print(e)
				f.write(str(e).encode())
				i+=1
				j+=1
				#每16個換行一次
				if j==16:
					j=0
					i=0
					f.write('\n'.encode())
					continue
				#每16bit空一格
				if i==2:
					i=0
					f.write(' '.encode())

	def	simulate(self):
		print("simulate");
		#TODO

		#i = program counter
		i=0
		length=len(self.instruction)

		while 1:

			if i >=length:
				break
			
			#Op-code1,依此類推
			if self.instruction[i][0]=='1':
				self.register[int(self.instruction[i][1],16)] = self.data[int(self.instruction[i][2] + self.instruction[i][3],16)]
			
			elif self.instruction[i][0]=='2':
				self.register[int(self.instruction[i][1],16)] = self.data[int(self.instruction[i][2] + self.instruction[i][3],16)]
			
			elif self.instruction[i][0]=='3':
				self.data[int(self.instruction[i][2]+self.instruction[i][3],16)] = self.register[int(self.instruction[i][1],16)]
			
			elif self.instruction[i][0]=='4':
				self.register[int(self.instruction[i][3],16)] = self.register[int(self.instruction[i][2],16)]
			
			elif self.instruction[i][0]=='5':
				self.register[int(self.instruction[i][1],16)] = self.register[int(self.instruction[i][2],16)] + self.register[int(self.instruction[i][3],16)]

			elif self.instruction[i][0]=='6':
				self.register[int(self.instruction[i][1],16)] = self.register[int(self.instruction[i][2],16)] + self.register[int(self.instruction[i][3],16)]
			
			elif self.instruction[i][0]=='7':

				#將register中的數值轉成2進位
				#OR operation
				a='{0:08b}'.format(self.register[int(self.instruction[i][2],16)])
				b='{0:08b}'.format(self.register[int(self.instruction[i][3],16)])
				c = int(a,2) or int(b,2)
				self.register[int(self.instruction[i][1],16)]=c

			elif self.instruction[i][0]=='8':

				#將register中的數值轉成2進位
				#AND operation
				a='{0:08b}'.format(self.register[int(self.instruction[i][2],16)])
				b='{0:08b}'.format(self.register[int(self.instruction[i][3],16)])
				c = int(a,2) and int(b,2)
				self.register[int(self.instruction[i][1],16)]=c

			elif self.instruction[i][0]=='9':

				#將register中的數值轉成2進位
				#XOR operation
				a='{0:08b}'.format(self.register[int(self.instruction[i][2],16)])
				b='{0:08b}'.format(self.register[int(self.instruction[i][3],16)])
				c = int(a,2)^int(b,2)
				self.register[int(self.instruction[i][1],16)]=c

			elif self.instruction[i][0]=='a':

				#將register中的數值轉成2進位
				#rotate x times
				a='{0:08b}'.format(self.register[int(self.instruction[i][1],16)])
				buf=list(a)
				#像是queue,以實現circle
				for i in range(int(self.instruction[i][3],16)):
					buf.append(buf[0])
					buf.pop()
				c=int(''.join(buf),2)
				self.register[int(self.instruction[i][1],16)]=c

			elif self.instruction[i][0]=='B':
				#program counter 跳到指定的數字
				if self.register[int(self.instruction[i][1],16)] == self.register[0]:
					i=int(self.instruction[i][2],16)+int(self.instruction[i][3],16)
				continue
				
			#HALT
			elif self.instruction[i][0]=='c':
				if self.instruction[i][1:]=='000':
					break
			i+=1
		#program counter
		print(i)

		#將register中的數值從10進位轉回16進位儲存
		for i in range(len(self.register)):
			self.register[i]='{0:02x}'.format(self.register[i])
		
		#將address中的data從10進位轉回16進位儲存
		for i in range(len(self.data)):
			self.data[i]='{0:02x}'.format(self.data[i])

		#register
		print(self.register)
		#address/cells
		print(self.data)

	def	simulate2(self):

		#program_counter
		PC=0
		length=len(self.instruction)

		while 1:
			if PC>=length:
				break
			codes=self.instruction[PC].split(' ')
			print(codes)
			if codes[0]=='lw' or codes[0]=='LW' or codes[0]=='Lw' or codes[0]=='lW':
				self.register[int(codes[1],16)]=self.data[int(codes[2],16)]
			
			elif codes[0]=='lb' or codes[0]=='LB' or codes[0]=='Lb' or codes[0]=='lB':
				self.register[int(codes[1],16)] = self.data[int(codes[2],16)]
			
			elif codes[0]=='sw' or codes[0]=='SW' or codes[0]=='sW' or codes[0]=='Sw':
				self.data[int(codes[2],16)] = self.register[int(codes[1],16)]
			
			elif codes[0]=='mv' or codes[0]=='MV' or codes[0]=='Mv' or codes[0]=='mV':
				self.register[int(codes[3],16)] = self.register[int(codes[2],16)]

			elif codes[0]=='add' or codes[0]=='ADD' or codes[0]=='aDD' or codes[0]=='Add':
				self.register[int(codes[1],16)] = self.register[int(codes[2],16)] + self.register[int(codes[3],16)]

			elif codes[0]=='addf' or codes[0]=='ADDF':
				self.register[int(codes[1],16)] = self.register[int(codes[2],16)] + self.register[int(codes[3],16)]

			elif codes[0]=='or' or codes[0]=='OR' or codes[0]=='Or' or codes[0]=='oR':

				#將register中的數值轉成2進位
				#OR operation
				a='{0:08b}'.format(self.register[int(codes[2],16)])
				b='{0:08b}'.format(self.register[int(codes[3],16)])
				c = int(a,2) or int(b,2)
				self.register[int(codes[1],16)]=c		

			elif codes[0]=='and' or codes[0]=='AND' or codes[0]=='And':

				#將register中的數值轉成2進位
				#AND operation
				a='{0:08b}'.format(self.register[int(codes[2],16)])
				b='{0:08b}'.format(self.register[int(codes[3],16)])
				c = int(a,2) and int(b,2)
				self.register[int(codes[1],16)]=c

			elif codes[0]=='xor' or codes[0]=='XOR':

				#將register中的數值轉成2進位
				#XOR operation
				a='{0:08b}'.format(self.register[int(codes[2],16)])
				b='{0:08b}'.format(self.register[int(codes[3],16)])
				c = int(a,2)^int(b,2)
				self.register[int(codes[1],16)]=c

			elif codes[0]=='srl' or codes[0]=='SRL':

				#將register中的數值轉成2進位
				#rotate x times
				a='{0:08b}'.format(self.register[int(codes[1],16)])
				buf=list(a)
				#像是queue,以實現circle
				for i in range(int(codes[3],16)):
					buf.append(buf[0])
					buf.pop()
				c=int(''.join(buf),2)
				self.register[int(codes[1],16)]=c

			elif codes[0]=='beq' or codes[0]=='BEQ':
				#program counter 跳到指定的數字
				if self.register[int(self.instruction[i][1],16)] == self.register[0]:
					i=int(codes[2],16)+int(codes[3],16)
				continue

			#HALT
			elif codes[0]=='halt' or codes[0]=='HALT':
				break
			PC+=1

		#PC=program counter
		print(PC)

		#將register中的數值從10進位轉回16進位儲存
		for i in range(len(self.register)):
			self.register[i]='{0:02x}'.format(self.register[i])
		
		#將address中的data從10進位轉回16進位儲存
		for i in range(len(self.data)):
			self.data[i]='{0:02x}'.format(self.data[i])

		#register
		print(self.register)
		#address/cells
		print(self.data)