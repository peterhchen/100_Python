class Cloud(object):
    # def print(self):
    #     pass
    # def __print__(self):
    #     pass   
    def string(self):
        pass
    # def __str__(self):
    #     print (self)
    pass

cloud = Cloud()
the_cloud_string = "%s" % (cloud)
print ('the_cloud_string: ', the_cloud_string)
#print ('__print__(self)', __print__(self))
#print ('__str__(self): ', cloud)
print(cloud.string())