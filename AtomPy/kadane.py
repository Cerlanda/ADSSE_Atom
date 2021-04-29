def maxSubSum(A,n):

	currentMax = A[0] #so far
	currentGlobal = 0 #ending here

	for i in range(0, n):
		currentGlobal = currentGlobal + A[i]
		if currentGlobal < 0:
			currentGlobal = 0

		elif (currentMax < currentGlobal):
			currentMax = currentGlobal

	return currentMax

A=[-2, 3, -4, 5, 7, -8, 12, -3]
n=len(A)
currentMax=maxSubSum(A,n-1)
print(currentMax)
