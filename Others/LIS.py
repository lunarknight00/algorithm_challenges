"""
Longest increasing subsequence

"""

def lis(nums:list) -> int:
	"""
	>>> lis([4, 2, 3, 1, 5])
	3
	"""
	if not nums or any([type(i) != int for i in nums]):
		return 0
	length = len(nums)
	dp = [0 for _ in range(length)]
	result = 0
	for i in range(length):
		dp[i] = 1
		for j in range(i):
			if nums[j]<nums[i]:
				dp[i] = max(dp[i],dp[j]+1)
		result = max(result, dp[i])
	# print(result)
	return result



if __name__ == '__main__':
	import doctest 
	doctest.testmod()

