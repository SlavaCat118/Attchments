import pyglet, objects, random, os, os.path

def loadWalls(ww, wh, num, colors, batch = None):
	walls = []
	for i in range(num):
		s = random.uniform(10, 30)
		nWall = objects.wall.Wall(
				x = random.randint(0, ww),
				y = random.randint(0, wh),
				width = s,
				height = s,
				batch = batch,
				color = colors[random.randrange(0, 4)]
			)
		nWall.anchor_position = nWall.width/2, nWall.height/2
		walls.append(nWall)
	return walls

def loadCursor(ww, wh, grabDist, maxLegs, batch = None):
	cursor = objects.cursor.Cursor(grabDist, maxLegs = maxLegs, x = ww//2, y = wh//2, radius = 10, color = (255, 255, 255), batch = batch)
	return cursor

def loadSectors(ww, wh, colors, batch = None):
	return [
		objects.sector.Sector(x = 0, y = 0, width = ww/2, height = wh/2, border_color = colors[0], color = colors[4], border = 50, batch = batch),
		objects.sector.Sector(x = ww/2, y = 0, width = ww/2, height = wh/2, border_color = colors[1], color = colors[5], border = 50, batch = batch),
		objects.sector.Sector(x = 0, y = wh/2, width = ww/2, height = wh/2, border_color = colors[2], color = colors[6], border = 50, batch = batch),
		objects.sector.Sector(x = ww/2, y = wh/2, width = ww/2, height = wh/2, border_color = colors[3], color = colors[7], border = 50, batch = batch)
	]
def loadAudio():
	path = './resources'
	pyglet.resource.path = [path]
	pyglet.resource.reindex()

	return [pyglet.media.load(os.path.join(path, i)) for i in os.listdir(path)]




















print(__name__ + " loaded")