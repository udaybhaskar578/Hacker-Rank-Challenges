#!/bin/python3
# Question : https://www.hackerrank.com/challenges/camelcase
# Time Complexity: O(n)
#!/bin/python3

import sys
s = input().strip()
x = 0
for c in s:
    if c.isupper():
        x = x+1   
print(x+1)