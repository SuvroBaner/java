from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a person is adult or not 
	@staticmethod
	def isAdult(age:int):
		return age > 18


if __name__ == '__main__':
	person1 = Person('Andy', 23)
	person2 = Person.fromBirthYear('Suvro', 1985)

	print(person1.age, person1.name)
	print(person2.age, person2.name)

	print(Person.isAdult(22))
