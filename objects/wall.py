import pyglet, random
from .pygletUtilities import movement, maths

class Wall(pyglet.shapes.Rectangle):
	"""docstring for Wall"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.speedX = 50
		self.speedY = 50
		self.collDist = 20
		self.rotSpeed = random.randrange(10, 45)
		self.rotation = random.randrange(0, 360)

	def move(self, xRange, yRange, dt):
		self.x += random.uniform(xRange[0], xRange[1]) * dt
		self.y += random.uniform(yRange[0], yRange[1]) * dt

	def update(self, dt):
		self.rotation += self.rotSpeed * dt
		self.move((-self.speedX, self.speedX), (-self.speedY, self.speedY), dt)






















print(__name__ + " loaded")