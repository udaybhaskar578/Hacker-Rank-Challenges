# Question : https://www.hackerrank.com/challenges/reduced-string
# Time Complexity :O(n)
# strinput = raw_input()
strinput = input()
strlist = list(strinput)
i=0
while i < len(strlist)-1:
    if strlist[i] == strlist[i+1]:
        del strlist[i]
        del strlist[i]
        i=0
        if len(strlist) == 0:
            print ("Empty String")
            break
    else:
        i = i+1
print ("".join(strlist))



