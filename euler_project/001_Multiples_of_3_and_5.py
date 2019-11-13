"""
PROBLEM 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""


MAX_NUM = 1000

if __name__ == "__main__":
	result = int()
	for nb in range(1,MAX_NUM):
		if nb % 3 == 0 or nb % 5 ==0:
			result += nb
	print(f"the sum of all the multiples of 3 or 5 below 1000 is {result}")
