# Question : https://www.hackerrank.com/challenges/caesar-cipher-1
#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
str = ""
if n == len(s):
    for c in s:
        if c.isalpha():
            a = 65 if c.isupper() else 97
            str+=(chr(a + ((ord(c)-a+k)%26)))
        else:
            str+=c  
    print(str)
    
