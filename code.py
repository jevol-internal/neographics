from neographics import visualObject,display
import board


class redBlinker(visualObject):
    def __init__(self):
        self.value = 2
        self.countUp = True
        self.pos = 1

    def clearFrame(self, display):
        display.subPx(self.pos//2 - 1, 1, (0.2*self.value, 0, 0))
        display.subPx(self.pos//2, 1, (self.value, 0, 0))
        display.subPx(self.pos//2 + 1, 1, (self.value, 0, 0))
        display.subPx(self.pos//2 + 2, 1, (0.2*self.value, 0, 0))

    def renderFrame(self, display):
        if self.countUp:
            self.value += 10
        else:
            self.value -= 10

        self.pos += 1
        
        display.addPx(self.pos//2 - 1, 1, (0.2*self.value, 0, 0))
        display.addPx(self.pos//2, 1, (self.value, 0, 0))
        display.addPx(self.pos//2 + 1, 1, (self.value, 0, 0))
        display.addPx(self.pos//2 + 2, 1, (0.2*self.value, 0, 0))
        if self.value >= 255:
            self.countUp = False
        elif self.value <= 2:
            self.countUp = True

        if self.pos >= 124:
            self.pos = -1


class blueBlinker(visualObject):
    def __init__(self):
        self.value = 1
        self.countUp = True
        self.pos = 1
        self.posUp = True

    def clearFrame(self, display):
        display.subPx(self.pos, 1, (0, 0, self.value))

    def renderFrame(self, display):
        if self.countUp:
            self.value += 1
        else:
            self.value -= 1

        if self.posUp:
            self.pos += 1
        else:
            self.pos -= 1
        display.addPx(self.pos, 1, (0, 0, self.value))
        if self.value >= 255:
            self.countUp = False
        elif self.value <= 1:
            self.countUp = True

        if self.pos >= 60:
            self.posUp = False
        elif self.pos <= 1:
            self.posUp = True

class comet(visualObject):
    def __init__(self):
        self.value = 2
        self.countUp = True
        self.pos = 10

    def clearFrame(self, display):
        display.subPx(self.pos//3 - 1, 1, (3, 3, 0))
        display.subPx(self.pos//3, 1, (255, 255, 0))
        display.subPx(self.pos//3 + 1, 1, (60, 60, 20))
        display.subPx(self.pos//3 + 2, 1, (50, 50, 50))
        display.subPx(self.pos//3 + 3, 1, (20, 20, 20))
        display.subPx(self.pos//3 + 4, 1, (10, 10, 10))

    def renderFrame(self, display):
        self.pos -= 1
        display.addPx(self.pos//3 - 1, 1, (3, 3, 0))
        display.addPx(self.pos//3, 1, (255, 255, 0))
        display.addPx(self.pos//3 + 1, 1, (60, 60, 20))
        display.addPx(self.pos//3 + 2, 1, (50, 50, 50))
        display.addPx(self.pos//3 + 3, 1, (20, 20, 20))
        display.addPx(self.pos//3 + 4, 1, (10, 10, 10))
        if self.pos <= -10:
            self.pos = 190
            


disp = display(board.D9, 60, 1)
disp.loadObjects([redBlinker(), blueBlinker(), comet()])
#disp.loadObjects([comet()])
disp.run()
