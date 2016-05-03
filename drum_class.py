class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])
        
    def __repr__(self):
        return "bassist"

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
    def __repr__(self):
        return "guitarist"
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boom", "Badda", "Boom", "Boom", "Chhhh"])

    def count(self):
        print("One!", "Two!", "Three!", "Fo'!")
        
    def combust(self):
        print("BOOM!!! He spontaneously combusted!")
    
    def __repr__(self):
        return "drummer"
        
class Band():
    
    def __init__(self, members=[]):
        self.members = members
        
    def hire_people(self, musician):
        self.members.append(musician) 
        print("You're hired!", musician)
    
    def fire_people(self, musician):
        self.members.remove(musician)
        print("You're fired!", musician)
        
        
        
        
Spinal_Tap = Band()

drummer = Drummer()
guitarist = Guitarist()
bassist = Bassist()

Spinal_Tap.hire_people(drummer)
Spinal_Tap.hire_people(guitarist)

Spinal_Tap.fire_people(drummer)


drummer.count()    
guitarist.solo(5)