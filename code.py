import time
import board
import neopixel

# Configure the setup
PIXEL_PIN = board.D5   # pin that the NeoPixel is connected to
ORDER = neopixel.RGB   # pixel color channel order
NUMBER_OF_PIXELS = 15

# Create the NeoPixel object
pix = neopixel.NeoPixel(PIXEL_PIN, NUMBER_OF_PIXELS, pixel_order=ORDER, auto_write = False)

RED = (0,255, 0) # color to blink
BLUE = (0,0, 255) # color to blink
GREEN = (255, 0, 0) # color to blink


CLEAR = (0, 0, 0)      # clear (or second color)
DELAY = 0.25           # blink rate in seconds

class Projection:
    # Types: 8BottomFrontTest
    RECT = "RECT"
    D_TEST2x4 = [2,4]

    def __init__(self, _type, _dsize):
        self._type = _type
        self._dsize = _dsize
    def draw(self,data):
        if([len(data),len(data[0])] == self._dsize and self._type == Projection.RECT):
            data = data[::-1]
            for y in range(len(data)):
                for x in range(len(data[y])):
                    pix[Projection.IDbyMAT(x,y, Projection.D_TEST2x4)] = data[y][x]
            pix.show()


    def IDbyMAT(x,y,_dtype):
        ret = 0
        if(_dtype == Projection.D_TEST2x4):
            if(y%2 == 0):
                ret += (3-x)
                ret += (3*y)
            else:
                ret += (3*y)
                ret += (x + 1)
        return ret

tinput = [[RED, BLUE, GREEN, RED], 
            [BLUE, GREEN, RED, BLUE]]
tinput2 = [[BLUE, RED, BLUE, GREEN],
            [RED, BLUE, GREEN, RED]]
ttype = Projection.RECT


proj = Projection(Projection.RECT, Projection.D_TEST2x4)
# Loop forever and blink the color
while True:
    proj.draw(tinput)
    time.sleep(DELAY)
    proj.draw(tinput2)
    time.sleep(DELAY)
