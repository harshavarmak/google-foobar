# The Grandest Staircase Of Them All
# ==================================

# With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

# Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

# #
# ##
# 21

# When N = 4, you still only have 1 staircase choice:

# #
# #
# ##
# 31
 
# But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

# #
# #
# #
# ##
# 41

# #
# ##
# ##
# 32

# Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

# Languages
# =========

# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution(200)
# Output:
#     487067745

# Input:
# solution.solution(3)
# Output:
#     1

def solution(bricks):
    staircase = [[0] * bricks for i in range(bricks + 1)]
    staircase[0][0] = 1
    staircase[1][1] = 1
    staircase[2][2] = 1
    for i in range(bricks +1):
        for j in range(1, bricks):
            staircase[i][j] = staircase[i][j-1]
            if(i >= j):
                staircase[i][j] += staircase[i-j][j-1]
    return staircase[bricks][bricks-1]


sampleBricks = 200
testBricks1 = 200
testBricks2 = 3

import time

# s1 = time.time()
# print(solution2(sampleBricks))
# e1 = time.time()
s = time.time()
print(solution(sampleBricks))
e = time.time()
# print(solution(testBricks1))
# print(solution(testBricks2))


print('####TIME')
# print('S1', e1-s1)
print('S ', e-s)