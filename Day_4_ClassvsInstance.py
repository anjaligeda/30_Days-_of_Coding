class Person:
    def __init__(self,initialAge):
        if (initialAge<0):
            print('Age is not valid,setting age to 0')
            self.age=0
        else:
            self.age=initialAge
    def amIOld(self):
        if (age<13):
            print('You are young')
        elif age>=13 and age<18:
            print('You are a teenager')
        else:
            print('You are old')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age += 1
        
        # Increment the age of the person in here

t = int(raw_input())
for i in range(0, t):
    age = int(raw_input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()        
    p.amIOld()
    print("")
    
'''#INPUT
4
-1
10
16
18

#OUPUT
Age is not valid,setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.'''
