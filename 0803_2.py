class person:
    friends = []
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getfriends(self):
        return self.friends
    def addfriend(self, friend):
        self.friends.append(friend)
    def getfriendsnames(self):
        for friend in self.fiends:
            print(friend.getname())


maverick = person("maverick", 32)

friend1 = person("phoenix",30)
maverick.addfriend(friend1)
friend2 = person("bob",30)
maverick.addfriend(friend2)

