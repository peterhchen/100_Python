class Cloud:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def f (self):
        print ('Hello World:', self.name, self.age)

cloud = Cloud('silver', 20)
cloud.f()