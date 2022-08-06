# 1. There are two sets of two robots that share the same model age.
# 2. When the robots line up in order by weight, their model ages alternate between new and old.
# 3. Ty is one of the newer-model robots.
# 4. Zat is heavier than Dex.
# 5. Ada is heavier than both of the older-model robots.
# Find the age and weight of robots.

import itertools

age= new,_,old,_= [0,0,1,1]
ageText = ["new","old"]
wt = light,secondlight,secondheavy,heavy = [0,1,2,3]
wtText = ["lightest","2ndlightest","2ndheaviest","heaviest"]

def sortByWeight(elem):
    return elem[1]

def isAgeNotAlternate(*robots):
    robots = list(robots) 
    robots.sort(key=sortByWeight)
    for i in range(len(robots)-1):
        if(robots[i][0]==robots[i+1][0] ):
            return True
    return False

def isAdaHeavierThanOldModels(robots,ada):
    oldModels = list(robot for robot in robots if robot[0]==old)
    for oldRobot in oldModels:
        if(ada[1] < oldRobot[1]):
            return False
    return True

ageshuffle = list(itertools.permutations(age)) 
wtshuffle = list(itertools.permutations(wt)) 

all_orderings = ([list(zip(*p)) for p in itertools.product(ageshuffle, wtshuffle)])

orderings = []
for x in all_orderings:
    if x not in orderings:
        orderings.append(x)

for ty,zat,ada,dex in orderings:  # [0] -> age / [1] -> weight
    if(
        ty [0] == new and   #3   
        zat[1] > dex[1] and #4

        ada[1] >= secondheavy and # 5
        ada[0] != old and #5        
        isAdaHeavierThanOldModels([ty,zat,dex],ada) and #5

        not isAgeNotAlternate(ty,zat,ada,dex) #2

    ):           
            print("Ty"  , ageText[ty[0]], wtText[ty[1]])
            print("Zat" , ageText[zat[0]],wtText[zat[1]])
            print("Ada" , ageText[ada[0]],wtText[ada[1]])
            print("Dex" , ageText[dex[0]],wtText[dex[1]])