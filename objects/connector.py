import pyglet, math
from .pygletUtilities import movement

class Connector(pyglet.shapes.Line):
	"""docstring for Connector"""

	def __init__(self, obj1, obj2, *args, **kwargs):
		super().__init__(x = obj1.x, y = obj1.y, x2 = obj2.x, y2 = obj2.y, *args, **kwargs)

		self.obj1 = obj1
		self.obj2 = obj2
		self.pullSpeed = 1000

	def pullObject(self, obj, anchor, dt):
		movement.anchorPullOrbit(anchor, obj, self.pullSpeed * dt, 30)

	def update(self, dt):
		self.x, self.y = self.obj1.x, self.obj1.y
		self.x2, self.y2 = self.obj2.x, self.obj2.y





















print(__name__ + " loaded")