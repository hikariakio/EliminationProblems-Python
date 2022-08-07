# IMPORTANT - CONTRADICTIONS ( Final Problem )

# In this problem, one of statements below is false. We don't know which.

# 1. When the robots line up in order by weight, the two older-model robots are not next to each other.
# 2. Ash is older than the lightest robot.
# 3. Jenk is older than the heaviest robot.
# 4. Zod is older than the medium-weight robot.
# 5. Jenk is the medium-weight robot.

# Rank the robots by model age and weight
# Robots - Ash Zod Jenk
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



# Statiscally, Clue #2, #3, #4 contradicts one another.
# Instead of bruteforcing one by one, we will assume statements #1 and #5 are correct.

for ash,zod,jenk in orderings:  
    if( 

        not isAdjacent #1
        (
            next(getWeight(oldestAge) for oldestAge in [ash,zod,jenk] if getAge(oldestAge) == old),
            next(getWeight(midAge) for midAge in [ash,zod,jenk] if getAge(midAge) == mid)
        ) and

        getWeight(jenk) == med and #5

        # either #2 , #3 , #4 is correct            
        (     
            #assume 2 is correct   
            ( #2
            getAge(ash) != new and
            getWeight(ash) != light and 
            getAge(ash) > next(getAge(lightestWt) for lightestWt in [ash,zod,jenk] if getWeight(lightestWt) == light)
            ) and
            ( #3
            getAge(jenk) != new and
            getWeight(jenk) != heavy and 
            getAge(jenk) > next(getAge(heaviestWt) for heaviestWt in [ash,zod,jenk] if getWeight(heaviestWt) == heavy)
            ) or
            ( #4
            getAge(zod) != new and
            getWeight(zod) != med and 
            getAge(zod) > next(getAge(mediumWt) for mediumWt in [ash,zod,jenk] if getWeight(mediumWt) == med)
            ) 
        ) and

        (        
            #assume 3 is correct   

            ( #3
            getAge(jenk) != new and
            getWeight(jenk) != heavy and 
            getAge(jenk) > next(getAge(heaviestWt) for heaviestWt in [ash,zod,jenk] if getWeight(heaviestWt) == heavy)
            ) and            
            ( #2
            getAge(ash) != new and
            getWeight(ash) != light and 
            getAge(ash) > next(getAge(lightestWt) for lightestWt in [ash,zod,jenk] if getWeight(lightestWt) == light)
            ) or            
            ( #4
            getAge(zod) != new and
            getWeight(zod) != med and 
            getAge(zod) > next(getAge(mediumWt) for mediumWt in [ash,zod,jenk] if getWeight(mediumWt) == med)
            ) 
        ) and   

        (        
            #assume 4 is correct   

             ( #4
            getAge(zod) != new and
            getWeight(zod) != med and 
            getAge(zod) > next(getAge(mediumWt) for mediumWt in [ash,zod,jenk] if getWeight(mediumWt) == med)
            ) and
            ( #2
            getAge(ash) != new and
            getWeight(ash) != light and 
            getAge(ash) > next(getAge(lightestWt) for lightestWt in [ash,zod,jenk] if getWeight(lightestWt) == light)
            ) or                       
            ( #3
            getAge(jenk) != new and
            getWeight(jenk) != heavy and 
            getAge(jenk) > next(getAge(heaviestWt) for heaviestWt in [ash,zod,jenk] if getWeight(heaviestWt) == heavy)
            ) 
        )   

    ):
            print("Ash" , ageText[ash[0]],wtText[ash[1]])
            print("Zod" , ageText[zod[0]],wtText[zod[1]])
            print("Jenk" , ageText[jenk[0]],wtText[jenk[1]])
