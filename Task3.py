# 1. There are two sets of two robots that share the same model age.
# 2. When the robots line up in order by weight, their model ages alternate between new and old.
# 3. Ty is one of the newer-model robots.
# 4. Zat is heavier than Dex.
# 5. Ada is heavier than both of the older-model robots.
# Find the age and weight of robots.
# Robot names - Ty , Zat , Ada , Dex

import itertools
from helper import *

age= new,_,old,_= [0,0,1,1] #1
ageText = ["new","old"]
wt = light,secondlight,secondheavy,heavy = [0,1,2,3]
wtText = ["lightest","2ndlightest","2ndheaviest","heaviest"]


def isAgeNotAlternate(robots):
    robots = sortByWeight(robots)
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

for ty,zat,ada,dex in orderings:  
    if(
        
        getAge(ty) == new and   #3   
        getWeight(zat) > getWeight(dex) and #4

        getWeight(ada) >= secondheavy and # 5
        getAge(ada) == new and #5        
        isAdaHeavierThanOldModels([ty,zat,dex],ada) and #5

        not isAgeNotAlternate([ty,zat,ada,dex]) #2
    ):           
            print("Ty"  , ageText[getAge(ty)], wtText[getWeight(ty)])
            print("Zat" , ageText[getAge(zat)],wtText[getWeight(zat)])
            print("Ada" , ageText[getAge(ada)],wtText[getWeight(ada)])
            print("Dex" , ageText[getAge(dex)],wtText[getWeight(dex)])