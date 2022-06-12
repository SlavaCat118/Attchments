import math

def dist(obj1 , obj2):
	return math.sqrt(
			(obj2.x - obj1.x) ** 2 +
			(obj2.y - obj1.y) ** 2
		)