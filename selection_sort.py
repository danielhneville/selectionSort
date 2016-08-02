import random

x = []
for i in range(100):
	x.append(int(round(random.random()*10000)))

def selectSort(lst):
	srted = 0
	while srted<len(lst)/2:
		small = srted
		large = srted
		for i in range(srted+1,len(lst)-srted):
			if lst[i]<lst[small]:
				small = i
			if lst[i]>lst[large]:
				large = i
		lst[srted], lst[small] = lst[small], lst[srted]
		lst[len(lst)-1-srted], lst[large] = lst[large],lst[len(lst)-1-srted]
		srted+=1
	print lst

selectSort(x)
