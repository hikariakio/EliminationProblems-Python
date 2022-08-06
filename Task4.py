# 1. When the robots line up in order by model age, Kit and the lightest robot are next to each other.
# 2. Ott is not the lightest robot.
# 3. The medium weight robot is newer than Kit.
# 4. When the robots line up in order by model age, the two lighter robots are next to each other.
# Rank the robots by model age and weight.
# Robot Names - Ott, Bo and Kit

from helper import *
import itertools

ageText = ['newest','mid','oldest']
wtText = ['lighest','med','heaviest']
age = new,mid,old = [0,1,2]
wt = light,med,heavy= [0,1,2]


num = [0,1,2]
shuffle = list(itertools.permutations(num)) 

orderings = [list(zip(*p)) for p in itertools.product(shuffle, shuffle)]

for ott,bo,kit in orderings:  
    
    if(

        getWeight(kit) != light and #1
        isAdjacent ( next( getAge(lightWt) for lightWt in [ott,bo] if getWeight(lightWt)== light), getAge(kit) ) and

        getWeight(ott) != light and #2

        getWeight(kit) != med and #3
        getAge(kit) != new and 

        next(getAge(mediumWt) for mediumWt in [ott,bo] if getWeight(mediumWt) == med) < getAge(kit)  and 

        isAdjacent(next(getAge(lightWt) for lightWt in [ott,bo,kit] if getWeight(lightWt) == light), #4
                   next(getAge(medWt) for medWt in [ott,bo,kit] if getWeight(medWt) == med))

    ):
            print("Ott" , ageText[getAge(ott)],wtText[getWeight(ott)])
            print("Bo" , ageText[getAge(bo)],wtText[getWeight(bo)])
            print("Kit" , ageText[getAge(kit)],wtText[getWeight(kit)])
