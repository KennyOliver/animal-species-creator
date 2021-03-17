class Animal:
  def __init__(self,species_name,limbs,eyes,fur,sound):
    self.species_name = species_name
    self.limbs = limbs
    self.eyes = eyes
    self.fur = fur
    self.sound = sound
    
    if fur is True:
      self.has_fur = "Yes"
    else:
      self.has_fur = "No"
  
  def describe(self):
    print(f"I am a {self.species_name}. I have {self.limbs} limbs, {self.eyes} eyes.")
    print(f"Do I have fur? {self.has_fur}")
    print(f"A {self.species_name} goes {self.sound}!")
#====================
# MAIN PROGRAM
print("Let's make a new animal species!!!")

species_name = input("What's its name?\n\t--> ")
limbs = int(input("How many limbs does it have?\n\t--> "))
eyes = int(input("How many eyes\n\t--> "))
fur = bool(input("Does it have fur? [True] [False]\n\t--> "))
sound = input("What sound does it make?\n\t--> ")

new_species = Animal(species_name,limbs,eyes,fur,sound)
new_species.describe()