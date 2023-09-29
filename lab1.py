#Liam Cummings
#AI Lab 1
#Jansen Orfan

#imports
import heapq
import sys
import math
import numpy as np
# import PIL
from PIL import Image, ImageDraw


#Global Variables
#pixel dims in m
xSize = 10.29
ySize = 7.55

#Terain Type Colors
openLand = (248, 148, 18)               #Orange         
roughMeadow = (255, 192, 0)             #Yellow        
easyMovementForest = (255, 255, 255)    #White          
slowRunForest = (2, 208, 60)            #Light Green    
walkForest = (2, 136, 40)               #Green          
impassibleVegetation = (5, 73, 24)      #Dark Green     
lake = (0, 0, 255)                      #Blue           
pavedRoad = (71, 51, 3)                 #Brown          
footpath = (0, 0, 0)                    #Black 
outOfBounds = (205, 0, 101)             #Magenta

#Terrain Speeds in m/s
openLandSpeed = 3                        
roughMeadowSpeed = 1                  
easyMovementForestSpeed = 3          
slowRunForestSpeed = 2               
walkForestSpeed = 1                        
impassibleVegetationSpeed = 0         
lakeSpeed = 0                                
pavedRoadSpeed = 2                     
footpathSpeed = 2             
outOfBoundsSpeed = 0            

#points have form [col, row, height]
#returns 3D straight line distance
def distance(point1, point2):
    #3D pythagoream theorum
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance

def getColor(col, row):
    r, g, b = rgb_im.getpixel((col, row)) 
    return r, g, b


#start and end both 2d tuples of form [col, row]
def drawPath(filepath, line):
    finalPath = (200, 100, 230)
    with Image.open(filepath) as img:
        draw = ImageDraw.Draw(img, "RGBA")
        for start, end in line:
            draw.line([start, end], fill=finalPath, width=5, joint=None)
            print([start, end])
        img.show()
    


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 lab1.py terrain-img elevation-file path-file output-img-filename")
        sys.exit(1)
        
    terrainImg = sys.argv[1].lower()
    elevationFile = sys.argv[2].lower()
    pathFile = sys.argv[3].lower()
    outputFile = sys.argv[4].lower()
  
    #PIL imports img, copy img, draw on copy, output copy
    with Image.open(terrainImg) as img:
        img.load()
        
    # get pixel colors
    # cols = 395
    # rows = 500
    # pixelcolors = [[0 for j in range(rows)] for i in range(cols)]

    # rgb_im = img.convert('RGB')
    # print(pixelcolors[100][100])
    # for row in range(0, 500):
    #     for col in range(0, 395):   
    #         r, g, b = rgb_im.getpixel((col, row)) 
    #         pixelcolors[col][row] = (r, g, b)
    #         print(col, row, pixelcolors[col][row])
            
    #get pixel elevations
    cols = 400
    rows = 500
    pixelheights = [[0 for j in range(rows)] for i in range(cols)]
    with open(elevationFile, 'r') as elevations:
        data = [line.rstrip() for line in elevations]
    row = 0
    for line in data:       
        parsedData = line.split()
        col = 0
        print(parsedData)
        print("\n")
        for height in parsedData:
            pixelheights[col][row] = height
            col = col + 1
        row = row + 1
    row = 0
    col = 0

    #1. add starting node to heapq
    #2. add all children to heapq, sort
    #3. pop lowest node, run test/solution case
    #4. go to next lowest, add its children,
    #repeat 3-4
    
    #Get points
    
    points = []
    
    with open(pathFile, 'r') as pointFile:
        points = (pointFile.read().split("\n"))

    print(points)
    line = []    
    #Go through each pair of points, get and draw the path
    i = 0
    while i < (len(points) - 2):
        start = points[i].split(" ")
        start[0] = int(start[0])
        start[1] = int(start[1])
        end = points[i + 1].split(" ")
        end[0] = int(end[0])
        end[1] = int(end[1]) 
        # print(start)
        # print(end)
        pair = []
        pair.append(tuple(start))
        pair.append(tuple(end))
        line.append(tuple(pair))
        i = i + 1
    drawPath(terrainImg, line)
    