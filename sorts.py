import random


def mergesort(nums):
	n = len(nums)
	if n==1 or n==0:
		return nums
	
	mid = n//2

	nums1 = mergesort(nums[:mid])
	nums2 = mergesort(nums[mid:])

	result = []
	i1 = 0
	i2 = 0
	for _ in range(n):
		if i1 == len(nums1):
			result.append(nums2[i2])
			i2 += 1
		elif i2 == len(nums2):
			result.append(nums1[i1])
			i1 += 1
		elif nums1[i1] <= nums2[i2]:
			result.append(nums1[i1]) 
			i1 += 1
		else:
			result.append(nums2[i2])
			i2 += 1

	return result		



def quicksort(nums):
	n = len(nums)
	if n==1 or n==0:
		return nums

	p = random.randint(0,n-1)
	nums[p], nums[-1] = nums[-1], nums[p]

	i = 0
	j = 0
	while j < n-1:
		if nums[j] >= nums[-1]:
			j += 1
		else:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j += 1

	nums[i], nums[-1] = nums[-1], nums[i]
	
	nums1 = quicksort(nums[:i])
	nums2 = quicksort(nums[i+1:])

	return nums1 + nums[i:i+1] + nums2



def heapsort(nums):
	n = len(nums)
	if n==0 or n==1:
		return nums

	def left(i):
		return 2*i+1
	def right(i):
		return 2*i+2


	def heapify(i,n):
		i1 = left(i)
		i2 = right(i)
		if i1<n and i2<n:
			if nums[i1] < nums[i] and nums[i1] < nums[i2]:
				nums[i1], nums[i] = nums[i], nums[i1]
				heapify(i1,n)
			elif nums[i2] < nums[i] and nums[i2] < nums[i1]:
				nums[i2], nums[i] = nums[i], nums[i2]
				heapify(i2,n)
		elif i1<n:
			if nums[i1] < nums[i]:
				nums[i1], nums[i] = nums[i], nums[i1]
				heapify(i1,n)
		elif i2<n:
			if nums[i2] < nums[i]:
				nums[i2], nums[i] = nums[i], nums[i2]
				heapify(i2,n)

	heapify(0,n)

	result = []
	
	for i in range(n):
		print(nums)
		result.append(nums[0])
		nums[0] = nums[-1]
		nums.pop()
		heapify(0,n-i-1)

	return result
