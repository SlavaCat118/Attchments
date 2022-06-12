import pyglet, time
import objects, load

class Attachments(object):
	"""docstring for Atatch"""

	def __init__(self, ww, wh, batch):
		self.grabDist =  100
		self.wallCount = 0
		self.colors = [
			(255, 0, 0),
			(0, 255, 0),
			(0, 0, 255),
			(255, 255, 0),
			(50, 0, 0),
			(0, 50, 0),
			(0, 0, 50),
			(50, 50, 0)
		]

		nWall = objects.wall.Wall(
				x = ww+ww/2,
				y = wh-wh/2,
				width = 30,
				height = 30,
				batch = batch,
				color = self.colors[1]
			)
		nWall.anchor_position = nWall.width/2, nWall.height/2
		self.walls = [nWall]
		self.cursor = load.loadCursor(ww, wh, self.grabDist, 5, batch)
		self.audio = load.loadAudio()

		self.mouseX = ww//2
		self.mouseY = wh//2

		self.ww = ww
		self.wh = wh

		self.batch = batch
		self.sectors = load.loadSectors(self.ww, self.wh, self.colors, self.batch)
		self.checkWinFrame = 0
		self.won = False
		self.levelCount = pyglet.text.Label(x = 0, y = self.wh-20, text = "Level: " + str(self.wallCount), batch = self.batch)

		self.audio[0].play().loop = True

	def fixBounds(self, obj, dt):
		if obj.x > self.ww:
			obj.move((-obj.speedX,0),(0,0),dt)
		elif obj.x < 0:
			obj.move((0,obj.speedX),(0,0),dt)

		if obj.y > self.wh:
			obj.move((0,0),(-obj.speedY,0),dt)
		elif obj.y < 0:
			obj.move((0,0),(0, obj.speedY),dt)

	def update(self, dt):

		self.cursor.update(self.mouseX, self.mouseY, dt)
		for i in range(len(self.walls)):
			wall1 = self.walls[i]
			if objects.util.objDist(self.cursor, wall1) < self.grabDist:
				if wall1 not in self.cursor.connectedTo:
					self.cursor.buildConnection(wall1)

			elif wall1 in self.cursor.connectedTo:
				self.cursor.deleteConnection(wall1)

			self.fixBounds(wall1, dt)
			wall1.update(dt)




		if self.checkWinFrame == 5:
			self.checkWinFrame = 0
			for sector in self.sectors:
				wallsCheck = [] + self.walls
				checked = []
				for wall in wallsCheck:
					if objects.util.contains(wall, sector):
						checked.append(wall)
						sector.addObject(wall)
				for wall in checked:
					wallsCheck.remove(wall)

				sector.update(dt)
			if sum([1 if i.complete else 0 for i in self.sectors]) == 4:
				self.won = True
		else:
			self.checkWinFrame += 1

	def reset(self):
		for wall in self.walls:
			wall.delete()
		self.cursor.delete()
		for sector in self.sectors:
			sector.delete()
		self.grabDist =  100
		self.colors = [
			(255, 0, 0),
			(0, 255, 0),
			(0, 0, 255),
			(255, 255, 0),
			(50, 0, 0),
			(0, 50, 0),
			(0, 0, 50),
			(50, 50, 0)
		]
		self.walls = load.loadWalls(self.ww, self.wh, self.wallCount, self.colors, batch)
		self.cursor = load.loadCursor(self.ww, self.wh, self.grabDist, 5, batch)

		self.mouseX = self.ww//2
		self.mouseY =self. wh//2

		self.batch = batch
		self.sectors = load.loadSectors(self.ww, self.wh, self.colors, self.batch)
		self.checkWinFrame = 0
		self.won = False
		self.levelCount.text = "Level: " + str(self.wallCount)



# Actual Program

batch = pyglet.graphics.Batch()
game = Attachments(1000, 500, batch)
gameWindow = pyglet.window.Window(game.ww, game.wh, "thig", resizable = True)

@gameWindow.event
def on_draw():
	gameWindow.clear()
	batch.draw()

@gameWindow.event
def on_mouse_motion(x, y, b, m):
	game.mouseX, game.mouseY = x, y

@gameWindow.event
def on_mouse_drag(x, y, dx, dy, b, m):
	game.mouseX, game.mouseY = x, y

gameWindow.push_handlers(game.cursor.mouseHandler)

def update(dt):
	game.update(dt)
	if game.won:
		game.wallCount += 1
		game.reset()
		gameWindow.push_handlers(game.cursor.mouseHandler)

time.sleep(0.2)
pyglet.clock.schedule_interval(update, 1/120.0)

pyglet.app.run()






















print(__name__ + " loaded")