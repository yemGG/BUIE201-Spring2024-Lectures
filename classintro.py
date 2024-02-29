x = 2
def f():
    y = 6
    print (y)

print (x)

class Apple:
    z = 13
    def g():
        pass

    f()

    class Table:
        pass

# Apple is called a class object
print (Apple.z)
Apple.g()

# For the class objects th following notation has a spesific meaning:
# "Create a new instance object"
myapple1 = Apple()
myapple2 = Apple()

print (myapple1.z)



