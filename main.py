# from move import Move
# from pokemon import Pokemon
# from trainer import Trainer
# from item import Item

# # Define some moves
# thunderbolt = Move("Thunderbolt", "Electric", 90, 1.0, "special")
# tackle = Move("Tackle", "Normal", 40, 1.0, "physical")

# # Define some Pokémon
# pikachu = Pokemon("Pikachu", "Electric", 100, 55, 40, 50, 50, 90, 5, 0, [thunderbolt, tackle], False)
# bulbasaur = Pokemon("Bulbasaur", "Grass", 100, 49, 49, 65, 65, 45, 5, 0, [tackle], True)

# # Define a trainer
# ash = Trainer("Ash", [pikachu], [])

# # Catch a wild Pokémon
# ash.catch_pokemon(bulbasaur)

# # Battle another trainer
# misty = Trainer("Misty", [bulbasaur], [])
# ash.battle(misty)


from move import Move
from pokemon import Pokemon
from trainer import Trainer
from item import Item

# Define some moves
thunderbolt = Move("Thunderbolt", "Electric", 90, 1.0, "special")
tackle = Move("Tackle", "Normal", 40, 1.0, "physical")

# Define some Pokémon
pikachu = Pokemon("Pikachu", "Electric", 100, 55, 40, 50, 50, 90, 5, 0, [thunderbolt, tackle], False)
bulbasaur = Pokemon("Bulbasaur", "Grass", 100, 49, 49, 65, 65, 45, 5, 0, [tackle], True)

# Define a trainer
ash = Trainer("Ash", [pikachu], [])

# Catch a wild Pokémon
ash.catch_pokemon(bulbasaur)

# Battle another trainer
misty = Trainer("Misty", [bulbasaur], [])
ash.battle(misty)
