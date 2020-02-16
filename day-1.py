""" 
Given a list of numbers and a number k , 

return wheather any two numbers from the list add up to k 

eg. given [10,15,3,7] and k of 17, return true since 10+7 is 17 

Bonus: Can you do in one Pass ?

"""

class Test():
	def __init__(self,list,k):
		self.list = list
		self.k = k
	def check(self):
		for i in self.list:
			for j in self.list:
				if i+j == self.k:
					return True 
		return False


if __name__ == '__main__':
		
	list = [11,10,3,7]
	k = 17

	c = Test(list,k)
	print(c.check())


""" Answer with Bonus"""
def printPairs(arr, arr_size, sum): 
	
	# Create an empty hash set 
	s = set() 
	
	for i in range(0, arr_size): 
		# print(s)
		temp = sum-arr[i] 
		if (temp in s): 
			return True
			# print "Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")"
		s.add(arr[i]) 
	return False

A = [1, 4, 45, 6, 11, 8] 
n = 1
ans =printPairs(A, len(A), n) 
print(ans)
