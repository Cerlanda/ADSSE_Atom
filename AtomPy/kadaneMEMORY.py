import os,psutil
import numpy
#defining
def maxCrossArraySum(A, low, mid, high):
    sum = 0
    left_sum = -999
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if (sum > left_sum):
            left_sum = sum
    sum = 0
    right_sum = -999
    for j in range(mid + 1, high +1):
        sum = sum + A[j]
        if (sum > right_sum):
            right_sum = sum

    return max(left_sum, right_sum, left_sum + right_sum)

def maxSubArraySum(A, low, high):
    if (low == high):
        return A[low]

    mid = (low + high) // 2

    return max(maxSubArraySum(A, low, mid),
               maxSubArraySum(A, mid+1, high),
               maxCrossArraySum(A, low, mid, high))

A = numpy.random.randint(-10,10,1000000)
n = len(A)

max_sum = maxSubArraySum(A, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
pid = os.getpid()
ps = psutil.Process(pid)
memoryUse = ps.memory_info()
print(memoryUse.rss)
