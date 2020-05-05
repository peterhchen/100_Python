def deco(func):
    def inner():
        print ('runner inner()')
    return inner
@deco
def target():
    print ("running target()")

# def decorator(t1):
#     print ('decorator():', t1)
#     return t1

# def target1():
#     print ('running target1()')

# target1 = decorator (target1)

target()
#print ('target():', target())
print ('target:', target)
