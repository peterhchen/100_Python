
# Sky class contains object oc Cloud Class
class Cloud:
    def __init__(self):
        self.firstname = 'Peter'
        self.lastname = 'Chen'
        self.clouds = 1

    def printname(self):
        print (self.clouds)

class Sky (Cloud):
    def __init__(self, number_of_clouds):
        self.clouds = [Cloud() for each in
                       range(number_of_clouds)] 

x = Sky (3)
x.printname()