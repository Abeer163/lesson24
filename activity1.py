#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

s1 = {1,3,5,5,7,7}
print(s1)
s2 = {1,"abeer",1.5,1}
print(s2)
s3 = {1,2,3,4,3,2}
print(s3)
l1 = [1,2,3,2]
s4 = set(l1)
print(s4)
s5 = {0,1,3,4,5}
s5.remove(0)
print(s5)