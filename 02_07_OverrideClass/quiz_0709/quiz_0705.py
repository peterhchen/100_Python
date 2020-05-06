class A(object):
    pass

abc = 'a'
your_object = A();
#print ('is(your_object)', your_object is ))
print ('isinstance(your_object, A)', isinstance(your_object, A))
print ('your_object.__class__:', your_object.__class__)
print ('abc.__class__', abc.__class__)