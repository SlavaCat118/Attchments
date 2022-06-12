import pyglet
from . import util, connector
from pyglet.window import mouse

class Cursor(pyglet.shapes.Circle):
	"""docstring for Cursor"""

	def __init__(self, grabDist, maxLegs = -1, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.connections = []
		self.connectedTo = []
		self.maxLegs = maxLegs
		self.grabDist = grabDist
		self.grabCirc = pyglet.shapes.Circle(x = self.x, y = self.y, radius = self.grabDist, color = self.color, batch = self._batch)
		self.grabCirc.opacity = 20
		self.mouseHandler = mouse.MouseStateHandler()

	def update(self, x, y, dt):
		self.x, self.y = x, y
		for i in self.connections:
			i.update(dt)
		self.grabCirc.position = self.position

		if self.mouseHandler[mouse.LEFT]:
			for connection in self.connections:
				connection.pullObject(connection.obj2, self, dt)

	def buildConnection(self, obj):
		if self.maxLegs < 0 or len(self.connections) < self.maxLegs:
			self.connectedTo.append(obj)
			self.connections.append(connector.Connector(
				self, obj, batch = self._batch, width = 3, color = self.color
				))

	def deleteConnection(self, obj):
		if obj in self.connectedTo:
			self.connectedTo.remove(obj)
			for i in self.connections:
				if obj == i.obj1 or obj == i.obj2:
					self.connections.remove(i)
					i.delete()

	def delete(self):
		self.grabCirc.delete()
		for connection in self.connections:
			connection.delete()
		super().delete()
		






















print(__name__ + " loaded")