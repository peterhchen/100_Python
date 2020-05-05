# Predict the output:
print('Predict the output:')
xlist=[1, 2, ['a', 'b']]
xlist_ref = xlist
import copy
xlist_deepcopy = copy.deepcopy (xlist)
xlist[0] = '***'
xlist[2][0] = '***'
print ('xlist:', xlist)
print ('xlist_ref:', xlist_ref)
print ('xlist_deepcopy:', xlist_deepcopy)

# More prediction
print()
print ('More Prediction:')
xdict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
xdict_ref = xdict
xdict_copy = xdict.copy()
import copy
xdict_deepcopy = copy.deepcopy (xdict)
xdict['a'] = 'ok'
xdict['b'][0] = 888
xdict['c'] = 'waterelon'
print ('xdict:', xdict)
print ('xdict_ref:', xdict_ref)
print ('xdict_copy:', xdict_copy)
print ('xdict_deepcopy:', xdict_deepcopy)

# Functional Programming
print()
print ('Functional Programming:')
print ('[str(x) for x in range (3)]:',[str(x) for x in range (3)])
print ('[[0] for x in range(3)]:', [[0] for x in range(3)])
print ('list(map(lambda x:x**2, range(5))):', list (map(lambda x:x**2, range(5))))
print ('[x for x in range(10) if not x % 2]:', [x for x in range(10) if not x % 2])