from numpy import number


age=20
price=19.50 
Name="Kamal"
is_online=True
#print("Hello World"+age) #not possible



#name=input("What is  your name: ")
#print("Hello "+name) #It is Possible



#b_year=input("Enter your birth year: ")
#age=2022- int(b_year) #Type casting int()  float() bool() str()
#print(age)

#f=float(input("First: "))
#s=float(input("Second: "))
#sum=f+s

#print("Sum: "+str(sum))

# String on python is immutable------------------------------------------->

course='Python for Begineers' # string objects
#print(course.find('for'))
#print('for' in course)
a=course.upper() 
b=course.find('e')
#print(course.replace('for','4'))
#print(b)


#Arithmetic Operation------------------------------------------------>

#print(10 / 3) 
#print(10 // 3)  floor values
#print(10 % 3)
#print(10 * 3)
#print("Kamal " * 100000)
#print(10 ** 3)  10^3

#x=10
#x=x + 3 # x+=3
#x=(10 + 3) * 2
#print(x)

# Compare --------------------------------------------->
#x =  3>=2     > >= < <= == !=
#print(x)

#Logical Operator------------------------------------------>

price=25
#print(price > 10 and price < 30) -------> and or not
#print(not price > 10)


#IF stetments-------------------->

#temp= 20
#if temp > 30:
    #("It is a hot day")
#elif temp>20:
    #print("It is nice day") #(20,30]
#elif temp>10:
    #print("It is a bit cold")
#else:
    #print("It is cold day") # if we do not use else:
    

#weight = int(input("Weight: "))
#unit= input("(K)g or (L)bs: ")
#if unit.upper() == "K":
    #con = weight / 0.45
   # print("Weight in Lbs: "+str(con))
#else:
    #con = weight * 0.45
    #print("Weight in Kgs: "+ str(con))
    
    
    
    
    #Loop---------------------------------->
    #i=1
    #while i <=10: # i<=1000
        #print(i * "*")
        #i+=1
    
    #i=1    
    #for i in range(10):
        #print(i * "*")
        #i+=1
        
        
     
 #List------------------------------------------------------------>
names = ["kamal","Kumar","Rana","15","July"]    # 0 1 2 3 4 5 .... n ------> $$ <---------------- -1 -2 -3 -4 -5 -6 -7 ............-n
names[1]="Kr"
print(names[0:-3])   
print(names)

#List Method---------------------------------------------------------->
#numbers=[1,2,3,4,5]
#numbers.append(6)   $$ insert in only end
#numbers.insert(-2,"Hi")
#numbers.remove(4)
#numbers.clear()
#print(numbers)
#print(5 in numbers)
#print(len(numbers))


#for item in numbers:
    #print(item)
    
#i=0
#while i < len(numbers):
    #print(numbers[i])
    #i+=1

# range()
#numbers=range(5,10,2) # increment 2 upto previous of 10
#print(numbers)

#for number in mbers: # range(5,10,2)
    #print(number)

# Tuple in python is immutable----------------------------------------->
numbers=(1,[1,2,3,4],3,4,5)
#numbers[1]=10 $$ it can not be changed 
print(numbers)
    
    

    
    
    







