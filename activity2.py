#Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}
s1 = {1,2,2,3,4,4}
s2 = {1,3,5,5,7}
s3 = s1.intersection(s2)
print(s3)
s4 = {1,2,4,4,3}
s5  = s1.union(s4)
print(s5)
s6 = s1.difference(s2)
print(s6)
s7 = s1.symmetric_difference(s2)
print(s7)