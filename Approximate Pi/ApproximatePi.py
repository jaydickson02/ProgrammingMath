import math
import sys

#Functions
def calculateSideLength(sides, radius):

    degrees = math.radians(180) #convert from degrees to radians

    sideLength = (math.tan(degrees/sides) * 2) / radius #Calculate the side length of a polygon based on num sides and the radius of said polygon
    return sideLength

def calculatePerimiter(sides, radius):

    sideLength = calculateSideLength(sides, radius)

    perimiter = sideLength * sides

    return perimiter

def calculatePi(sides, radius):

    perimiter = calculatePerimiter(sides, radius)

    piApproximation = perimiter/(radius * 2)

    return piApproximation

# Logic

radius = 1;
if len(sys.argv) > 1:
    sides = int(sys.argv[1]) # Square
else:
    sides = 1000

# while(sides <= 10000):
#    piApprox = calculatePi(sides, radius)
#    sides += 100000
#    print("Sides: " + str(sides) + " pi: " + '{0:.50f}'.format(piApprox))

piApprox = calculatePi(sides, radius)
print("Sides: " + str(sides))
print("Pi Approx  : " + '{0:.50f}'.format(piApprox))
print("Pi Constant: " + '{0:.50f}'.format(math.pi))
