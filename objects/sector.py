import pyglet
from . import util

class Sector(pyglet.shapes.BorderedRectangle):
	"""docstring for Sector"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.contains = []
		self.complete = False
		self.opacity = 20

	def addObject(self, obj):
		self.contains.append(obj)

	def checkState(self):
		for i in self.contains:
			if i.color != self.color and i.color != self.border_color:
				self.complete = False
				return
		self.complete = True

	def update(self, dt):
		self.checkState()
		toRem = []
		for obj in self.contains:
			if not util.contains(obj, self):
				toRem.append(obj)
		for obj in toRem:
			self.contains.remove(obj)

		if self.complete:
			self.opacity = 50
		else:
			self.opacity = 20