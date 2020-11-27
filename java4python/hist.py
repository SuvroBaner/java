def hist():
	count = [0] * 10
	data = open('test.dat')

	for line in data:
		count[int(line)] += 1

	print(count)

	idx = 0
	for num in count:
		print(str(idx) + ' occur ' + str(num) +' times ')
		idx += 1

if __name__ == '__main__':
	hist()