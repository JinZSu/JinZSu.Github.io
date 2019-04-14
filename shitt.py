# python3 A\*Algo.py 
import copy
import sys
# sys.setrecursionlimit(10000)

class Man:
	def __init__(self,fp):
		self.fp= fp
		self.begin= []
		self.end= []
		self.scan()

	def manhattan(self,a,b,c,d):
		return abs(a-c)+abs(b-d)

	def linear_conflict(self):
		return 

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
		for distance in dictionary:
			x1,y1=dictionary[distance]
			x2,y2=goaldictionary[distance]
			sum+=self.manhattan(x1,y1,x2,y2)
			# print(distance,":",self.manhattan(x1,y1,x2,y2))
		# print(self.sum)
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

	def astar(self,temp=[],confirm=" ",thenext=[]):
		if(temp==[]):
			temp=self.begin
		if(temp==self.end):
			print("DONEEEEE")
			return confirm
		y,x = self.algo(temp)
		if(y-1>=0):#move up
			tempu=copy.deepcopy(temp)
			tempu[y][x]=tempu[y-1][x]
			tempu[y-1][x]="0"
			if(confirm[-1]!="D" and [self.update(tempu),tempu," U"] not in thenext):
				thenext.append([self.update(tempu),tempu," U"])
		if(y+1<3):#move down
			tempd=copy.deepcopy(temp)
			tempd[y][x]=tempd[y+1][x]
			tempd[y+1][x]="0"
			if(confirm[-1]!="U" and [self.update(tempd),tempd," D"] not in thenext):
				thenext.append([self.update(tempd),tempd," D"])
		if(x-1>=0):#move left
			templ=copy.deepcopy(temp)
			templ[y][x]=templ[y][x-1]
			templ[y][x-1]="0"
			if(confirm[-1]!="R" and [self.update(templ),templ," L"] not in thenext):
				thenext.append([self.update(templ),templ," L"])
		if(x+1<3):#move right
			tempr=copy.deepcopy(temp)
			tempr[y][x]=tempr[y][x+1]
			tempr[y][x+1]="0"
			if(confirm[-1]!="L" and [self.update(tempr),tempr," R"] not in thenext):
				thenext.append([self.update(tempr),tempr," R"])
		thenext.sort()
		confirm+=thenext[0][2]
		nexttemp=thenext.pop(0)[1]
		print(confirm)
		return self.astar(nexttemp,confirm,thenext)





def main():
	for i in range(1,5):
		fp = open("Input"+str(i)+".txt",'r')
		woman = Man(fp)
		print(woman.astar())
		# woman.astar("Output"+str(i)+".txt")

if __name__ == '__main__':
	main()
