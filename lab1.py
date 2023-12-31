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

 
# Terain Type Colors
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

#points have form [col, row, height]
#returns 3D straight line distance
#Update: became general heuristic funtion, now returns time from curr to target
def getDistance(point1, point2, color):
    #3D pythagoream theorum
    x1, y1, z1 = float(point1[0]), float(point1[1]), float(point1[2])
    x2, y2, z2 = float(point2[0]), float(point2[1]), float(point1[2])
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    if color == (248, 148, 18):
        speed = 3
    elif color == (255, 192, 0):
        speed = 1
    elif color == (255, 255, 255):
        speed = 3
    elif color == (2, 208, 60):
        speed = 2
    elif color == (2, 136, 40):
        speed = 1
    elif color == (5, 73, 24):
        speed = 0.01
    elif color == (0, 0, 255):
        speed = 0.01
    elif color == (71, 51, 3):
        speed = 2
    elif color == (0, 0, 0):
        speed = 2
    elif color == (205, 0, 101):
        speed = 0.01

    return distance / speed

def getColor(col, row):
    r, g, b = rgb_im.getpixel((col, row)) 
    return r, g, b



def drawPath(filepath, outputFile, line):
    
    finalPath = (200, 100, 230)
    with Image.open(filepath) as img:
        output = img.copy()
        draw = ImageDraw.Draw(output, "RGBA")
        
        for i in range(len(line) - 1):
            # print(line[i])
            #print("hi")
            #print(line[i + 1])
            #print("\n")
            draw.line([tuple(line[i]), tuple(line[i + 1])], fill=finalPath, width=1, joint=None)
    output.save(outputFile)
    output.show()

# outOfBounds = (205, 0, 101)
# impassibleVegetation = (5, 73, 24)
# lake = (0, 0, 255)
#Check if neighbors invalid (bad color)
def checkNeighbors(neighbors):
    i = 0
    valid = []
    #print(neighbors)
    for neighbor in neighbors:
        # print(neighbor)
        
        thisColor = neighbor[3]
        thisPoint = neighbor[1]
        
        #Check for invalid colors
        colorBool =  (thisColor == (0, 0, 255) or thisColor == (5, 73, 24) or thisColor == (205, 0, 101))
        # print("color:", colorBool)
        # print("point:", pointBool)
        if colorBool:
            del neighbors[i]
        # elif pointBool:
        #     del neighbors[i]
        else:
            i = i + 1   
            valid.append(neighbor)
    i = 0
    return valid

#takes in the current node, the target node, and the height of pixels 2d array
#returns the 4 neighbors in form (heuristic, location, elevation, color)
def getNeighbors(curr, target, pixelheight):
    # print("a")
    # print(curr)
    if len(curr) == 2:
        currX = curr[0]
        currY = curr[1]
    else:
        currX = curr[1][0]
        currY = curr[1][1]
    # print("\nhi")
    # print(curr)
    # print("hi")
    target = target + (pixelheight[target[0]][target[1]],)
    #print(target)
    
    up = (currX, currY + 1)
    down = (currX, currY - 1)
    left = (currX - 1, currY)
    right = (currX + 1, currY)
    coords = [up, down, left, right] 
    
    upColor = getColor(up[0], up[1])
    downColor = getColor(down[0], down[1])
    leftColor = getColor(left[0], left[1])
    rightColor = getColor(right[0], right[1])
    fails = []
    
    #coords = [up, down, left, right]   
    #check up [0]
    if coords[0][0] < 0  or coords[0][0] > 394 or coords[0][1] < 0 or coords[0][1] > 499:
        fails.append("up")
    #check down [1]
    if coords[1][0] < 0  or coords[1][0] > 394 or coords[1][1] < 0 or coords[1][1] > 499:
        fails.append("down")
    #check left [2]
    if coords[2][0] < 0  or coords[2][0] > 394 or coords[2][1] < 0 or coords[2][1] > 499:
        fails.append("left")
    #check right [3]
    if coords[3][0] < 0  or coords[3][0] > 394 or coords[3][1] < 0 or coords[3][1] > 499:
        fails.append("up")
    
    upHeur = getDistance((up[0], up[1], pixelheight[up[0]][up[1]]), target, upColor)
    downHeur = getDistance((down[0], down[1], pixelheight[down[0]][down[1]]), target, downColor)
    leftHeur = getDistance((left[0], left[1], pixelheight[left[0]][left[1]]), target, leftColor)
    rightHeur = getDistance((right[0], right[1], pixelheight[right[0]][right[1]]), target, rightColor)
    
    upFinal = (upHeur, up, pixelheight[up[0]][up[1]], upColor)
    downFinal = (downHeur, down, pixelheight[down[0]][down[1]], downColor)
    leftFinal = (leftHeur, left, pixelheight[left[0]][left[1]], leftColor)
    rightFinal = (rightHeur, right, pixelheight[right[0]][right[1]], rightColor)
    
    neighbors = []
    if "up" not in fails:
        neighbors.append(upFinal)
    if "down" not in fails:
        neighbors.append(downFinal)
    if "left" not in fails:
        neighbors.append(leftFinal)
    if "right" not in fails:
        neighbors.append(rightFinal)
    return neighbors

def heap_sort(queue):
    heap = [(item[0], item) for item in queue]  # Create a heap of tuples (key, item)
    heapq.heapify(heap)  # Convert the heap into a min-heap in-place
    sorted = [heapq.heappop(heap)[1] for _ in range(len(heap))]  # Pop and extract items
    # print(sorted)
    # print("\n\n")
    return sorted
    
#takes in map filepath, elevation filepath one pair of (x, y) tuples
#returns longer set of points, of correct path between the first points
def correctPath(mapFilepath, pixelheights, points):
    start = points[0]
    end = points[1]
    queue = []
    visited = []
    path = []
    queue.append(start)
    # print("to gN")
    # print(queue[0])
    neighbors = getNeighbors(queue[0], end, pixelheights)
    visited.append(queue[0])
    del queue[0]
    
    #Check if neighbors valid, add to list
    valids = checkNeighbors(neighbors)
    for node in valids:
        queue.append(node)
    #resort heapQ by index
    
    queue = heap_sort(queue)

    #queue = queue[0]
    while queue[0] is not None:
        #Main debug prints
        # print("\n")
        # print(path)
        # print(queue[0][1])
        # print(end)
        # print("a")
        # print(queue)
        # print(visited)
        
        # print(queue[1])
        # print(end)
        # print("\n")
        queue = heap_sort(queue)
        if queue[0][1] == end:
            path.append(queue[0])
            return path
        elif queue[0] in visited:
            del queue[0]
        else:
            queue = heap_sort(queue)
            #print(queue)
            #print(queue[0])
            neighbors = getNeighbors(queue[0][1], end, pixelheights)
            visited.append(queue[0])
            path.append(queue[0][1])
            queue.extend(checkNeighbors(neighbors))
            del queue[0]
    #return("queue cleared, no path found")


 
    #takes in path of points, returns path dist   
def pathDistance(finalPath, pixelheights):
    
    #pixel dims in m
    xSize = 10.29
    ySize = 7.55
    i = 0
    agg = 0
    while i < len(finalPath) - 1:
        point1 = finalPath[i]
        point2 = finalPath[i + 1]
        agg = agg + getDistance( 
            (point1[0] * xSize, point1[1] * ySize, pixelheights[point1[0]][point1[1]]),
            (point2[0] * xSize, point2[1] * ySize, pixelheights[point2[0]][point2[1]]), (2, 136, 40)
            )
        
        i = i + 1
    return float(agg)
            
            

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 lab1.py terrain-img elevation-file path-file output-img-filename")
        sys.exit(1)
        
    terrainImg = sys.argv[1]
    elevationFile = sys.argv[2]
    pathFile = sys.argv[3]
    outputFile = sys.argv[4]
    
    #PIL imports img, copy img, draw on copy, output copy
    with Image.open(terrainImg) as img:
        img.load()
        
    # get pixel colors
    cols = 395
    rows = 500
    pixelcolors = [[0 for j in range(rows)] for i in range(cols)]

    rgb_im = img.convert('RGB')
    #print(pixelcolors[100][100])
    for row in range(0, 500):
        for col in range(0, 395):   
            r, g, b = rgb_im.getpixel((col, row)) 
            pixelcolors[col][row] = (r, g, b)
            #print(col, row, pixelcolors[col][row])
            
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
        #print(parsedData)
        #print("\n")
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

    #print(points)
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
    finalPath = []
    for node in line:
        individualPath = correctPath(terrainImg, pixelheights, node)
        del individualPath[len(individualPath) - 1]
        finalPath.extend(individualPath)
    finalDist = pathDistance(finalPath, pixelheights)
    print(float(finalDist))
    
    print(outputFile)
    
    drawPath(terrainImg, outputFile, finalPath)
    
    