class Temperature:
	def __init__(self, farhen):
		self.farhen = farhen
		print(self.farhen)

	@classmethod
	def from_input(cls):
		return cls(int(input("Enter the temperature in F: ")))

	@staticmethod
	def farToCel(f):
		return "the temperature in C is: {}".format((f - 32) * 5.0/9.0)

if __name__ == '__main__':
	temp = Temperature.from_input()
	print(temp.farToCel(temp.farhen))