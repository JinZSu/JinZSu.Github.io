# python3 A\*Algo.py 
import copy
import sys
# sys.setrecursionlimit(10000)

class states:
	def __init__(self,world,score,move,confirm):
		self.world=world
		self.score=score
		self.move=move
		self.confirm=confirm


class Man:
	def __init__(self,fp,inputx):
		self.fp= fp
		self.begin= []
		self.end= []
		self.inputx=inputx
		self.history={}
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

	def astar(self,temp=[],confirm=" ",thenext=[], level=0):
		level += 1
		if(temp==[]):
			temp=self.begin
		if(temp==self.end):
			print("A* has finished")
			return confirm
		y,x = self.algo(temp)
		if(y-1>=0):#move up
			tempu=copy.deepcopy(temp)
			tempu[y][x]=tempu[y-1][x]
			tempu[y-1][x]="0"
			score=self.update(tempu)+level
			move="U"
			confirm+=move
			tempstack=states(score,tempu,move,confirm)

			if(confirm[-1]!="D" and [self.update(tempu)+level,tempu] not in thenext):
				thenext.append([self.update(tempu)+level,tempu])
		if(y+1<3):#move down
			tempd=copy.deepcopy(temp)
			tempd[y][x]=tempd[y+1][x]
			tempd[y+1][x]="0"
			score=self.update(tempd)+level
			move="D"
			confirm+=move
			tempstack=states(score,tempd,move,confirm)

			if(confirm[-1]!="U" and [self.update(tempd)+level,tempd] not in thenext):
				thenext.append([self.update(tempd)+level,tempd])
		if(x-1>=0):#move left
			templ=copy.deepcopy(temp)
			templ[y][x]=templ[y][x-1]
			templ[y][x-1]="0"
			score=self.update(templ)+level
			move="L"
			confirm+=move
			tempstack=states(score,templ,move,confirm)

			if(confirm[-1]!="R" and [self.update(templ)+level,templ] not in thenext):
				thenext.append([self.update(templ)+level,templ])
		if(x+1<3):#move right
			tempr=copy.deepcopy(temp)
			tempr[y][x]=tempr[y][x+1]
			tempr[y][x+1]="0"
			score=self.update(tempr)+level
			move="R"
			confirm+=move
			tempstack=states(score,tempr,move,confirm)


			if(confirm[-1]!="L" and [self.update(tempr)+level,tempr] not in thenext):
				thenext.append([self.update(tempr)+level,tempr])

		thenext.sort()
		n=thenext.pop(0)
		# if(n not in self.history):
		# 	self.history[n]=states()
		nexttemp=n[1]
		if(level!=)


		return self.astar(nexttemp,confirm,thenext,level)
	# def out(self,ostring):





def main():
	print("Would you like to use:")
	print("(1) sum of Manhattan distances of tiles from their goal position \n (2) sum of Manhattan distances + 2× # linear conflicts. ")
	print("Enter the number 1 or 2 : ")
	inputx=input()
	if(inputx=="1" or inputx=="2"):
			fp = open("Input"+str(1)+".txt",'r')
			woman = Man(fp,inputx)
			print(woman.astar())
		# for i in range(1,5):
		# 	fp = open("Input"+str(i)+".txt",'r')
		# 	woman = Man(fp,inputx)
		# 	print(woman.astar())
			# woman.out("Output"+str(i)+".txt")
	else:
		print("ERROR")
		print("Input not valid")

if __name__ == '__main__':
	main()
