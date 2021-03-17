class Animal:
  def __init__(self,species_name,limbs,eyes,fur,sound):
    self.species_name = species_name
    self.limbs = limbs
    self.eyes = eyes
    self.fur = fur
    self.sound = sound
    
    if self.fur in ["yes","y"]:
      self.has_fur = "has"
    else:
      self.has_fur = "doesn\'t have"
  
  def describe(self):
    print(f"You have created a {self.species_name}!")
    print(f"\tIt has {self.limbs} limbs and {self.eyes} eyes.")
    print(f"\tIt {self.has_fur} fur.")
    print(f"\tA {self.species_name} goes \"{self.sound}\"!")
#====================
def create_animal():
  """ create an animal """
  print("-" * 30)
  species_name = input("What\'s its name?\n\t--> ")
  limbs = int(input("How many limbs does it have?\n\t--> "))
  eyes = int(input("How many eyes?\n\t--> "))
  fur = input("Does it have fur? [Yes] [No]\n\t--> ").lower()
  sound = input("What sound does it make?\n\t--> ")
  print("-" * 30)
  
  new_species = Animal(species_name,limbs,eyes,fur,sound)
  new_species.describe()
#====================
# MAIN PROGRAM
print("<-- Animal Species Creator -->")
print("Let's make a new animal species!!!")

create_animal()