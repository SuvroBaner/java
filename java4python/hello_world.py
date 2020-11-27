'''class hello_world:
	def printName(self):
		print("Hello Andy and Suvro")

if __name__ == '__main__':
	hw = hello_world()
	hw.printName()'''

class hello_world:
	@staticmethod
	def printName():
		print("Hello Andy and Suvro")

if __name__ == '__main__':
	hello_world.printName()