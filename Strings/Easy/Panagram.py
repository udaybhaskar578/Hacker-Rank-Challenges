#Question : https://www.hackerrank.com/challenges/pangrams?h_r=next-challenge&h_v=zen
s = input()
alphabets = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
calc=0
s = s.upper()
for c in alphabets:
    if c in s:
        calc = calc+1
    else:
        break
if calc == 26:
    print("pangram")
else:
    print("not pangram")


'''Other Solution
from string import ascii_lowercase
s = input().lower() # lowercase input
s = list(set(s)-set(' ')) # remove ' ' spaces
s = ''.join(sorted(s)) # joined the sorted list of unique charaters
if ascii_lowercase  == s:
    print("pangram")
else:
    print("not pangram")'''
        