A = [1,2,3]
print (A) 
B = [1,2,3,1,2,3]
print (B) 


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
# prints out 1,2,3
for x in mylist:
    print (x)
    
    
A = [2,4,6,8]
B = [1,3,5,7]
C = A + B
print (C) 


M= A * 3


astring = "Hello world!"
Q= print (len (astring))
W= print (astring.index("o"))
E= print (astring.count("l"))
F= print (astring[3:7])



name = "John"
age = 23
if name == "John" and age == 23:
    print ("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print ("Your name is either John or Rick.")

    
    
# Prints out the numbers 0,1,2,3,4
for R in range (5) : # or range(5)
    print (R)
print ("#######")
# Prints out 3,4,5
for T in range (4, 6): # or range(3, 6)
    print (T)
print ("#######")
# Prints out 3,5,7
for Y in range (3, 8, 3): # or range(3, 8, 2)
    print (Y)
print ("#######")    
  
  
    
Count = 2
while Count < 7:
    print (Count)
    Count = Count+1  # This is the same as count = count + 1  
    #count += 1  # This is the same as count = count + 1    
print ("#######")        
    
    
    
# Prints out 0,1,2,3,4

count = 0
while True:
    print (count)
    count += 1
    if count >= 5:
        break
print ("HHHHHHHHHHH") 

# Prints out only odd numbers - 1,3,5,7,9
for U in range(10):
    # Check if x is even
    if U % 2 == 0:
        continue
    print (U) 
    
print ("MMMMMMMMMMMMM")  
 
 
 
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
