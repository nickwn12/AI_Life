import random
import constants as c


class CUBE():
    def __init__(self, height, length, width, sensor, cords):
        self.height = height
        self.length = length
        self.width = width
        self.sensor = sensor
        self.centerX = cords[0]
        self.centerY = cords[1]
        self.centerZ = cords[2]
        self.cubeName = -1
        self.parent = -1

        self.Xmin = self.centerX - self.length/2
        self.Xmax = self.centerX + self.length/2
        self.Ymin = self.centerY - self.width/2
        self.Ymax = self.centerY + self.width/2
        self.Zmin = self.centerZ - self.height/2
        self.Zmax = self.centerZ + self.height/2

        self.kids = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}

    def nameCube(self, name, parent):
        self.cubeName = name
        self.parent = parent

    def addCubeRandomSide(self, cubes):
  
        length, width, height = random.random() * c.scale + c.baseLength, c.baseWidth + random.random() * \
            c.scale, c.baseHeight + random.random() * c.scale
        avalibleSides = []
        for i in range(6):
            if self.kids[i] == None:
                avalibleSides.append(i)
        if len(avalibleSides) == 0:
            return False
        chosenSide = random.sample(avalibleSides, 1)[0]
        NewCenterX = self.centerX
        NewCenterY = self.centerY
        NewCenterZ = self.centerZ

        if chosenSide == 0:
            NewCenterX += self.length/2 + length/2
        elif chosenSide == 1:
            NewCenterX -= self.length/2 + length/2
        elif chosenSide == 2:
            NewCenterY += self.width/2 + width/2
        elif chosenSide == 3:
            NewCenterY -= self.width/2 + width/2
        elif chosenSide == 4:
            NewCenterZ += self.height/2 + height/2
        elif chosenSide == 5:
            NewCenterZ -= self.height/2 + height/2

        # Check that the new cube does not overlap
        curCube = CUBE(height=height, length=length, width=width,
                       sensor=True, cords=[NewCenterX, NewCenterY, NewCenterZ])
        cubList = cubes.getCubesList()
        for cube in cubList:
            if curCube.intersect(cube):
                return False

        cubes.addCube(curCube, self.cubeName)
        self.kids[chosenSide] = curCube
        return True
    
    def setSize(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def mutateSize(self):
        self.height = self.height * (random.random() - .5)/10
        self.length = self.length * (random.random() - .5)/10
        self.width = self.width * (random.random() - .5)/10

    def intersect(self, Cube):
        if self.Xmin >= Cube.Xmax or self.Xmax <= Cube.Xmin:
            return False
        if self.Ymin >= Cube.Ymax or self.Ymax <= Cube.Ymin:
            return False
        if self.Zmin >= Cube.Zmax or self.Zmax <= Cube.Zmin:
            return False
        return True
