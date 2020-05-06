class A(object):
    def __init__(self):
        print(self)

    def __call__ (call, something):
        print (something, "yourself!")

a = A() # call __init__
a('a')  # call __call__
#a()