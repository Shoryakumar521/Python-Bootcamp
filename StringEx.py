# Collection of chracter is called string.It is immutable.It is once create we can not reassign
# and remodified into same memory address space.

# Program-:

# To create a string
str ="amit"
print(str)

# To know the len of string
str ="amit"
n=len(str)
print(n)

# To put the space in every word 
str="core python is lang"
for i in str:
               print (i,end=" ")
print (" ")
for i in str[:: -1]:
        print(i,end=" ")

# To add two string
str ="shorya"
str2 ="tyagi"
str3 =str + str2
print(str3)

# Taking user input form string
str=input("enter a messgae: ")
sub =input("enter a word")
if sub in str:
        print(sub, "is found in str")
else:
        print(sub, "not found in str")

# Slicing in string
name="   shorya  kumar  "
print(name)
print(len(name))
rst=(name.rstrip())
print(rst)
Ist=(name.lstrip())
print(Ist)
print(len(Ist))
st=(name.strip())
print(st)
print(len(st))
      
# program to find the length of string by user input

str=input("enter a message")
sub =input("enter a sub string")
n=str.find(sub,0,len(str))
if n==-1:
               print(sub,"is not found in str")
else:
        print(sub,"is found in str",n+1)

 


