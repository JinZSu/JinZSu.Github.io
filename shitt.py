# python3 A\*Algo.py 
import copy
import sys
sys.setrecursionlimit(1000000)

class State:
	def __init__(self, score, world, move, confirm, tkscore,level):
		self.s = score
		self.w = world
		self.m = move
		self.c = confirm
		self.t = tkscore
		self.l = level
	def __hash__(self):
		return hash(self.w)

class Man:
	def __init__(self,fp,inputx):
		self.fp= fp
		self.begin= []
		self.end= []
		self.inputx=inputx
		self.count=0
		self.scan()

	def manhattan(self,a,b,c,d):
		return abs(a-c)+abs(b-d)

	def linear_conflict(self,temp=[]):
		goaldictionary={}
		dictionary={}
		if(temp==[]):
			temp=self.begin
		for y in range(len(self.end)):
			for x in range(len(self.end[0])):
				if(self.end[y][x]!="0"):
					goaldictionary[self.end[y][x]]=(x+1,y+1)

		for y in range(len(temp)):
			for x in range(len(temp[0])):
				if(self.begin[y][x]!="0"):
					dictionary[self.begin[y][x]]=(x+1,y+1)

		sum=0
		for distance in dictionary:
			x1,y1=dictionary[distance]
			x2,y2=goaldictionary[distance]
			if(x1==x2 or y1==y2):
				sum+=1
			# print(distance,":",self.manhattan(x1,y1,x2,y2))
		# print(sum)
		return sum

	def update(self,temp=[]):
		goaldictionary={}
		dictionary={}
		if(temp==[]):
			temp=self.begin
		for y in range(len(self.end)):
			for x in range(len(self.end[0])):
				if(self.end[y][x]!="0"):
					goaldictionary[self.end[y][x]]=(x+1,y+1)

		for y in range(len(temp)):
			for x in range(len(temp[0])):
				if(self.begin[y][x]!="0"):
					dictionary[self.begin[y][x]]=(x+1,y+1)

		sum=0
		linear=self.linear_conflict(temp)
		for distance in dictionary:
			x1,y1=dictionary[distance]
			x2,y2=goaldictionary[distance]
			sum+=self.manhattan(x1,y1,x2,y2)
			# print(distance,":",self.manhattan(x1,y1,x2,y2))
		# print(sum)
		if(self.inputx=="2"):
			return sum+linear
		return sum


	def fprint(self):
		print("="*10,"BEGIN","="*10)
		for line in self.begin:
			print(line)
		print("="*11,"END","="*11)
		for line in self.end:
			print(line)

	def scan(self):
		R=[]
		flag = True
		for line in self.fp:
			for words in line:
				if(words.isdigit()):
					R.append(words)
			if(line == '\n'):
				flag=False
			if(flag and R!=[]):
				self.begin.append(R)
			elif(not flag and R!=[]):
				self.end.append(R)
			R=[]
		self.fprint()
		self.update()


	def algo(self,temp=[]):
		if(temp==[]):
			self.begin=[]
		for y in range(len(temp)):
			for x in range(len(temp[0])):
				if(temp[y][x]=="0"):
					return (y,x)

	def astar(self,temp=[],confirm=" ",kscore=[],thenext=[], level=0):
		level += 1
		if(temp==[] and kscore==[]):
			temp=self.begin
			kscore.append(self.update(temp))
		if(temp==self.end):
			print("DONEEEEE")
			return confirm,level,kscore
		y,x = self.algo(temp)
		if(y-1>=0):#move up
			tempu=copy.deepcopy(temp)
			tempu[y][x]=tempu[y-1][x]
			tempu[y-1][x]="0"
			score = self.update(tempu)
			move = " U"
			confirm2 = confirm + move
			tkscore=kscore
			tkscore.append(score)
			tempstate = State(score, tempu, move, confirm2,tkscore,level)

			#NEED TO FIX THIS IF, IDK IF THIS IF WORKS
			if(confirm[-1]!="D" or tempstate not in thenext):
				self.count+=1
				thenext.append(tempstate)

		if(y+1<3):#move down
			tempd=copy.deepcopy(temp)
			tempd[y][x]=tempd[y+1][x]
			tempd[y+1][x]="0"

			score = self.update(tempd)
			move = " D"
			confirm2 = confirm + move
			tkscore=kscore
			tkscore.append(score)
			tempstate = State(score, tempd, move, confirm2,tkscore,level)

			if(confirm[-1]!="U" or tempstate not in thenext):
				thenext.append(tempstate)
				self.count+=1

		if(x-1>=0):#move left
			templ=copy.deepcopy(temp)
			templ[y][x]=templ[y][x-1]
			templ[y][x-1]="0"

			score = self.update(templ)
			move = " L"
			confirm2 = confirm + move
			tkscore=kscore
			tkscore.append(score)
			tempstate = State(score, templ, move, confirm2,tkscore,level)

			if(confirm[-1]!="R" or tempstate not in thenext):
				thenext.append(tempstate)
				self.count+=1
		if(x+1<3):#move right
			tempr=copy.deepcopy(temp)
			tempr[y][x]=tempr[y][x+1]
			tempr[y][x+1]="0"

			score = self.update(tempr)
			move = " R"
			confirm2 = confirm + move
			tkscore=kscore
			tkscore.append(score)
			tempstate = State(score, tempr, move, confirm2,tkscore,level)

			if(confirm[-1]!="L" or tempstate not in thenext):
				thenext.append(tempstate)
				self.count+=1
		thenext.sort(key=lambda x: x.s, reverse=False)

		# print(self.count)
		nextstate=thenext.pop(0)
		score = nextstate.s
		nexttemp = nextstate.w
		confirm = nextstate.c
		kscore = nextstate.t
		level = nextstate.l
		
		# print("SCORE")
		# print(score)
		# print("nexttemp")
		# for line in nexttemp:
		# 	print(line)
		# print("CONFIRM")
		# print(confirm)
		# input()
		return self.astar(nexttemp,confirm,kscore,thenext, level)
	
	def out(self,fp):

		confirm,level,kscore=self.astar(self.begin," ",[self.update(self.begin)],[],0)
		
		for lines in self.begin:
			for i in lines:
				fp.write(i+' ')
			fp.write("\r\n") #lines 1-3 of begin 

		fp.write("\r\n") #line 4 empty

		for lines in self.end:
			for i in lines:
				fp.write(i+' ')
			fp.write("\r\n") #line 5-7 of end

		fp.write("\r\n") #line 8 empty

		fp.write(str(level-1)+"\r\n") #line 9 of depth

		fp.write(str(self.count)+"\n") #line 10 for generated nodes
		# self.count=0
 
		fp.write(confirm[2:]+"\r\n") #the path of the answer. Getting rid of empty space by [2:]

		for i in kscore:
			fp.write(str(i)+" ") #f(n)






def main():
	print("Would you like to use:")
	print("(1) sum of Manhattan distances of tiles from their goal position \n(2) sum of Manhattan distances + 2× # linear conflicts. ")
	print("Enter the number 1 or 2 : ")
	inputx=input()
	if(inputx=="1" or inputx=="2"):
			# fp = open("Input"+str(1)+".txt",'r')
			# woman = Man(fp,inputx)
			# print(woman.astar())
		for i in range(1,4):
			fp = open("Input"+str(i)+".txt",'r')
			print(fp)
			woman = Man(fp,inputx)
			# print(woman.astar())
			fp.close()
			fp = open("Output"+str(i)+".txt",'w')
			woman.out(fp)
			fp.close()
	else:
		print("ERROR")
		print("Input not valid")

if __name__ == '__main__':
	main()
