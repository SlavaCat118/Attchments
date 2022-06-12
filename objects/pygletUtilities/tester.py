import pyglet, movement, math

win = pyglet.window.Window(300, 300, "Thig")
batch = pyglet.graphics.Batch()

anchor = pyglet.shapes.Circle(100, 200, 10, batch = batch)
obj = pyglet.shapes.Circle(200, 200, 5, batch = batch)
clock = pyglet.clock.Clock()

@win.event
def on_draw():
	win.clear()
	batch.draw()

def update(dt):
	movement.anchorPullOrbit(anchor, obj, 100 * dt, anchor.radius + obj.radius)
	anchor.y = math.sin(clock.time()*20)*10 + 200

pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()