# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:29:06 2016

@author: hhosseinisafa
"""

count=0
while count<5:
    print (count)
    count +=1
else:
    print ("count value reached %d") 
print ("HHHHHHHHHHH") 
  
for i in range(1, 10):
    if(i%5==0):
        break
    print (i)
else:
    print ("this is not printed because for loop is terminated because of break but not due to fail in condition")
