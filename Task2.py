
# 1. The lightest robot is newer than Rae.
# 2. The heaviest robot is newer than Lex.
# 3. Loy is not the heaviest robot.
# Find the age and weight of robots.
# Robot names - Rae, Lex , Loy

import itertools
from helper import *

ageText = ['newest','mid','oldest']
wtText = ['lighest','med','heaviest']
age = new,mid,old = [0,1,2]
wt = light,med,heavy= [0,1,2]
num = [0,1,2]
shuffle = list(itertools.permutations(num)) 

orderings = [list(zip(*p)) for p in itertools.product(shuffle, shuffle)]


for rae,lex,loy in orderings: 
        if(
            getWeight(rae) != light and #1
            getAge(rae) != new and #1

            #1 Lighest != Oldest
            #2 Heaviest!= Oldest
            #  means MedWeight == Oldest
            next( getWeight(oldest) for oldest in [rae,lex,loy] if getAge(oldest) == old) == med and
            
            getWeight(lex) != heavy and #2
            getAge(lex) != new and #2

            getWeight(loy) != heavy #3
        ):
            print("Rae" , ageText[getAge(rae)],wtText[getWeight(rae)])
            print("Lex" , ageText[getAge(lex)],wtText[getWeight(lex)])
            print("Loy" , ageText[getAge(loy)],wtText[getWeight(loy)])

