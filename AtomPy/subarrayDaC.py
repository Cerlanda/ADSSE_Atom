#defining
def maxCrossSum(A, low, mid, high):
    sum = 0
    left_sum = -999 #supposed to be minus infinity like in the book
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if (sum > left_sum): #update according to statement
            left_sum = sum
    sum = 0 #reuse integer to less memory usage?
    right_sum = -999 #supposed to be minus infinity like in the book
    for j in range(mid + 1, high +1):
        sum = sum + A[j]
        if (sum > right_sum): #update according to statement
            right_sum = sum

    return max(left_sum, right_sum, left_sum + right_sum) #return values

def maxSubSum(A, low, high):
    if (low == high):
        return A[low]

    mid = (low + high) // 2

    #A[low to mid]
    #A[mid+1 to high]
    #max of left sum, right sum and crossing
    return max(maxSubSum(A, low, mid),
               maxSubSum(A, mid+1, high),
               maxCrossSum(A, low, mid, high))

A = [-2, 3, -4, 5, 7, -8, 12, -3] #array to be used, can be changed
n = len(A) #len = length

max_sum = maxSubSum(A, 0, n-1)
print("Maximum contiguous sum is ", max_sum) #print max contiguous sum
