# Question : https://www.hackerrank.com/challenges/two-characters
#!/bin/python3

import sys
from collections import OrderedDict
from itertools import combinations

def CheckForT(s):
    c = list(s)
    i=0
    if len(c) == 2:
        if c[0] == c[1]:
            return False
        else:
            return True
    while i < len(c)-2:
        if c[i] == c[i+2] and c[i]!=c[i+1]:
            i = i+1
            continue
        elif c[i] == c[i+1]:
            return False  
        else:
            return False     
    return True
s_len = int(input())
s = input()
uniquekeys = ''.join(OrderedDict.fromkeys(s))
maxlen = 0
for pair in combinations(uniquekeys,2):
    substr = "".join(i for i in s if i in pair)
    if CheckForT(substr):
        maxlen = max(maxlen,len(substr))
print(maxlen)


#### Problem Testers Code
'''import sys
#sys.stdin=open("in","r")
n=int(raw_input())
s=raw_input()
assert s.isalpha()
ans=0
for i in range(0,26):
    for j in range(0,26):
        if i==j:
            continue
        p1 = i
        p2 = j
        flag = 1
        l = 0
        for c in s:
            if ord(c)-ord('a')!=p1 and ord(c)-ord('a')!=p2:
                continue
            if ord(c)-ord('a') == p1:
                l = l + 1
                p1,p2 = p2,p1
            else:
                flag = 0
        if flag == 1 and l>1:
            ans=max(ans,l)

print ans'''







