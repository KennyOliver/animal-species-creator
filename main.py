#====================
from VividHues import Clr
class Animal:
  def __init__(self,species_name,limbs,eyes,fur,tail,sound):
    self.species_name = species_name
    self.limbs = limbs
    self.eyes = eyes
    self.fur = fur
    self.tail = tail
    self.sound = sound
    
    if self.fur in ["yes","y"]:
      self.has_fur = "has"
    else:
      self.has_fur = "doesn\'t have"
    
    if self.tail in ["yes","y"]:
      self.has_tail = "has"
    else:
      self.has_tail = "doesn\'t have"
  
  def describe(self):
    print(f"{Clr.BOLD}{Clr.GREEN}You have created a new animal species called \"{self.species_name}\"!{Clr.RESET}")
    print(f"{Clr.CYAN}\tIt has {self.limbs} limbs and {self.eyes} eyes.")
    print(f"\tIt {self.has_fur} fur.")
    print(f"\tIt {self.has_tail} a tail.")
    print(f"\tA {self.species_name} goes {Clr.LIME}\"{self.sound}\"{Clr.CYAN}!{Clr.RESET}")
#====================
def create_animal():
  """ create an animal """
  
  print(Clr.BLACK + "-" * 30 + Clr.RESET)
  species_name = input(Clr.YELLOW + "What will you call it?\n\t--> " + Clr.RESET)
  limbs = int(input(f"{Clr.YELLOW}How many limbs does this \"{species_name}\" have?\n\t--> {Clr.RESET}"))
  eyes = int(input(f"{Clr.YELLOW}How many eyes?\n\t--> {Clr.RESET}"))
  fur = input(f"{Clr.YELLOW}Does your \"{species_name}\" have fur? [Yes] [No]\n\t--> {Clr.RESET}").lower()
  tail = input(f"{Clr.YELLOW}A tail? [Yes] [No]\n\t--> {Clr.RESET}").lower()
  sound = input(f"{Clr.YELLOW}What sound would a \"{species_name}\" make?\n\t--> {Clr.RESET}")
  print(Clr.BLACK + "-" * 30 + Clr.RESET)
  
  new_species = Animal(species_name,limbs,eyes,fur,tail,sound)
  new_species.describe()
#====================
# MAIN PROGRAM
print("<-- Animal Species Creator -->")
print("Let's make a new animal species!!!")

create_animal()