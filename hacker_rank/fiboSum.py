def calcFiboTerms(fibo, K):
	i = 3
	fibo += [0,1,1]
	while True:
		nextTerm = fibo[i - 1] + fibo[i - 2]
		if nextTerm > K:
			return
		fibo.append(nextTerm)
		i += 1

def findMinTerms(K):
	fibo = []
	calcFiboTerms(fibo, K)
	count, j = 0, len(fibo) - 1
	while K > 0:
		count += K // fibo[j]
		K %= fibo[j]
		j -= 1
	return count

if __name__ == "__main__":
	K = 17
	print(findMinTerms(K))