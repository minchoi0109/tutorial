class dog:
    pass

dog1 = dog()
dog2 = dog()
s = 1
print (type(dog1))
print(isinstance(dog2, dog))
print(isinstance(s, dog))

dog1.name = "a"
dog1.age = 10
dog2.name = "b"
dog2.age = 14

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.woofcount = 0

    def sayhi(self):
        print("hello, my name is", self.name, "and I am", self.age)

    def cry(self, times):
        self.woofcount += times
        print(f'{self.name} says: {"woof"*times} ({self.woofcount} woofs!)')

cat1 = cat("a", 1)
cat2 = cat("b", 2)
cat3 = cat("c",3)

print(cat3.name, cat3.age)
cat2.sayhi()
cat2.cry(10)

class tiger:
    def speak(self):
        print("wraaaaaaaa!")
tiger().speak()