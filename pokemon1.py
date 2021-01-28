class Pokemon:
  
  def __init__(self, name, typeof, level=5, xp = 0):
    self.name = name
    self.level = level
    self.type = typeof
    self.health = level * 5
    self.maximum_health = level * 5
    self.isknocked_out = False
    self.xp = xp
  def __repr__(self):
    return "{nom} is at level {level}. It is a {typeof} pokemon. Its remaining health is {health} out of {maximum_health}. XP = {exp}".format(level = self.level, nom = self.name, typeof = self.type, health = self.health, maximum_health = self.maximum_health, exp = self.xp)
  
  def lose_health (self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0
      self.knock_out()
    else:
      print("{nom} is hurt, it has now {helse} health.".format(nom = self.name, helse = self.health))
    
  
  def revive (self):
    self.isknocked_out = False
    print("{nom} is revived.".format(nom = self.name))

  def regain_health (self, gained):
    if self.health == 0:
      self.revive()
    self.health += gained
    
    if self.health > self.maximum_health:
      self.health = self.maximum_health
    print("Hurra!{nom} has now {helse} health.".format(nom = self.name, helse = self.health))
  
  def knock_out (self):
    print("Uh oh! {nom} is knocked out! :(".format(nom = self.name))
    self.isknocked_out = True
    
  
  def attack (self, other_pokemon):
    if self.isknocked_out == True:
      print(f"{self.name} is knocked out, it can't attack another pokémon.")
      return
    elif other_pokemon.isknocked_out == True:
      print(f"{other_pokemon.name} is already knocked out!")
      return
    
    if self.type == "Fire":
      if other_pokemon.type == "Fire":
        print("Both Pokemons are fire pokemons.")
        other_pokemon.lose_health(0.5)
        self.xp += 1
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
      elif other_pokemon.type == "Water":
        print("Your fire pokemon attacks a water pokemon.")
        self.xp += 1
        other_pokemon.lose_health(0.5)
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        
      elif other_pokemon.type == "Grass":
        print("Your fire pokemon attacks a grass pokemon.")
        other_pokemon.lose_health(2.0)
        self.xp += 1
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        
      
    elif self.type == "Water":
      if other_pokemon.type == "Water":
          print("Both Pokemons are water pokemons.")
          other_pokemon.lose_health(0.5)
          self.xp += 1
          if self.xp >= 7:
            self.level +=1
            print(f"{self.name}, has leveled up to {self.level}!")
            self.xp = 0
          
      elif other_pokemon.type == "Fire":
        print("Your water pokemon attacks a fire pokemon.")
        other_pokemon.lose_health(2.0)
        self.xp += 1
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        
      elif other_pokemon.type == "Grass":
       print("Your water pokemon attacks a grass pokemon.")
       other_pokemon.lose_health(0.5)
       self.xp += 1
       if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        
    
    elif self.type == "Grass":
      if other_pokemon.type == "Water":
        print("Your grass pokemon attacks a water pokemon.")
        other_pokemon.lose_health(2.0)
        self.xp += 1
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        
      elif other_pokemon.type == "Fire":
        print("Your grass pokemon attacks a fire pokemon.")
        other_pokemon.lose_health(0.5)
        self.xp += 1
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        
      elif other_pokemon.type == "Grass":
        print("Both Pokemons are grass pokemons.")
        other_pokemon.lose_health(0.5)
        self.xp += 1
        if self.xp >= 7:
          self.level +=1
          print(f"{self.name}, has leveled up to {self.level}!")
          self.xp = 0
        

class Trainer:
  
  def __init__(self, name, pokemons, potions_num):
    self.pokemons = pokemons
    self.name = name
    self.potions = potions_num
    self.current_pokemon = 0
  def __repr__(self):
    print (f"The trainer {self.name} has the following pokemons:")
    for pokemon in self.pokemons:
      print(pokemon)
    return "The active pokemon is {actpok}".format(actpok = self.pokemons[self.current_pokemon].name)

  def use_potion (self):
    if self.potions > 0:
      gained = self.pokemons[self.current_pokemon].maximum_health - self.pokemons[self.current_pokemon].health
      if gained == 0:
        print("Gulp! {active_pokemon} drunk a potion!".format(active_pokemon = self.pokemons[self.current_pokemon].name))
        print("{active_pokemon} had already full health! What a waste of potion!".format(active_pokemon = self.pokemons[self.current_pokemon].name))
      else:
        print("Gulp! {active_pokemon} drunk a potion!".format(active_pokemon = self.pokemons[self.current_pokemon].name))
        self.pokemons[self.current_pokemon].regain_health(gained)
     
      self.potions -= 1
    else:
      print("You have no potions left!")
    
  
  def attack_trainer (self, other_trainer):
    print(f"Your pokemon {self.pokemons[self.current_pokemon].name} attacked {other_trainer.name}'s pokemon {other_trainer.pokemons[other_trainer.current_pokemon].name}!")
    self.pokemons[self.current_pokemon].attack(other_trainer.pokemons[other_trainer.current_pokemon])
    
  
  def switch_pokemon (self, value):
    if value == self.current_pokemon:
      print("That was you pokémon to begin with!")
    elif value < 0 or value > len(self.pokemons)-1:
      print("Please choose a valid value!")
    else:
      self.current_pokemon = value
      print(f"Your new active pokémon is {self.pokemons[self.current_pokemon].name}.")
# Creating Four fire pokemons
charizard = Pokemon(name ="Charizard", typeof="Fire", level=7 )
houndoom = Pokemon(name = "Houndoom", typeof="Fire", level = 4)
camerupt = Pokemon(name = "Camerupt", typeof="Fire", level = 7)
chandelure = Pokemon(name = "Chandelure", typeof="Fire", level = 9)
# Creating Four water pokemons
psyduck = Pokemon(name = "Psyduck", typeof="Water", level = 6)
blastoise= Pokemon(name = "Blastoise", typeof="Water", level = 7)
wailord= Pokemon(name = "Wailord", typeof="Water", level =8)
octillery= Pokemon(name = "Octillery", typeof="Water", level =5) 
# Creating Four grass pokemons
venusaur = Pokemon(name = "Venusaur", typeof="Grass", level = 8)
victreebel = Pokemon(name = "Victreebel", typeof="Grass", level = 8)
wormadam = Pokemon(name = "Wormadam", typeof="Grass", level = 6)
shiinotic = Pokemon(name = "Shiinotic", typeof="Grass", level = 6) 

ashley = Trainer("Ashley", [shiinotic, venusaur, octillery, psyduck,charizard, camerupt], 4)

erika = Trainer("Erika", [victreebel, wormadam, blastoise, wailord, houndoom, chandelure], 3)
erika.switch_pokemon(2)
erika.attack_trainer(ashley)
ashley.use_potion()


