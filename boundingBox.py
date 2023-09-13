### Lecture 4 - Check if polyline is inside bbox
# GEOG 554
# Ben Marosites
# 2023-09-11

# -------- function to check if points are real ------- are coords between -180 and 180
def validCoords(data):
    for coords in data:
        if -180 <= coords[0] <= 180 and -90 <= coords[1] <= 90:
            return True
        else:
            return False


# -------- function to check if point in bbox --------- Provided by Dr. Li. -- altered to remove defaults. provided in polyline function
def pointInBbox(x,y,minX, minY, maxX, maxY):
    if minX < x < maxX and minY < y < maxY:
        return True
    else:
        return False

# -------- function to check if polyline in bbox ---------
def checkPoints(polyline, bbox=[(-110,30),(-100,48)], breakRule=True, contains=True):
    if validCoords(polyline):
        Xs = [x[0] for x in bbox]       # List comprehension for X coords
        Ys = [y[1] for y in bbox]       # List comprehension for Y coords
        minX = min(Xs)                  # Find min/max for bbox
        maxX = max(Xs)
        minY = min(Ys)
        maxY = max(Ys)
        badPoints = []
        for point in polyline:
            if not pointInBbox(point[0], point[1], minX, minY, maxX, maxY):
                if breakRule:
                    return False            # No need for a break command. The return jumps out of the loop.
                else:
                    badPoints.append((point[0], point[1])) ## breakRule param reports points with issues. Could be helpful
        if badPoints:
            return 'Please check the following points...{}'.format(badPoints)
        return True
    else:
        return 'You encountered an error. Please check parameters.'


##def polylineInBbox(polyline,bbox=[(-110,30),(-100,48)]):
##    numPointInBbox = 0
##    for point in polyline:
##        pass
##                   
##   

#Call the function to check whether polyline
bbox = [(-110,30),(-100,48)]
polyline = [(-101,35),(-108,39),(-106,46),(-103,38)]
result = checkPoints(polyline, bbox, breakRule = False)
print(result)

##
###Call the function to check whether polyline
##bbox = [(-110,30),(-100,48)]
##polyline = [(-108,35),(-108,39),(-101,41),(-103,38)]
##result = checkPoints(polyline, bbox, breakRule=True)
##print(result)
##
##
###Call the function to check whether polyline
##bbox = [(-110,30),(-100,48)]
##polyline = [(-109,35),(-108,39),(45,67),(-103,38)]
##result = checkPoints(polyline, bbox)
##print(result)
