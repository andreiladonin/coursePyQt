import pyglet

sound = pyglet.media.load('music.mp3', streaming=False)
sound.play()
pyglet.app.run()