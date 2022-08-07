# IMPORTANT - CONTRADICTIONS

# In this problem, one of statements below is false. We don't know which.

# 1. Mig is the oldest-model robot.
# 2. When the robots line up in order by weight, the two newest-model robots are next to each other.
# 3. Mig is the heaviest robot.
# 4. Gom is older than the heaviest robot.
# 5. Jett is the heaviest robot.

# Rank the robots by model age and weight
# Robots - Mig Jett Gom
# REMINDER - ONE CLUE IS FALSE

import itertools
from webbrowser import get
from helper import *

ageText = ['newest','mid','oldest']
wtText = ['lighest','med','heaviest']
age = new,mid,old = [0,1,2]
wt = light,med,heavy= [0,1,2]


num = [0,1,2]
shuffle = list(itertools.permutations(num)) 

orderings = [list(zip(*p)) for p in itertools.product(shuffle, shuffle)]



# Clue #3 and Clue #5 contradicts each other.
# Instead of bruteforcing one by one, we will assume other statements are correct.

for jett,mig,gom in orderings:  
    if(  
            #3 or #5 is correct            
        (        
        getWeight(mig) == heavy or   
        getWeight(jett)==heavy
        ) and

        getAge(mig) == old and  #1 

        isAdjacent #2
        (
            next(getWeight(newestAge) for newestAge in [jett,mig,gom] if getAge(newestAge) == new),
            next(getWeight(midAge) for midAge in [jett,mig,gom] if getAge(midAge) == mid)
        ) and

        #4
        getAge(gom) != new and
        getWeight(gom) != heavy and
        getAge(gom) > next(getAge(heavyWt) for heavyWt in [jett,mig,gom] if getWeight(heavyWt) == heavy)
    ):
            print("Jett" , ageText[jett[0]],wtText[jett[1]])
            print("Mig" , ageText[mig[0]],wtText[mig[1]])
            print("Gom" , ageText[gom[0]],wtText[gom[1]])
