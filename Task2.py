
# 1. The lightest robot is newer than Rae.
# 2. The heaviest robot is newer than Lex.
# 3. Loy is not the heaviest robot.
# Find the age and weight of robots.


import itertools

ageText = ['newest','mid','oldest']
wtText = ['lighest','med','heaviest']
age = new,mid,old = [0,1,2]
wt = light,med,heavy= [0,1,2]

def isOldest_MediumWeight(*robots):
    for robot in robots:
        if(robot[0] == old and robot[1]==med):
            return True
    return False

num = [0,1,2]
shuffle = list(itertools.permutations(num)) 

# orderings = []
# for x,y,z in shuffle:
#     for a,b,c in shuffle:
#         orderings.append([[x,a],[y,b],[z,c]])

# import itertools
# num = [0,1,2]
# shuffle = list(itertools.permutations(num)) 

orderings = [list(zip(*p)) for p in itertools.product(shuffle, shuffle)]


for rae,lex,loy in orderings:  # [0] -> age / [1] -> weight
        if(
            rae[1] != light and #1
            rae[0] != new and #1

            isOldest_MediumWeight(rae,lex,loy) and 
            #1 Lighest != Oldest
            #2 Heaviest!= Oldest
            #  means MedWeight == Oldest

            lex[1] != heavy and #2
            lex[0] != new and #2

            loy[1] != heavy #3
        ):
            print("Rae" , ageText[rae[0]],wtText[rae[1]])
            print("Lex" , ageText[lex[0]],wtText[lex[1]])
            print("Loy" , ageText[loy[0]],wtText[loy[1]])

