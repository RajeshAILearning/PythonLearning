#Classes are user defined blueprint or prototype
#example caculator class has different operation methods sum, sub, mul, div
#Class contains methods, class variable, instance variable, Constructor..etc
#Keyword class

class Calc:
    #variable
    num = 100

    #Declare a method
    def GetData(self):
        print("I am now executing as method in class")

#to call this method come out of the class create object and call
#to create object in python we dont have any new operator just call the class name
obj = Calc()
obj.GetData()
print(obj.num)

#SELF
#Constructor -  it is method which is automatically called when you create object any class
#If no constructor is declared then default constructor is called
class Calcu:
    #variable
    num = 100
#Constructor
    # __init__ is the keyword to declare constructors in python 2 underscores at begining and end
    def __init__(self):
        print("I am automatically called when object is created")

    #Declare a method
    def GetData(self):
        print("I am now executing as method in class")

obj = Calcu()
obj.GetData()
print(obj.num)

#Class Varaibles -  defined immediately inside class,
# Class variables - Constant always no matter how many object we create
#Instance variables - Variables defined inside constructor are called instance variables
#Instance variables differs for each and every object

#How to send parameters from my created object to this class ?
class Calculator:

    num = 100
    #How many arguents we sending in a class that many arguments should be in constructor declaration
    #Self default added in python that is ignored, Self is nothing but objet created for this class
    #When we created object obj, this obj is passed as first argument self in the constructor
    #for this object we attaching 2 variables self.a self.b or self.firstnum self.secondnum
    def __init__(self, a, b): #once constructor catches that passed variable 2,3 store that 2,3 into your class
        self.firstnum = a #Self.a self.b this firstnum and secondnum are the instance variables
        self.secondnum = b
        #2 is stored in firstnum and 3 is stored in secondnum
        print("I am automatically called when object is created")

    def GetData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnum+self.secondnum+ Calculator.num #self.num or Calculator.num
        # class variable should be called by classname.variablename
        # In python you can never call variable with its name have to always attach self. or clasname.variablename

obj = Calculator(2,3) # these 2, 3 is passed to constructor that has to be catched as (self,2,3)
obj.GetData()
print(obj.Summation()) #105

obj = Calculator(4,5)
print(obj.Summation())

#Summary:
#Self keyword is mandatory for calling variable names into method
#Instance and class varaibles have whole different purpose
#Constructor name should be __init__
#new keyword is not required when you create object
