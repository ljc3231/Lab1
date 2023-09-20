#Liam Cummings
#AI Lab 1
#Jansen Orfan

#imports
import heapq
import sys
import math
from PIL import Image


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

finalPath = (200, 100, 230)             #Purple

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

#points have form [x, y, z]
#returns 3D straight line distance
def distance(point1, point2):
    #3D pythagoream theorum
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance


#start and end both 2d tuples of form [x, y]
def drawPath(filepath, start, end):
    with Image.open(filepath) as img:
        im._copy()
    PIL.ImageDraw.Draw(img, "RGBA")
    ImageDraw.line((start[0], start[1]), (end[0], end[1]), fill=finalPath, width=1, joint=None)


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
    #get pixel vals
    pixels[395][500]
    rgb_im = im.convert('RGB')
    for y in range(0, 395):
        for x in range(0, 500):
            r, g, b = rgb_im.getpixel((x, y)) 
            pixels[x][y] = (r, g, b)