"""
Given an array of integers, return a new array such that each element at index i 

of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 

If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
def newArr(arr):
	arr2 = []
	for i in range(0 ,len(arr)):
		temp = 1
		for j in range(0,len(arr)):
			if i != j:
				temp = temp * arr[j]
		arr2.append(temp)
	return arr2

if __name__ == '__main__':
		
	arr = [1, 2, 3, 4, 5]
	ar = [3, 2, 1]

	print(newArr(arr))
	print(newArr(ar))