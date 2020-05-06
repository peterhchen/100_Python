class PoliteList(list):
    def __str__(self):
        return """Here are your data:
%s
Thank you for asking.""" % (list.__str__(self))

#a) OK
numbers = PoliteList()
numbers += [3]

print ('numbers:', numbers)
#b) OK class A(list) ==> new style: list is a loewrcase object.
#c) OK
print ('PoliteList([1,2,3]):', PoliteList([1,2,3]))
#d) NG print PoliteList([1,2,3]) will crash