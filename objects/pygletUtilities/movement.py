import pyglet, math
from . import maths

def anchorPull(anchor, obj, speed): # Credit: https://gamedev.stackexchange.com/a/201277/162920

	deltaX = anchor.x - obj.x
	deltaY = anchor.y - obj.y

	mag = deltaX * deltaX + deltaY * deltaY

	if mag < speed * speed:
		obj.x = anchor.x
		obj.y = anchor.y 
	else:
		scale = speed /  math.sqrt(mag)
	
		obj.x += deltaX * scale
		obj.y += deltaY * scale

def anchorPullOrbit(anchor, obj, speed, termDist): # Credit: https://gamedev.stackexchange.com/a/201277/162920

	deltaX = anchor.x - obj.x
	deltaY = anchor.y - obj.y

	distance = math.sqrt(deltaX * deltaX + deltaY * deltaY)

	unitScale = 1 / distance

	deltaX *= unitScale
	deltaY *= unitScale

	onCircleX = anchor.x - deltaX * termDist
	onCircleY = anchor.y - deltaY * termDist

	fromStop = distance - termDist

	if abs(fromStop) <= speed:
		obj.x = onCircleX
		obj.y = onCircleY
	else:
		if fromStop < 0:
			deltaX *= -1
			deltaY *= -1
	
		obj.x += deltaX * speed
		obj.y += deltaY * speed