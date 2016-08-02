import random

x = []
for i in range(100):
	x.append(int(round(random.random()*10000)))

def selectSort(lst):
	srted = 0
	while srted<len(lst):
		small = srted
		for i in range(srted+1,len(lst)):
			if lst[i]<lst[small]:
				small = i
		lst[srted], lst[small] = lst[small], lst[srted]
		srted+=1
	print lst

selectSort(x)
