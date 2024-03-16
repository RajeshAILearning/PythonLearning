#Inheritance - without redefining properties and methods we can inherit from its parent class
#No object is required to call when you inherit
#pass the parent classname in the parenthesis and import
from OopsDemo import Calculator
#from Filenmae import keyword and classname

class Child(Calculator): # python treats this as inheritance
    num2 = 200;
    def __init__(self):
        Calculator.__init__(self,2,10)
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()
       # return self.num2 + self.num + self.Summation()# this num value comes from parent class also sum method called
       #Error because Parent class constructor is expecting 2 inputs also we have used those in summation method
       #SO logically we have to invoke that constructor with proper declared parameter inputs
       #call the parent class constructor from here from this class constructor

obj = Child()
print(obj.getCompleteData())
