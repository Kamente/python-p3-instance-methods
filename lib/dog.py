#!/usr/bin/env python3

class Dog: # class
    def bark (self): # instance method(bark is now an instance of Dogs)
        print("Woof!")
    def sit (self): 
        print("The dog is sitting.")
        
fido = Dog() # instance of Dog
fido.bark()
fido.sit()

snoop = Dog()
snoop.bark()
