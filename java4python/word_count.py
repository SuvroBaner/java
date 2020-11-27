def word_count():
	data = open('alice30.txt')
	wordList = data.read().split()

	count = {}
	for w in wordList:
		w = w.lower()
		count[w] = count.get(w, 0) + 1

	keyList = sorted(count.keys())
	for k in keyList:
		print("%-20s occurred %4d times" % (k, count[k]))

if __name__ == '__main__':
	word_count()