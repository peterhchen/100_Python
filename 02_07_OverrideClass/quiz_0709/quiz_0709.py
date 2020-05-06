Method Resolution Order :
Method Resolution Order(MRO) it denotes the way a programming language resolves a 
method or attribute. Python supports classes inheriting from other classes. 
The class being inherited is called the Parent or Superclass, while the class that 
inherits is called the Child or Subclass. In python, method resolution order defines 
the order in which the base classes are searched when executing a method. 
First, the method or attribute is searched within a class and then it follows 
the order we specified while inheriting. This order is also called Linearization of 
a class and set of rules are called MRO(Method Resolution Order). 
While inheriting from another class, the 
interpreter needs a way to resolve the methods that are being called via an instance.