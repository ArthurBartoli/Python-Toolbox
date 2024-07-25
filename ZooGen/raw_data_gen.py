import random
import pandas as pd
from datetime import datetime, timedelta

#TODO: Use the biome data to generate the animals 

##### Animals

def generate_animals(nb_animals, show_progress=True):
    species = ["Antelope", "Giraffe", "Lion", "Termite", "Suricate"
               "Elephant (Asian)", "Capybara", "Jaguar", "Red Ant", "Ant Eater",
               "Camel", "Gazelle", "Fennec", "Scorpion", "Gecko",
               "Deer", "Hare", "Wolf", "Beetle", "Mocking Jay",
               "Bison", "Wild Horse", "Coyote", "Cricket", "Swallow",
               "Capybara", "Hippopotamus", "Alligator", "Moskito", "Frog"]
    data = []
    i = 0

    if show_progress and i%10==0:
        print("Now at step {i} on {nb_animals}")
    for _ in range(nb_animals):
        this_species = random.choice(species)
        animal = {
            "id": _,
            "species": this_species,
            "age": age_from_species(this_species),
            "weight": weight_from_species(this_species),
            "habitat": habitat_from_species(this_species),
        }
        data.append(animal)
    return pd.DataFrame(data)

def age_from_species(species):
    '''Age is modeled from the mean in the wilds and the std from it.
    The lognorm is the best as it can be infered from normal characteristics
    but doesn't get negative and has a long tail, matching a real distribution.
    '''
    match species:
        case "Antelope":
            return random.lognormvariate(10, 3)
        case "Giraffe":
            return random.lognormvariate(15, 5)
        case "Lion":
            return random.lognormvariate(12, 3)
        case "Termite":
            return random.lognormvariate(1.5, 0.5)
        case "Suricate":
            return random.lognormvariate(6, 2)
        case "Elephant (Asian)":
            return random.lognormvariate(48, 10)
        case "Capybara":
            return random.lognormvariate(8, 2)
        case "Jaguar":
            return random.lognormvariate(12, 4)
        case "Red Ant":
            return random.lognormvariate(1, 0.5)
        case "Ant Eater":
            return random.lognormvariate(14, 3)
        case "Camel":
            return random.lognormvariate(40, 5)
        case "Gazelle":
            return random.lognormvariate(12, 3)
        case "Fennec":
            return random.lognormvariate(10, 2)
        case "Scorpion":
            return random.lognormvariate(6, 1)
        case "Gecko":
            return random.lognormvariate(6, 1)
        case "Deer":
            return random.lognormvariate(20, 5)
        case "Hare":
            return random.lognormvariate(9, 2)
        case "Wolf":
            return random.lognormvariate(10, 3)
        case "Beetle":
            return random.lognormvariate(1, 0.2)
        case "Mocking Jay":
            return random.lognormvariate(6, 2)
        case "Bison":
            return random.lognormvariate(20, 4)
        case "Wild Horse":
            return random.lognormvariate(25, 5)
        case "Coyote":
            return random.lognormvariate(10, 2)
        case "Cricket":
            return random.lognormvariate(1, 0.2)
        case "Swallow":
            return random.lognormvariate(4, 1)
        case "Hippopotamus":
            return random.lognormvariate(40, 5)
        case "Alligator":
            return random.lognormvariate(35, 8)
        case "Moskito":
            return random.lognormvariate(0.5, 0.1)
        case "Frog":
            return random.lognormvariate(10, 2)
    return int(0) 

def weight_from_species(species):
    match species:
        case "Antelope":
            return random.normalvariate(50, 0.1)
        case "Giraffe":
            return random.normalvariate(1200, 200)
        case "Lion":
            return random.normalvariate(190, 20)
        case "Termite":
            return random.normalvariate(0.3/1000, 0.01/1000) # Weight is in kg
        case "Suricate":
            return random.normalvariate(0.7, 0.1)
        case "Elephant (Asian)":
            return random.normalvariate(4000, 800)
        case "Capybara":
            return random.normalvariate(50, 10)
        case "Jaguar":
            return random.normalvariate(100, 20)
        case "Red Ant":
            return random.normalvariate(0.005/1000, 0.001/1000) # Weight is in kg
        case "Ant Eater":
            return random.normalvariate(40, 8)
        case "Camel":
            return random.normalvariate(600, 100)
        case "Gazelle":
            return random.normalvariate(35, 7)
        case "Fennec":
            return random.normalvariate(1.5, 0.3)
        case "Scorpion":
            return random.normalvariate(0.030, 0.005)
        case "Gecko":
            return random.normalvariate(0.1, 0.02)
        case "Deer":
            return random.normalvariate(150, 30)
        case "Hare":
            return random.normalvariate(3, 0.5)
        case "Wolf":
            return random.normalvariate(40, 8)
        case "Beetle":
            return random.normalvariate(2/1000, 0.4/1000) # Weight is in kg
        case "Mocking Jay":
            return random.normalvariate(0.02, 0.004)
        case "Bison":
            return random.normalvariate(900, 150)
        case "Wild Horse":
            return random.normalvariate(500, 100)
        case "Coyote":
            return random.normalvariate(12, 2)
        case "Cricket":
            return random.normalvariate(0.5/1000, 0.1/1000) # Weight is in kg
        case "Swallow":
            return random.normalvariate(0.018, 0.003)
        case "Hippopotamus":
            return random.normalvariate(1500, 300)
        case "Alligator":
            return random.normalvariate(250, 50)
        case "Moskito":
            return random.normalvariate(0.002/1000, 0.0004/1000) # Weight is in kg
        case "Frog":
            return random.normalvariate(4000, 800)
    return int(0)

def habitat_from_species(species):
    if species in ["Antelope", "Giraffe", "Lion", "Termite", "Suricate"]:
        return "Savannah"
    if species in ["Elephant (Asian)", "Jaguar", "Red Ant", "Ant Eater"]:
        return "Jungle"
    if species in ["Camel", "Gazelle", "Fennec", "Scorpion", "Gecko"]:
        return "Desert"
    if species in ["Deer", "Hare", "Wolf", "Beetle", "Mocking Jay"]:
        return "Forest"
    if species in ["Bison", "Wild Horse", "Coyote", "Cricket", "Swallow"]:
        return "Plains"
    if species in ["Hippopotamus", "Alligator", "Moskito", "Frog"]:
        return "Marshes"
    if species == "Capybara":
        return random.choice(["Marshes", "Jungle"])
    return "NA"

##### Biomes

def generate_biomes(nb_biomes):
    enclosure_types = ["Savannah", "Jungle", "Desert", "Forest", "Plains", "Marshes"]
    data = []
    for _ in range(nb_biomes):
        enclosure = {
            "id": _,
            "type": random.choice(enclosure_types),
            "size": round(random.uniform(100, 1000), 2),
            "location": f"Zone-{random.randint(1, 10)}",
        }
        data.append(enclosure)
    return pd.DataFrame(data)



# Exemple d'utilisation
animals_df = generate_animals(100)
enclosures_df = generate_biomes(20)

# Afficher les données générées
print(animals_df)
print(enclosures_df)

