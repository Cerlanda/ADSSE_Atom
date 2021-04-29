def maxSubSum(A,n):

	currentMax = A[0] #biggest so far
	currentGlobal = 0 #current index value we are at

	for i in range(0, n):
		currentGlobal = currentGlobal + A[i]
		if currentGlobal < 0:
			currentGlobal = 0

		elif (currentMax < currentGlobal): #if global > currentMax, update the value
			currentMax = currentGlobal

	return currentMax

A=[-2, 3, -4, 5, 7, -8, 12, -3] #array to be used, can be changed
n=len(A) # len = length
currentMax=maxSubSum(A,n-1)
print(currentMax) #print results if wanted
