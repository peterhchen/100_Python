
# Sky class contains object oc Cloud Class
class Mother:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Daughter (Mother):
    pass

x = Daughter ('Peter', 'Chen')
x.printname()