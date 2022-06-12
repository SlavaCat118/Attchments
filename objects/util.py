import math

def objDist(obj1, obj2):
	return math.sqrt(
			(obj1.x-obj2.x)**2 + 
			(obj1.y-obj2.y)**2
		)

def contains(pos, rect):
	return pos.x > rect.x and pos.x < rect.x + rect.width and pos.y > rect.y and pos.y < rect.y + rect.height
	