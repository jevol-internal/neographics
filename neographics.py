import time
import board
import neopixel

class display:
    def __init__(self, pin, width, height):
        self.pixels = neopixel.NeoPixel(pin, width*height, auto_write=False)
        self.object = []
        self.framebuf = []
        for i in range(width * height): self.framebuf.append((0, 0, 0))

        self.width = width
        self.height = height

    def loadObjects(self, objects):
        self.object = objects

    def run(self):
        while True:
            for v in self.object:
                v.clearFrame(self)
            for v in self.object:
                v.renderFrame(self)
            #for i in range(self.width*self.height):
            #    self.pixels[i] = self.framebuf[i]
            self.pixels.show()
            time.sleep(1.0/100.0)

    def getPx(self, x, y):  # UNSAFE
        return self.pixels[(y - 1) * self.width + x - 1]

    def visible(self, x, y):
        return 0 < x and x <= self.width and 0 < y and y <= self.height

    def clampColor(self, c):
        if c < 0:
            return 0
        if c > 255:
            return 255
        return c

    def setPx(self, x, y, color):
        if self.visible(x, y):
            self.pixels[(y - 1) * self.width + x - 1] = (
                self.clampColor(color[0]),
                self.clampColor(color[1]),
                self.clampColor(color[2]),
            )

    def subPx(self, x, y, color):
        if self.visible(x, y):
            self.setPx(x, y,
            (
                self.getPx(x, y)[0] - color[0],
                self.getPx(x, y)[1] - color[1],
                self.getPx(x, y)[2] - color[2]
            ))

    def addPx(self, x, y, color):
        if self.visible(x, y):
            self.setPx(x, y,
            (
                self.getPx(x, y)[0] + color[0],
                self.getPx(x, y)[1] + color[1],
                self.getPx(x, y)[2] + color[2]
            ))

class visualObject(object):

    def __init__(self):
        pass

    def clearFrame(self, display):
        pass

    def renderFrame(self, display):
        pass