# Question : https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot
#!/bin/python3

import sys

def isShortOfCandies(candies):
    if candies < 5:
        return True
    return False

def refillCandies(x):
    global candies
    candies = candies+x
    
    
def noOfCandiesRefilled(left,total,currTime,time):
    if currTime == time:
        return 0
    elif currTime <= time and left < 5:
        refillCandies(total-left)
        return (total-left)
    return 0

n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
c = list(map(int, input().strip().split(' ')))
candiesAdded = 0
candies = n
x =1
for candiesTaken in c:
    candies = candies - candiesTaken
    if isShortOfCandies(candies):
        candiesAdded = candiesAdded + noOfCandiesRefilled(candies,n,x,t)
        candies = n
    x = x+1
    
print(candiesAdded)
    
    
# your code goes here







