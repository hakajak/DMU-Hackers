from collections import defaultdict

wordtally = defaultdict(int)

with open('WordFrequencyText.txt','r') as f:
    for word in f.read().split():
    	wordtally[word] += 1

longestword = len(max(wordtally, key=len))
print('longestword = ' + str(longestword))

for word in sorted(wordtally):
	print('{0:{1}} : {2:*<{3}}'.format(word, longestword, '*', len(word)))
