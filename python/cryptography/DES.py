import string

class Des(object):

	table3_1=57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36, 63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4
	key    ="YOURSECRETSBSCPE"
	message="THEQUICKBROWNFOX"
	key = key[:8]
	message = message[:8]
	key    ="581fbc94d3a452ea"
	message="3570e2f1ba4682c7"
	
	#key    ="SECRETSX"
	#message="BROWNFOX"
	
	def getBits(self,b):
		return '00000000'+b[2:][-8:]
		
	def getBinary(self,msg):
		pt=""
		for c in msg:
			##print (c,ord(c),bin(ord(c)),self.getBits(bin(ord(c))))
			pt += self.getBits(bin(ord(c)))
		return pt	
		
	def getPermutation(self,table,msg):
		p=""
		for x in table:
			p += msg[x-1:x],
		return p
		
		
def main():
	e=Des()
	messageb=e.getBinary(e.message)
	keyb=e.getBinary(e.key)
	p=e.getPermutation(e.table3_1,keyb)
	c0=p[:32]
	d0=p[32:]
	
	print p
	print c0
	print d0
		
	
	
main()
	
	

