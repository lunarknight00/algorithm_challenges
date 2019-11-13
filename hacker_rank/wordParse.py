import sys, re, string

data = sys.stdin.readlines()
# if it is not working then using 

# data = [line for line in sys.stdin]
# data =list(map(int,sys.stdin.read().split()))

tmp = []
findNonWord = False
wordList = []

for line in data:
	findNonWord = False
	for idx in range(len(line)):
		iChar = line[idx]
		if re.match("[a-z]", iChar) and not findNonWord:
			tmp.append(iChar)
		elif iChar == ' ':
			if not findNonWord and len(tmp)>0:
				wordList.append(''.join(tmp))
			tmp = []
			findNonWord = False
		else:
			findNonWord = True
			tmp = []
		if idx==len(line)-1:
			if not findNonWord and len(tmp)>0:
				wordList.append(''.join(tmp))
			tmp = []


wordCount = len(wordList)
print(wordCount)
print('words')
wordSet = sorted(set(wordList))

for iWord in wordSet:
	print(iWord + " " + str(wordList.count(iWord)))

print('letters')
for iLetters in string.ascii_lowercase[:26]:
	count = 0
	for iWord in wordList:
		count += iWord.count(iLetters)
	print(iLetters + " " + str(count))