# ## Problem 3 of Euler Project 
# https://www.projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# iteration solution 1
# How it works?
# As 2 is the smallest prime number 
def solution1(number:int)-> int:
	"""

	>>> solution1(13195)
	29

	"""
	result = list()
	divisor = 2
	# outer loop to find all divisor 
	# exit loop when is number can be divided
	while number > 1:
		# a inner loop to increment divisor
		while number % divisor == 0:
			result.append(divisor)
			number /= divisor
		divisor  += 1
	return max(result)

# recursive way 
def helper(number:int,result:list)

def solution2(number:int) -> int:
	"""
	>>> solution2(13195)
	29

	"""
	if number <= 1:
		return max(result)
	return 


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print(solution1(6000851475143))
