#Answer 4
class Shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def Area(self):
		print(self.length*self.breadth)
class Rectangle(Shape):
	pass
class Sqaure(Shape):
	pass
print("Area of rectangle:",end=' ')
rect=Rectangle(12,10)
rect.Area()
print("Area of Square:",end=' ')
sq=Sqaure(10,10)
sq.Area()
