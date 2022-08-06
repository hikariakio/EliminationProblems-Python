def isAdjacent(robot1, robot2):
    return abs(robot1-robot2) == 1

def getAge(robot):
    return robot[0]

def getWeight(robot):
    return robot[1]

def sortByAge(robots):
    robots.sort(key=getAge)
    return robots

def sortByWeight(robots):
    robots.sort(key=getWeight)
    return robots    