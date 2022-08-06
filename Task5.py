# 1. Var is not the heaviest robot.
# 2. When the robots line up in order by model age, Var and Ig are not next to each other.
# 3. The heaviest robot is newer than the medium-weight robot.
# 4. The lightest robot is newer than Ig.
# Rank the robots by model age and weight.
# Robot Names - Yan, Ig and Var

import itertools
from helper import *

ageText = ['newest','mid','oldest']
wtText = ['lighest','med','heaviest']
age = new,mid,old = [0,1,2]
wt = light,med,heavy= [0,1,2]


num = [0,1,2]
shuffle = list(itertools.permutations(num)) 

orderings = [list(zip(*p)) for p in itertools.product(shuffle, shuffle)]




for yan,ig,var in orderings:  
    if(  
        getWeight(var) != heavy and #1

        #var and ig not next together in age means Yan is middle age.
        getAge(yan) == mid and #2
       
        #3
        next(getAge(heavyWt) for heavyWt in [yan,ig,var] if getWeight(heavyWt) == heavy) <
        next(getAge(medWt) for medWt in [yan,ig,var] if getWeight(medWt) == med) and

        #4
        getAge(ig) != new and
        getWeight(ig)!= light and
        next(getAge(lightWt) for lightWt in [yan,ig,var] if getWeight(lightWt) == light) < getAge(ig) 

    ):
            print("Yan" , ageText[yan[0]],wtText[yan[1]])
            print("Ig" , ageText[ig[0]],wtText[ig[1]])
            print("Var" , ageText[var[0]],wtText[var[1]])
