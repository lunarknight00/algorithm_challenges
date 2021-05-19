
# time complexity O(n)
# space complexity O(1)
def sortOneN(L):
	"""
	>>> sortOneN([5, 3, 2, 1, 4])
	[1, 2, 3, 4, 5]
	"""
	n = len(L)
	for i in range(1, n+1):
		L[i-1] = i
	print(L)

if __name__ == "__main__":
	from doctest import testmod
	testmod()

