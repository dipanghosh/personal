import svgwrite
import numpy as np

linelen = 10

def calculateEndCoord(startcoord):
    if (np.random.random()<0.95):
        return (startcoord[0], startcoord[1]+10)
    elif (np.random.random()<0.9):
        return (startcoord[0]+10, startcoord[1] + 10)
    else:
        return (startcoord[0] - 10, startcoord[1] + 10)

dwg = svgwrite.Drawing('test.svg', profile='full', size=(2000,1000))

def getline(startcoord):
    startcoord = startcoord
    endcoord = calculateEndCoord(startcoord)
    dwg.add(dwg.circle(startcoord, 2.5, stroke=svgwrite.rgb(10, 10, 16, '%'), fill='white'))
    for i in range(50):
        dwg.add(dwg.line(startcoord, endcoord, stroke=svgwrite.rgb(10, 10, 16, '%')))
        startcoord = endcoord
        endcoord = calculateEndCoord(startcoord)
    dwg.add(dwg.circle(startcoord, 2.5, stroke=svgwrite.rgb(10, 10, 16, '%'),fill='white'))

for i in range(100):
    getline((100+(5*i), 100))

dwg.save()

