# name
# avatar (profile picture)
# inventory

#def do_stuff():
# pass

class Character():
    # the "dunder init" method is the constructor
    def __init__(self, new_name, new_avatar):
        # 'self is the customary way to refer to 
        # In some other languages,they use 'this 
        self.name = new_name
        self.avatar = new_avatar
        self.inventory =[]
    #`someone=None`is a default argument
    # `None` is equivalent to `null` in other languages
    # this is an Object-Oriented Programming principle called Polymorphism
    # In Python, its called "Duck Typing"
    def greet(self, someone=None):
        if someone is not None:
            return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name,)
        else:
            return "Hello, I am %s. I am awesome." % (self.name,)



# Hero is a kind of Character
# Hero is a subclass of Character
# Hero inherits from Charcter
# Character is the superclass of hero
class Hero():
    pass