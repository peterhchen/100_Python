#!/usr/bin/env python
class Animal:
	says = 'Grrrr'

	def __init__(self):
		self.mobile = True

	def __str__(self):
		return self.says

	def __call__(self):
		print ("run")
		
class Human(Animal):
	says = 'Hi'

class Plant:
	says = 'Sunshine'

	def __init__(self):
		self.mobile = False

	def __call__(self):
		print ("flowering")
		
class Flower(Plant):
	says = 'Bloom'

#c) OK, but the HUmand and Flower order changed.
# class FlowerChild(Human, Flower):
#     says = 'Peace'
#     def __init__(self): 
#         Human.__init__(self)


#a) OK
class FlowerChild(Flower, Human):
    says = 'Peace'
    def __init__(self): 
        Human.__init__(self)

#class FlowerChild(Flower, Human):
    #NG
    #says = 'Peace'
    #d) NG
    # says = 'mobile'
    #c) OK
    # says = 'Peace'
    # def __init__(self): 
    #     Human.__init__(self)
    #b) NG
    #says = 'Peace' 
    #Human.__init__(self)

#print ('Flowerchild(): ', FlowerChild())
print ('FlowerChild().mobile:',FlowerChild().mobile)