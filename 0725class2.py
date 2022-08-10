class dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age
dog1= dog("dino", 10)
dog2 = dog1
print(dog2.name)
dog1.name = "s"
print(dog2.name)