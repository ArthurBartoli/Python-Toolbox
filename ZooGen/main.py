'''The goal of this project is to randomly generate a natural environment datascape
for training data analyst at extracting complex information in visual form. 
This is more complicated than it looks because it can only be a purely data driven
program, and not use that much objects. 
'''

import pandas as pd
import numpy as np 
from pprint import pprint

from raw_data_gen import *


grass = pd.DataFrame(np.random.randint(0, 60, size=(100, 1)), columns=["Grass height (cm)"]) 
zebras = pd.DataFrame(np.random.randint(0, 100, size=(10, 1)), columns=["Satiation"])



# for index, zebra in zebras.iterrows():
#     print("######## ", index)
#     satiation = zebra["Satiation"].item()
#     print("This zebras has a satiation of : ", satiation)

#     for index, grassnip in grass.iterrows():

#         satiation = zebra["Satiation"].item()
#         grass_height = grassnip["Grass height (cm)"].item()
#         print("It sees a grassnip, which is of length : ", grass_height)

#         if satiation <= 0:
#             print("* ZEBRA IS SATIATED")
#             print("But he wasn't hungry anymore")
#             break
#         elif satiation - grass_height < 0:
#             print("* GRASS IS TALLER THAN SATIATION")
#             eaten = grass_height - satiation
#             print("But it was a small satiation so he ate ", eaten)
#             zebra["Satiation"] = 0
#             grassnip["Grass height (cm)"] = grassnip["Grass height (cm)"] - eaten
#             print("Now there is a grassnip of length : ", grassnip["Grass height (cm)"])
#             print("And the zebra has a satiation of ", zebra["Satiation"])
#         elif grass_height == 0:
#             print("* GRASS HAS ALREADY BEEN EATEN")
#             print("Because it was eaten already...")
#             next
#         elif satiation - grass_height >= 0:
#             print("* ZEBRA EATS WHOLE GRASS")
#             zebra["Satiation"] = zebra["Satiation"] - grass_height 
#             grassnip["Grass height (cm)"] = 0
#             satiation = zebra["Satiation"].item()
#             print("So it ate it, and now it has a satiation of ", satiation)
#         else:
#             break
            
grass_before = grass.copy()


def process_zebra(zebra, grass):
    print("######## ", zebra.name)
    satiation = zebra["Satiation"]

    print("This zebra has a satiation of: ", satiation)

    if (grass["Grass height (cm)"] == 0).all() :
        print("But the grass was all gone...")
        return 

    for grass_index, grassnip in grass.iterrows():
        grass_height = grassnip["Grass height (cm)"]
        print("It sees a grassnip, which is of length: ", grass_height)

        if satiation <= 0:
            print("* ZEBRA IS SATIATED")
            print("But he wasn't hungry anymore")
            break
        elif satiation - grass_height < 0:
            print("* GRASS IS TALLER THAN SATIATION")
            eaten = grass_height - satiation
            print("But it was a small satiation so he ate ", eaten)
            zebra["Satiation"] = 0
            grassnip["Grass height (cm)"] = grassnip["Grass height (cm)"] - eaten
            print("Now there is a grassnip of length : ", grassnip["Grass height (cm)"])
            print("And the zebra has a satiation of ", zebra["Satiation"])
        elif grass_height == 0:
            print("* GRASS HAS ALREADY BEEN EATEN")
            print("Because it was eaten already...")
            continue
        elif satiation - grass_height >= 0:
            print("* ZEBRA EATS WHOLE GRASS")
            zebra["Satiation"] = zebra["Satiation"] - grass_height 
            grassnip["Grass height (cm)"] = 0
            satiation = zebra["Satiation"].item()
            print("So it ate it, and now it has a satiation of ", satiation)
        else:
            break

zebras.apply(process_zebra, axis=1, grass=grass)
pprint(grass_before)
pprint(zebras)
pprint(grass)