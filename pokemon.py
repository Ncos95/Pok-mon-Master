class Pokemon:
  def __init__(self, name, level, pokemon_type, max_health,current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.pokemon_type = pokemon_type
    self.max_health = max_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out

  def __repr__(self):
    return "This " + self.name + " is level " + str(self.level) + " and type " + self.pokemon_type

  def lose_health(self, current_health, damage, name):
    print(name + " has lost " + damage + " health points! " + name + " now has " + current_health)

  def gain_health(self, current_health, heal_amount, name):
    print(name + " has gained " + heal_amount + " health points! " + name + " now has " + current_health)

  def knocked_out(self, name, is_knocked_out, current_health):
    if (current_health == 0):
      is_knocked_out == True
    print(name + " is knocked out!")
    if (name == is_knocked_out):
      Pokemon.attack == False

  def attack(self, pokemon_type, enemy_type, name, damage, attack_name):
    # Fire type Attacks
    if (pokemon_type == "Fire" and enemy_type == "Grass"):
      damage * 2
      print(name + " used " + attack_name + " and has dealt " + damage + " damage! This is super effective!")
    
    elif (pokemon_type == "Fire" and enemy_type == "Fire"):
      print(name + " used " + attack_name + " and has dealt " + damage + " damage!")

    elif (pokemon_type == "Fire" and enemy_type == "Water"):
      damage * 0.5
      print(name + " used " + attack_name + " and has dealt " + damage + " damage! This is not very effective.")

    # Water type attacks
    elif (pokemon_type == "Water" and enemy_type == "Fire"):
      damage * 2
      print(name + " used " + attack_name + " and has dealt " + damage + " damage! This is super effective!")
    
    elif (pokemon_type == "Water" and enemy_type == "Water"):
      print(name + " used " + attack_name + " and has dealt " + damage + " damage!")

    elif (pokemon_type == "Water" and enemy_type == "Grass"):
      damage * 0.5
      print(name + " used " + attack_name + " and has dealt " + damage + " damage! This is not very effective.")

    #Grass type attacks
    elif (pokemon_type == "Grass" and enemy_type == "Water"):
      damage * 2
      print(name + " used " + attack_name + " and has dealt " + damage + " damage! This is super effective!")
    
    elif (pokemon_type == "Grass" and enemy_type == "Grass"):
      print(name + " used " + attack_name + " and has dealt " + damage + " damage!")

    elif (pokemon_type == "Grass" and enemy_type == "Fire"):
      damage * 0.5
      print(name + " used " + attack_name + " and has dealt " + damage + " damage! This is not very effective.")
    else:
      print("An error has occured.")
     
class Trainer:
  def __init__(self, trainer_name, number_of_potions, potion_heal_amount, pokemon_collection, currently_active_pokemon):
    self.trainer_name = trainer_name
    self.pokemon_collection = pokemon_collection
    self.number_of_potions = number_of_potions
    self.potion_heal_amount = potion_heal_amount
    self.currently_active_pokemon = currently_active_pokemon

  def __repr__(self):
      return "Your trainer is called " + self.trainer_name + " and has " + str(self.number_of_potions) + " potions which heal " + str(self.potion_heal_amount) + " healthpoints and has these Pokemon: "
      for pokemon in self.pokemon_collection:
        print(pokemon_collection[pokemon])

  def use_potion(self, currently_active_pokemon, number_of_potions, name):
    if (number_of_potions == 0):
      print("You do not have any potions.")

    elif (currently_active_pokemon == Pokemon.max_health):
      print("This Pokemon is already at full health.")
      Trainer.use_potions == False
    else:
      Pokemon.gain_health(currently_active_pokemon)
      print(name + " has gained " + heal_amount + " health.")

  def attack_enemy_pokemon(self, currently_active_pokemon, enemy_pokemon, pokemon_type, enemy_type):
    print(Pokemon.attack())
    if (enemy_pokemon.is_knocked_out == True):
      attack_enemy_pokemon == False
      print("The enemy Pokemon has been knocked out!")


  def change_current_pokemon(self, pokemon_collection, currently_active_pokemon, name):
    if (Pokemon.name == currently_active_pokemon):
      print("This Pokemon is already selected")
    elif (Pokemon.name == is_knocked_out):
      change_current_pokemon == False
      print("This Pokemon is knocked out and cannot fight! Select another Pokemon")
    else:
      print("You have chosen " + Pokemon.name)

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", level, "Fire", 40, 20, False)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", level, "Water", 35, 15, False)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", level, "Grass", 35, 35, False)

a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(7)
e = Charmander()
f = Squirtle(2)

Trainer_Bob = Trainer("Bob", 4, 15, [a,b,c], a)
Trainer_Schmichael = Trainer("Schmichael", 4, 15, [d,e,f], d)

print(Trainer_Bob) 

print(Trainer_Schmichael)