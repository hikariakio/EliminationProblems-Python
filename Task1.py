
# 1.When the robots are lined up in order by age, Knuck is next to Norb.
# 2.Flo is heavier than the newest-model robot.
# 3.When the robots are lined up in order by age, Flo is next to Knuck.
# Find the age of robots.
# Flo,Knuck,Norb

import itertools, time
from helper import *

robot_sort = [0,1,2]
age = new,mid,old = [0,1,2]
ageText = ['newest','mid','oldest']

orderings = list(itertools.permutations(robot_sort))

for flo,knuck,norb in orderings: 
    if(
        isAdjacent(knuck,norb) and #1
        flo != new and #2
        isAdjacent(flo,knuck) #3
    ):
        print("Flo  ", ageText[flo])
        print("Knuck",ageText[knuck])
        print("Norb ",ageText[norb])