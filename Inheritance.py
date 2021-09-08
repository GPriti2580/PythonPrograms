class Animal:
    def speak (self):
        print("Animal speak")


class dog(Animal):
    def bark(self):
        print("dog barking")

d = dog ()
d.speak()
d.bark()
