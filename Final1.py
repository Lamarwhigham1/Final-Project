'''
Created on Dec 2, 2017

@author: ITAUser
'''
numberlist=[];
Number=int(input("Enter a Number:"))

for i in range(1,Number + 1):
    if (Number%i==0):
        numberlist.append(i)
print(numberlist);
