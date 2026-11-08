
import os
import time
from random import randint
from sys import exit
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class Savanna_Animal:
    def __init__(self, name, age, description,endangered_status):
        self.name = name
        self.age = age
        self.description = description
        self.status = endangered_status
Black_Rhinoceroes = Savanna_Animal("Jabari", 19, r"""
Scientific Name:
   Diceros bicornis
Weight:
   800 - 1,400 kg (1,750 - 3,100 lbs)
Height:
   1.4 - 1.8 m (4.5 - 6 ft) at shoulder
Skin Color:
   Dark gray / brownish-gray (not black)
Horns:
   2 keratin horns (front horn up to 60+ cm)
Diet:
   Folivorous browser (twigs, leaves, shrubs)
Habitat:
   Tropical/subtropical grasslands, savannas, shrublands
Lifespan:
   35 - 50 years""", 
"Critically Endangered (IUCN Red List)")
def see_rhino():
    while True:
        Clear()
        print(RHINO)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the Rhino...')
            time.sleep(0.5)
            print('It stares...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Black_Rhinoceroes.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Black_Rhinoceroes.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Black_Rhinoceroes.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Black_Rhinoceroes.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Ocelot = Savanna_Animal("Copan", 5, 
r"""Scientific Name:
    Leopardus pardalis.
Physical Specs: 
    Weighs 18-34 lbs (8-15 kg); 
    features a distinctive coat of chain-like spots, rosettes, and stripes over tawny fur.
Habitat: 
    Adaptable but prefers dense thornscrub or tropical forest cover.
Diet:
    it is an opportunistic solitary carnivore hunting small rodents, birds, and reptiles.
Behavior: 
    Highly adept climber and swimmer; primarily crepuscular and nocturnal.
Life Span:
    7 - 13 years""",
 "Listed as Least Concern globally, but critically endangered in the United States IUCN Red List.")
def see_ocelot():
    while True:
        Clear()
        print(OCELOT)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the ocelot...')
            time.sleep(0.5)
            print('The ocelot admires you back...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Ocelot.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Ocelot.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Ocelot.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Ocelot.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Painted_Wolf = Savanna_Animal("Splotch", 4, r"""
Scientific Name:
   Lycaon pictus
Weight:
   20 to 27 kg (44 to 60 lbs).
Appearance:
   Unique black, yellow, and white patchwork coat, large rounded ears, and a white-tipped tail.
Behavior:
   Nomadic, highly cooperative pack hunter relying on high-stamina endurance running.
Efficiency:
   Achieves a phenomenal 80% hunting success rate through intense social teamwork.
Life Span:
   10 - 12 years""",
"Globally classified as Endangered on the IUCN Red List")
def see_wolf():
    while True:
        Clear()
        print(PAINTED_WOLF)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the Wolf...')
            time.sleep(0.5)
            print('It looks back with a silly look...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Painted_Wolf.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Painted_Wolf.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Painted_Wolf.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Painted_Wolf.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Pangolin = Savanna_Animal("Kaiju", 15, 
r"""Scientific Name
   Family Manidae 
Weight
   1.6 to 33 kg (3.5 to 73 lbs), varying drastically by species
Height / Length
   30 to 100 cm (12 to 39 in) head-to-tail
Skin / Scale Color
   Pale olive, dark brown, yellowish-brown, or dark gray-brown
Scales
   Overlapping protective armor made of keratin, covering the entire body except the underside
Diet
   Myrmecophage (highly specialized; strictly ants and termites)
Habitat
   Tropical/subtropical forests, dry woodlands, savannas, and grasslands
Lifespan
   Up to 20 years in the wild (rarely survives long in captivity)""",
"Ranging from Vulnerable to Critically Endangered across all 8 species (IUCN Red List)")
def see_pangolin():
    while True:
        Clear()
        print(PANGOLIN)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the pangolin...')
            time.sleep(0.5)
            print('The pangolin rolls into a ball as if it is scared of you...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Pangolin.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"he is {Pangolin.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Pangolin.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Pangolin.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue

class Forest_Animal:
    def __init__(self, name, age, description,endangered_status):
        self.name = name
        self.age = age
        self.description = description
        self.status = endangered_status
Lynx = Forest_Animal("Baku", 13, 
r"""
Scientific name:
   The Eurasian lynx (Lynx lynx), Canada lynx (Lynx canadensis), Iberian lynx (Lynx pardinus), and bobcat (Lynx rufus).
Physical Traits:
   Medium-sized wildcat easily recognized by its iconic black ear tufts, 
   flared facial ruffs, a short "bobbed" tail with a black tip, and disproportionately large, 
   heavily furred paws that act as natural snowshoes.
Habitat & Range:
   Solitary and nocturnal hunters native to the dense boreal forests and mountainous regions across North America, Europe, and Asia.
Weight: 
   Typically ranges from 22 to 44 lbs (10 to 20 kg), though this varies significantly by species (the Eurasian lynx can exceed 65 lbs, while the Canada lynx averages 18 to 30 lbs).
Lifespan:
   Ranges from 7 to 17 years in the wild, but can extend up to 20-24 years in captivity.
Diet: 
   Strictly carnivorous apex predators that rely heavily on small mammals, 
   with a specialized evolutionary dependence on lagomorphs like the snowshoe hare.
""", "Iberian Lynx: Vulnerable, Canada Lynx: Least Concern, Eurasian Lynx: Least Concern, Lynx Lynx: Least Concern. IUCN Status")
def see_lynx():
     while True:
        Clear()
        print(LYNX)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the lynx...')
            time.sleep(0.5)
            print('The lynx quietly hisses...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Lynx.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Lynx.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Lynx.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Lynx.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Capybara = Forest_Animal("Andie", 2, 
r"""
Scientific Name:
   Hydrochoerus hydrochaeris
Nature:
   A semi-aquatic mammal native to South America and holds the title of the world's largest living rodent.
Physical Characteristics: 
   Features a heavy, barrel-shaped body, blunt snout, reddish-brown fur, and partially webbed feet highly adapted for swimming.
Weight: 
   Ranging between 77 and 146 lbs (35 to 66 kg).
Lifespan: 
   Averages 7-10 years in the wild and can reach up to 12 years in captivity.
Behavior: 
   Highly social, gentle, and herd-dwelling animals that thrive in wetlands, marshes, and dense forests near water sources.""", "Least Concern on the IUCN Red List.")
def see_capybara():
     while True:
        Clear()
        print(CAPYBARA)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the capybara...')
            time.sleep(0.5)
            print('The capybara is just straight chillin...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Capybara.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Capybara.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Capybara.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Capybara.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Silverback_Gorilla = Forest_Animal("Titan", 11,
r"""
Scientific Name: 
   Gorilla gorilla (Western Gorilla) or Gorilla beringei (Eastern Gorilla).
Role: 
   Mature, dominant male gorilla that leads, protects, and navigates a social group.
Distinct Feature: 
   A saddle of silver-gray fur across the back and shoulders, developing around 12 to 13 years of age.
Average Weight: 
   136 - 227 kg (300 - 500 lbs).
Average Lifespan: 
   35 - 40 years in the wild, and up to 50+ years in captivity.""", "Almost all species of gorrila are critiacally endangered, IUCN status list.")
def see_gorilla():
     while True:
        Clear()
        print(SILVERBACK_GORILLA)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the silverback...')
            time.sleep(0.5)
            print('The gorilla looks off into the distance...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Silverback_Gorilla.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Silverback_Gorilla.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Silverback_Gorilla.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Silverback_Gorilla.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Wolverine = Forest_Animal("Rogue", 4,
r"""
Scientific Name: 
   Gulo gulo, meaning "glutton" in Latin.
Average Weight: 
   17 to 40 lbs (8 to 18 kg), with males being significantly larger than females.
Average Life Span: 
   7 to 10 years in the wild, though they can reach up to 15 years in captivity.
Physical Adaptations: 
   Possess thick, frost-resistant fur, large snowshoe-like paws, and a specialized molar rotated 90 degrees for crushing frozen meat and bone.
Habitat & Range: 
   Inhabits arctic, subarctic, and alpine regions across North America, Europe, and Asia.
Behavior: 
   Renowned as solitary, highly territorial, and incredibly strong apex scavengers and hunters capable of taking down prey many times their size.""", "Least Concern IUCN status.")
def see_wolverine():
     while True:
        Clear()
        print(WOLVERINE)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the wolverine...')
            time.sleep(0.5)
            print("The wolverine looks at you and it feels as if it wants to say 'Im not from marvel'...")
            time.sleep(2)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Wolverine.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Wolverine.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Wolverine.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Wolverine.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Jaguar = Forest_Animal("Ozzy", 7, 
r"""
Scientific Name:
   Panthera onca
Physical Profile: 
   Compact, muscular build with a tawny coat covered in "rosettes" (spots with central dots) for camouflage.
Distinct Behavior: 
   An adept swimmer and climber that kills prey by biting directly through the skull to pierce the brain, rather than suffocating the neck.
Habitat Range: 
   Extends from the southwestern United States and Mexico, through Central America, down to Paraguay and northern Argentina.
Average Weight: 
   56-96 kg (123-212 lbs), with large males occasionally reaching up to 158 kg (348 lbs).
Average Lifespan:
   12-15 years in the wild; can exceed 20 years in captivity.""", "Near Threatened on the IUCN Red List.")
def see_jaguar():
     while True:
        Clear()
        print(JAGUAR)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the jaguar...')
            time.sleep(0.5)
            print('The jaguar dances...?')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Jaguar.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Jaguar.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Jaguar.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Jaguar.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue

class Reptile_House_Animal:
    def __init__(self, name, age, description,endangered_status):
        self.name = name
        self.age = age
        self.description = description
        self.status = endangered_status
Indian_Gharial = Reptile_House_Animal("Winston", 22, #male
r"""
Scientific Name:
   Gavialis gangeticus
Original Range: 
   Native to the northern part of the Indian Subcontinent, 
   primarily found today in deep, fast-flowing rivers of northern India and Nepal 
   (historic ranges included Pakistan, Bhutan, and Myanmar).
Description:
   A unique crocodilian easily identified by its long, 
   extremely thin snout specialized for catching fish.
Avg Weight: 
   160-250 kg (350-550 lbs)
Avg Life Span:
   40-50 years""","IUCN Status: Critically Endangered")
def see_indian_gharial():
     while True:
        Clear()
        print(INDIAN_GHARIAL)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the crocodile...')
            time.sleep(0.5)
            print('The crocodile glares back with an intense feeling...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Indian_Gharial.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Indian_Gharial.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Indian_Gharial.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Indian_Gharial.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Axolotl = Reptile_House_Animal("Pip", 4, # female
r"""
Scientific Name: 
   Ambystoma mexicanum
Original Range: 
   Endemic exclusively to the high-altitude lake 
   complex of Xochimilco near Mexico City, Mexico.
Description: 
   A permanently aquatic salamander famous for its neotenic traits 
   (retaining its larval gills into adulthood) and incredible regenerative capabilities.
Avg Weight: 
   60-220 g (2-8 oz)
Avg Life Span: 
   10-15 years""", "IUCN Status: Critically Endangered") 
def see_axolotl():
     while True:
        Clear()
        print(AXOLOTL)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the axolotl...')
            time.sleep(0.5)
            print('The axolotl looks excited to see you...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Axolotl.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Axolotl.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Axolotl.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Axolotl.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Jerboa = Reptile_House_Animal("Bounce", 1, # male
r"""
Scientific Name: 
   Family Dipodidae (Multiple species)
Original Range: 
   Widely distributed across the hot deserts and arid steppes of North Africa, 
   the Middle East, and Central Asia up to northern China.
Description: 
   A small, hopping desert rodent resembling a tiny kangaroo, 
   featuring long hind legs and a very long tufted tail used for balance.
Avg Weight: 
   20-50 g (0.7-1.8 oz)
Avg Life Span: 
   2-4 years""","IUCN Status: Species-dependent (mostly Least Concern / Data Deficient)")
def see_jerboa():
     while True:
        Clear()
        print(JERBOA)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the jeroboa...')
            time.sleep(0.5)
            print('The jerboa hops up and down...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Jerboa.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Jerboa.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Jerboa.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Jerboa.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Crested_Newt = Reptile_House_Animal("Finley", 5, # male
r"""
Scientific Name: 
   Triturus dobrogicus
Original Range: 
   Native to Europe, specifically restricted to the Danube River basin and its tributaries 
   across countries like Austria, Hungary, Serbia, Romania, and Ukraine.
Description: 
   An amphibious newt native to Central and Eastern Europe, featuring a distinct,
    jagged dorsal crest along the backs of breeding males.
Avg Weight: 
   7-12 g (0.2-0.4 oz)
Avg Life Span: 
   8-12 years""","IUCN Status: Near Threatened")
def see_newt():
     while True:
        Clear()
        print(CRESTED_NEWT)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the crested newt...')
            time.sleep(0.5)
            print('The newt shows off his crest...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Crested_Newt.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Crested_Newt.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Crested_Newt.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Crested_Newt.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Amazon_Mata_Mata = Reptile_House_Animal("Moss", 14, #female
r"""
Scientific Name: 
   Chelus fimbriata
Original Range: 
   Native to the slow-moving freshwater basins of Northern South America,
   covering the Amazon and Orinoco basins (including Brazil, Peru, Colombia, Venezuela, and the Guianas).
Description: 
   A highly unique freshwater turtle with a flat, triangular head,
    bumpy fringed skin, and a shell resembling a piece of bark or 
    leaf litter for perfect camouflage.
Avg Weight: 
   15 kg (33 lbs)
Avg Life Span: 
   15-30 years""","IUCN Status: Least Concern")
def see_mata():
     while True:
        Clear()
        print(MATA_MATA)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the mata mata...')
            time.sleep(0.5)
            print('The mata mata snaps at you...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Amazon_Mata_Mata.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Amazon_Mata_Mata.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Amazon_Mata_Mata.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Amazon_Mata_Mata.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Worm_lizard = Reptile_House_Animal("Monty", 3, #Male
r"""
Scientific Name: 
   Suborder Amphisbaenia (Multiple species)
Original Range: 
   Found natively across South America, the Caribbean, Sub-Saharan Africa, 
   the Middle East, and parts of Southern Europe and Florida.
Description: 
   A legless, burrowing reptile belonging to the amphisbaenian group, 
   closely related to lizards and snakes but adapted for an underground lifestyle.
Avg Weight: 
   10-50 g (0.3-1.7 oz)
Avg Life Span:
   5-10 years""","IUCN Status: Species-dependent (mostly Least Concern)")
def see_worm_lizard():
     while True:
        Clear()
        print(WORM_LIZARD)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the worm lizard...')
            time.sleep(0.5)
            print('The worm lizard slithers around...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Worm_lizard.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Worm_lizard.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Worm_lizard.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Worm_lizard.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Arabian_Sand_Boa = Reptile_House_Animal("Sandy", 7, # female
r"""
Scientific Name:
   Eryx jayakari
Original Range: 
   Endemic to the arid regions of the Arabian Peninsula, 
   spanning Saudi Arabia, Yemen, Oman, and the United Arab Emirates.
Description: 
   A small, non-venomous constrictor fully adapted to desert life, 
   with eyes placed flat on top of its head to see above the sand while submerged.
Avg Weight: 
   100-300 g (3.5-10.5 oz)
Avg Life Span: 
   15-20 years""","IUCN Status: Least Concern")
def see_sand_boa():
     while True:
        Clear()
        print(SAND_BOA)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the sand boa...')
            time.sleep(0.5)
            print('The sand boa looks back...but you can not tell which eye is looking...')
            time.sleep(1.75)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Arabian_Sand_Boa.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Arabian_Sand_Boa.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Arabian_Sand_Boa.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Arabian_Sand_Boa.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Burmese_Python = Reptile_House_Animal("Julius", 11, #male
r"""
Scientific Name: 
   Python bivittatus
Original Range: 
   Native to the tropical forests and marshes of Southeast Asia, including Myanmar, Thailand, 
   Vietnam, and parts of southern China (though famously established as an invasive species in Florida, USA).
Description: 
   One of the largest species of snakes in the world, 
   recognizable by its beautiful dark-blotched coloration 
   pattern and powerful constricting capabilities.
Avg Weight: 
   40-90 kg (90-200 lbs)
Avg Life Span: 
   20-25 years""", "IUCN Status: Vulnerable")
def see_python():
     while True:
        Clear()
        print(BURMESE_PYTHON)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the python...')
            time.sleep(0.5)
            print('The python has a murderous intent in his eyes...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Burmese_Python.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Burmese_Python.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Burmese_Python.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Burmese_Python.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Mountain_Chicken = Reptile_House_Animal("Nugget", 6, #female
r"""
Scientific Name:
   Leptodactylus fallax
Original Range:    
   Endemic to the Caribbean, historically found on many islands 
   but now restricted strictly to the islands of Dominica and Montserrat.
Description:
   Despite the deceptive name, this is actually a critically endangered giant frog 
   native to Caribbean islands, named because its meat traditionally tasted like chicken.
Avg Weight: 
   600-1,000 g (1.3-2.2 lbs)
Avg Life Span: 
   10-12 years""","IUCN Status: Critically Endangered")
def see_mountain_chicken():
     while True:
        Clear()
        print(MOUNTAIN_CHICKEN)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the frog...')
            time.sleep(0.5)
            print('The thinks you look like a chicken...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Mountain_Chicken.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Mountain_Chicken.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Mountain_Chicken.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Axolotl.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Jackson_Chameleon = Reptile_House_Animal("Bowie", 2, #male
r"""
Scientific Name: 
   Trioceros jacksonii
Original Range: 
   Native to the montane regions and woodlands of East Africa,
   primarily Kenya and Tanzania (though introduced populations thrive in Hawaii).
Description: 
   A distinctive tree-dwelling lizard native to East Africa where adult males exhibit 
   three prominent prehistoric-looking horns on the front of their head.
Avg Weight: 
   80-150 g (2.8-5.3 oz)
Avg Life Span:
   5-10 years""", "IUCN Status: Least Concern")
def see_chameleon():
     while True:
        Clear()
        print(CHAMELEON)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the chameleon...')
            time.sleep(0.5)
            print('The chameleon taps his horns on the glass...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Jackson_Chameleon.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Jackson_Chameleon.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Jackson_Chameleon.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Jackson_Chameleon.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Snake_Necked_Turtle = Reptile_House_Animal("Noodles", 28, #female
r"""
Scientific Name: 
   Family Chelidae (Multiple species, e.g., Chelodina longicollis)
Original Range: 
   Depending on the specific genus, they are entirely native to 
   freshwater systems across Australia, New Guinea, and parts of South America.
Description: 
   A freshwater turtle named for its extraordinarily elongated neck, which it 
   cannot retract straight back into its shell, bending it sideways instead.
 Avg Weight:
   1-3 kg (2.2-6.6 lbs)
Avg Life Span: 
   30-40 years""","IUCN Status: Species-dependent (ranging from Near Threatened to Critically Endangered)")
def see_snake_turtle():
     while True:
        Clear()
        print(SNAKE_NECKED_TURTLE)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the turtle...')
            time.sleep(0.5)
            print('The turtle wiggles her head around...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Snake_Necked_Turtle.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Snake_Necked_Turtle.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Snake_Necked_Turtle.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Snake_Necked_Turtle.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue

class Aquarium_Animal:
    def __init__(self, name, age, description,endangered_status):
        self.name = name
        self.age = age
        self.description = description
        self.status = endangered_status
Manta_Ray = Aquarium_Animal("Barnaby",14, #male
r"""
Scientific Name: 
   Mobula birostris
Description: 
   A massive, intelligent filter-feeding ray that glides using large pectoral fins and uses cephalic flaps to channel plankton into its mouth.
Origin Range: 
   Worldwide in tropical, subtropical, and temperate oceans.
Avg Weight: 
   1,200 - 1,400 kg
Avg Lifespan:
   ~40 years""",
"IUCN Status: Endangered")
def see_manta_ray():
     while True:
        Clear()
        print(MANTA_RAY)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the manta...')
            time.sleep(0.5)
            print('He majestically swims around...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Manta_Ray.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Manta_Ray.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Manta_Ray.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Manta_Ray.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Lamprey = Aquarium_Animal("Penelope", 4, # female
r"""
Scientific Name: 
   Petromyzon marinus
Description: 
   A jawless, primitive parasitic fish equipped with a tooth-lined, 
   funnel-like sucking mouth used to bore into host fish and drink fluids.
Origin Range: 
   Northern and Western Atlantic Ocean; invasive in the North American Great Lakes.
Avg Weight: 
   0.5 - 1.0 kg
Avg Lifespan: 
    5 - 9 years""",
"IUCN Status: Least Concern")
def see_lamprey():
     while True:
        Clear()
        print(LAMPREY)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the lamprey...')
            time.sleep(0.5)
            print('She flashes her teeth at you...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Lamprey.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Lamprey.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Lamprey.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Lamprey.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Bichir = Aquarium_Animal("Gunther", 11, # male
r"""
Scientific Name: 
   Polypterus senegalus
Description: 
   An elongated, prehistoric freshwater fish covered in heavy ganoid scales, 
   featuring a modified lung-like swim bladder to breathe atmospheric air.
Origin Range: 
   Tropical Africa, including the Nile, Congo, and Chad river basins.
Avg Weight: 
   0.2 - 0.4 kg
Avg Lifespan: 
   15 - 30 years""","IUCN Status: Least Concern")
def see_bichir():
     while True:
        Clear()
        print(BICHIR)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the birchir...')
            time.sleep(0.5)
            print('He swims behind some rocks...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Bichir.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Bichir.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Bichir.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Bichir.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Pelican_Eel = Aquarium_Animal("Zephyr", 7, # No gender
r"""
Scientific Name: 
   Eurypharynx pelecanoides
Description: 
   A deep-sea eel recognizable by an enormous, loosely-hinged jaw and expandable pouch that allows it to swallow prey much larger than itself.
   Does not develop a distinct biological sex or sexual organs until the final phase of its life.
Origin Range: 
   Worldwide temperate and tropical oceans at abyssal depths (500 to 3,000 meters).
Avg Weight: 
   0.1 - 0.3 kg
Avg Lifespan: 
   up to 85+ years""","IUCN Status: Least Concern")
def see_pelican_eel():
     while True:
        Clear()
        print(PELICAN_EEL)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the eel...')
            time.sleep(0.5)
            print('It looks ready to swallow you whole...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"It's name is {Pelican_Eel.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"It is {Pelican_Eel.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Pelican_Eel.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Pelican_Eel.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Blue_Dragon = Aquarium_Animal("Cleo", 6, # Hermaphrodite
r"""
Scientific Name: 
   Glaucus atlanticus
Description: 
   A small, pelagic nudibranch (sea slug) that floats upside down on the surface tension of the ocean, 
   feeding on and weaponizing the stinging cells of venomous siphonophores.
   Simultaneous hermaphrodites, meaning each individual possesses both functional male and female reproductive organs.
Origin Range:
   Cosmopolitan across tropical and temperate pelagic waters.
Avg Weight: 
   0.003 - 0.004 kg (3-4 grams)
Avg Lifespan: 
   1 month to 1 year""", "IUCN Status: Not Evaluated")
def see_blue_dragon():
     while True:
        Clear()
        print(BLUE_DRAGON)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the blue dragon...')
            time.sleep(0.5)
            print("It slightly wiggles...")
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"It's name is {Blue_Dragon.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"It is {Blue_Dragon.age} months old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Blue_Dragon.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Blue_Dragon.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Sunfish = Aquarium_Animal("Wally", 19, # male
r"""
Scientific Name: 
   Mola mola
Description: 
   One of the heaviest bony fish alive, known for its distinct horizontally flattened,
   tailless disc shape and a diet primarily consisting of jellyfish.
Origin Range: 
   Global tropical and temperate marine waters.
Avg Weight: 
   247 - 1,000 kg
Avg Lifespan: 
   20 - 23 years""", "IUCN Status: Vulnerable")
def see_sunfish():
     while True:
        Clear()
        print(SUNFISH)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the sunfish...')
            time.sleep(0.5)
            print('He swims into the glass...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Sunfish.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Sunfish.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Sunfish.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Sunfish.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Giant_Isopod = Aquarium_Animal("Bertha", 32, # female
r"""
Scientific Name: 
   Bathynomus giganteus
Description:
   A massive, bottom-dwelling scavenging crustacean exhibiting deep-sea gigantism, protected by a rigid, overlapping calcareous exoskeleton.
Origin Range: 
   Deep, cold waters of the Atlantic, Pacific, and Indian Oceans.
Avg Weight:
   1.0 - 1.7 kg
Avg Lifespan: 
   40 - 60 years""","IUCN Status: Not Evaluated")
def see_giant_isopod():
     while True:
        Clear()
        print(GIANT_ISOPOD)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the isopod...')
            time.sleep(0.5)
            print('She wiggles her claws...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Giant_Isopod.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Giant_Isopod.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Giant_Isopod.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Giant_Isopod.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue

class Bird_House_Animal:
    def __init__(self, name, age, description,endangered_status):
        self.name = name
        self.age = age
        self.description = description
        self.status = endangered_status
Shoebill = Bird_House_Animal("Diablo",22, # male
r"""
Scientific Name:
   Balaeniceps rex
Origin Range:
   East Africa (Swamps)
Description:
   A massive, prehistoric-looking wading bird defined by its enormous, 
   clog-shaped bill used to hunt lungfish. 
   They are solitary and known for standing completely motionless for long periods.
Avg Weight:
   5 kg (11 lbs)
Avg Lifespan:
   35-50 years
""","IUCN Status: Vulnerable")
def see_shoebill():
     while True:
        Clear()
        print(SHOEBILL)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the shoebill...')
            time.sleep(0.5)
            print('Your soul has been tainted...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Shoebill.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Shoebill.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Shoebill.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Shoebill.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Pukeko = Bird_House_Animal("Evie",3, # femle
r"""
Scientific Name:
   Porphyrio melanotus
Origin Range:
   New Zealand & Australia
Description:
   A large, charismatic rail known for its deep blue-violet plumage, bright red bill, 
   frontal shield, and long orange legs. They are highly adaptable wetland birds with bold, 
   quirky personalities and complex communal breeding societies.
Avg Weight:
   0.85 kg (1.9 lbs)
Avg Lifespan:
   8-10 years
""","IUCN Status: Least Concern")
def see_pukeko():
     while True:
        Clear()
        print(PUKEKO)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the pukeko...')
            time.sleep(0.5)
            print('It looks dumb...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"Her name is {Pukeko.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"She is {Pukeko.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Pukeko.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Pukeko.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Potoo = Bird_House_Animal("Echo",4, # male
r"""
Scientific Name:
   Nyctibius griseus
Origin Range:
   Central & South America
Description:
   Nocturnal, insectivorous birds with specialized camouflage that allows them to perfectly 
   mimic dead tree stumps during the day. They possess slits in their eyelids to see while sleeping.
Avg Weight:
   0.25 kg (0.6 lbs)
Avg Lifespan:
   10-12 years
""","IUCN Status: Least Concern")
def see_potoo():
     while True:
        Clear()
        print(POTOO)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the potoo...')
            time.sleep(0.5)
            print('His pupils widen...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Potoo.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Potoo.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Potoo.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Potoo.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
Macaw = Bird_House_Animal("Jasper",14, #male
r"""
Scientific Name:
   Ara macao
Origin Range:
   Central & South America
Description:
   Vibrant, highly intelligent neotropical parrots known for their powerful, 
   seed-cracking beaks, social behavior, and loud vocalizations.
Avg Weight:
   1 kg (2.2 lbs)
Avg Lifespan:
   40-50 years
""","IUCN Status: Least Concern")
def see_macaw():
     while True:
        Clear()
        print(MACAW)
        time.sleep(0.2)
        Action = input('What would you like to do?: (admire/get info/leave): ').lower()
        if Action == 'admire':
            print('You admire the macaw...')
            time.sleep(0.5)
            print('He says he wants a cracker...')
            time.sleep(1.5)
            continue
        elif Action in ['info','get info','get']:
            get_info = input('What do you want to know? (name/age/description/status): ')
            if get_info == 'name':
                print(f"His name is {Macaw.name}.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'age':
                print(f"He is {Macaw.age} years old.")
                Proceed = input('Proceed?: ')
                continue
            elif get_info == 'description':
                print(Macaw.description)
                Proceed = input('Proceed?: ')
                continue
            elif get_info in ['status','endangered status','endangered']:
                print(Macaw.status)
                Proceed = input('Proceed?: ')
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue

Normal_Ticket_Price = randint(10,15)
Sale_Ticket_Price = randint(2,5)
Your_Money = randint(35,80)
Penguin_Plush_Count = randint(1,3)
Tiger_Plush_Count = randint(1,4)
Koala_Plush_Count = randint(1,2)
Giraffe_Plush_Count = randint(1,2)
Elephant_Plush_Count = randint(1,2)
Monkey_Plush_Count = randint(2,4)
Safari_Apparel_Count = randint(2,3)
Giraffe_Apparel_Count = randint(2,3)
Tiger_Apparel_Count = randint(2,3)
Zoo_Guide_Book_Count = randint(4,6)
Keychain_Count = randint(13,18)
Postcard_Count = randint (8,12)
Zoo_Guide_Book_Count = randint(7,10)
Help_desk_attendent_lines = ["No, you cannot pet the geese.", "No, we don't rent out the capybaras for birthday parties.",
 "No, the monkeys didn't steal your keys, but check your pockets anyway.", "If a bird poops on you, it's technically good luck.",
  "If you drop your phone in the alligator exhibit, it belongs to the alligator now.","The hyenas aren't laughing at you. Well, they might be, but it's nothing personal.",
  "The Hippo Cam is down because a hippo sat on it. We are working on a solution.","I heard that there is a secret command called 'Jump' at the fountain...","I miss mae...if only I could see her again...Anyways, what's up?"]
GATE1_PASS = False
GATE2_PASS = False
Inventory = []
Sale = False
Total_Cost = 00.00

WIP = r"""
                              ..
                           -@@@@@@@@@@@#-.
                      .=#@@@@@@@@@@@@@@@@@@@o.
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
                 =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
               .#@@@@@@@@@@@@@@@@@@@@@@@@@@######@@@@.
               =@@@@@@@@@@@@@@@@#oooooooooooooooooooooo.
              .@@@@@@@@@@@#oooo===oo===ooo========---=oo.
              =@@@@@@@#o=========ooooo##############o=.--.
              #@@@@#o=======ooo######@@@@@@@@@@@@@@@@@o--.
             .@@@#===-==ooo####@@@@@@@@@@@@@@@@@@@@@@@@-..
              =@#---=oo####@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
             .#=.-=o###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
             .--.=##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
              .--=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                ..=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
                   .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.             -@@@@@@@@@@@@@@@@@@@@@#.
                    .o#############################=.             .#@@@##o=@@@@@@@@@@@@@@@@.
                      .=#################oooooooo#@#####@@@@@@@@@###########@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                         .=ooooooooooooooooooo=- =@--oooooooooooooooooooooo==#@@@@@@@@@@@@ooooooooooooooooooooooooooooooooooooooooooooooo=.#=
                            ..-=ooo==---......   =@-=@@@@@@@@@@@@@@@@@@@@@@@###oooooooo##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.#=
                                ...-=oo-....-##o-o@-o@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.#=
                              .-#@@@@@@@=...-#@@@@@-o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.#=
                           .o@@@@@@@@@@@@@-..-#@@@@-o@@@@@@@@@@@@@@@@@@@@@@@@@#-=@=-o#-=@o=o#--==o@#====o#-===o@@@@@@@@@@@@@@@@@@@@@@@@@@o.#=
                         .o@@@@@@@@@@@@@@@=....##@@.o@@@@@@@@@@@@@@@@@@@@@@@@@o.-@-.=o..o=.=#.....o#....-o.....#@@@@@@@@@@@@@@@@@@@@@@@@@o.#o
                        .#@@@@@@@@@@@@@@@@@....-##@.o@@@@@@@@@@@@@@@@@@@@@@@@@o.-@-.=o..-=.=#..@=.=#..@@@o.-@-.=@@@@@@@@@@@@@@@@@@@@@@@@@#.#o
                       .@@@@@@@@@@@@@@@@@@@=.....#@.o@@@@@@@@@@@@@@@@@@@@@@@@@o.-@-.=o.....=#..@=.-@..--=o.-#..o@@@@@@@@@@@@@@@@@@@@@@@@@#.#o
                      .#@@@@@@####@@@@@@@@@@.....o@.o@@@@@@@@@@@@@@@@@@@@@@@@@o.-@-.=o.--..=#..@=.-#....-o....=@@@@@@@@@@@@@@@@@@@@@@@@@@#.#o
                      =@@@@@@@ooo#@@@@@@@@@@=....o@.o@@@@@@@@@@@@@@@@@@@@@@@@@o.-@-.=o.-o..=#..@=.-@..@@@o.-o..@@@@@@@@@@@@@@@@@@@@@@@@@@#.#o
                     .@@@@@@@@o=o#@@@@@@@@@@#....o@-o@@@@@@@@@@@@@@@@@@@@@@@@@o.-o-.=o.-@=.=#..-..=@..--=o.-#..o@@@@@@@@@@@@@@@@@@@@@@@@@#.oo
                     =@@@@@@@@ooo#@@@@@@@@@@#-...o@.o@@@@@@@@@@@@@@@@@@@@@@@@@#-....#o.-@@-=#.....##....-o.-@-.-@@@@@@@@@@@@@@@@@@@@@@@@@#.oo
                     =@@@@@@@@o=o#@@@@@@@@@@@-...o@.o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.oo
                     .#@@@@@@@@@o##@@@@@@@@@@=...o@.o@@@@o....o@=...-##..#o.=@-...=o.....o-....o#..@o.-@=....#-....-@..##....o@-.=@..@@@@#.oo
                      .@@@@@@@@@@@##@@@@@@@@@#...#@.o@@@@-.--..#..-..=#..=o.=o.-=..o-...-o-....-#..@o.-#..=-.-=-...-@..#-.--..#-..#..@@@@#.oo
                       .#@@@@@@@@@@@##@@@@@@@@#=.#@.o@@@#-.o#..#..@-.=#...-.=o.=@o=@@=.-@@-.=#..#..@o.-o.-@o.-@@..o@@..#-.o@..#-..=--@@@@#.oo
                        .=@@@@@@@@@@@@@@@@@@@@@###@.o@@@#..o@@@#..@=.=#.....=#...-@@@=.-@@-..-.-#..@o.-o.-@@@@@@..o@@..#-.o@..#-.....#@@@#.o#.
                          .o@@@@@@@@@@@@@@@@@@@@@@#.o@@@#..o@@@#..@-.=#.-o..=@@o...#@=.-@@-....=#..@o.-o.-@@@@@@..o@@..#-.o@..#-.=...#@@@@.o#.
                            .o@@@@@@@@@@@@@@@@@@#o#.o@@@#..o#..#..@-.=#.-#-.=o-o@-.#@=.-@@-.==.-#..@o.-o.-#o.-@@..o@@..#-.o@..#-.#=..#@@@@.o#.
                             .###@@@@@@@@@@@@@@@@@@@@@@@#-.....#.....=o.-@o.==..-..#@=..@@-.=o.-#.....-#.....-@@..o@@..#=.....#-.#@-.#@@@@.o#.
                             .o@@@#@@@@@@@@@@@@@@@@@@@@@@=....#@=...-#o.-@@-=@-...=@@=.-@@-.-#..#o....o@=....#@@..o@@..##....o@-.o@#-#@@@@.o#.
                             .o@@@@@#@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.o#.
                             .o@@@@@@##@@@@@@@@@@@@@@@@####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.=#.
                             .o@@@@@@@#####@@@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.=#.
                             .@@@@@@@@@##oooo=ooooo=o#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.=#.
                             -@@@@@@@@@###ooo==--oo........................................................................................=#.
                            .o@@@@@@@@@@###oo-.-==oo##########oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-
                            .@@@@@@@@@@@####=. -===oooooooo##o.
                            =@@@@@@@@@@@@###.  .==oooo########.
                           .#@@@@@@@@@@@@##-   .=oooo#########-
                           .@@@@@@@@@@@@@#o.    .ooo#########@-
                           -@@@@@@@@@@@@@#-     .=oo######@@@@=
                           =@@@@@@@@@@@@@#.      -oo#####@@@@@o
                           o@@@@@@@@@@@@#=       .oo#####@@@@@o.
                           #@@@@@@@@@@@@#.       .=o#########@=
                          .@@@@@@@@@@@##-         -###########-
                          .@@@@@@@@@###=.         .o#########o.
                          .@@@@@@@####=.           o#########=
                          -@@@@@@####=.            =########o.
                          =@@@@@####=.             -########.
                          o@@@@####=               -########.
                         -@@@@@@##=.              .o@@@@@@@@@@@#o=-..
                       .#@@@@@@@@#.             .o@@@@@@@@@@@@@@@@@@@@@@=.
                    .=@@@@@@@@@@@@#.           -@@@@@@@@@@@@@@@@@@@@@@@@@@@.
                  .#@@@@@@@@@@@@@@@@-         .o@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
                 .@@@@@@@@@@@@@@@@@@@-        .=o#########@@@@@@@@@@@@@@@@@o.
                 -@@@@@@@@@@@@@@@@@@@=           .....---====oooooo#oooo=-.
                 .#@@@@@@@@@@@@@@##o-
                   ..----------...
"""

ZOO_ENTRANCE = r"""
        ________________________________________________
       /                                                \ 
      /         [P][Y][T][H][O][N]   [Z][O][O]           \ 
     /        8% CHANCE FOR TICKETS TO BE ON SALE         \
    /     ============================================     \ 
   /________________________________________________________\
   |                 | |_________________| |                |
   |  ___    ___     | |   [ TICKETS ]   | |    ___    ___  |
   | |   |  |   |    | |                 | |   |   |  |   | |
   | |   |  |   |    | |   [ ]     [ ]   | |   |   |  |   | |
   | |___|  |___|    |_|_________________|_|   |___|  |___| |
   |                 |                     |                |
   |   ,---------.   |     ___________     |   ,---------.  |
   |  /  _     _  \  |    |     |     |    |  /  _     _  \ |
   |  | | |   | | |  |    |     |     |    |  | | |   | | | |
   |  \ |_|   |_| /  |    |     |     |    |  \ |_|   |_| / |
   |   `---------'   |    |     |     |    |   `---------'  |
   |                 |____|_____|_____|____|                |
  /                  [======]       [======]                 \ 
 /____________________________________________________________\
    
    """
ZOO_MAIN_AREA = r"""
   #################################################################################################
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      PYTHON ZOO MAP     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
   #################################################################################################

     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
       ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ NORTHERN RIVER ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

  /===========* NORTH WEST *===========\                      /===========* NORTH EAST *===========\
  |                                     |                     |                                     |
  |  [M] The Savanna                    |==== NORTH  WALK ====|  [M] The Forest                     |
  |                     .-------------. |  :::::::::::::::::  | .-------------.                     |
  |                     | [G] Gate #1 | |=====================| | [G] Gate #2 |                     |
  \=====================| ::::::::::: |=/                     \=| ::::::::::: |=====================/
                        '-----+ +-----'                         '-----+ +-----'
                              |:|                                     |:|
                        .-----+ +-----.                         .-----+ +-----.
                        |  WEST ROAD  |                         |  EAST ROAD  |
                        | ::::::::::: |                         | ::::::::::: |
                        '-----+ +-----'                         '-----+ +-----'
                              |:|             ___________             |:|
                              |:|            / C-PLAZA   \            |:|
                              |:|           |=============|           |:|
                              |:|           |[O]Fountain  |           |:|
                              +:------------+[O]Restrooms +------------:+
                              |::::::::::::  [O]Help Desk   ::::::::::::|
                              +:------------+             +------------:+
                              |:|           \=============/           |:|
                              |:|                 |:|                 |:|
                        .-----+ +-----.           |:|           .-----+ +-----.
                        |  WEST ROAD  |           |:|           |  EAST ROAD  |
                        | ::::::::::: |     .-----+ +-----.     | ::::::::::: |
                        '-----+ +-----'     |  MAIN PATH  |     '-----+ +-----'
                              |:|           | ::::::::::: |           |:|
                              |:|           '-----+:+-----'           |:|
             /========*SOUTH WEST*========\       |:|       /========*SOUTH EAST*========\
            |                              |      |:|      |                              |
            |   [M] The Reptiles           |      |:|      |    [M] The Bird House        |
            |   [M] The Aquarium           |------+ +------|                              |
            |                              :::::::::::::::::                              | 
            \=====================================|:|=====================================/
                                                  |:|
                                      /===========v v===========\
                                      |      ENTRANCE PLAZA     |
                                      | ======================= |
                                      |     [O] Tickets         |
                                      |     [O]Gift Shop        |
                                      |     [O]  Cafe           |
                                      \===========| |===========/
                                                  | |
                                               [ ENTER ]

    #################################################################################################
    # LEGEND: (Tag means you can go there) [M] Main Exhibit  [O] Other [G] Gate [I] Inventory       #
    #################################################################################################
"""
GIFT_SHOP = r"""
                               ===================================================================
                              |                                                                   |
                              |          [ P Y T H O N    Z O O    G I F T   S H O P  ]           |
                              |                                                                   |
                               ===================================================================

     _____________________________________________________________________________________________________________________
    |                                                                                                                     |
    |                                                                                                                     |
    |      [  A P P A R E L  &  S A F A R I  W E A R  ]                           [ S O U V N I E R S ]                   |
    |     ____________________________________________             _____________________________________________________  |
    |    |     _   _         _   _         _   _      |           |   _______________________________________________   | |
    |    |    | |_| |       | |_| |       | |_| |     |           |  |                                               |  | | 
    |    |    |  _  |       |  _  |       |  _  |     |           |  |                                               |  | |    
    |    |    |_| |_|       |_| |_|       |_| |_|     |           |  |                                               |  | | 
    |    |   ( Safari )    ( Giraffe )   ( Tiger )    |           |  |                                               |  | |  
    |    |   ==========    ==========    ==========|  |           |  |                                               |  | | 
    |    |   |   __   |    |    _/\  |   | _/\_/\  |  |           |  |                                               |  | |    
    |    |   |  /  \  |    |   (*_*) |   |(=^.^=)  |  |           |  |_______________________________________________|  | |    
    |    |   |  \__/  |    |    ||   |   | )   (   |  |           |   |                                             |   | | 
    |    |   |________|    |____||___|   |____v____|  |           |   |   ( )     ( )     ( )     ( )     ( )       |   | |
    |    |____________________________________________|           |   |    |       |       |       |       |        |   | | 
    |                                                             |   |   [O]     [O]     [O]     [O]     [O]       |   | |
    |_____________________________________________________________|___|            ( K E Y C H A I N S)             |___|_|
    |                                                                 |_____________________________________________|     |
    |                                                                                                                     |
    |      [  P L U S H  &  S T U F F E D   A N I M A L   K I N G D O M  ]                                                |
    |     _________________________________________________________________                                               |
    |    |       __  __              __  __              _  _              |             Your Money : ${money}              |
    |    |      (oo)(oo)            (@@)(@@)            (o)(o)             |                                              |
    |    |     / ||  || \          / ||  || \           / || \             |              [C H E C K O U T]               |
    |    |    *  ||  ||  *        *  ||  ||  *         *  ||  *            |         ___________________________          |  
    |    |       ||  ||              ||  ||               ||               |        |    .-----------------.    |         |  
    |    |      (  GIRAFFE  )       ( ELEPHANT )        ( MONKEY )         |        |    | TOTAL: $  {cost} |    |         |  
    |    |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    |        |    '-----------------'    |         |  
    |    |       _/\_/\                __                _  _              |        |   ______________________  |         |  
    |    |       (=^.^=)              (oo)              (@@)               |        |  [ 1 ] [ 2 ] [ 3 ] [ + ]  |         |
    |    |       (") (")              /||\              /||\               |        |  [ 4 ] [ 5 ] [ 6 ] [ - ]  |         |
    |    |      (  TIGER  )         (PENGUIN)          ( KOALA )           |        |  [ 7 ] [ 8 ] [ 9 ] [ X ]  |         |
    |    |_________________________________________________________________|        |  [ C ] [ 0 ] [ . ] [ENT]  |         |
    |                                                                               |___________________________|         |
    |_______________________________________________________________________________|___________________________|_________|
"""

CAFE = r"""
  ======================================================================================
     ____  _  _  ____  _  _  _____  _  _      ___   __   ____  ____    
    (  _ \( \/ )( __ )( \/ )(  _  )( \( )    / __) /__\ ( ___)( ___)   _.._  
     )___/ \  /   ||   \  /  )(_)(  )  (    ( (__ /(__)\ )__)  )__)   (oo  ) *hiss*
    (__)   (__)  (__)  (__) (_____)(_)\_)    \___(__)(__)(__) (____)   //~~\\ 
  ======================================================================================
       ||                                 ||                                 ||
       ||        _.-'''''''-._            ||                                 || 
       ||      .'  _     _    '.          ||        Your Money : ${money}      ||
       ||     /   ´◔    ◔`     \          ||                                 ||
       ||    |                   |        ||                                 ||
       ||    |         ゝ        |        ||                                 ||
       ||     \      ‿          /         ||                                 ||
  =====╩╩======'.             .'==========||=================================╩╩====
               _.-'-.......-'-._          ||
             .'                 '.        ||           [ ORDER TERMINAL ]
            /                     \       ||       .------------------------.
           |                       |      ||       |        {items} items        |
           |                       |      ||       |   Total For Purchase   |
            \                     /       ||       |         ${cost}         |
             '.                 .'        ||       '------------------------'
               '-.__       __.-'          ||                   ||
                    '''''''               ||             ______||______
  ========================================╣╠============[______________]============
                                          ||
             [ ZOOKEEPER'S BREWS ]        ||             [ WILD BITES ]
       .--------------------------------. ||       .------------------------.
       |   Anaconda Americano $4.50     | ||      | Dugong Doughnut   $3.50  |
       |   Silverback Espresso $4.00    | ||      | Sun Bear Scone    $4.00  |
       |   Pink Flamingo Latte $5.25    | ||      | Oreo Panda Bun    $4.50  |
       |   Toucan Tropical Tea $4.20    | ||      | Lion Claw Pastry  $3.75  |
       '--------------------------------' ||       '------------------------'
                       ||                 ||                   ||
                 ______||______           ||             ______||______
                [______________]          ||            [______________]
  ========================================╩╩============================================
         _   _            _   _                          _   _            _   _
        ( )_( )          ( )_( )                        ( )_( )          ( )_( )
         \_ _/            \_ _/                          \_ _/            \_ _/
          (_)              (_)                            (_)              (_)
       _________        _________                      _________        _________
      [_________]      [_________]                    [_________]      [_________]
       |       |        |       |                      |       |        |       |
       |       |        |       |                      |       |        |       |
  ======================================================================================
"""
HELP_DESK = r"""
                       _________________________________________________________________________________________________
                      |                                                                                                 |
                      |                                        H E L P    D E S K                                       |
                      |_________________________________________________________________________________________________|
                      |                                                                                                 |
                      |     _______________________________________________________________________________________     |
                      |    |                                                                                       |    |
                      |    |  {Help_desk_text:<85}|    |                                                                 
                      |    |                                          +.         ...   .                           |    |
                      |    |                          .        ...@@@@@@@@@@##%%#*=%@%@@            .      .       |    |
                      |    |                   .        ...*@@@+@*:@:#-+%@%@@@@@@@@@@+@%=@:.                       |    |
                      |    |                           +@@*% :@:%@-%=--#%%**%#*%*+: :-:=::@@@@#@                   |    |
                      |    |                          @@=+:@#+##=#::@-+.=%****##%%%**=:%#@@@*@@@                   |    |
                      |    |                     .   @:  *%#+-=..+.:@++:=@@%@%#**#*=+.#@*@#@@@@@.          .       |    |
                      |    |                  ..   @@@#*@%*@%++-+%--+#--. ++==*==*+#==@@@@@@@@*      .             |    |
                      |    |                     @@@# #*%@+-:=%==-:-+#+:=*%%@%@#-=*+:%%#@@@@@: @.                  |    |
                      |    |                   .@@#+::+=+@+#=:+@@@%* -#-@*%@@@%*@@%**@+@%=*@   #                   |    |
                      |    |                  @@@:.%%@@%@@ =+@@@@#-@@**-@@@@%@%*@+:*%#%@*#@@                       |    |
                      |    |                 @@*=%%**=%#@@ *@@*%@@@@%#*=+%@@@@#+---@@*#@@=@..                      |    |
                      |    |                .@@@@@+*@@@@%@ :-+@@@%=:::+@#  .:+*+*+%@-+%%.@. @@@@.                  |    |
                      |    |                 # @+@@@*=%@#@:---- :.-+=:%%%%+=--+%@%%*%#@-%@@                        |    |
                      |    |               .%@@@@-%@@@@@@@@*.:=.-=---:#@@#*-:::  =#**%#@@@.                        |    |
                      |    |              .:.. . @@@+@@@:#@@%#+-=#%%*:#@@@@@@@@@=@@%@*=#@+                         |    |
                      |    |           .  @    .@  ..@ @-+@*@#@@@@@@@@@@%@%%@%@@@@##@=@*@                          |    |
                      |    |            @:..       . @:@@**#%*@@@@%%%%%%%%%%%#%%#%%@%+@#@@                         |    |
                      |    |           -: .          -  @@+%@*#%@@%%%%%%%@%%%%@@@%#@:.#%@@.                        |    |
                      |    |               .         @  .@@@@@@-%@@%%%%%%%%@@@%%@%@@ =@@@@@@@                      |    |
                      |    |       .                 @     .@@@@+-@#@*@%%%%%%%@@@%@@ *@%%%*#@@                     |    |
                      |    |                        .   .+     -@@@%@%%@%%@%%@@%%%@@.*@%%#%*@@@                    |    |
                      |    |    .                   ..  . .    .. @@@+@%@%%@@@@#*#@*-@%##@%@%%@@@@#                |    |
                      |    |                        .      .   .   :@@@@@%#+##+*@@% +***######%@%%@@               |    |
                      |    |                              ..   . @.  @@#%@@@%%#@@@ =%##*#%@%#%#%@#=@@@@            |    |
                      |    |                          .        .      @@@=#*@@@@@::%@@##@%%%@%%%%@@@@@@@@          |    |
                      |    |                        .         .    .   #@@%+=::  -%@####%%%%@%%%%%%%%@%#@@.        |    |
                      |    |                                           ..@@@#%@@@@#=*##%%%%%%%%%%%%%%@#%#@@%       |    |
                      |    |                                             @@%%#*+++*####%%%%%%%%%%%%%%%@@@@@@@@#    |    |
 _____________________|____|_______________________________________________________________________________________|____|_____________________
[______________________________________________________________________________________________________________________________________________]
        |                                                                                                                                  |
        |                   [ TAKE A FLYER ]                                              [ LOST & FOUND ]                                 |
        |                .---.  .---.  .---.                                           .-------------------.                               |
        |                |   |  |   |  |   |                                           |   ______________   |                              |
        |                | λ |  | Ω |  | Σ |                                           |  |    ︻╦̵̵̿╤──   |  |                              |
        |                |___|  |___|  |___|                                           |  |______________|  |                              |
        |                                                                              '-------------------'                               |
"""


FOUNTAIN = r"""
                                                                .#@@@@@@@@@@@@@.
                                                              .@@@@@@@@@@@@@@@@@@-
                                                            .@@@@@@@@@@@@@@@@@@@@@@=
                                                          =@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                                                        #@@@@@@@@=.=@@@@@@@@o..@@@@@@@@@.
                                                        #@@@@@@-.   .-@@@@o..  ..@@@@@@@.
                                                        #@@@@@@.   -#@@@@@@#o   .@@@@@@@.
                                                        o@@@@--..=##o#@@@@#oo#o. --@@@@@.
                                                        o@@@@.  .o##=o@@@@#=o@#.   #@@@@.
                                                     .oo@@#==..==oo####ooo###oo==. -=o@@oo.
                                                     .@@@@o .ooooo=ooo####ooo==oooo- -@@@@-
                                                     .@@@@# .=------oo###@oo=-----=. =@@@@-
                                                     .@@@@@      -==oo####oo==-.     =@@@@-
                                                     .@@@@@------o##oo####oo###------o@@@@-
                                                   .==@@@@@oo#########oooo#########oo#@@@@o=.
                                               -=--=@@@@@@@##@@@@@@#oo####ooo@@@@@@@##@@@@@@o-=--.
                                            .--@@@@@@@@@@@@@@@@@@@####oooo#@###@@@@@@@@@@@@@@@@@@==.
                                            .@@@@@@@@@@@@@@@@@@@@#o####@@@###o#@@@@@@@@@@@@@@@@@@@@-
                                            .@@@@@==oooo@@@@@@@@@@@@oo@@@@oo#@@@@@@@@@@@ooooo=#@@@@-
                                            .@@@@o .==ooooooo@@@@@@@@@@@@@@@@@@@@@@#oooooo==- =@@@@-
                                            .@@@@o   .=======oooooooooooooooooooooo=======.   =@@@@-
                                            .@@@@o...........======================-..........=@@@@-
                                            .@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                                   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#==ooooo=o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                           #@@@@@@@@@@@@@@@@@@@@@@oo==ooooo==oooo#@@##====#####oo==oooooooooo=#@@@@@@@@@@@@@@@@@@@@@@
                    . =@@@@@@@@@@@ooooooooo==@@@@@oooo==ooo==ooooooo=o####o=ooooooo===ooooooo=#@@@@ooooooo==oo@@@@@@@@@@@#.
                 .@@@@@@@@@ooooo====ooooooo==@@@@#ooooooo=ooo==#####==ooooo=o@###oo=========oo#@@@@ooooooo==ooooooooo@@@@@@@@@-
             =@@@@@@#oo==ooooooo==oo=========@@@@@@@@@@@@@@@@@#ooo=o##@@#####==oo#@@@@@@@@@@@@@@@@@o======oo=====ooooooo==oo@@@@@@#
        .@@@@@@@==ooooooo======#@@@@@@@@@@@@@@@@@@@@@@@@@@@##ooooo===o#@##o====oooo##@@@@@@@@@@@@@@@@@@@@@@@@@@@@=========oooo==@@@@@@@-
      -@@@@@@#==oo==oooo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#========o##====###========o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@======oooo#@@@@@@#
    =@@@@@@#oo==oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@###====#@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=ooooo@@@@@@#.
 .@@@@@@@o=ooo=o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ooooo=o#@@@o=ooooo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@==oo==@@@@@@@.
@@@@@@@====oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o===o#@@#o====@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@==oooo#@@@@@@
@@@@@@@====@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@#oooo#@@@###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=oo#@@@@@@
@@@@@@@oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ooo=o##oooo###==oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=#@@@@@@
@@@@@@@==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o===o##oooo#@#====#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=#@@@@@@
@@@@@@@==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#====###==ooooo=o##====#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=#@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#===o####o===o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o
ooo##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##oo
ooooo##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#ooo==
##o=ooo##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##oooo==
@#o==oooo##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##ooooo====
##o===o##oo#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####ooooo======
oo====o##o=ooooo####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####ooooooooo======
oo====o##o====oooooo#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#######ooooooo==oo##o======
oo=====oo=======ooooooooooo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#ooooooooo=====oo##o====oooo
oo=====oo=======##ooo====ooooooooooooo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ooooooooooo==ooo##======o@@oo===oo####
ooo====oo=======oo#@o========oooooooooooooooooooo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#oooooooooooooooooo======o##========o@@oo==o##oooo
oo#####oo=========##o========oo#@#===========ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo==oo##o========ooo========o##oo###oo====
==oo###@#oo=======oo=========oo###===========ooooooooooooooooooooooooo===========oooooooooooo============o####o========oooo==oo=###oo##ooooo====
====ooo####o======ooo========##o===============oo###=============ooo##=============###oo===============o##oo===========ooo#######oooo##ooooo====
  =====oo###@@@#ooooooooo====ooo===============ooo##=============#@@##=============ooo##================oooo===========####@##ooooo==#@ooooo==.
    -oooo===========##@##oo==ooo===============###oo=============###===============ooo##================oooo===========#@#ooooooo====##ooo==
      .===============o#@#@@#ooooo#@@#o========ooo===============ooo=================o#@##o==========ooooo=============o@#oo===========oo-
           =========oo#@@@#oo=====oooo#@###====ooo===============ooo==================oooo===========ooo##@@#@####@##@##oo===========.
               .==ooooo===============ooo###@@##@########@#======ooo==================oooo===========##@@######oo====##@##======-
                    -======================ooooooooo###@@###@@@@####====================oo=========##@##oo=============ooo==
                        .====================ooooooo=========oooo##@######o====#@@@@@@@#@##@@@@@@@####oo===============-
                               -=============ooooo======================oooo######@o==oooo#@@@@@@@#ooo===========
                                        .==ooooo==========================ooooo===============ooooo====-.
                                                                                                                                                                               
"""

RESTROOM = r"""
                _______________________________________________________________
               /                                                               \
              /                 P U B L I C   R E S T R O O M S                 \
             /___________________________________________________________________\
             |                                                                   |
             |           =============================================           |
             |           |       X   C L O S E D   F O R   X         |           |
             |           |       X  M A I N T E N A N C E  X         |           |
             |           =============================================           |
             |                                                                   |
             |                     _________________________                     |
             |                    /                         \                    |
             |                   /  O U T   O F   O R D E R  \                   |
             |                  /_____________________________\                  |
             |                  |  _________________________  |                  |
             |                  | |                         | |                  |
             |                  | |   XXXX   XXXX   XXXX    | |                  |
             |                  | |   X  X   X  X   X  X    | |                  |
             |                  | |   XXXX   XXXX   XXXX    | |                  |
             |      [MALE]      | |                         | |    [FEMALE]      |
             |     _________    | |     [ DO NOT ENTER ]    | |    _________     |
             |    |    _    |   | |                         | |   |    _    |    |
             |    |   (_)   |   | |     _______________     | |   |   (_)   |    |
             |    |         |   | |    |               |    | |   |         |    |
             |    |         |   | |    |  [ LOCKED ]   |    | |   |         |    |
_____________|____|_________|___|_|____|_______________|____|_|___|_________|____|_____________

"""

GATE1 = r"""
                             _______________________
                            |                       |
                            |   TICKET CHECKPOINT   |
                            |_______________________|
                                    ||     ||
                                    ||     ||
       _____________________________||_____||_____________________________
      [___________________________________________________________________]
         ||     ||     ||     ||   PINEAPPLE   ||     ||     ||     ||
         ||_____||_____||_____||___SECURITY!___||_____||_____||_____||
         ||     ||     ||     ||               ||     ||     ||     ||
         ||     ||     ||     ||               ||     ||     ||     ||
         ||     ||     ||     ||     (⌐■_■)    ||     ||     ||     ||
         ||     ||     ||     ||       |       ||     ||     ||     ||
         ||     ||     ||     ||     __|__     ||     ||     ||     ||
         ||     ||     ||     ||    /| | |\    ||     ||     ||     ||
         ||     ||     ||     ||   / | | | \   ||     ||     ||     ||
  _______||_____||_____||_____||__/__|_|_|__\__||_____||_____||_____||_______
 [_______||_____||_____||_____||_/___________\_||_____||_____||_____||_______]
         ||     ||     ||     ||               ||     ||     ||     ||
         ||     ||     ||     ||  [=========]  ||     ||     ||     ||
         ||     ||     ||     ||  |  SHOW   |  ||     ||     ||     ||
         ||     ||     ||     ||  | TICKETS |  ||     ||     ||     ||
         ||     ||     ||     ||  |         |  ||     ||     ||     ||
         ||     ||     ||     ||  |_________|  ||     ||     ||     ||
         ||     ||     ||     ||               ||     ||     ||     ||
        _||_____||_____||_____||_______________||_____||_____||_____||_
       [_______________________________________________________________]

"""

GATE2 = r"""
                             _______________________
                            |                       |
                            |   TICKET CHECKPOINT   |
                            |_______________________|
                                    ||     ||
                                    ||     ||
       _____________________________||_____||_____________________________
      [___________________________________________________________________]
         ||     ||     ||     ||   BULGARIAN   ||     ||     ||     ||
         ||_____||_____||_____||___SECURITY!___||_____||_____||_____||
         ||     ||     ||     ||               ||     ||     ||     ||
         ||     ||     ||     ||               ||     ||     ||     ||
         ||     ||     ||     ||     (▀̿Ĺ̯▀̿ ̿)  ||     ||     ||     ||
         ||     ||     ||     ||       |       ||     ||     ||     ||
         ||     ||     ||     ||     __|__     ||     ||     ||     ||
         ||     ||     ||     ||    /| | |\    ||     ||     ||     ||
         ||     ||     ||     ||   / | | | \   ||     ||     ||     ||
  _______||_____||_____||_____||__/__|_|_|__\__||_____||_____||_____||_______
 [_______||_____||_____||_____||_/___________\_||_____||_____||_____||_______]
         ||     ||     ||     ||               ||     ||     ||     ||
         ||     ||     ||     ||  [=========]  ||     ||     ||     ||
         ||     ||     ||     ||  |  SHOW   |  ||     ||     ||     ||
         ||     ||     ||     ||  | TICKETS |  ||     ||     ||     ||
         ||     ||     ||     ||  |         |  ||     ||     ||     ||
         ||     ||     ||     ||  |_________|  ||     ||     ||     ||
         ||     ||     ||     ||               ||     ||     ||     ||
        _||_____||_____||_____||_______________||_____||_____||_____||_
       [_______________________________________________________________]

"""

SAVANNA = r"""
                                   [ GATE 1 ]
                                       ||
                                       ||
                                       ||
      _________________________________||__________________________________________________________________________
     /  ...............................||......................................................................... \
    /  .                               ||                                                                         . \
   /  .     _/\_                    _/\_                                        _/\_                              .  \
  |   .    /    \                  /    \                                      /    \      _________________      .  |
  |   .     ||||                    ||||                                        ||||      |                 |     .  |
  |   .                                                                                   |     Painted     |     .  |
  |   .                                                                                   |       Wolf      |     .  |
  |   .                                                                                   |_________________|     .  |
  |   .                                                                                                           .  |
  |   .                                                                                                           .  |
  |   .     _________________                                                                                     .  |
  |   .    |                 |                                                                                    .  |
  |   .    |      Black      |                                                                                    .  |
  |   .    |   Rhinoceros    |                                                    _/\_                            .  |
  |   .    |                 |                                                   /    \                           .  |
  |   .    |_________________|                         _.._.._.._                 ||||                            .  |
  |   .                                             (              )                                              .  |
  |   .                                             (  _.._.._.._    )                                            .  |
  |   .                                            (  _.._.._.._  )                                               .  |
  |   .                  _/\_                       (               )                                             .  |
  |   .                 /    \                       `-.._.._..-''                                                .  |
  |   .                  ||||                                                                      _/\_           .  |
  |   .                                                                                           /    \          .  |
  |   .                                                                     _________________      ||||           .  |
  |   .       {=================}                                          |                 |                    .  |
  |   .       |                 |                                          |                 |                    .  |
  |   .       |     Ocelot      |                                          |    Pangolin     |                    .  |
  |   .       |                 |                                          |                 |                    .  |
  |   .       {=================}                                          |_________________|                    .  |
   \  .                                                                                                            . /
    \  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  /
     \_____________________________________________________________________________________________________________/



"""

OCELOT = r"""



                          ........
                         ..      . ..
                        ..    ...... .-                               .......
                        ...    ........-... ............ ..       ...........-=.
                        -...    ..-....-=.....  .........   .-...-..............
                         ....   ........--...  --. .  .--. .....-...---........
                          ...    ............  ..-... .---..----.............-
                         .-..  .............  ....     ..-. .-.--.--.........
                           .......-.........  .-.-.......-.  .------.......-
                             ...............  ---......---.  ---------...--.
                             ---.......-....  .. ..--.-..=- .-------==-..
                           .........--...--   ..--....-.-... .-----=-==--. .
                          .... .....======-  .  ..-.....---. -=---===--=---  .-.
                          .  ...         .   .    .--...... .===o#o===-==---. -=---
                                     ...      -. ..--.....-       .-------.-=-===....
                               .   .  .....   -=......--=o ...  .. ....-==-.----==-...--.
                           ......             -=..--.---o=  .--- .....  -===-----========-...
                             ......   -=oo=.   ...--==---.  ...--. .=-..---==-.-==-====o====---..
                                        ..      ...-===--   -#o=. .-=--==..-==-.---..====--=o======.
                                  .....   .--.   ..-----. .-...    ...===-...==-------===---====-..==--.
                             ...  ..-.  . .-==. .--=--=---===....   ..=oo=.---==----=---==-======--.-====-
                                   .........===  . ...---oo-..... .. .=ooo=.---=-----=---=--====o===--===-..
                                  ..........-===.      .=oo=.--......-=oooo-.---=---===--=====--===---=ooo==o=
                                ..... ............   ..--==-------=====.-ooo=-=-==--====--===ooo=oo-..==---=o==-
                                 ........    ..      .....---....---==- .=ooo=-=-==-=--=--=======oooooo=====-===-
                                .--........               .. ....--===-. .=oo====----=----====--=--oooo=-====-=o==.
                                .----..................-...      .-==--...=o=--===.-===--=-.==-.----=oo==--==--====-
                                 -----................ ....       .....-. .=-.---====-o=.=-.-==-.==-.-=o==---..=o=---
                                  ..---.....................-..---..  .---------.==---==--=.-==-..---..====-..-====---
                                  . .----.......................-----..--===---=.-----=---==-===..----..-===--==--==---.
                                  -.. ...................          .-=-. ...-===--.-=.--=====-===..----.-=======..------.
                                  .---        .......               .-=---=====-.--.-.-.----=====-.----..-.--===-....----.
                                   ----.......             ..  .--...-======--=-=----.-.---.-==-===-..---....==-=--...--.-
                                   .---------............------------------====-==--..-. .-..=--====..----...----------..--
                                    ------.....-...........----------...  -- .====------. ...----======-.--..-....-----...-.
                                     ..........-..........-----..----   .---..===-==-.---......-. .====..----...  .--........
                                     .---........ ........... .-............---=---.-..---.  ..-- .-==-.......... ............
                                      .-........................      ... ..-.  .--.--..---....--. .----.  ...... ............
                                        ..................      ........    ...--.--------.-....-   .-----. ........ ..........
                                         .........................--..........--..---.-..........    .----.    ..... ..........
                                         .-........ ........  .         .......---.--... ... .-...  ...---..---...... ......---."""


RHINO = r"""




                                                                                                                        .-
                                                                                                             -o         =
                                                                            .=ooo#@########o-.              =#-       .#.
                                    .-o#@@@@@#@@@#o-.                 .=#@@#@##@@@@########-..===....    .=##o.      -#-
                              .#@@@@@@@#@@@@@@@@@@@@@@@@@##ooooo###@@@@@@@@###############=.  =oo#oo===oo=o@#=      ##=
                            =@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@@###########o#####=---=ooo===o==#@#oo.  .#@o-.
                          #@@@@@@#######@@@@@@@@@#@@@@@@@@@@@@@@@##@##@@@##############o#@###ooo==ooooo##@o#oo-=@@#o-
                        #@@@@########@@@@@@@@@@@@@@@##@@@@@#@@#@@##@#@#################o##oo#ooooo##########@@@@#oo-
                      #@#@@@##oo######@@@@@@@#@@@@@@#@@@@################@##############o#o#@###o#@@@##########oo=--
                    =@##@@####oo#o#####@@@@@@@@@@@@@#@@@@@########@@####@@####oo#####o#oooo##o#####o..ooo####o==---.
                   .@@@###oo##o-o#o#####@@#@@@@#@###@#@@#@##o#####@###o#@@#####oo####oo#o=o########ooo=o#ooooo==----
                   o###oooooooo=-ooo#########@@@############=#####@##oo#@#@##ooooo###oo#o==o#######o=oooo==oo=------
                   o#ooooooooooo-=ooo######################ooo###@##o###@####oooooooo==oo===oooooooooo====---.-=
                   oo======ooo===-oooooooo#####o#######oooooooo#############ooooo=====--=o=---.-==-====---.. . .
                   ==--==========-oooooooo####ooooo#o#oooooooo#######o#####oo=o==--===-.-----..          .
                   -=-----======o-.=oooooooooooooooooooooo=oooo#=#########ooo===------..--...
                   .-----------==- .===oo======o=oooo=oooo=oo=o#-ooooooooooo=---.......-----
                   .-----------==.   =====================o==oo=--==oooo===----.......---.
                    .---------=-.     .--====o==---=========-==-....====oo======-....--..-
                    .---------.         .----===========-=------.....==========--..--..--.
                    .---.-..    ..      .   .--------=--====---......-===-====---. ...--
                    ---....      -..   ..       .-------------.....   -==-------. ..--.
                    --..--.     .-.......                              ---------.---.
                   -------      -..-....                                --------.-.
                  ----.--.      --------                                ..--...-.
                   -----..      -----.--                                 -......
                    .--...        .------                                .-....
                      .-...         ....--                                -.....
                      .....          .--.-..                              -..   .
                     .---. ..         . ...                              ---  ..-.-
"""

PAINTED_WOLF = r"""
                                                                     .
                                                                       .                   .
                                                                        .-.             ..
                                                                        .....         - ...
                                                                  .. .-===..          ..=oo=  .
                                                                   .. .===..===ooo#===--===. .
                                                                    -.  -=ooo###o-o###oo==.  -.
                                                                       .o##o####o.-oooo###-
                                                                       =##o..  -=.--  ..o@#
                                                                       ##o...-.-====-..--o#.
                                                                     .#@==-..-----====-.-=#-
                                                                   .#@##-==----.----=-----##
                                                 ..----=--=oo====oo@@##o=. .-....   ..-- =#=
                                   --.---o@#--=o##o#@@@#ooo==o-==#@@@o===....... .....-.==o.
                                .=###o====---------==----=o#-...-####=-..--.   .-..-..--.
                              -oo#o##o##o=..===.-=-o#o=-o=oo--..-###o-.........    ..-=-
                           o@#-=====oooo=ooooo==-----.-=o==--...o#o=-..  ..-.--. ..--=.
                     ..-o@@#o-..=====ooooooooooooo==-==--.==.....o==-... ..--.-..--===
              .=o@@@=--=o##o---=-==--oooooooo#ooo==.-====--=-...--..-  -- ..------==-
         .o@@@@@@@@#o-.-===.-=..--=-.==o=ooooooooooo---=- .=-...-.-=.. .-.  ......-
      -#@@@@@@@@@@#o==---==o=-..-=--oo=-==o==-==o=ooo==---.oo-.. .-=---..--. ...-
      -==o#@@@@@#ooo==-----=-..--.-==.  .-===--==o=oooooo=====-. -.-==..- -- .. .
     -=o##@@@@##@#o=o==-.--....==-.-  --.  -==---..=o===o=-. .--..-..-.-o-o#-==..
    -ooooo#########oo=  --=.-=-==-....---.  .-==-..-==o---==oo=---......o##o-oo.
     oo#o=------===-    --...==-.-.   .--..   -==-.=oo---.=-ooo= ... ..-..-.-=.
    -.                  .-.-.-----    ...........--... ...--=oo==.  =-. .--..
                        ---......      ..-.........=   ....-.....--... -=..
                       .o--.....         -...-.-..--            -.--- -..--
                       o-...-..           .--------=            =..o=.-.-.-
                      -o=-..---            ----===-.            --.-==.....=
                     .#==-.--              .=-====-             =..=..-oo=..
                    .##o=--.               .======o            .---oo---=--=o.
                   -#o=--.                  =======            .=--o#   ==-==o
                  o#==-.                    -=====             .--=#o    -..=##
                -=o=-.                      -===-.             .== -.     .o===o
                =-=-                       .-===-              .-=          o=...
               ---                         -====               -....         ==.-
               -=-                         =o==-               -=#o           -=== .
              --=                          ===-               .-#-             .=o- .
             -==.                         --=--              =o-.o              .-- oo
            -===                          .=--.=            .. .-                 .o.#-
           -o==-                            ===o          ...---                  ..===-
          --..-                              -oo-     .==--=o                       =-.-=
       =o-.                                   =o#=  ---. -..                          ==-o
     ####.                                     o=-##o=.                               .==---
    #####=.                                     =###o-                                 ..---=-
   =###o#.                                      o##o.                                      -.
"""

PANGOLIN = r"""
                                             -==ooooooo=oooooooooo===ooo##ooooo#ooooo#o=ooooo#o-=o=.-==oooo===oooooooo=======o=oooooooo==oo===--
                                           .oooooooooooooooooooooooooooooooooooooooooooo==ooo=-=oooo======-===oooooooooo======ooooooooooooooo===
                                       .====ooooooooooooooooooooooooooo=ooooooooo=oooo##=oooo=oooo#oooo=---====oooooooooooo===ooooooooooooo===oo
                                      ==ooo====oooo==ooooooooo=oooooooooooooooooo==ooo==oooooo====oooooo#o=======ooooooooooo======ooooooooooo===
                                     ======oooo==oooo======ooooooooo=ooooooo=ooo--==o=-=======o====ooooooooo=======ooo=oooooo=====ooooooo==oooo=
                                    =========ooo=====oo===oooooooooo==-ooo=ooo=-==oo=---=====oo===o=oo===ooo=--=====o===oo#=========oo==o==ooooo
                                  -====o=====o=oo==o=oooooooo=o====-.-======-..====..----====o=.-==ooo=ooo#o====-=======oo===o==oooooo======oooo
                                .====oooooooooo=======oo========----====---..-=o=- ..--=====-. .-===--=oo=.---=ooooooooo=.-=====oooooooo=======-
                              -========oo=====oooooo==oooo=====... .=---==.-----. .-=---=..   .-==--==o=-.-.---=====oooooo=========o==oooo-==-.-
                            .==-=========oo===oooooo==ooo=o==----...  ...-==.--. .=-=-.    .--=-.--==-=oo---==========oo#o=============oooo=..==
                           ====-=oooo==oooooooo==ooo========o=-o--..     .--..-......    .--.  .---=o##-.-=-=---====ooo=ooo================oo===
                          =====o=====o======ooooooooo====--=--=====.-..   ----....  .  .=-.   ...==-.  .-===---========ooo#o==================--
                         --=-====oooo=-====o===o===oo===-----------....    .==-... .-...     ..-.  . .-===ooo=-=====-======-======-==========---
                       .-======o=========ooo====oo==------------------.... .-==-... .--..     .  .=o--=====o============-.-===oooo===========---
                       -======o========ooo=oooo=======------=-=-==--=-.-.. .--=--.  .... .  .   -=o#====ooooo======----..-=========ooo=-===-.---
                      .---=======oooo=o===============--=-======--===-..--..------.  . ....   -=o#o=--===oo##o=======. .===----======oo=-..-----
                      .---=o==-===o====o=====oo=====------..    .--====-..-.----.---...   . .=oo-....-=o=---..=========================o=----===
                       .---o=========oooooooo======----=--...  .===-==--===-=-...... ..     ..-=. ..---=ooo========--======--=============--====
                       .-=====o--===o==========--.------..     .=------..--=-. .  .       .=oo- ..---========--===--==o=------==----------------
                       .--=--=o==================------.---=-------------- .     ..      .--   -..----==ooo=-==----==--====----------==-.-------
                        .---===============o==-==-------..---=..-.. ..---- ....-.. ..   .  .- -=---==--==..---==o=.. .--=====-.------.. ..------
                         ---==--================---------...   .-. .----..=o=oooo=----.    ...-========-.-------===--.------===-... ........  .-
                          .--..--===o======o-==----------==-.-.......-. .-=--o####oo=.-#o==--.-===o====oo---=====----..--------=.    ...  .=oooo
                           ..-=--====--=====-====-=--------=--..---.... -=-...=oo=-.   .oooo---==-===ooo=----====o-..-------...-.    .=o=====o=o
                            ..---------====-------==-==--=--.-----.--  .--..-.    .-===- -o=-....-=-  ..-...--.   ..-------..    .-=oooooooo=ooo
                             .-.-----======--==========-----....--..  .--.=-=oo=---ooo===---.-===----........--......-......-=oooo=oooo=========
                               .--==-=---=-==========-----..----.... ..-.---====-.-#oooooo=--=-====-==---==-------   .--ooooooo=o====o====-===oo
                               .--====-===ooo======--------.......  .....--------. -oooooo-.=====--=o==------------=oo======o=o===oo==oo==o=====
                                .---========-=---===-----........ ....--==-.-.--. ..-ooo-.=-..ooo===o-.....--=oooooo===o====oo=ooo==oooo====oo==
                                .------====-...-------==---..  .......--==--.---.---..-===---.  .-==. .-==oooooo=ooooo==ooo===ooooo======oo=oo==
                                .-----=ooo=. ....---==o-=-..   -.....---=--..--..-=-..-=------..  .=oooo=o===oo=ooooooooo=====o==oo=--====ooooo=
                                 .-------..  .....-----.-  .. .-.....-===---.----==-...---...==o=oooooo=ooo==ooooooo==o==ooo==ooooo==o==========
                                 .........  .-...... ..    ...--.....-===--- ...----.     .=o===oooo==========--======oooooo==o=o==oo===========
                                   .. .....-.....------...   ..--.--.--==--.    .-..    -==o=====o=ooooo======oo=oooooooooooooooo==oooo==o======
                                        .....=o===-.-----....  -----..-==--     ..    =o===o========ooo==o=-======ooo=====ooooo===ooooo==o====--
                                          .-=o#=...  ..-----....----..--=-.        -=ooooooo==o=oo=-=====o=====oo=============o====o======ooo===
                                          .=oooo-.....   ........---- .---    .---==========o===o=oo=======oo==oooo=======oooo==================
                                           -ooo#=.....--...   ....---. .--   -====o======o=ooooo==oo=ooooooo====oo==============================
                                            =ooo#=.............    ---  .-- .o==---========o======o=----===oooooo=ooooooo========ooooo===o======
                                             -=oo#o..      .......  .-... .=oo=======oo=--===o================--=============ooo==ooooo=ooo=====
                                              -=oo#o-...            .....=o---oo=o====oooooo==oo======oo========--=======oo====oo=========ooooo=
                                               -ooo#o-..... ..  .....-======ooo======ooo===oooo=======ooo======--=ooo===================----====
                                            ....-=o##o-..-----..-=o==o==o=-==--==o==--=====ooo==--..-=ooo==ooo=============================--..-
                                          ....--..-o##o-.---..-========o===o=-===o===-=oo====----============ooo===========oooo=================
               ..                        .----------=##=....-=====-====o==o====ooo=o==o==o====ooo===-==========----===o=====================ooo=
               -oo=         ...--====----------------.------=o==oo==-===o===-=o=========o=====-====---=====-======ooooo=====oo==============ooo=
           --===o##o=.-o#ooo##o=======------------------..-=--===oo===-====o======o==oooo=====o==o=---=====o===========o=========o==============
        -===--==oo##ooooooooo#oo=o=-..--------------------====ooo=oo=====o======ooo=oo====--====ooo==--==o=----=--=========ooo================--
     .======-===-....=o##ooooooo==-..-----==---==---------===o=--ooo=ooo==oo===ooooo=====o=-------======--==================o===================
"""

FOREST = r"""
                                      [ GATE 2 ]
                                          ||
                                          ||
  .---------------------------------------||---------------------------------------.
 /                                                                                  \
|   ☘         ,,,             ❀                                 _/\_      Ѫ         |
|   "        ((~))            " {===================}         _((~))_     "          |
|           ((~~~))             |     Wolverine     |        ((~~~~~))               |
|   Ѫ         |||               {===================}          |||||        ❀        |
|   "        /   \         ☘                                  /     \       "        |
|                          "                                .-----------.            |
|                                         ,,,               |  Silver   |   ☘        |
|                                        ((~))              |  Gorilla  |   "        |
|  ❀                                    ((~~~))             '-----------'            |
|  " .-----------.                        |||                                        |
|    |   Jaguar  |                       /   \                     Ѫ                 |
|    '-----------'             .-----------.                       "                 |
|                   Ѫ          |   Lynx    |                                         |
|              ,,,  "          '-----------'                     ,,,        ❀        |
|             ((~))                                             ((~))       "        |
|            ((~~~))                                           ((~~~))               |
|              |||                                               |||                 |
|             /   \                                             /   \        ☘       |
|                                ❀                                           "       |
|     {================}         "                                                   |
|     |    Capybara    |                 _/\_              Ѫ                         |
|     {================}                _((~))_            "                         |
|                                      ((~~~~~))                                     |
 \         ☘                             |||||                                      /
  '--------"----------------------------/     \-------------------------------------'
"""

LYNX = r"""
                                                                                                ............
                                                                                 ..==o#@###o@@@@@@@#@@@@#######=.
                                                                           .=#@@@@@@oo@@##o#@#o#@#=o##o@@@@@@o#o#@#=.
                                                                       .=#@@@o#@@@o##o#####-oo==o=o#ooo==o##o##oo#oo@o-.
                                                                     -#@@@@@@#@#o####@@@#o###oooo=--o=o@##o=#o=oo=o=-==o#o-.
                                                                   =@@@@@@@###oo###-==-==o#@o-.ooooo#o##==o==o#o---=#@@#oo#@@#.
                                                                 -##@o=@#ooo==-=-o#####@@@##o=-.==oo=#@####==#oo=ooo#=-----=-o@#=.
                              ..                   ..  ..=ooooo@@@@@o#@#=o#####@@#ooo@##o==o=-==--=@@@@@#ooo@@#oo==o=o=-...-.=##@#=
                              ..                  ..o##@###o@@@#o#o#@#===ooo=o@#o@oo#oo=ooo---=-=#o#@#o=o==#=oo-===-=-..-----=o=#@@o-
                               -.            ..---=-=##oo##====#@o===o####o##oooo###@@#==o====-.o@##=oo===o#=-=--==----.---.  -oo=#@#o--...
                               .#-...   .=@@@@#=oo=-=##o=oo--=oo===-ooo=-=######o==oo@##o-=-=-.o#====.---##o====---..-..=-=.   .ooo===......
                                -@o...==ooo####o===---=oo==--=##o=-=====oo#####o#oo#@##o==-...ooo==o=----o@#o=-.-.--------.      .--....  .
                                .#@#===oo#o#ooo=o==-.===---=o=-..--.-===oo#oo##=ooo==oo-..--.-#o=oo===oo#o@o------.----=-
                                 -#@@oo#o####==-==oo==oo-...----...-.-=====ooo=====ooo==-=-..=@o###o=ooo##o-....----==-.
                                 .#@##oo##ooo##o====-=-==...---..-===-.-=oo=--=---==--.--.-..=oo##o####o=-...-.---=-=.
                                 -@@@#o##@#=oo#ooo-.=--.=-....----==--...--=o=---.--.----.-.-=#=#@@##======---..-==.
                                 -@#@ooo=o==--o-=-o--=-.--.---------......-----------...-..---#@#@@oo##o-=--------.
                                 .#@@ooooo##==-==--=o=---.-----------=---......-....-..-..----=###@@o=-==--.--.-=-
                                  .=#oo=o#o@@o-.-.####---....----.........-........--...-.-==-==@@#ooo=----...--=-.
                                    .-##ooo##=---==. -----........-.-..--..--....---------.     .o@ooo=-.--..-===--.
     ..                                 .====---.   ..====--.......-====-.....---=-..             -##==o==----.-=...
#oo--.                                             ..  ..===---..--------......                    .-@#o===-----=-...
=oo####o=.                                                 ..-=-------......                         .=oo=---.----..
----===oo#@@@o=-.                                           .--.==-..-..-..                            =#oo===-.-..
-==-------=o#o-=##@@@o-..                                  -o==------...                               .##==oo=-...
-----===ooo===o=-..----=o####=.                          .oo=------...                                 .##=-o=-...
------.---==oooo=oo----..----==o=o####o=-..      ...=. .=@#===--.....                                 .o#===--.
===-----=----==-=====--------------==oo=o#@@#######@##@@@#o=--.....          .....                ..-=@#=o=-..
====ooo======-==---------------=-===========-----...@@@@#o---...---..--.....------=--..     .-#@@##@##oo==-..
=====o===oo===o=======----------========o-------===-#@##=----..--==----.-------------.-=--..o#@o=o###oo=-..
oo=oo==oo=--==--=--==o========--=------=o======--=--=@#o-----.-=--.....-----------..------=----##=-..-..
ooo=======-------=======-------=-==o#oo==---=====--=o##o#=o=--=--.....-==o=-------....--------=-..     ............
oo=========o====----====----------..--======oooo=..-##oo=---......---=====--.----------------.----========---==========o=====--...
===-------====oo========------------....---=--------##o==-.-..-=====-==-==---=----=---=======---==--------=oo==--=o#ooooooo=====ooooo#o=--....
=====---==o=---====o====--------------====---====oo======--...=====---..-..---------.----------===========#o.-=====---ooo=o##o==oooooooooo==oooo
=================--=====----...---====oo=o##o====-.--o===----====-..---....--...-.----.-----------=====ooo#o=-------===oo---======o##ooooooo==-=
=======================-----....--======-----==oooooooo==-....---......--..-.--...--=-..-======oooo======oo##ooo###o#o=---.-==-=o##oooo==oo==--=
----==================-----.....................--==oo==o=---.---......---..-==...----...-===oo====oo###o=o=oo--.---.......--=====o=ooo=====----
...-------==========-------............................--==o----.-=.---.--........-===-..--===o=o==o=oo#o=o#oo-....   ......---------=----------
..........-----=-----------............---.............  ... .=---=--......--.......--..-==-.==-=-====ooo###=-----------=-===oooo====--------.--
"""

CAPYBARA = r"""
                                             .-==--.
                                            .===--==o-
                                           =oooooo==-======---==------...
                                          -=-==------==ooo#oo##ooooooooo########ooo==..
                                          .---------==oooo########oooo#oo##o##ooooooo====-.
                                           .--------==oo########oooooooooooooooooooooooo====-.
                                             ------=oo==---==oooooooooooooooooo###ooooooo#ooo==-.
                                              ------===-.....--=ooooo=oooooooooooo#oo##oo#ooooooo=.
                                                -==oooo-....-===oo==oooooo=oooooooooooooooooooooooo-
                                                 -oooooo==ooo=ooooooo=ooooooooooooooooooooo===ooooooo.
                                               .=ooooooooooooooooooooooooooooooooooooooooooooooooooooo-
                                              -ooooooooooooooooooooooo=ooooooooooooooooooooooooooooooooo.
                                             -oooooooooooo==oooooooooooooooo=ooooooo==ooooooooooooooooo#o-
                                           .oo==oooo=ooo===ooooooooooooooooooooooooooooooo====o======ooo#o.
                                          =oo=====oo=o====ooooooo=====o===ooooooooooo==--------=======ooooo.
                                        .=oo====ooo==oo=oooooooooooooooo=ooooooooo==----....------=========.
                                       .ooo=====o==oo==oo==o========o==oooooooooo==----.. ..-------==-----=.
                                      .=o=o=======oo==================o===ooooooo==-----=--======--====o=-=-
                                     .=ooo=============o===============o=oooooo====---..---===========ooo==-
                                    .=oooo======oo===o=============-===o==o=oooo==---------------=====ooo=o.
                                   -ooooo=============ooo===============oooooooo===-------------=-====ooooo.
                                 .-oooooooo=oooo=ooooo====o=====o====o=oooooooo=====---------------=====oo=.
                              .-ooooooooooooooooo===o======ooo===ooooooooooooooo==-----------------===oooo=.
                     ...    -=oooooooooooooooooooo============o=ooooo=oooooooooo==-----------------===ooo=--
                 ..-=oo##oooooooooooooo####oooooo=oooo=====o=====oooo=ooooooooo===-----------------===ooo==.
                --ooo###oooooooooooo####oooooooooo=o=================oo=oooooo======--------------==oooo-.-...
.            ..-=oooooooooooooooooo#o#####oooooooooo===================oooooooo==-=---------------==ooo=-.-
=============oooooooooooooooooooo#oo#oooooo#oooooooo====-==-------=--====ooooo====------===-=----=ooo#o...-.
==============oooooooooooooooooooooooooooooooooooooo======-----------===ooooo======-=======---.-==oooo-   -.
=============ooooooooooooooooooooooooooooooooooooo======---------.----======o====----=====------===oo=.
=============ooo=oooooooooooooooooooooooooooooo=ooooo=====-----.......-========----------...---===-.
-=============ooooooo=ooooooo=ooooooooooooooooooo=oo==o===------......--.-----------------====ooo-
===============ooooooo=ooooo====oooo=ooooooo=====ooo==oo=-====----------..-----.-------======oooo.
-----......   -==ooooooooooo=====oooooooo======o=o==oo========--=-----.-..--..-..------===o=ooooo.
              -==ooo=ooooooo====oooooo=====o====o=ooo=======---------------.-..-------=====ooooo#=
              -ooo==oo===o=======oooo=o=o===o=oooo===========--------------.---------=======oooo#o.
              -=oooo==o==o=========ooooo=oo=ooo=============----..-------------------===oo=ooooo#o=.
               =o=========o=======oooooo=oooo=o===o=========------------------------======oooooo##=-
               -o============-=====oo=oooo=oo=oo===========-=-----------------------=====oooooo###o=
               .======o=============oooooooooo==o=oo========------------------------=-====oooooo#oo-
                -==============---==ooooooooooooooo==o==-===-=-----------------------=====ooooo##o-.
                 -======-======-=====oooooooooooo===========-=-=---==-------------=-=========ooooo.
                 .-=======-==---=--===ooooo=oooooo===o==========--------------------=-======ooo###o.
                  .-========-=------==ooo==ooooooo=========-=====---------------------=--==oooo#####o=-
                    -=====-=--------==oooooooooooo======-==-====--=--------------------======ooooo#o.
                     ..--------------==ooo#oooooooo=o======-=-------------.---------------==oooo##o-
                        ...--------=-==o#####oooooo====-==------------....-..------...---==ooooo###=
                            ..-----==oo#ooooo===============-------...........----...----=oooooo####-
                                 ..--=====o=====oooooooooooooo=-----..    ....-....------===oooooo###-
                                         .-===ooooooooooooooooooo=               ...------==ooo######=
                                           .==ooo=ooooooooooooooooo=-.            ..-------==oo######o
                                            .=====ooooooooooooooooooooo=-          ..------==ooo######-
                                              -===ooooooooooooooooooooooooo.         ..----====oooooooo-
                                                .==ooooooo=oooooooooooooooooo-          .--=======oooooo-
                                                  -=oooooooooooo==oooooo===ooo=.         .-============oo=.
                                                    .-===oooooo===oo=======ooooo=          -==============o=-
                                                        .-==ooo=ooo===========o=oo-         ---============ooo=-
                                                            -=ooooo=============ooo=.       .--==============ooooo----.
                                                              -o============o====o==oo=.     .--====ooo======oooooooooo#o-
                                                               -=o===================ooooo.   .--==oooooo==ooooooo###ooooo#=.
                                                                .=o=======ooo===o===oooooooo-  .--==ooooooo=-===oooooo###ooooo###=-..
                                                                .ooo=====ooooooo===ooooooooo##=..--=oo####ooo======oooooo####o###o-=o##o.
                                                               -oooooo===oooooooo=oo=ooooooo##oo#o-=ooo##ooo=-..----===ooo###ooooooo.
                                                              -oooooo====oooooooo=ooooooooooooooooo=-=oo##o.         ..-==oooo=.-=oo-
                                                             .oooooo====ooooooooo==ooooooo#ooooooo=oo....
                                                             -ooo===. -==oooooooooo=ooooooo####ooooooo=-
                                                             .oooo-    .=ooooooooooo====o####o#oo==oooooo-
                                                                        -ooooo##oo. .-==oo###oooo- .-=oooo-
                                                                        .ooo#####=     .-oooooooo-      -.
                                                                         .=ooo##o-        -===o=-.
                                                                             ....
"""

SILVERBACK_GORILLA = r"""
                                                 ...-==o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o=-..
                                              ..=oo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@#o-..
                                            ..-o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@#@@@@#o-..
                                          .-=o#@@@@@@@@@@@@@@@@@@@@@##@@@@@##@@@@@@@@@@@######@#####@@#@@#@@@@@o-.
                                       .-=o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@@##@@#################@@@@o-...
                                     .=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@###@@#@@########################@@@o-..
                                   .-o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@#########@##################o###########@@@@o-.
                                ..-o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@#@################################@######@@@#-.
                              .-o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#############################o##########@@####@@@@@#=.
                             .-o#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@#############################o###############@@@@@#-.
                           .-o######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############ooo#############################@@#@@@@@@o=..
                         .-o########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@################################################@@@@@@o..
                       ..=o###########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###############@##@@##############################@@@@@@@@o.
                      .-o############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################o#####ooo#####@@@@@@@@@#-.
                     .-o############@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@##########@###############################o#######@@@@@@@@@o-.
                    .-o############@@@@@@@@@@@@@@@@@###@@@@@########@@########@#@################################o##oo####@@@#@@@@@@@=.
                   .-o###########@@@@@@@@@@@@@@@@#@@#@############o######@##########@@########################ooo##########@@@@@@@@@@@o..
                  .-=##########@@@##@@@@@@#@##############################################################################@@@@@@@@@@@@@#=.
                 ..=o#########@@#@@@@############oo######o#########oo#####oo#####o######################o############oo#####@@@@@@@@@@@@@#-.
                 .-o##########@#@######o#####ooooooooooooo##oo#o#ooo#oooooooooooo###ooo#oo#############oooo#o###############@@@@@@@@@@@@@@@=..
                ..=#ooo#####@@@######ooooooooooooooooooooo#ooooooooooooooooooooooooooo###o#################oooo#ooo#oooooo##@#@@@@@@@@@@@@@@o..
               ..=oooo#########oo###ooooooooooooooooooooooooooooooooooooooooo==ooooooo##o#####################o###oooooooooo##@@@@@@@@@@@@@@@#=.
               .-o#o##################ooooooooooo=oooooooooooooooooooooooooooo=oooo#ooooooo################oo#####oooo==oo########@@@@@@@@@@@@@o
               .=o########o#######oo##oooooooooo==oooooooooooooooooooooooooo==ooooooooooo###oo###############oo##o#oooooooo##ooo##@@@@@@@@@@@@@@
              .=o######ooooooo###ooooooooooo=oooooooooooo#ooooooo##ooooo=====ooo#oooooo#oo#ooo#oooo#################oooooooooo==ooo##@@@@@@@@@@@
             ..-o#@###ooo#####o#o#####oooooo=====ooooooooooooooooo=o=oo======oooooo##o#####################o########ooooooooo=--=oooo####@@@@@@@
             .=o####ooooo####o###o####oooooooo====oo=ooo=o=oooooo=oo====o==oo####@@@@@@@@#@@@@@@@@@@#######oooo########ooo=oooo=--=oooo#o###@@@@
             .-=#@#ooo############@@@@@@@@@###@@oo=oo===o=ooo=o==ooooo=ooo##@@@@@@@@@@@@@@@@@@@@#@#####@####oooooooo####oooooooo=-.-=oooooo####@
             .-o############@@@@@@@@@@@@#######ooo==oo=======ooooooooo#@@@@@@@@@@@@@@@@@@@@@#####@###@########ooooooo##ooooooo###oo--=ooooo###o#
             .o@#oo#####@@@@@@@@@@@#######ooooooo==--=======oooo#@@@@@@@@@@@@@@@@@@@@#####################o###oooooooooooo####ooo#oooo=o##oo####
            .=##ooo#@@@@@@@@@@@@##ooo##ooooo##o==-===oooo###@@@@@@@@@@@@@@@@@@@@@#@#######ooooo##oooo#o#########oooooooo##ooo#####ooooo=oo######
           .-##oo#@@@@@@@@@@@@#ooooo##o===ooo=====oo######@@@#@@@@@@@@@@@@@@@@@#####oooooo=====ooo==ooooooo###oooooooooooooooo########ooo#######
           -#@@@@@@@@@@@@@@@#ooo=oo##o=-=====ooooooo#####@#@@@@@@@@@@#o@@@@####oooo=====---=========ooooooooooooooo==oooooooooooooo####o##o#####
         .-@@@@@@@@@@@@@@@@#ooooo#oo=----==ooooo##@####@@@@#@@##@####oo#ooo=oo=======--------------=====ooooo#ooooooooooooooooo=oooooo######@###
     .-=#@@@@@@@@@@@#@##@#ooo=o##o==--==oo###o#############o###oooooo======o==----.---..-.....------======oooooooo=ooooooooooooooo###oooo#######
 ..=#@@@@@@@@@@@@@######ooo=oooo==---===o######o#########o=ooooo============---.........--......----======oooooooooooooooooooooooooooo######@###
-o@@@@####oooooooo####ooo==oo==------==ooooooooooo##oooo#o=================-----..--===-------...---=========oo===ooooooo#ooooooooooooooooo##@@#
##@#######@@@@@##@######oo===--.....---======oo==oooo==============----=-------.----==-==o=..--.------=-===o===ooooo=oooo###ooooooooooo=oo##@###
##@########ooo##ooooooooo===---.....-------------==oo====------------------------=o=o#o=oo=-==---===========oooooooooooooooooooooooo#oooooo##@@#
####ooo#oooo#o==ooo==========--....-...-.............-...-------.------.-...--------==oo=====--==oo=ooo==ooooooooooooo=oo#ooo=o=ooooo##oo#o#####
ooooooooo#oo=o#@@@@@@@o=-=o#o=--..................................-==------=---===============ooooooooooooooooooooooooooooooooooooooo##oooo##@@#
ooooo=oo==oo#@#@@@@@@####@##o=---..............=====-==...........-===----===-==ooooooooooooooooooooooooooooooooo=oooooooooooooo==oooooooooo#@@@
oo======o###@@@@@@@##@##@@@#o=----...........-======-.........-...-===oo===-===ooooo###ooooooooooooooooooooooooooooooooooooooooooo=ooooooooo#@@@
=oo==#@@@@@###@#@#####o##o###@#=---..........------------========--=ooooooooo####o==ooo###oooooooo##oooooooooooooooo=ooooooo=oo=o===oo#oo==oo#@@
oo##@@##@@@@@@#####oo###oo##o#@@@o=-.----....--===========oooo==o=o########o###o=-==oooo####oooooooooooooooooooo#oooooo===oooooooooooo#oo=ooo##@
###@@######@@#o#######@#####oooo####o------======oooooooo#o=-=ooo#######@#########o=---=oooooooooooooooooooooooooooooooo====ooooooooooooo==ooo##
####@##@@@@@@@@@@######oooo###oooo#####=---====ooooooo#o===######@@@@##@@@####@@#########==============ooooooooooooooooooooooooooo=oooooo====o##
ooo###oo#####ooooooo===-=====oooooo######o======oo##o-=o####@@@@@@@@@@@@@@@@@@@@@@@@@####oooooo======ooooooooooooooooooooo=oooo#oo=oooooo===oo##
oo########ooooooo==---=-===ooooooooooooo###o==oooo=-o############@@@@@@@#####@@@@@#@@@@@##o==========oo=oooooooooooo=ooooooooooooo=oooooooo=oo##
oooo===oo==========----.--========oo=ooooooo#o=--=o##@@@@@@@####@@@@@#o==---------=@@@@#oooo=======o===oo=oooooooooooooooo=ooooooo=oo=oooooooo##
o==oooooooo=====----....-------===========o=o#==o##@@@####@@@@@@@@#o=--.......-o@@@@@##o===oo================o#oooooooooooooo=o==oooo=oooooooooo
====o=======----............-------========-===o###oo===--==o@@#o=-.......=#@@@@###ooo==--=-=======o======oooo#ooooooooo===ooooo==o=oooo#oo===oo
=========--........---......---------------..-o#oo=-........-o=-.......-#@@@@#o=------...---=oo=======ooooo#ooooooooooooo=ooooooo==ooooooooo===o
=========---................------------...-=o==---.----....=@@#o=-=#@@@@@@#####o=oooooooooooooooo==oooo==oooooooooo==ooo==ooooooo=ooooooo======
=======--------..........-...-------------=oo###########oo==@@@@@@@#@@@@@@#####oo##ooooooooooooooo#oooooooooooooooooo=o#ooo=oooo=ooooo#ooo======
=======-----------...........-------------====o#@@@@#oo##@@@@@@@@@@@@@@@@@@@##ooo###ooooooooooooooooo#ooooooo#ooo#ooo=oo==oo=oooooooooooooo==-==
=====---......----.............------.--..----=o#@@#o=o@@@@@@@@@@@@@@@@@@@####ooooooooooo#ooooooooooooooo==ooo=oo#o#oo=ooo==ooooooooooo=ooo=====
===---........--.................-.------.--=oo##@##@@@@@@@@@@@@@@@@@@###o#ooooo=ooooooooooooooooooo=oooooo===oo=oooooooo==oooooo=oooooo=====--=
----...............................-.-.---=oooo####@@@@@@@@@@@@@####oooooo=oo============================ooo=o=oooo=oooooooooooo=ooooooo=oo=====
--....--............................----===ooo######@@###oooo#@#######oooooo=-----=---=-----===---==============oooooooooo=o=oo=oooooooo===o====
.     ..---.......................----===oo=ooo#ooo===o@@@@@@@@@@@#@@###oooo###oooo===--.------------------=======o=oo=oooooo===oooooooooo=oo===
       .-o-.......................---====o========-#@@@@@@@####oooooooo=oo==oo=oooooooo======----.------.---========ooo===o====oo===oooo=o======
        -#o-.....................---========-=--=o@######oooo=o==-o========--====================--------.----========oo=====o======ooo==o====-=
       .-=#@=....................------=====---ooo#o#ooooo====o====--===-===-=-======--======o===--------..---=========oo====oo=========o======-
        .--o@@#o=-.................-----------ooo=oo======-==-==-==o=---=====-----==----------------------=----==-===o==================o===-===
         ..=o#@##=-................---------=================---========-=--=o=----=-=-=-----------------------=======================o====---==
          ...-#@#o=-..................---.-==========o========o======--====--=-=-=---=--=-----------------------================================
           ..-=####o-.....................-===--==-====--====o========--=oo====---==--=----=--------------------======--================---==---
            ..-==o##o=-......-............-----==-=====--==========oo=-===-==-=-==-====--------------------------=====---===-==========-====-..-
             ..-=o##oo==-.................----=======---=o=o===o==-==---==----===-----=--------------------------=====----===-=====----==-----..
               .-==o#o-====----..........------===-===--==o=-=--====-----=---=-==------=----.-----------------------------=-=====--------------.
               .--==o#o====--=--.........--------=--=-=--=o=------o=---=---=-.---=---------------------------------------==----=--------.-...-..
              .=#@@@@@#o==------...-.......-----=--==----=====--------=------------------------------.------=----------------------------......-
              .o@@@@@@@@o==-----.....-.....-.------=-=--===-==-------------=--=-------------------------------------------=----------.----..----
            ..o@@@@@@@@@@o==-=------.......-.-----=-=--------==------------===--------...-----------.--.--------------------------.--..-..-.----
            ..=#@@@@@@@@@@#===--------........----=---=-------------------.-==--------.--.----.---.-..-.------------.--.----.----....---...-----
.... .......-o@@@@@@@@@@@@@#==-----------.....-------------.--=----------..--------..---..---..-...-..--.--.-.---------------.........-.....----
=oooooooo#####@@@@@@@@@@@@@@o==---------......-------------.----------..-....--------.-...--..--......--..-.------.-..---................-..---=
ooooooo####oooo####@@@#@@@####o==------------.-------...---..----.---........----..---..................-..-------.........-........---.--..--==
oooooooooooooooooooo#####ooo##oo==----------..----.--...-....-----------.-.---..-....-..-..........-...-..--------.........................--===
ooooooooooooooooo##oooooooooooo#oo=-------=--------.---....-.----.-------..----..................---...----.-........................-....-----=
===oooooooooooooooooooooooooooooooo=-===--=-------.-.....-..---------...-.---....................-..-..-..................................----==
ooooo=ooo==ooooooooooooooooooooooooo=====--==---------....-......---------=--..---.....--............-....................................---===
==ooooo=ooooooooo=o====oo====oooo##ooooo=======--=-----.....-..-.----=-=---------......-........--..-....................................----==o
oooooooooooooo========oooo=o====oo##=ooo====oo===-=---=---..---..---=====-------.........................................................---====
oooooooooooooo========o==oo=========oo=ooooo=oooooo=====--------------===-=---.-........................................................----===o
=o=oooooooooo=ooo===========o===oo==oo==o==o=ooooo#oo=======-----------=o=--............................................................---===oo
ooooooo#oooooooo====oo==========o==-======-===ooo=o=ooooo=oo======---======---..........................................................--=====o
oooooooooooo============----=-====-=-======-=====oooooooooooooo====o======-----.......................................................---=====oo
#oooo#oooooo===oo==--===-----=----==-----==----==o=oooooo#ooooo=o=oooooo=------......................................................----=====oo
oooooooooooo=o===oo-.=---------==--=-------o==-==ooo#o#oooooooo=====ooooo=------.....................................................---=====oo#
#oooooo=o#oo==-===--.==-------==-------.------=ooooooooo=ooooo===oo=oo==oo=----...................................................--.--======ooo
ooooo===oo====-===---=-.---=-----.----....--===o=oo#ooooooooo=ooooo===oo=o=--=-.--................................................----====ooooo#
oooo==ooo=======o=---------.-----.-..-...-=-======oo=oooooo===ooooo============..............................................----.----==oooo####
o===o=o====o==o===---------.....--...-..--==o=====oo====o=oo==o=========o=======-.........................................-.--------=====oo#####
========o==o=-o==-----.-.--.....--..------==============ooo===oo=o============oo-..........................................-------======o#o#####
=========-===-===----.--.--.....-...-----=====oo======ooooo=o=oo=o=====-=========-..........................................-----=====oo###o###o
====-==o========------.............----===o==oooo======ooooo=o============-=======........................................-----====ooooo##oo##oo
=----======-===---..--......-..-------==o=oo=oooo=ooo=oo=o==============-=========........................................-----===oooo##ooo###o#
----=======--=--=-..-.......-.------====oooooooooooooo=o=oo=======-===-=========o=-...................................-------===oooooooo########
"""

WOLVERINE = r"""
                                                   ....---=-......
                                              .=@@@@@@@@@@@@@@@@@@@@#=..
                                      .=o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o=-.
                                 ..=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#oo==-..
                                .o####@@@@@@@@#oo=o###@####@@@@##o=o#@@@@@@@@@####@@@@@-
                                =oooo##@@@@@#=-=-oo#@@@@@@@@@###o---==o@@########ooooo#@-
                               .oooo##@@@#o=-.-=o##@@@@@@@@@@##oo=-..-.=#oo#@@#oo======o-
                               .oo=o###@o==o#o##@@###@@#@@@@###@#o==-.---ooo#ooooo==---=.
                              .-#o###@@#oo=ooo#@@#@@@@@@@@@#o####o===-----==oooo===--.--
                             .-o#####@#o#oooo@@@@o---.-=o-oooo##@#o==----===o=ooo===---.
                            .-oo##oo##o###oo#@##=..........-ooo=ooo===-==-=====ooo===o=.
                           .=o###o=o#####ooo####o-..........--====oo======o====oo====o=.
                          .ooo###o=ooo=o====o#oo=--..........--======o==----==oo===--oo.
                         -o=ooo##o==ooo==---ooo=--...........---=--=---------====----=o=.
                        .ooo#oo##o====----.=ooo=--...........---====---..-----==---.--o#=.
                       .oooooooo#o=---------====...............-------...--.----=-----o#o-.
                      .=oooo==ooooo------....---.---...............-......-......----=o#oo-
                      -oooooooooooo=---.........-...................................-==ooo=.
                    .=oooooooooooooo=--.-................................ .........--=oooo=..
                  .-###oooooo=oo===o==----.........................................--======..
                 .=#####ooooooo=======----.........................................--=====o-..
                .o@########o####o===--=--..........................................--=====o-..
               .o##@@@@####o=oo===-------..........................................---======..
              .=o##@@@#####ooooo=====-----...........................................----===-.
             .=ooo#######oooooooo====----==----.................................-.......-----.
             .o##@@@###oo##o#oo=====--=--=----......................................-...-----.
            .-ooo=ooo####o=oooooo=----....--.............................................-==..
             .=o==oooooooooooooo===--...................................................----..
             .=========oooooooo=o==----.................................................----.
              -===--.-===o====oo====---.................................................---..
              .-=----..--======oo==---..................................................-...
              .-----....---====ooo==---................................................-...
              ..-=-.......--===oo=------.................................................
               .--..-.....--========--.................................................
               ...-........=---=====---...............................................
                 ...........----=-=----..............................................
                           ..-..-===--..............................................
                             ..--===---......................    ..................
                               .-=o---.--.................        ................
                                 .-=------................       ................
                                   .---.-.................       ...............
                                    ..---..................     ................
                                      .....................    ...............--.
                                       .....................   ................--
                                       ......................  .............-..--.
                                         ...................................--.-.
                                          ..................................---..
                                          .................. ......-.........-..
                                           ................. ..........o...-..
                                            ...-=.................-.........
                                             ..----...............-o.
                                              ....---..-........--..
                                                .........-..-=...o-
                                                  ............o-..
                                                         . . .
"""

JAGUAR = r"""
                                                                  ..-o#o#o=-..
                                                                .-=oo=##-#@@=oo@=.
                                                             ..o##-=#-=#-o#=o=ooo@#=.
                                                         .=#==#o#oo#o#=-ooo=ooooo###ooo.
                                                        =#o@@-#o@#@#=##o==o#oo#oo###@@#o-
                                                       .@#@#-@@@@@oo@o##o@##==o-o-o###@o-
                                                        #@@@@o##@#-@=o####o##oo#oo##o@@#o
                                                        #@@@@#@o@o@o@=o#=#o@o@=o####o@@@@.
                                                        o@@@@@#@@o#@=o@=oo#o#####@o####o#=
                                                        o@o#@@@@@@@@ooo====@#@@#oo@#@@@=##-
                                                       .#@#@@@@###o@##o#oo#@##.#==@@###o=@#-
                                                      .#@@@@@@@#oo-#@###o@o@o=-=o#@##ooooo@o.
                                                     .o#@@@#@o##@o#@#o=##oo###-o#oo###@#@#@oo.
                                                     -@@@@##o@##=#-@o-o@=o#oo.=#-#-o==-@@o=@@o.
                                                    .#@o@@-#@#@#@o@#@#o=o==@=oo##=o###@#@=@@=@=.
                                                    o@#@@@==@@#@@#######ooo#oo#o#####o@@o-@=@#@-
                                                   -@o@@@@@#oo#o=#######o=o=o#@=oo##o@@o=@@@@-@=-
                                                  .@@@@@o@@@@#o==@###@##=o#=o=@o-=#=#o.o@#o@-@ooo.
                                                  -o@@@@@#@@@@@#o#=#@####o=@o-==-@o#@@@@o##=@@=@#=
                                                 -@@@@@@@@o@@@#@@@###@#..o#ooooo@@###o@#=@#@@o#o@o.
                                                .o@@@@@o#@@@@@@@@-@#=-=o===--.#o@#@@@@#@@#-o=-@@=o.
                                                -@@@@@o@@@@@@@@@@o#@@---==-..#@@@@@#-=#@@###@o-@#o.
                                                @=@o#@@@@#-@@#@=-@@#o###oo#####o#@ooo.-o##=oo=#o@#.
                                               =@@#@@#-@@@o=-=#@@@@@@o##=o#=#@@oo@oo==#-=o#@#o#oo=.
                                              .@@@==@@=o@@@@#@@o=--#o#@@oo#o@#@##o.ooo@@#@--=@@#@-
                                             .#=@@@@@@@-...=@@##@@####@#@###=@@@@#o#@@#oo#@oooo==.
                                             =@@==#-=#@@#-#@#o==o###-.o@@##=@@#-#o@@-.o@o.##o-=-.
                                            -@@@@@@--=#@@@@o##==oo#oo@#=-#=#@@@###o@#@#.-@.=o-=.
                                          .@#=.-=o@@=...##oo#==-oo##@o--#@##o@#o@@@@o@.#=o#-@=.
                                         .@@@@@@@oo@o..-##@@o@#-oooo###-.=@#o=#@@@#@=#@@=##==.
                                        -##o@@==o=oo@@#.-#@o#@#=oooooo@@##=-#@@@.-@@@@-#@=#o
                                       =@@@@@@-.@@@@#####-##@@@@ooo-.-##=o@@@-=@o@#.#oo-@#o=
                                      .@#@#.o@@##.o@o##@==#=o@@##@@=-o##@@@@@.@@#@.#o@@#@=#=
                                     -@#.@@#.#@-@@@@#=o#@@@@@@#@=@==##o@@@@@@@@@-@@@#=@-=@@-
                                    .=@@#-o@@@@#@--@-.###o@#ooo@@@#@.@@@@@#o#@o#@@-=o..o##@-
                                   .@@@@@@@##=@@@... =@@@o@=@o@@#@#=@@@@@@@@=@ooo#@##o---@@-
                                  .#@#-o@@.=@-oo#.  -o@o@#o=@o@-@#@@@@@@@#o@o@@o@@@o==--#@@=
                                 .o=@@@@-#@@o@@@- .##=@@@@@@@@@##@@@@@@@@@=#@=##=#-=-.-o=#==.
                                .@@@-=@@o#o@@o-. =@@@@#-=@o...-####-o##@#@@@#o#=o###=o#@oo##o.
                               .=#o@@@-@@#.@o.  o@=o#@-.o@@#o---..##oo#@##=----ooo---oooo=o@@@=.
                               -@@@@@@@@#=#.  .#=@@#@o=@@@#o......---=--o=--ooo-..-=====o#@=.oo#=.
                             .@o#=o@@.-@=-.  o@@@@@o.....=-.....--....-=====oo=--...----......@@@@.
                            .#@@@@#@@@o#.  .o#@=o@#@@#o=-o=--..-----.--=--..--=--.-====--=###@@o@=o=.
                           -@=#-@-=#.@#.  .=@@@o@@#..-##oooooo====-....--.....=-..-oooooo-o#o...o@@@#.
                         .o@#@@@@@@@@o-   o@@o#@@@@--o=####ooo----=o=-====-==oo==ooooooo#####-o@#@#.-#.
                        o@@@@@@@@@@#o-   .#o@@=.=@#oo.o#######oooo=-oo=..--..ooo=#####o###o=oo-o@#@@@@@o.
                     -#@@@@@#o@@@@@##.   -o@@@=..#@@@#=.oooooo=o##=o-==-=--==.-o#####@@###==#@o##@o##-..=-
                  .#@@@@@@@@@@@@#ooo.    =o=@@@@#=##@--oo.o####o-oo-=-...... .==o--.o@o-o#-=-=#=.##..o@@@@@.
                 -@@@#@@##o@#=#@#@=.     =@@@o@-..o#@###==ooo#-..#o.           .=@@@o.#-...--#@@@@@@#@@@@#..o.
                 #@@@@@@@#@@@@@@=.       o#=@@@@@@#@-.o@#o-.o#==-.                .=oo@@@=..#@@@@###@@=.o@o..o#-.
                 #@@@@@@@@##o-.         .@o..-@@#..@##=#=-o###-.                     -#@#o@@@@@@@o@@@@-.o#@@@@@@#=.
                  ........              .@@@.o@@#=#@#@###ooo=                           .=o@#o@@oo@@-=o@@@@@=..=@#==.
                                       .###@@@#@@##o-#o=o--.                               .o@@@@@##o#o=###@@@@@@=.=@#.
                                        -@@@@-..#@@-#-oo=.                                    ..-.--...=@@@@--o@@@@@@@--.
                                        .@o=o###o-#@oo#-                                           .-=#@@@o--o=@@@=-.=@@@.
o-.                                  .-#@o#-.=@@#=@o@#.                                                 .o@@o#@@@@@@@@@@o-=.
o=--                              .#@=-o@@@@@@..o##ooo.                                                    .-#@@@#@@@@@@=.=@.
.oo@@o.                     ..=-oo#@=o=o@@@@o#o#o=###o.                                                      ..#@@@@==..-@@@@=.
  .-#o@@=.           ....-o#=-o@@-==oo#o-@#o@#-=-=-=..                                                         .o@@@##@#@@@@@@@-.
        .-ooo#o#o##oo@@@=-oo#=@@@o==-..  -@@@@=oo=#@o.                                                            .#o..oo#@@@@@@#.
           .=@#o-=#@@##o###=-....        -@#@@@@@@@@-.                                                              .-o@@@@oo#@@#o
             ......                     -@@@###@##@@-                                                                 .o@@@@@@@##-
                                     .#@@@@@@@@@@#@-                                                                    .--o@o=o.
                                    =@@@@@@@@@@#@oo.                                                                         .
                                    .=#@@o@@@@@=-.
                                         ...
"""

REPTILE_HOUSE = r"""
====================================================================================================================================================
                                                         REPTILE & AMPHIBIAN & OTHER BUILDING
====================================================================================================================================================

               +---------------------------------------------+--------------------+--------------------+--------------------+-------+--------+ 
               |               The Indian Gharial            |                    |                    |     Danube         |                |
               |                  Crocodile                  |      Axolotl       |      Jerboa        |     Crested        |   Amazon       |
               |                                             |                    |                    |     Newt           |  Mata Mata     | 
               +=========|=========================|=========+====================+====================+====================+================+
               |/ / / / / / / / / GLASS / / / / / / / / / / /|/ / / / GLASS / / / |/ / / GLASS / / / / |/ / / GLASS / / / / |/ / GLASS / / / |
               +---------------------------------------------+--------------------+--------------------+--------------------+----------------+
  [MAIN   _____|                                                                                                                             |
 ENTRANCE]_____                                                                                                                              |
               |             o                   o                     o                          o                     o                    |     
               |            /|\                 /|\                   /|\                        /|\                   /|\                   |     
               |            / \                 / \                   / \                        / \                   / \                   |     
               +--------------------+--------------------+--------------------+--------------------+--------------------+----------------+---|    
               |  +-----------------+  +-----------------+  +-----------------+  +-----------------+  +-----------------+  +-----------------+    
               |  |/ / / GLASS / / /|  |/ / / GLASS / / /|  |/ / / GLASS / / /|  |/ / / GLASS / / /|  |/ / / GLASS / / /|  |/ / / GLASS / / /|    
               |  +-----------------+  +-----------------+  +-----------------+  +-----------------+  +-----------------+  +-----------------+    
               |    Worm Lizard     |  Arabia Sand Boa   |                    |                    |   Jackson's        | Snake-Necked       |    
               |                    |                    |   Burmese Python   |  Mountain Chicken  |    Chameleon       | Turtle             |         
               +--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+    

"""


INDIAN_GHARIAL = r"""
                                                                                                         .....--=------=---....
                                                                                                  ....---------=-------------------...
                                                                                               .-..............-.-.---------==-----==---..
                                                                                                                       ....---------=o===-..
                                                                                                                             ...----o#o=o=--.
                                                                                                                                ..-oooooo=--.
                                                                                                                             ...=oooooo##=#=.
                                                                                                                       ..-oooo###o#@#####@@o.
                                                                                                                ..===ooooooo###o###@@@@@@@@#.
                                                                                                        .--==oooooooooooo=o###@@@@##@@@@@@@=.
                                                                                                   .-=ooooo===o=oooo#######o#@@@#@oo@@@@@@o.
                                                                                            ..--=ooooooooo=oo=o==ooo###@@@@###ooo#@@@####-
                                                                                           ..=====oo=oooooo##ooo=ooo##@#@###oooo#@@@#oo-.
                                                                                        .-=oooo=o===o######################=-oooo###=-.
                                                                              ..-.. .-=oooooooooo==ooo##########oooo##@##oo=--oo=o#@@@##=.
                                                                      .....=o##oooo=====ooo####o##oooo####o####ooooo#o#o=o=-....-ooo##@@@=
                                                    .--.            .-=oo==-====ooo=ooo############oooooooo=o##ooooo#ooo===..    .--====o#.
                                                   -#@##@##oo==--oo=ooo=ooo######o######oo@##@########o#ooo#o#oooo#oooo=-.      .==ooooo##o.
         ......                                  ..o#@@@@#oo#######@####oo######@@@@####ooooo####oo###ooo=ooooooooooo-.        .-oooo#oo##.
      .o###oooo###oooo###oooo====-------===oo#####@@@#oo===oo#######@@@#####o#####@###oo==ooo##ooo#ooooo##o=o=o=o-.            .. .o===o.
      ..---=-=----------======ooooooo=o=======oooo###o=---=o====oo###@@@@#o#oo##########ooo#oooooo=oooooo==--.                    ..
            .                         ..........-=o####oo===--====-oooooo###o=oo###oo##o#########o====-..
                                                       ...-=o##oooo==oo#o##ooooooo=o==oo#=oo=o#######o.
                                                                ....--=------.-------......--=o#o#o#o##o.
                                                                                                .=ooo##o-
                                                                                               .=####o#o-
                                                                                               .oooo##o=
                                                                                               =ooo#o-.
                                                                                             .=oooo#==.
                                                                                             .==-==.-.
                                                                                              .  ..
"""
AXOLOTL = r"""
                                                       =--
                                                       o@#.-.-                                        .o.
                                                       =#@=====.                               .    =@#.-
                                                        .o#@##=o   ..                      ..--o..o@@o-=.
                                                       ..=o#@@o-...o                       =-.===@@@==- .
                                                        .oooo#@=-.=. -.                   ==o-=#@@#-==o=. ..
                                             -...        =ooo##@=#=-.=                   .o-o###@@oo===..=..=  ...==
                                            -@@=#=.=-    ooooo##@#=.#==.                .#o-#@@@@o=====o=..o..o=@@..
                                             =@@@@=.#=o. .ooo=###@o-oo.o-             -.-ooo@@@@#==oo==.=.#.-#@@oo.
                                             .@@@@@#-#=#-.oo#oo@@@@o#o#...           .oo#=##@@@@oo=oo..=-o.#@@@#=-.
                                             -oo@@@@@o#o#- =###@@@@@##.#. -o@@@=.     .o=##@@@@#oooo==o#=#@@@#ooo=-.
                                             .=####@@@@####..oo=@@@@@@#o@@@@@@@@@@@@=. ###@@@@@oooo=ooo@@@@@##ooo=
                                               =#o####@@@@@#. .=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o==o#@@@@@@o==##o-
                                                 .o#oo###@@@o...-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###=====o.
                                                .=@o#ooo@##@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@#oo##@#=
                                                 -.#@#@####o#o@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=oooo#@@@@==.
                                           .@@o.. o@@@#####oooo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=o.
                                        ......o@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@###oo##-
                                       .--o@@@@@@@@@@#@@@@@##@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@######o-.
                                            -@@@@@@@@@@@@#######@@@@@@@@#@@@@@@@@@@@@@@@@@@#@@@@@@@##@@@@@@=.
                                         =@@@o..@@oooo###@@@@@@o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#    =@@@@@@@#-.
                                       .#.    .=@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.     .@@@@@@..-#@@.
                                            -#o#@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=        -@@@@@@o
                                         .o#o##@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@#.         .##-@@o-@@#.
                                      .-#oo#@@@@@@@@@@@@@@@@@@@@@@@@@######@@@@@@@@####.              .@-   -@= .=@#
                                    .o#oo#@@@@@@@@@@@@@@@@@@@@@@@@###########@@@#####.                ..     =@.
                                  .o#o##@@@@@@@@@@@@@@@@@@@@@@@@@@@##############o..                          -@.
                                .o#o##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@########=-.
                               -####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######=.
                             .o###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###oo==-
                            =o###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=.o===o-
                          .oo###@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.  .oooo#.
                         -o###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-    .##o#o
                        -o###@@@@@@@@@@@@@@@@@@@@@@@@@@@@-      o@@@@.
                       -o##@@@@@@@@@@@@@@@@@@@@@@@@@@@@-      .#@@@#
                      .o##@@@@@@@@@@@@@@@@@@@@@@@@@@=.    -=o@@@@@-
                     .o##@@@@@@@@@@@@@@@@@@@@@@@@@.         .@@@@=
                     =##@@@@@@@@@@@@@@@@@@@@@@@@#.         .@o@@o@.
                    -###@@@@@@@@@@@@@@@@@@-.              -#.oo#-
                   .o##@@@@@@@@@@@@@@@@-                    .@.@
                  .o#@@@@@@@@@@@@@@@@@.
                  .##@@@@@@@@@@@@@@@@@.
                 .o#@@@@@@@@@@@@@@@@@=
                 -#@@@@@@@@@@@@@#=.
                .#@@@@@@@@@@@@@.
               .#@@@@@@@@@@@@@#
              .#@@@@@@@@@@@@@@#
   -#.       .#@@@@@@@@@@@@@##=
     .#@o==@@@@@@@@@@@@@@#@@#-
        .-#@@@@@@o-.......
"""

JERBOA = r"""
                                                                                                                      .ooo.
                                                                                                                     -####o  .=o.
                                                                                                                    .ooo#oo.=##oo-
                                                                                                                    .o=oooo.##ooo-
                                                                                                                     -==oooo#o#o=
                                                                                                                      =oo#o####o.
                                                                                                                      =o##o####o.
                                                                                                                      -o##o@###o.
                                                                                                          ..         .o####@@@#o.
                                                                                                 .--===oooooooooooo##o##@@@@@###.
                                                                                             .-===oooo#o###o#o##oo######@@@@###@#=-.
                                                                                          .-==o=ooooooo##########o#######@@@@@@@@@##=.
                                                                                        .-==oooo##o##o####################@@@@@#-...oo-
                                                                                       .==oooo####o######################@@@@@@#....o#o.
                                                     ..                              .-=ooo################@###@###@####@@@@@@@@@#####oo.
                                             .-o##@@@@@@@@@###o-.                   .=o#########@##@@#####@###@###@####@@@@@@@@@@@@@###oo.
                                          .=#@@@@#=-.....-=#@@@@@##=..            -o###@#@@######@#@#####@@@@@@@@@@@@@@@@@#@@@@#@@@@@##o.
                                        .o@@@@.               ..o@@@@@##o-...  .=@@###@@##@@@#####@##@@@@@@@@@@@@@@@@@@@@###@##o##o=ooo-
                                      .=@@@o.                       .o#@@@@@@@@#@@@@@@@@@##@@##########@@@@@@@@@@###@###@@@@###-.  ..--.
                                     .o@@#.                                ...-=##@@@@@@@@#####ooo#@@@@@@@@@@@@@oo#oo-====o####o.    .
                                    .#@@o.                                      .o#oo#####oooo=#@@@@@@@@@@@@##-.. .
                                   -#@@-                                          -o#o=====oo##ooo###@#@@o=.
                                  -#@@-                                          .####o===#@@@@##o##oo==-.
                                .=@@#.                                             .....#@@@@@#=---=ooo#@@@@@@@@@@@@@@-
                              .=##@o                                                    -o##@@@@@@@@@@@@@@#o==-=o#@@@@@#.
                    ...... .-o##@#-                                                                                ..
                 .......-o#####=.
              .....--..--=..
           ..-..----.---.
       .o#@@@@o=-----..
      =####oo=-..
"""

CRESTED_NEWT = r"""
                                                                     -==o==-o#o=-.  .-.
                                                                    .==-=o@##oo==--==o-.  .-##...
                                                                    .......#@#o-=--.=-----====ooo=..-.....
                                                                  ..  .-==-=oooo==o===-=...---..-------...........
                                                                   .o-...ooo==---.....-==o=-=.........-...---..........
                                                                    .o==-===---.....-----=##.=-..----.-===---=---=-------....
                                                              .===---==-----..--==---=--..=#o--.----.--=------..-=----.===--=-.
                                                                -==----...-=======-==--=--.=#=-.--===-##o#o=--=--=---====--==---.
                                                          .====--=----.-==--o--=o=-----=.----o=--==oo-#@##@##=ooo#=##@=#o#o##oo#-
                                                             .-=--..===o=======--=o=-o##==-=o=o#@@=-===o#o##ooo##o#ooo#oo#o####=.
                                                         .-oo===--=o-====--===o==ooo##=-o#-==--o@@@o-=#o=o###==oooo==...  ....
                                                            .--=oo=o=-=#=oo======@o#@@==@@@@@o-#@@#--=#@@@@@###-..
                                                     ..-=o=====o==oo-=o#ooo#o##=-##===o#@###o#@@o==o#@@@##oo==-=-...
                                                       ..-==o=o===ooooo#@#@@#=o@@@@#-=@@@o=oo#o-............-=#oo---.
                                                   .o###o======oo==@#o#@@o=#@=..-#@@@@#===..                   .=o=--..
                                                    .-ooooo====o####@o==#@o-.=#@@@@@@@o.                         -oo===-.
                                                     .--oo=ooooo#@#@@#o=-o@@@@@@@#=--.                            .-o#=--.
                                                    .==o=o=oo###@o=-==o@@@@@@@@@@o-.                                .=@=-=oo-..
                                                    .-oo=oooo#oo==o@@o-=@@@#=-==-.                                  .o#-=#@oo=-.
                                                    .=oo=ooo##oo@@@@@@@@@@@@@#.                                            .-#@#=..
                                                   .=oo=#oo===--#@@@@@@@@@#o.                                                    -oo.
                                                  .-oo==##oo#o@@@@@@@o--==.                                                        .=.
                                                 .=oooo=o#o=###=o@#--=o#-
                                                .=-===-=##@#=--#@@@@#o-.
                                            ...-==-------=@@@@@@@@o=-.
                                         .-o#oo=--==o#o=-=#@@@@@@#=oo--=--=.
                                        .=oo=-o@@@@@##-=@@@@@@@@@o#@@@@@#--o=.
                                      .-====#o=oo=---.-#@@@@@@@=....-==ooo=oo=.
                                     .=====o=..oo-.-.-o#@@@#oo-        .-oo#@o=.
                                   .-o=.---=. -oo-.-...-o=---.            -#@#==-
                                  .=o=----==-.-oo=----==----.               .=##@=.
                               ..=o=====---=#=.=oo===----==----................o@@#-....
                              .-..-#####o#@o==@#o=-=o-...-========ooooooo########@@oo@@@@@@@@#o=-...
                                .#o--==-..=o=...-==-==o-..---------=-=-=====----==o@@@#oooooo##########oo=-..
                              .-==..#@-   .##.    .-=oo=--.........---.-------....=#@@#-             ......-==ooo==-..
                             -#o. .-o-    .-o-        ..-.......----.---....        .o@@-
                           .#o.   -@=.     .=-               ...........             .o@@=
                            .     =o-                                                  ...
                                 .@=
"""

MATA_MATA = r"""
                           .=@@@@@@@@@@@@@@@###o##oo#@@@@@@###@########oo#@@@@@@###oo##ooo==--.
                         .=@@@@@@@@@@@@@@@#@#####ooooo##@@######ooooooo##ooo#@@@@@@#####oooo===-.
                        .o@@@@@@@@@@@@@@@@@@@###@##oo####@@@@##@@##ooo####ooooo#@@@@@@@o####oo===-.
                      .-o@@@@@@@@@@@@@@@@@@@@@#@@##@@##o#####@@@@@@######o###ooo##@@@@@@@@@@#o#oo==-.
                     .=#@@@@@@@@@@@@@@@@@@@@#@#@@@@@@@@@@@##@@@@@@@@@@##@####o#oooo##@@@@@#######oo=-.
                    .=#@@@@@@@@@@@@@@@@@@@@@###@@@@@@@@@@@#o#@@@@@@@@@#####ooo#oo--=oo#o#########o#oo=-
                   .-o#@@@@@@@@@@@@@@@@@####@@##@@@@@###@######@######ooo=------.------=-==oooooooooooo=.
                   .=oo##@@@@@@@@@@@@@@@################ooo##o-....--........-..------.............-==oooo=-.
            ..-=o#@@@##@@@@@@@@@@@@@@@@@#####@@######ooooooo=..................----..................---=oo##o.
           .o#@@@@@@@##@@@@@@@@@@@@@@@@@@###o###oo##oo#==-......................=--.-..----............ ..----.
         .-o#####@@#ooo==oo####o@@@@@@@@@o-....--=--.....................-----..-====----====---...
        .-oo########o=-=-===-----....................................-------===--==oooooooooooooo=-.
      ..ooo==ooo=---....----=o==---...................................-=====o==o=-ooo#############oo--....
       ..-.-==-.....   ......-o#@##o=--........  .....................-==ooo#o##o#o=o#####@###########o--==-.
                           .=#@@@###oo==--.....   . ..............--..-=ooo##o##@##==#@#@######@######o===ooo=.
                         .-#@@#######oo===----..................------=oo##ooo#@##@#==@@#o###oooo###@##ooooo###=..
                        .o#@#######o=o===----..................-----=o##o#o####o##@#==#######@########ooooooooo##o-.
                      .-#@#######ooooo-==-......------..-------=====o#####o#######@#=-#@###############oo=oo##o####o-.
                     .=###ooo##oo=--==o=--.....----------===========o#@#oo###=##@#@#==##o###o##ooo###o##oooooo##o#####=.
                    -o#o##ooo===o====-=-=..--...------=============o####o#####o##@@@o-#@@######@#o###oooo##o##o#####o#####-.
                 ..=####ooo=====---===--.    ..-===-=====ooooooooooo###o=o###@###@@@#o#@####=###=-=o##oo##o===oo##@#####=oo#=.
                .-#@######oo=----------.      .-----==oooooooooooo#####=-=##@###o#@#o=o########o=-==##o###@######oo#######==o=.
               .o###oo#oooo##oo#@#@@#o..      ...... ...-=######@@@#o##o=--==#######o-=###o###=---ooooo#############@##o###=....
              .o#oo##oo##ooooo##o#####o.                  ..=########=oooo===#o##@@@#oo@@#####o-ooo#ooo####o=o-o@@@@@##o#@#o  ..
              .-=-=o#oo####oooooo======-                  .-o--ooooo#ooo=ooo###@o##@#oo@@@@##oooooo=ooo==o###o-=ooooo##o=o#o.
              ....=o#oooooo====o=--..=o=.             ..-=ooooo####@@######@@@#@@@@@@##@@@@@#######o##oo#####o--oo=--==oo=-=.
               .  .=o==oo=====ooo=.....               .=###@###@@#@@#o##@#@#@@@o#@@@##@@@@@@#oo##@######ooooo=-.-=-..==o..==o.
                  .--.  .-=#=.-=---..                 .=#####oo###@@@@@oo##o==##o=oooooo#ooooo==oo###oo####o#####==. .=-=.  ..
                  .-.   .-=-.                         .-o####@@####ooooo#@###=-=o#======oo====ooo=#####oo##########-.
                        ...                       .-=o################@#@###@#o=oooo#oooo=o==#@@@@@####ooo#########..
                                                  .-##@@@###oo#@@#####@@@@#@#@##-oooo==ooo=o@@@@@@@@@@@@#########o=.
                                                    .-##@@#@#######o=o###@####@#=oo==o=oo=#@@@@@@@@@@@@@@@#############=
                                                       .-o#########ooo=oo###@@@@==o====o###@@@@@#oo##ooo############o=.
                                                        .-====o#o#oo====oo@@@@@@@#o#oooooo##@@##ooooooooooo####oo=-..
                                                        .-====ooo#oooooo#@@@@@@@@@##oooo#@##o#@###ooooo###oo===-.
                                                         .======--=o##o########o@o=o=oo=o####o##########ooo==---.
                                                         .-oo=====--=o####o#@#oooooooooooo#o#########o=---====-.
                                                         .-oo=======---o#--o#####oooooo##o###o=o##o=-..-===-==-.
                                                         .-ooo=====------=ooooo###@@#####oooo=-o#=---=========..
                                                          .-=====--==-==-..---==##@@##@#=-=====---oo====-=====.
                                                                .. .-======--..-===o===-.....---==-------===-.
                                                                     ..--=====--........-----===----.......
                                                                        -o=-.--=----..--=----==-.
                                                                       -o-.    ..............--=-.
                                                                       -=.                  ...-=-
                                                                        .                     .--.
"""

WORM_LIZARD = r"""
                                                         ......
                                                  .=#@@@@@@@@@@@@@@@#-.
                                            .-##@@@@@@@@@@@@@@@@@@@@@@@@@#o-.                           ...-=====-..
                                        .=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##oo=-......-=o#@@@@@@@@@@@@@@@@@@@@@@#o=.
                                    .=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=.
                                .-#@@@@@@@@@@@@@####################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                             .#@@@@@@@@@@@@@@#ooooo####oooooooooo##############@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
                         .=#@@@@@@@@@@@@@@#######oooooo====oooooooooooooooo##########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.
                     .-o@@@@@@@@@@@@@@@#######ooo======ooo==--===ooooooooooooooooooo#######@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=
                   .o@@@@@@@@@@@@@@@@#####oooo==--.-o#@@@##oo==------=====o=oooooooooooooo##############@###@@@@@@@@@@@@@@@@@@@@@@####.
                .-@@@@@@@@@@@@@@@@######oo===-..  .o#@@@@@@##ooo===----   ...----====o=oooooooooooo######o##############@#############-
               =#@@@@@@@@@@@@@@##@@###o==-..      -##@@@@@@@@@@@@@#####ooo=-----=oooooo==-===oooooooooooo#o#ooo##oooo############ooooo.
             .#@@@@@@@@@@@@@@@@@@@##o=..          -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##ooo======ooo=oo===ooooooooooooooooooooooooo-
            -#@@@@@@@@@@@@@@@@@@@#o-.             -#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####oo==----====ooo========o=ooooooooooooo=.
           .o###@@@@@@@@@@@@@@@@o.                .o###############@@@@@@@@@@@@@@########ooooooo====--..  .--======o==========---.
           .o#####@@@@@@@@@@@@@@@=..               .o###############@##@#@@@@@##########o#ooooo====--.          ..------..
            -######@@@@@@@@@@@@@@@@@@@@o-..         .=o###o#o##o################o#oo#oooooooo====-..
             -o####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##o-..-o####oooo##oooooooooooooooooooooo====-...
              -o####@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o======----....
               -ooo############@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@o.
                .-ooo#ooo##################@@@@@@@@@@@@@####@@@@#@#@@@@@@@@@o.
                  .==oooooooooooooooooooooo#########o#o#############@@@@@@@@@#-
                    .-=================ooo==ooo==##o==ooooooooo#ooooo-=#######=
                        ...---=========---------o#@@@#=-.---===========ooooooo.
                                       ...      .-o@@##ooo---.........------.
                                                   .=@@@@@@@##-
                                                      ..-=oo-..
"""

SAND_BOA = r"""
                                .==========================oooo========oooo==oo##oo=o####oo=oo#ooooooooooooo==ooo###oooo###oooo###ooooo#ooo##ooo
                                  .--================--===========ooooo==oo#oo=oooo=oooo#ooo#####==o####o==#####o=o#####==#####o=######o######oo
                                     .-----====================ooo==oo===ooooo==o####o==o###ooooo==oo###o=oo####o=o#####oo#####==oo###o=oooooooo
                                          ...----========-=====ooooooooooo====o=ooooo==ooo###o=######o=######oo#####==o#@##o=o#####oo#####=o####
                                          ...-=ooooooo########oo##o##@@@@#oo###o#@@@@##ooo=oooooooooo==oooooooo####ooo#####oo#####oooo##oooooooo
                              ..-=ooooooo#@@@#oo##o####@##o###o###o#@@@@@@@@###@o##@@@@@@###@@@@@#o#####o=oo##ooooo####o=o#####oo#####oo####oooo
               .....-=o###@ooooo#####oo####@#@@####@##@###@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@###@@@@#oooo####oo==ooooooooo#ooo==oooooooo
--===oo@@@@#oo####@@@@@@@@@@#oo#ooo#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@#o##@@@####o###ooooooo=oooooo
#ooooo##@@@@@@@@@@@@@@@###@@@@@oooo####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@##oo#####@@##
##o##@o#@@@@@@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#oo#####oo#oo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@#@@@@@@@@@@@@@@@@@
ooo@###@@@@@ooo#@@@@@##@@@@@@@@@@@@@@@@@@@@@@@###@@#@#@#ooo#@@@oo######@###ooo#o##ooo#@@@###@####@@@@@#oo####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@#@
#@#oo#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@#@###@@@@oo####@@@#=oooooo=oooo#ooo#oooooo#####oo#oooo=oo#@@#ooo###@####@@@@@@@@@#@@#@@#@@@#o@####oo@
@@@@##@###@@#@@@@@@@@@##@@@#####@@@@@@@@o==oooo###oo==oooo#@@#oooooooo##@#oo=oooooooooooo=oooooooo#@@#oooo#o####oo##@@#oo##o##o#@##o#@@@#####ooo
@@@@@@#@@@ooo@oo#@@o#@@##o#@#ooooo=o##@@@@#ooooooo##oooooooo#@@#=ooo=o#####ooooooooooo#@#oooooooo#####=ooooo#oooooooooooooooooo###o#@@#ooo####o#
@@@@@@####@##o#@oooo##@@ooo####ooo##@@@#@@#oooo###@@@oooooo###ooo==oo##@##@o=ooooooooo###oooooooooo##@@oooo##@###ooo###ooo###oooooo#@@@#@#oo#oo#
@@@#@@@#==ooooo##o#oo##o==oooooooo#####@#ooo=oooo##o=oooooo#@#==ooooooo#@o====ooooooooo###==o==oooooo=ooooo###o#oooo##ooo####ooooo==o###oooo==oo
@##@@#oo##oooooooooooo#oooooooooooooo#####oooooooooo=ooooooo##@o=o=====ooo=oooooo=o=oooo=o======o==============o=ooo##@o==o=ooo=oooo#ooo#oo##ooo
@###@#ooooooo#oooooo##@@#ooooooooooo#@@ooooo==oooo###=oo===ooooo==oo==ooo##oooooo====oo==oo-===ooo-===ooooo#o=oo===o==##oo##ooo===o=o#oo###o#@##
#@@##@@#==o=ooooooooooooo#ooooo====o##o#oo==o===oo##oo==o=o##o=====o==oooo#===========oo=oo==oo=oo==o=================oooo###########oo##o##o#o#
########oooooooooooo=====ooooooooo###o###====o=====o##=====oooooooooo=oo===================================oooo###@####o#######o#####@@@@@#oo##@
@###@#####====oooooooo##o========o#oooo===========o==o#o====o====o==oo=o============================oo#oo###@@@@#ooooo##oo###oo#####@@@@@#o=####
o#oo=o#o=======o====ooo#o====o===o=oo#o==========ooo===o==oo===============---.......-o##o##oo#oo@####o##oo#@@@@@@@####oooo#oo#@@#@@oooo@@@@@##@
=====o#o=======ooo=o#o=o##o==========oo#=======oo==o=======oo===--..        .-=########o##oo#oo##oo#o##oo#oo#@@@@#oo##ooo#ooo@@@@@@@@@@@@@@@#oo#
===oooo##==========ooo==========-==o===ooo=oo====o==o====-..          .-o#@#@@##@###oo#@@o#####oooo=o#oo#oo#@@@@@###@##@@@@@@@@@@@@@@@@@@@@ooo#@
ooooo=oo============oooo=======oo==oo===ooo=ooo==-..              .o##@@#@#o##########@##@@@@#o=oo=o@@@@#oo@@@@@@o###oo#@@@@@@@#@@@#ooo@@@@@@@oo
oo===oo===============ooo=======ooo=oo====-..                 .=####@@@###o#@##o###o@#o#@@@@@o##===#@@@@@@@@@@@@###ooo@@##@@@@#@@@@@@@oo#@@@###@
======o==ooo=============oo===oo===-..                    .=#@@@@#@######@###@##@#o@##@@@@@#o##oo#ooo#@##@ooo@@##@##@@#oo@@#o#@@@@@@@@@@@@@@@@@#
=oo===o====oo==ooo==oooo===-...                       .-o#@@##o###@#o########oo##@@oo##oo####@#oo#oo#@#####@@oo#@#o####@@ooo#@@oo#@@oo#@@@###@@@
o==oo==oo===ooo==-....                             -###@@##@#########oo#o###oo@o##oo##ooo####@@@@@#@@oo@@@@#o#@@#@@@oo###@@@ooo#@@ooo@@oooo@@o==
====--...                                     ..o=..o@@@@@@#####o#oooooo=o###o=o####@@@@@##@##o@@#@@#@@@oo@@@@#o#@#===ooooo##@@###@@@##@@@##@@##
                                           .=###=oo###@@#@@###o=oo#oooo#oo###oo###@@##@@##@@#o@@o#@@@@#@@@@oo#######@#o==oo===o=oo=ooo=ooo#oooo#
                                        .o@@#oo##=#o#@#####@@###=oo=o###oooo###ooo##@@@###@@@@o#@@@#@@@@@##@@ooo#ooooooo###o@#ooooo===oo====ooo=
                                     .=#####o#ooo=ooo#o@#@@@@#o###oooooooo#######@##@@@#@@==o##@#ooo#o=o###oo##o==oooo=ooooo##oo###ooo####o#####
                                   .o##@@#######oo##o########@@#o##ooooo##############@@###@o==oo@#ooo#===oooo###oo##oo===oo===oooo=oo==o#oo=ooo
                                 .=#####o##oo#oo####o####@@@@#####oooo#@###oo##@@########@@##ooooooooooo#o===o===oooo##oo###o=o###o=ooo=o###o==o
                                -#@@@#oo##o#@#ooo#########@@#@@####@@####oo####o#####o#oo####ooooo==oooooooo=oooo==o===o=oooo#oo==ooo==ooooo####
                              .ooo#ooo####o####@#oo#oooo-oo@@#####o##o@oooo######oo###ooooooooo##o#oo==o===oooooooooo=ooo#o===oooooooooooooooooo
                             .o=ooo=oo#oo##oo######o#-=-..-o#o######o######ooooo#oooooooooo#ooooooo###o==o==ooooooooo==oo======ooooooooooooooooo
                             =####ooo###oooooo####oo#@oooo#oo##o=oo=ooooo=ooooooooooooo#oooooooooooooooooooo==oo=oooooooooo=======oooo=ooooooooo
                             -o##ooo#@@#o###o#####==o####o###oooooo==ooooooooooooooooo#ooo#oooo#ooooooooooo=oo==oooooooooooooooooooooooooooooooo
                             .=oo=o===##o=o##o=#@#########oo#####ooooooooooooooo=oo=oooooooo##oooooooooooooo==oooooooooooooooooooooooooooooooooo
                               -==-==-=o==o==o##oo###ooo##############oooooo=ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                 -=----=o=oo#ooooooooooooooo==ooo===oo=====o==oooooooooooooooooooooooooooooooooooo==----.......
                                    .-=======o==ooo==ooo=oooooooooooooo===============ooo=oooo======---....
                                         ...-=======--........
"""

BURMESE_PYTHON = r"""
     ..=ooooooooo=====o===--========oo====oo#@@o.
       ..-ooooooo=o====-------========oooooo#@@@@o.
          .-ooooo=======---------======ooooo####@@@o..                ......
            .-=ooo=======---------==-=======oo###@@@@o..        ..-=o@@@@@@@#=.
              ..=oo==========---------=======oo##@@@@@@@##=..=#@@@@@@@@@@@@@@@@#.         ......
                 .ooo==========------------====oo#@@#@@@@@#@@@@@@@@@@@@@@@@@@@@#o-   .-o@@@@@###@o.
                   -##o========-----------======o#@@@@@@@@@@@@@@@@@@@@@@@@@@###oo@o@@@@@@@@#@@@@@@@#-.
                    .oo======----==-----------===#@@@@@@@@@@@@@@@@@@@@@@@@@@##o@@@@@@@@@@@@@@@@@@@@@@@#=.
                     .ooo===---=====----------==oooo#@@@@@@##@@@@@@@@@@@@#o=##o=o=@@@@@@@@@@@@@@#####@###o-.
                     .-@@#=====-=====--------==ooo===o#@##o#oo###@#@@@##o=--o=-===#-o@@@@@@@@@#oo##@@@##@@@##=-.
                      .-o#=-===========================oooo=ooooo#@@@o=====#o----=oo@####@@@@#o###@@@####==o#@@#o-..
                         ......======================--=========#@@#oo#@@@@o---=##o#==#@@#@@@##@#@####o##o-===o#o#@@o.
                                .-=============------------===-=-#@@@@#ooo@====##.o@#o#@@@@@@@@###ooo#@@@#==oo#@@@@@@@#=.
                                 -@@#o==========--------------=-==#@#o#####=-o@#--@#@@@@@@@#@@@@##@@@@@o=o=..=#oo#@##@@##o-.
                                -@@@@@#o=========-------------=--=o@@#########@=o#@#o=##oooo===o#@@#o====o=.-ooo@@######@@#o=.
                              .o@@@@@@@@#o=========-----------=#---#@@#oo#@@@@@@#@##@@##ooooo==---==--=-===-===o@@#######@@@@@#-.                                             ..
                             .o@@@@@@@@@@o=o========-----------@@@o---=#@@@@###@@@#@@@@@@@o=====-===----===---=@@@#####@@@@##o#@@-.                                          .#@
                            .o@@@@@@@@@@@@@@o=====-------------##=--------oo##oooo###@@@##@##o#@@o=------=---ooo#@@##@@@@######oo@o.                                       ..o@@
                            =@@@@@@@@@@@@#@@@@#o=------------..-o=oooooo=--=@@@######o#@@@@@@##@@@@=----=o====--@@@@@@@###oo######@#.                                    .=#@@@@
                           .o@@@@@@@@@@@@@@@@@@#===---------.-=====-==o==-=#@@@@@@@@@@@##@@@@@@@@@@@==oo=-==----o@@@#o#oo#o==oooo#o#=.                                   .=#@@#o
                           .o@@@@@@@@@@@@@@@@@@@@@@@@@o=--o@#oo#o--#@@@@@@@@@@@@@@@@@@@@@@####o#@@@ooo=-=oo-.-=#@@@@##@@@@@@@@@@@@@##..                                 .-#@@@@@
                           .=@@@@@@@@@@@@@@@@@@@@@@@@@oo@@@@=oo=--=###@@#@@#o==---oo#o#@@@@@@@@@@@@o=o--.=o#o==ooo@@@@#ooo@@@#oooo###=.                                .-#@@@@@@
                            -#@@@@@@@@@@@@@@@@@@@@oo#@@@=#@@#o#@##o=oo--=####==o=o#o=oo===o#@###@#==##..-========-o@@o=ooo@@o==o###oo=.                               .=#@@@@@@@
                            .-o###@@@@@@@@@@@@@@#o#o==##-@@@@@@@@oo###o-...#=@@@@@@=#@@@@@@@#o--=-==--o--------==o@@@#oo##@#o==ooo##o=..                           ..-o@@@@@@@@@
                             -#@@@oo#@@@@@@@@@@###o##@#@#=-====.--..-=ooooooo#@@oo#o#@@@@@#==oo==-=o##==ooooo##@@@@@@@@@@#@@#o===ooo=#@###o-..                    .-o@@@@@@@@@@#
                              ..-o###oo#o#@@@@@@@@@@@@#==-----------....-ooo-..=o@@@@@@@@@##@oo=ooooo---==----#@@@####oooo=o@@@o==o==@@#o##o=o=.                ..=@@@@###oo#@@@
                               ..-=oo@@ooo==o===o=o@@@==-=-=--------.....-o-........----=o##@@@o=----==-....-o#@o==#oo#=o==--=o@@#o-=@o----=oooo.              ..=@@@@@@##ooo#@@
                                 .-====#o=o#=====-o@@o-=-=-----------...=##o..............----.....--=oooo##@@#=-==o#=oo====----#@o====----.-=---              .=@@@@@@@@@@@@@@#
                                   .-==========--o@@@o---------------..o##=...........-----......-------..=o=o@#=-=oo==--=-------oo=-==-----=----           ..=@@@@@@@@@@@@@@@@#
                                     ..====----o#@@#=---------------...-=o==-..---===-=--......--=oo-....=oo==oo#o---------------=o=--===-===-.-..   ...---=o#@@@@@@@@@@@@@@@@@@
                                        ..=oo==oo=-...----------........-======--..---.......--=--===ooooo-...-ooo#=...----....---===#@#---==oo=-..-=o##@@@@@@@@@@@#=o#@@@@@@@@#
                                            .-=o=========----------====--..-----=--......-===-.---.-==-oo-...-.-==oo-.......---.-===---=o....-=-=#@@@@@@@@@@@@@@###o===o#@###o##
                                                ...-----=====ooo==o=---=o##@@@@@#=ooooo=====-.--..-oo=o====oooooo=-=o====o###oo=oo-....-==--.-=-o@@@@@@@@@@@@@@@@@@@@#oo####o===
                                                        ....=##@@@@@@@@@@@@@@@@@ooo#o-----=o-...=ooo-.......------=o=-----.....-=-......-==--=--o@@@@@@@@@@@@@@@@@@@@@@##oooo===
                                                           .=#@@@@@@@@@@@@@@@@@ooo#o-===--=o==ooo.........----.....-=-........--.........--==o#@#@@@@@@@@@@@@@@@@@@@@@@##oooo===
                                                           .#@@@@@@@@@@@@@@#o@@oo@#=-----======........------.......=o=.....---=-.........o#-.=###@@@@@@@@@@@#@@##@@###oooooo==-
                                                            -=###@@@@@@@@@@@@@#o@@o--=oooo=====-........----........-oo....-----==--.....-o--=#o-=o#@@@@@@@@@#oooo#oo#@ooooo===-
                                                            .=oooo#@@@@@@@@#oo=o@@@##o#o-....--==-..................-==....--==-...---===o=.=o=.-=oooo########o=======o#oooo=-..
                                                            .-=ooo##@@@@@@@@@@@@#=##o-...--..-=--==-................-=-.-..-==..............-=#o--===-=ooooooo======---==oooo--.
                                                             .o=oooo#@@@#@@@#ooo=###=-.----..===-=-==-.............-===--...==-.............-.=o======oooooo==========o#@@@@@@@@
                                                             .-o====o@#===ooooooo=###o=-...........--===-........----..-=-..-===-..........-=-==-=========oo======o###@@@@@@####
                                                               .====o@o-====o====--o#oooo-............-===-...----====-.-===------.........-=-.-======----=ooooo--o###oo===----=
                                                                ..--o@o---====--------=o=................-===--===-o=-.===--..-=------===..-.--======------==oo=------------====
                                                                  .-o#oo=--------------oo=-............--=--====--..-==o=-...........---....-=========------===---------......
                                                                    ...=oo=----------.-oo=-.....-----==o@#=-=o=-....-==-.............--....  ......................
                                                                         ..===-----------=o=---====---=--o@##oooo=--==--.............-=-.
                                                                               .........----==-o@#=-----.-=o===oo====----............-..
                                                                                            .-#@oo#=----..-o=-........-==--...........
                                                                                              ..===#o-....-=-............-===-......
                                                                                                 ..-=oo=-.-==--------.......---..
                                                                                                     ..--==o=---------........
                                                                                                           ...........
"""

MOUNTAIN_CHICKEN = r"""
                                                                          ....
                                                   .-###o=------------=======-==---..
                       .-==-..                  .-o#oooo#o=oooo=====----=oo=========---.
                     .=====o=--.            .-=====oooo=oooo=o#oooo================----==-.
                   .-=--=o====--.         ..-====o===ooo#oo###oooooooo====--========--===o###.
                .-==-------=oo==.        .--=-===ooooo##oo#ooooo#oooooooo====--=====-----==oo##=.
              .-===========--o=-.      -==o#o--oooooo#ooooooooooo######ooo#ooooo====ooooooooooo====-.
            .-===----=oooo=o=-=.  .-=======o=.-o##o@ooooooooo##ooooo#==##oo##ooo===-==o=ooo===--=----==.
           .--------..--..=oo==--===---##-..=o=###o####o#@#@@#o##oo##=.-o##oooo####@@###o======---========-.
         .---.---======o=..-======----===-.ooo###########@#######oo####o--oooooooo######oo============ooooo===-.
        .-=oo====oo===oooo=.---------oo==oo#####=####@@@@@@#@@###o######oooooooo##oooooooooo=o#####oo============-     .-==ooooooo=.
       .=====oooooooooo=ooooooooo------=ooo=####@@@#@@@@@@@@@@##o###@#o############o=ooooo#@@@@@@@@@@##oo============ooooooo#######o.
      .-=ooooo===-==o##o======oooo###=--.=o#@@@@@@@@@@@@@@@@@@@###################oooo=oo@@@@@###@@@@@@@##oo=====oooooo##@@@@#o@@@@#=.
      .==-----=------..---=-====oo#####o=o#@@@@@@@@@@@@@@@@@@@@#####ooo#oooo#oooooooooo#@@=.---o#@@@@@@@@@@@###ooooooo######@@#@@@@@-..
      -==----=------=oo###o======oo##oo#o#@@@@#@@@@@#@@@@@@@@@@@@@#ooooo-........-...............o.--##@@@@@@######ooooooooooooo#@@o...
     .-==-----==--====oo#####@@#@@###=ooo#@@#@@@@@@@##@@@@@@o....-#oo##o-..............-........-......=@@@@@@@######ooooo#ooooo=o#....
      -==---=##@o=oooo##o#@@@@#@@#####=-##@@#=o@##@#=##@###......-oo###...=---..-----==o@=--.........--o.-@@@@@@@@########oo##oooo=-.
      .===oo#@#o#oo@@@@@##@@###oo==o@@@##@@@@@@#-..=-=#@@#.......#oo#...-o#=-.-#==ooo=o@#==-.-------..-.o@@@@@@#o=o@@@@@@####ooo#oo-.
      .-=o==ooo=-=oooooooo=-======-..=-o#@@@@@@@o....=#@@-..-.=#oo-...---==--o=oo###@###@@@o#o-..-=o=-#@@@@@@@@@@@o-.-#@##@#oo###ooo-
       .---=oo===ooo#@@##oooooo=--oooo=#@@@@@@@@@@##@######oooo=...-oo####@##@@@@@@@@@@@@@@@@-=#@@@@@@@@@@@@@@@@@@@@@@@@==-=@##@@@###o.
        -=--=====o#@@@@####ooooo=-=@###oooo#####@@@##@@@@##ooo#=.-@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@o==-
        .=---==oo###@@@@@@@@@@@@@@@oo##ooo##@@@@@@@@@@@@@@@@@#@@@@#ooo-=@@@ooo###@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#==o=.
        -=o=-==oo#@@@@@@@@@@@@@@@#ooo#####@@@@@@@@@@@@@o#@@@@@@@#==-==oo@@@###@@@#o==oo@@#@#oo=o@####@@@@@@@@@@@@@@@@@@@@@@@@##@@@###==oo.
        .oooo=oo#####@@@@@@@#oo#o#o###o##@#####@@@@@@@@@@@@@@@#o#o--====ooo####@@@##o@@@@@@#o==ooo########@#@@@@@@@@@@@@@@@@@#@@#oo======.
       .=#o==o=ooo####@@@#oo@@##oo##########@#@@@o--.--o##o-@#@#=..--======o=ooooooooo###@@#@@@@@@@@@#==---=###ooo##@@@@@@@@@@###oo====.
       .=##==oo####@@@@@@#oo###ooo#==o##@@@@###@@##o===o#o#@#@o=oo==ooo===============-----=-====oo#@#@@@@@@#@@@##oo=======oooo====--.
       .o##o=oo#@@@@@@@@@@#=--===ooo#@@#o##o##oo##oo#@@@@@@@@####oooo##@@#ooo=========oo####o=====--=-===-------===========oo===-....
        -==-..=-==o##@@#o==oo##oo=ooo###oooo#o#oooo##@@@@@@@@@@@@@#o#@@@@@@#ooo=o###o===--ooo##ooooo========---=-..---------..........
        .==o....----==-...-===-=oooo=oooooo####o####@@@@@@@@@@@@@@@@@@@@@@@@###ooooooooo======oooo==o======-..-===-......-............
        .ooo- ..-.--=-...=ooo=.=@#o==oooo####@##########o=o##@@@@@@@@@@@@@##########@#####oo==----==-==-===-==-.......--.....-.......-.
        .===-.  ..-=o#o. .=oooo=oooooooo######@@@##########o#@####oo##@@@@@######@#@@@@#@@@@@o==o=======-.--........................--.
         .=oo==-.  -oo#@o.  ..===oo##==o#o=##@@@@@@#@#oo#o##@@##@@@@@@##o===o==ooooooooooo====---....--.............................-.
          .o####o= .-o####o.   .oo###ooo####@@#@@@@@@#oo#=o.--==o==oooooo===-.                      .........-.----........-...-===-.
                     ..-=o##o.   ==oo#ooo=#@#@@@@@#####ooooo.                                         ... ...-----....--=oo==oooo==-.
                         .=oo###=.=oooooo##@@@@@@@@@#######oo=----=-.                                                -#@@o-.-..===-.
                           .===o##o-oo#ooo##@@##@@##@@o====-=@@oo#@@@@-                                           .=#@@o.    .=##o.
                               ..oo#o##ooo######@@##oooo=-=o#o#o=-..##@@-        .-.....                        ..=#o=-.     .#@##.
                                  .=##=o###o###oo###oooo#####@@#oo==#@@#o####oo####@##oo.                      .o==-.
                                     .-o===ooooo####ooooo###o#ooo###@###@#@@@#@@@@@@=
                                           .-=o#oo==oooooooo##@@@##o=--.....    .-=-.
"""

CHAMELEON = r"""
                                                                                                                ...
                                                                                            ......-ooo=-=#@#@o=o@###oooo----.     .-==o=oo=-.                                                  .
                                                                                    .---...=##oo@@@#ooo@@###oo###ooo@####@@@@=-..##oo=====oo@@#-.                                     ..--o####-.
                                                                            ..----..o##o##@##o#o############o#o##o##o#oo###oooo####o=o=========o@#-.....-=o#@oo-..       ......-=o###@##ooo=-.        .==.
                                                                       ......=oooo####o#######oo##################ooo######oo#oo#oo#o============#@@@@@@@@@##@o##@@@#@@@@@#####oooo===-..--.      ..o@@#=.
                                                                   ...-=#oooo#ooooooo#o##o#############o#####oo#o####o########oo#o@@==ooo==ooooo@@@@@@@@@@@@@##=#ooo=#@@#@@@@@@@@@@@@@@##-.    .o@@###o.
                                                               ..-o#o#@#oooooo#o####oooo#o#o########o###o######o#o#############@#oo=o=o==oooo#@#oo#@@@##@@##o##@#@@@@@@@###ooo#ooooo=.. ...-=###oooo=.
                                                            .-=###oooo#####oo##oo#o###o#o####o########=######o#####o#o#o####@##======o#@@o#o==-oo@@@@@@@@@@@#ooo#####ooooo==----....-=o####ooo===o-.
                                                         ...-oo###o##oo##oo##o###o#o###ooo#oooo####o########@@###########@##o#oo-==--=o---.----=#@@@@@@@@@@@@@#o-o##@@##@#@@@@@@@###oo#oo=====-..
                                                       ..o#o##=oo#o#########oo##oo#o#oooo###o######@##########@@@###@@@@#oo###ooo=-=-======-=====#@@@@@#o-o@@@###==o==#@######@@@##ooo=====-..
                                                  .-=o##ooooo##o##@##@##oo##ooooo########@##@@@@####@#@@#####@##o#@###@#####ooooo====o==========o@@@@@@@@@@@#@o#======ooooooooooooo=--..
                                               ...=ooo#oo##o#oo#####oo#ooooo###########@@###@@@@@@@##o#o####@@@@@@@#@##########ooo===oo===ooo=====@@@@@@@##@#oo===-===oo========-.
                                              .=ooooo#oooo###o##oo##ooo###o@##@@##@@@@@@@@@@@#@#@###@####@@#@#@@##@###########oo#o==ooooooo=oooo====oo#o#ooo=ooooooo=oo========o=.
                                          .=###o#ooo#oo#o######o###@###o#########@@###@@#@@@@#@@##@o####@#@@@@@@########@######ooooo###oo=o#oooo=ooooooo===oooooooo#oo#ooooooooo-.
                                       .o##ooo##o#########oo##oo####@##@#@@@@##@@@@@@@@@@@@@@@@@@###@@@@@@#@##@#################oooooooo#o===ooooooooo=oo#o###oooooooooooooo==-.
                                    .o##oooo##oo########o##########@@@@@#@@@@@@@@@@@@@@@@#@##@@@@#@#####@@@#@#####o#oooo#o#o########o#oooooo=oo============ooooo=oooooo##o=-..
                                 ..o#ooo#o########o######@@@#####o#@@@@@@@@@#@@@@@###@@@@@@@##@o@####@#######@#ooooo#oooo###o#######o##oo#ooooo====oooooooooooooooooo=-..
                               .=##ooooooo####@##@@##@@###@#######@@@@@@@@@#@#@@@@@@##@#@#####@####################o#oooo#############@########oooo#o########ooo=-..
                            .-#@#ooo#########@@#@@#@@@@@########@##@##@@###@@@@##@@@@########@##@##o##o#@##oo#ooooooooo###oooo###oo#######################o=-..
                         .-##o########@@@@@#@@@#@##@@###oo###o##@@@@@##@@###@@##@@@@####@###########o@###ooo#oooooo=##o##ooo##oo=#o################@@#=..
                      .-#########@@#@#######################ooo###@@#######@##@@###########@###o###@####o###ooo#o#oo#o#ooooo=ooooo##########oo@@@@@@@@@@-.                                          
                    .=#@@@@@@@@@#@@###o##ooo=o#@@@@o#########oo==o#######@###o####o##oo########oooo@##oo#oo==ooooooooo==----===oo=oooo##oo=--#@o#o####@##-                              ....=o#@@@@@
                 .-##@@@@@@@#@@@@@@@@@############ooo=####o##ooo=-oo####################ooo###oooooo##ooo=ooooooooo=ooooooo===------==oooooo=--##o@#=##=o@@@@###oooooooo####@@@@@@@@@@@@@@@@@@@#####
                .o#@@@@@@@@@@@@@@#@@@@@########ooooooooooooooooooo==oooo########oo###oo##o###ooooooooooooooooooooooooooooo#ooo##o#o###o#oooo..----o---===@@@@@@@@@@@@@@@@@@##@###@###ooooooooooooo==
               .@@@@##@@@@@@@##@############oo#ooooooo=ooooooooooo==-=ooooo###ooo####oooo####o#o##oooooooo#oooo###oooooooo#oooooo#####oooo-.--==o====oo=ooooooo===ooooooo========o========ooo====o==
              .#@@@@@@@@@@@###@@@@@#@###o####o#oooooooooooooooooooooo=-=ooooo####ooo####ooo#oooooo#oo#oooooooooooooooooooooooooo##oo###ooo=.---==ooo#@@#o#ooooo=ooooooo====o=======--==----===------
              o@@@@@@@@@@@@@@@@#@######o#######oooooooo=o=oooooooooo=o==-=oooo#######ooooo###oo##oo###ooooo#==o@@@@@@@#oooo=oooooo######oooo=.--=-=-o#o=-===o==o=o=ooo===-==-=-====---------------..
             -@@@@@@@##@@@@#####################ooooooooo====ooooooooooo==--==oo##o###oo####ooo#oo#oooooo#@@@@#o-=#o--=====-==--=oo##ooooooo##o--===ooo=------------=---=====oooooo===-------.......
           .-@@@@@@##@##@#@@###o###o#ooo######oo##ooooooooooo===#oooo=ooo===-.--==o#############o#@@@@@@#o#oo--=oooo==-==-----------=oooo###oooo-----==----.......................----...........
          .=@@@@@@###@#o##oooooo#oo=oooo#@@@@=..-------======oo==ooooooooo===-=====o@@@@@@@@@@@@@@#======oooo###oo===---------=---.-..-==ooooo#==-.
           .#@@@@@##@##oo=--=====ooooo#o###o#@@o---=oooooo=======oooooooo==ooo=====-#@@#ooooo=o==o======ooo=---=-=---=--==----.......  ...-=ooo==.
           .#@@@@@###ooo=-=o#ooo======oo######o@o-###oo==-==----=oooooooooooo#oo===---==o#oooooooo#oo=======-------===---.....               ..
           .#@@@@@#@#oo=-o###o==o#oooo==ooo#####@@@#o##o===-.---------oo#####oooo=o=--======o###ooooo======-=====---....
           .o@@@@@@@#oo==####o=oo==o=oo==o#######@@##@@#o=--==oo=ooooooo#####ooooooo==.-========oo===--=------.....
            -@@@@@#####o=####o=oo#@#=o===oooo###@@@#=@@o=--==oooooooo####oo#####oo##o==.-----=---------.....
            .o@#@@####o====oo===ooooo#######oooooo#o-=#=.-==========oo####oo###ooo=ooo==-.---.......
\###@@@@@@@@@@@@@@@@@@@@@##ooo=#@@@##oo#########oooooo##oo==============ooo====ooooo==oo==...
@@@@@@@@@@@@@@@#oo######ooo==oo=#@@@########ooooooooo===o======-=====-----......=oo====-.
ooooooooooooooo##oooooooooooooo#@#oooo=======o================---......           ..
=======ooooo==ooo#oo#o===oo-----oo=========-=====-=--=-----======.
-============oo=ooooo======--==============--------............
==-------===---===----------------======--...
.................        ...--------....
"""

SNAKE_NECKED_TURTLE = r"""
                                                                                                                                                                                     ...
                                                                                                                                                              .......--===o#@@@@@@@@@@@@
                                                                                                                                              ..-=o###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####
             ...------....                                                                                                       ..-=oo#@@@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@###########oo
          .=#=-=====oo====oo===---..                                                                                     ..-o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@####oooo
          ===--.--o#oooo===-=-..--==-.                                                                               .=@@@@@@@@@@@@@@@@############@@@@@#####ooo###oo#########o#####oooo
         -@##oo-...=o##o=--=-..=.oo==-.                                                                          .=#@@@@@@@@@@@##ooo###oooooo####ooo=======oooooo===o========ooooooooooo
        .@@@@@##o=-..=oo=---....--..-=o=..                                                                    ..#@@@@@#####oo==oooooooooooooo==------===oooo======-----------===========
        .#o====#@@@#o---===-..---------==oo=..                                                              .o@@@@####oooooooo===========-------------=====-------------=----======ooo==
        .@@###o===---==oo=---==-----===ooooo==ooo=-.                                                   .-o#@@##oooooooooo======---====---------------===-=-------------------=oo===ooooo
        .@@@@@@@@@#oo=-..-==o----====--====ooo==oooooo=..                                         ..-=o####oo=========-----------===--==----------=--------------==-----------=o===ooooo
         o@@@@@@@@@@@@@#o-----=oo=-.---==--===========ooo=.                                 ..=ooo####oo=========----==-----------==---------====----------------==-----=-----==-=oo=ooo
          o@@@@@@@@@#@@@@@@#o=--------.-------===----o===ooo-                 ..-----===o#############oo===------------------------------...-----=------==------===-----------=--=ooo===
          .o@@@@@@@@@@@@@@@@@@@#o=--===-----------==========o=-..           .@@@@@@@@@@@@@@##@@@@##oo==============-------------------------------------------------------------=oo==o=-
            -@@@@@@@@@@@@@@@@@@@@@@####@o==---------------=--oo=@=-.          ..-o###ooooooooo==-==o#oooo=ooo======================-----------------------.---------------===--==o==oo==
             .@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=o==-------===o=o=ooo=-===-.              ...--oo======ooooooo######oooooooooo=============-------------===-----------------===----=====ooo==
              .o@@@@@@@@@@@@@@@@@@@@@@@@#@@#oo==------------===---=-===-.                   .=o#oo================oooooooooooo==========--------------------------=------===========o==-
                -@@@@@@@@@@@@@#@@@@@@@@@@@@@@o#o===========--.---===.==-==-.                   oo==--=================----...--oo-----=============---------------=--==================-
                 .o@@@@@@@@@@@@@@@@@@@@@@@@@@##@@o==========---=-===-=-=-==---..            .-oo=====----=======o##o===---.................---===oo=====================================
                   -@@@@@@@@@@@@@@@@@@@@@@@@@@@@##==========---==-=--==--=-===-==..        -ooo=====--------====o##o=-.....--.................---==ooooooo###=-.--...--===o#ooooo=======
                     .@@@@@@@@@@@@@@@@@@@@@@@@@@ooo=====---------===-==---.--=.-=--=-.    o#ooooooo======---====ooooo-...................   . ........--------......----===o######o###@#
                       -@@@@@@@@@@@@@@@@@@@@@@@@@o===========---===-==--------=-.-----==-==o==oooo=============oooo==-.......---.-------...............---.................-=##@@@@@@@@@
                         -@@@@@@@@@@@@@@@@@@@@@@#@@#o###o=o=-====----==---==--.---------===-==========-====-=---=-=======---==--------------.................................-=oo#######
                           .o@@@@@@@@@@@@@@@@@@@##@###oo#oo======-==----------.-=-=-=--..-=-===----.==-===--=---.---------==----=--=---.---------..-..-..................-------.---===-
                              -@@@@@@@@@@@@@@@@@@@@@@@@#@@@@oo===o===--=------------==-------------.-------..-..------....--------.--=-----.--.-...--.........-----........----------...
                                .=@@@@@@@@@@@@@@@@@@@@@@@@@@@==ooo==-=-------------------..=-..----------.--.--..--..---.......----------.-----...---........-=oo=---....---------------
                                    .o@@@@@@@@@@@@@@@@@@#@#o#@@@#o======-----.---------.--.-...---.---=.-...--..--.......--.....-....-----..-----...--.....------=-...........----.-----
                                        .=#@@@@@@@@@@@@@@@@@@@@@o###ooo==----.----.----...---.-----....----...--..--...---......---=-------........-----..-....................---===--.
                                            .-o#@@@@@@@@@@@@@@@@@@@@@oo=-=---------.--..--.....----.-.--.-..--.--.-..-----.--.--.----------.......---...........-----...-.--.......--==-
                                                .o@@@@@@@@@@@@@#o@@#o==o=====-=---..----.-...--------..-..-------.....--.--------.---.-........-----.......--------.--------=--.....--==
                                             .==--==o#@@@@@@@@@@@@######oo==-===---=------------....-...----..---..-------------.................--.-.....--====------------------------
                                                .-----..-o@@@@@@@@@@@@@@##o##oo=====--------.---.-----.....---.-..-----------.--..........................----=-=---------.-----=--===-.
                                                            ...-#@@@@@@@@@@@#@#@#o==o==--==---=-------------.----------.----..............-................--------....-...-.-----..-==.
                                                                  ..-=@@@@@@@@########ooo=======---------------------..--.--............................------===---.---.........--..---
                                                                         .-=o@@@@@@@@@@#######o=o#o==--------------------------.....................-...---------------......--......-..
                                                                              .-=o@@@@@@@@@###o=oooooo=o=========--------....----....--...-.........------------.--..........--.-...
                                                                                          ...-=###o#####ooo====oo======-.........-=========================------------......--...-.....
                                                                                                   ...---=----...-------.........-----============---======-------------.--..-...--....-
                                                                                                                                    ............................-----------.--..--...--.
                                                                                                                                                                 ..--------.---.---..---
                                                                                                                                                                    .---------------..--
                                                                                                                                                                      ..-------------...
                                                                                                                                                                             ...........
"""

AQUARIUM = r"""
                             _.._       _.._       _.._
                           .'    '.   .'    '.   .'    '.
  _______________________.'________'.'________'.'________'._______________________
 [_________________________________________________________________________________]
  |     _____________________________________________________________________     |
  |    |                                                                     |    |
  |    |     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~      |    |
  |    |       ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~          |    |
  |    |              o                      O          o                    |    |
  |    |         O                                            O              |    |
  |    |        o                              .             o               |    |
  |    |                                                      .              |    |
  |    |                     ______                      _______             |    |
  |    |                 _.-'      '-._                 <_______)))   O      |    |
  |    |                (_   Manta    _)                  Lamprey    o       |    |
  |    |                  '-.______.-'              O                        |    |
  |    |                        |                  o                         |    |
  |    |            o           |                                            |    |
  |    |       ________         |                                            |    |
  |    |      <________)))      |                      O                     |    |
  |    |         Bichir         |                     o   ____               |    |
  |    |          o             .                      . /_   \              |    |
  |    |         .               .                         |   |             |    |
  |    |       )                                           /_ /   Pelican    |    |
  |    |      (         _  _ _                            / /       Eel      |    |
  |    |     ) \       (_(_(_))           _______        / /                 |    |
  |    |    (   )                        <_______)))    / /                  |    |
  |    |     \ (                         Blue Dragon   (_/          )        |    |
  |    |    )   )  O                                                 (       |    |
  |    |   (   (  o                         _______                   ) \    |    |
  |    |    )   ).                         <_______)))               (   )   |    |
  |    |   (   /      _  _                    Sunfish        ________ \ (    |    |
  |    |    \_/_ _   ( \/ )  _ _ _          O               <________))) )   |    |
  |    |    (_(_(_))  \  /  (_(_(_))       o            Giant Isopod    (   (|    |
  |____|______/_/______)_(___/_/_________________________________________\___|____|
 [_________________________________________________________________________________]
   /                                                                             \
  /    +--------------------------+                         +---------------+     \
 /     | PYTHON ZOO AQUARIUM      |                         |  Do Not Tap   |      \
/      +--------------------------+                         +---------------+       \
/___________________________________________________________________________________\
"""

MANTA_RAY = r"""
                                                                     .-=-.
                                                            .-o##o  .o##o=-.
                                                          .=oo##@@.  .=###oooo.
                                                         .-=oo##o.      .=-.-oo-
                                                        .===oo=.     .-=oo=--===-
                                                       -###==---=#@@##ooo######oo=-.
                                                       -o#o=---o@@#####@@@@@@@@##oooo-.
                                                       -o#ooo#@@@@@@@@@@@@@@@@###ooo#######o==--..
                                                      .#oo##@@@@@@@@@@@@@@@@@@@@#ooo##################o-
                                                      o#oo##@@@@@#@@@@@@@@@@@@@@##oo#@@@@@@@@@@@@@@@#######o=-..
                                                     =@@#o##@@@@@@@@@@@@@@@@@@@@##o#@@@@@@@@@@@@@@@@######ooooo===----.
                                                   .o@@@@####@@@@@@@@@@@@@@@@@@####@@@@@@@@@@@@@@##ooo======-----..
                                                  -#@@@@@@@##@@@@@@@@@@=o@o-#@@@ooo#@@@@@@@@###ooo====oooo=..
                                                .o@@@@@@@@@@@#@@@@@@@@@@#-.-o########@@@@@####oooo###o-.
                                               =@@@@@@@@@@@@@@#@@#@@@@@####@@####oo#############@@-
                                             -#@@@@@@@@@@@@@@@@@@o@@@@@@@@@@@@@##o=#########@@@o.
                                           .o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########@@@-
                                          .o@@@@@@@@@@@@@@@@@@@@###o##=-oo@##o##o#oo#######-
                                         .#@@###################=o###########o-ooooo#####=
                                        -########oooo=oooo#=o#######o###ooooo==oooooo#@#-
                                       -#####ooo=-===ooooooooo#####ooooooooooooooo###@o
                                     .=ooooo======oooo#o######oo####o##oooooooo#o###o.
                                    .oooo=====oooo#########@@@@@@@@@@@####oo#oo###=.
                                  .-o========-..                .-=o#@@@@@@#####=.
                                 .==-===-                                     o
                               .----..                                        ..
                             .--..                                             =
                          ....                                                 ..
                        ...                                                     -
                                                                                ..
                                                                                .-
                                                                                 .
                                                                                 ..
                                                                                  ..
"""

LAMPREY = r"""
                                                                                                           .-ooo#oooooo=-..
                          .-=ooo-.                                                                      =#oo=====--------=o##=.
                     .=@@@@@@@@@@@@@@#-.                                                        ..-=###o==-==o=ooooooo=====---o#o-
                   -#@@@@@@@@@@@@@@@@@@@@#=.                                                .-o@@@@#o==-==oo###o#ooooooo##ooo==--o#=.
                  =#####@@@@@@@@@@@@@@@@@@@@@o-.                                     .-=oo#@@@#oooo==-=ooo###ooo#o=ooooooo####o==--=#-
                 -oo===ooo###@@@@@@@@@@@@@@@@@@@@#-.                     .-=o#@@@@@@@@@@@@@#o==-=#o=-=oo#####oo=oo---o==ooooo###o=---o-
                 -==========ooo#@@@@@@@@@@@@@@@@@@@@@@@@o-.--=#@@@@@@@@@@@@@@@@@@@@@@@@@##o==--o#=--=o#####oo=o... .....--==o####oo=--o-
                .-=============oo###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###ooo===----==--==#######o-..-o=o=--=o#@#o#####o=-.-o.
                .-=-===-==#=..-===ooo###@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@##@@##oooo=====-------oo=--=ooo###o=..-=o==-.....--=o#oo#oo---==.
                 -=-----=o=.    .-====ooooooo####@@@@@@@@@@@@@@@@#@@##@#oooo==-------------....-=---=ooooo##o=...--o==-...===oo=ooo=-..==.
                 .------=o.        .--==========oo####ooo######ooooooo====-----------------------=---=ooooo##===-....-o####oooo==o=--.--=.
                 .------=-.           ..----------=============-=====---------------------------------======oooooo=oo===-==oo======-..---.
                 .------=.                ..---------------------------------....--......-----.....--.----=======-====oooo=======--...-.
                  .-----=-.                    ...---------------------..............................--...-------------=======---......
                   ------=.                               ..-------.................................................----.....-.....-.
                   .-----=o-.                                        ..............                       .........................
                    .---=====-.                                                                               .................
                     .---==o===-
                      .--==oo====
                       ---==ooooo-
                        --==oooooo.
                         --==o####-
                          .-=oo####-
                            -=oo####=.
                             .==o#####-
                               .=o#####o-
                                 .=o#####o.
                                    -oo####=.
                                      .=o#######o=.
                                         -=###ooooo-
                                           ..=ooo=-.
"""

BICHIR = r"""
                                                                                                            .
                                                                                       .o#=.    .=oo-    .=oo=    .o#o-    .o@o.   .=#o.  .o#-    ...
                                                                                     .-===o-  .-====-. .=o====  .=o===-  -=o=o=. .=o==-.-oo==. .=ooo=.  .---.
                                                                                    .======- -oo====-.=#o=o===.=#o===-.-ooo===..=oo====oo===.=##o==-.==oo===...-==-.
                                                                                 .-o#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@##oooo##oo=o###oooo##oo==oo##oooo=======.
                                                           .-=o####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####oooo##oo==o###ooo=====-.
                                        ...---=o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##ooooooooooo#ooooo==ooo-.
                              -o@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@#@#@@@@@@#@@@@@@@@@@@@#######@######@#@###ooooooo==ooooooooooooo=.
                    .-.   .o##@@@@@@@@@@@##o#@@@@@@@@@@@@@@@@@@@@@@@@@#o=#oo###################@#@####@##@#@####@########################o#ooooo##ooooooo==o=====oooooooooo==oo.
                       -#@@@@@#o@@@@@@#=.=..==##o###########@@@@##@##@@@oo=o#=#o#o#o#o###oooo##o#oo###o##ooo##o#o####o########oo#ooooooooooooooooooooooo=========oooooooo=o===o=.
                      .-ooooo####o#o#ooo=-===o############o#########@##@#o=oo=oo=#oooooooooo#o#oo#o##o#o##o#oo#o#oooo#ooooooooooooooooooooooooooooooooo=======================oo.
                         -o########o##oo====oo#########o#ooo###o####@@@#o-=o=ooooooooooooooooo#oooo#o#oo#o#o##o##o#ooooooooooooooooooooooooooooooooooo=================o==ooo=o-.
                           .-o########o#oooo####o####################@#ooo=ooooooooooooooooooooooooo#oooo#o#o##o#o##ooooooo#ooooooooooooooooo=o=ooo=o=================oooooooo-
                                ..o##############oo#########@@@@######ooo@#=oooooooooooooooo#ooooooo#ooooooo#o#oo#o#o##ooo########oooooooo===============-------==========-.
                                       .-ooo#######################o=oo#@@@@@##oo#oo#ooooo#o##o#o#o#oo#o#o#o#o####o################ooo=-.
                                     .--=o####o=ooooooo###########oooo##ooo#=ooooo###@@@@########################################oo=.
                                 .==########==---=-..---====oooooooooooooo==oooooooooooo###@@@@##################oooooooooo==--..
                            .-oo####@#####==o=---=-          ...---====-==-=o=#o=#o=oo#@#########ooooooo====---.......
                          =##@@@####o###oooo====o=.                     .=oo==#=#ooo###=o##o######-
                            .-===-=====-----.--..                        -#o##o##o###o##@#####@@#o-.
                                                                          @@@#@##@@#@@@@##@@@####@=.
                                                                          .o@@@@@##@@@##@##@@@##@=.
                                                                             -#@@@@###@@##@####-.
                                                                                  ..-=oo=-.
"""

PELICAN_EEL = r"""
                                                                                                    ...............
                                                                                                 ......................
                                                                                            ..........................-....
                                                                                        ..-..............-----..................
                                                                                    ..-.......----------------------=--------.........
                                                                                 ......------------------==--=-================-...........
                                                                              ...----------------------=-=------------=--========--.....-----..
                                                                           ..--------------------==oo=-..----.............-----------....-------..
                                                                     ...-------------------==oooooo-.----......................--------.....-------.
                                                              ...-----=--------.-------==oooooooo=-----.................. ........-=----.---.----==--.
                                                        ..----=======------------------=ooooo===--=--... .-...............  .........-===--------------.
                                                 ..------======---------------------.--=========---...     ..............     .........-====--------------
                                           ..------====--=-------=-========---------.-======--=-...               ......           ......-=o==---=------==-.
                                      ..-----========----==============----...........----...-=..                                       ...-=oo---====------.
                                   .-=-=========-----==========------...............--......--.                                            .-=#o---====------.
                                .==-========----========--------...................-----.. .-.                                              .--o=----====----..
                             .-==========----=======--..----------................-.....  .-.                                               .-===..-.-====----.
                          .-=========----======-------------...-.................--.-..  --                                                 .===-...----------.
                         .#o=====------=========--------.-..-....................----. .-.                                                  -===.  .----------.
                         .==oooo=-....------------=-----------...................------.                                                  .==o=-.    .------.-.
                          .-=ooo----.....................-----==-=----..-.......-------.                                                .-=ooo=-      .------=.
                              ..................----.-.....................-------===---=.                                           .---=oooo-        .----==.
                                                             ........--.....-==--.......--=o=. ...                                 -=-==oooo=-         .---=o-
                                                                    ..---.----=ooo====------..     ..-.                        .-=---=oo=o==-     ..--====o=-.
                                                                 ..----------------------..          .o.                    .-==-===oo==o==-.........--=o==.
                                                               .----------=--=----=----.             o@-                  .===-===oo======-........----=--.
                                                             .-----------==========--.                                   .=--======-=====-......------...
                                                           .---------============--..                                     ..=====-=--==-.....----.......
                                                         .---------=============-.                                        .==------===-.-------........
                                                        .---------=-=========--.                                          .-----.-=-===--............
                                                      .-----------==========-.                                             .----==---........-.....
                                                    .------------========--.                                                 ..---..--==o#o===..
                                                  .------------========-..                                                       .========..
                                                 .---------=--=======-..                                                           ....
                                               .-------------=====--..
                                              .----=-------====--..
                                            .--------=---===--...
                                           .------=---====--..
                                          .-------=-===-...
                                          ------====-...
                                         .======-...
                                          .--..
"""

BLUE_DRAGON = r"""
                                                             -.
                                                             --
                                                             --
                                                             --     -.
                                                             -=-    .-.
                                                              -=.    --.-
                                                              .-=.   .=-.-.
                                                               .==.   -#..=. .
                                                                -oo.  .@@.=@= --  ..
                                                                .-@@=. -@@=o@#.#@..#.
                                                                 .-@@@- =@@@@@@o@@o@o .-
                                                ....-=---..        -@@@@.=@@@#@@o@o@@-##
                                                        ..-=#@@o-   -@@@@@ooo#==--==oo@=#@.
                                                             ..o@@@@#=#@@#==--=-------o###o.               --.
                                                                 .=@@@@@ooo=----o@@@@o==#@.            oo=-o#=--.
                                                                   .-o@@#-----#@@@@@@@#@@-          .#@o=--=o==---
                                                                    ..-==----#@@@@@@@@@@#o====-...-o###-.--.--oo@@-
                                                             ..=@@@@@@#o-----@@@@@@@@@@@@@@@@@@@#@@@@oo=o@@o----o
                                                      ..-=#@@@@@@@@@@@@o--=---@@@@##@@@@@@@@@@@@#=---o#@@@#------
                                                                   -#@@#=-o--===---@o###@@@@o=#oo#@@@@##=..-===.
                                                         ...-o@@@#o=----@@#@=o.o=o@o=o#@@@@#o##@@@@@@#-..-o=.
                                                                      =@=o#@#.#o=-. .o##@@-=o@@@@@@#=-..##o=          .- .-.  ..
                                                                     =#. .o- .o.   .oo@@@@@#@@@@@##=-..#@o==.    ..o#@@#@##@#- ....
                                                                    ..           -#@@@@oo@@@@@##o=-..-@@@#oo=-  -@##=#o=#@ooo#=..
                                                                                -#@@@@#-=#@@@#o---==@@@@@@@#oo=o@-------=oo-.-===--.....
                                                                              .=o@@#--=o@@@#=--.=#@@@@@@@@@@@@@@@@@@@o...-=ooo=..  .................
                                                                             -=o@#-=o###@#=-.-#@@#o===oo#oo#@@@@@@@@@#..---=o#@@@@@@@@@#-..
                                                           -o-.  -=         -@@@@@##@@#o=-.=@@@o===----===o#o#@@@@@@@=.--==o#@@#o=..
                                                     .=###==-#@@o=@@=@#    -o#@##=ooo=-..o#@#o=-        .o=.-@@@@@#@o.---=o####o====--------.............
                                                     ... .=@@@@o@@==o@oo  -=#--#####=..=@@o==.            -o.-o@@#=.--.-=-=o@@@@@@@@@@@oo-.....
                                                  .=#@@@@@@##==-------oo=@o#..-#@@#--=@##==.             .=@-..--.-.-=#@@@@@@@o.
                                      ....-=#@@@@@@@@@@@@@#===---..-@@@@o#o---#@@o-.o@#o=               .#@-=o----==-=#=#@@@@@@@@@@o..
                                             ..--=#@@@@#o=----.....@@@#@@-.-#@@#--=@#o-                 -..o@o#@=@=@o=#@@o. .....----=oo=.
                               .....-=====oo####@#@@###o-=#@o=-=-----..o.-=#@#=.-#@#==--o.                -@=-@@=@#o@#.-#@@@-           ..--.
                                                     -@@@@oo@@o#@o@-@o===#@@o-==@@###-@#o#o.              .. -@- o@.=@@=  .=@@-             .....
                                                 .#@@o-..@@@oo@@=@#-#o--#@@=.-#@@@@@@-..=@#oo=.               .  .#.  .#o.    .-.                ...
                                               ..     .#@=.  #o. -  o--#@#--#@@o-#@@#--==o===.                    .      ..      ..
                                                                   o--@@=.-@##@#--.-..--=@@@@o.
                                                           .#oo#. =--#@=-o#=.o@@o-------=@@#@@@#-
                                                         .#@@ooooo.-#@=-#o-  -oo@o===----=@@@@=
                                                   ..-o#@@@@=..o#.-@@-=#o@o=. =@##@@#@=---#@@#@@-
                                                      .-=o@#====--@=-=@@o-=##=  =o@@o@#==o=-@@#-
                                                  .o#@=-=##o=o=--@=-o==-.-#@#-  .#@@=@@.=@@@--@@-
                                                .   .-#@o-.=@o-.#--@o-@o==@o@o   o=  #@. -#@@#.o@=.
                                                .=@@o-.   .=#=.=-.=#@@=@@o@@=        -@-   .o@@o-==.
                                             .-#=.         -=.-=.o#@@##@@@@@o.        =.     .-@@=...
                                           ...            .-..o-.o@##.=@@@o=@=        .         .-o#..
                                                           ..-o--=@-  -@=@#..-                     .-=-.
                                                           ..==-==o   -@ #@.                          ..-.
                                                           ..o-..-.   =@ .#.                               ...
                                                           ..o..      -@  ..
                                                           ..=..      -=
                                                           ..=..      ..
                                                            .-..       .
                                                             ...
                                                              .-.
                                                               .-..
                                                                ..-.
                                                                  .--.
                                                                    ....
                                                                        .
"""


SUNFISH = r"""
                       ...............
                        ..............-.
                         .................
                          .-................
                           .-...............-.
                             --...............-.
                              .................---
                               .-................---.
                                .-.................---.
                                 .-.................-----                              .-==oo####o##################oooo=--.
                                  .-..................----=.                   .-o#######oooooooooooooooooo####oooooooooooooooooo=-.
                                   .-....................---==.          .-o####oooooooooooooooooooooooooooooooooooooooooooooooooooooooo=-..
                                    .-....................----==oooo##ooo#o##ooooooooooooooooooooooooooooooooooooooooooooooooooooooo#ooo##oo#@@@#o.
                                     .......................-----======ooooooooooooo====ooooooooo===oooooooooooooooooooooo#oooo#####ooooo###########@@=
                                      .--....................-----======ooooooo===========oo======oooooooo=ooooooooooooooooooooooooooooooo########@@@@@#
                                       .....................---==========================================ooooooooooooooooooooooooooo###############@@@@@#.
                                          .-..............-.---===================================oooooooooooooooooooo======o####oo##@@@@@@@#######@@@@@@@.
                                           ............-.------===-------=================oo===========ooooooooooo=========oo###o=o#@@@@@@@@########@@@@@@=
                                             .........----=-----------============================ooooooooo=============o=====ooo---=###oooo#########@@@@@@#
                                         .......--------------------====-======================oooo##ooo=======-========-====--==----=====ooooo##########@@@o
                                     .-----.----------=-----------------==========ooo===============--------------=--========-----------==ooooooooo###oo##@@#
                                   .-----------==-------------------==-==========oooo=======---------------------=====ooooooo==----====ooooooooooo#######@@@@.
                                  ----------------------------------========o====-=====---------------------========oooooooooo=====oo#############@####@@@@@#
                                .-===--==------=----------------===--=====--===========-----==-----------------=oo=--=============oooo############@@@@###@@@#
                                ----------------------------------===========-===-----===----=====-=======-------==---=============oo########@@@@##@@@@###@@o
                               .--------------=----.---------===============o========-====--========----==-----==oo=======--======o##ooo####################.
                               -====----===-----------------===========oo=======-=============oo#=----=---.....---===============oooooo#####oooooooooooo###o
                              .-------=======----------------==============---=--=o=====oooo==oo==-===--.....---================ooooooooooooooooooooooooooo.
                              .---=oo=============--------------========---======oo========o=oo======o=-..--==oooo===============================ooooooooo.
                              ----=o=-=============-----------=======---=============ooo======oooooo=------===--================================ooooooooo.
                              --------==oo====oo====------------=====-----============oooo######o==-----------------===========================ooooooooo.
                              -------==ooooo==ooo====----------==-=--------=====ooooo####ooo=====--------------------------=======-===========oooooooo=.
                              .----======ooooooooo====--------------==---======o==oooo==o==o=====------------------------------===============oooooo=-
                               -========oooooo#oo======-------=============ooooooo===ooo==========---------=--=============================ooooooo=-
                               .---======ooooooooo=====-------============oooooooooo==ooooo===========================================oooooooooo==.
                               .-----====oooooooo#o=====--------==============ooooooooooooo==o==============o========ooooooooooooooooooooooo====.
                                .--======ooooo=ooooooo==---------==-=============oooooooooooo===============oooooooooooooooooooooooooooooo====.
                                 -=ooooooooo##oooooo=====----------============ooooooooooooooooooooooo#ooooooooooooooooooooooooooooooooo====-
                                 .=========ooooooooo======-----------============ooooooooooooooooooooooooooooooooooooooooooooooooooooo====-
                                  .-----====ooooooooooo===------------==========ooooooooooo######oooooo#ooooooooooooooooooooooooooooo===-.
                                    --==ooo=====ooo==oo====-------------=========oooooooooo#ooo#o####oooooooooooooooooooooooooooooo====.
                                     -===========oo==========-------------=========ooooooooooooo#o######o####oooooooooooooooo=ooo====.
                                      .----===================-------------===========oooooooooooooooooooooo==oooooooo===o=========.
                                       ..--=====================-----------==--=-=========oooooooooooo=========================-.
                                          .=====---================--------------=========oooooooooo=====================--..
                                            -------==============o========--===---=======oooo##ooo===========-------..
                                               .---======-==-==============-=====--====oooo###oo====----...
                                                   .------==-------=--=============oooooooo##=.
                                                         ..---------------===oooooooooo###@#.
                                                                        -===oo===oo########.
                                                                        -o=====ooooo######o
                                                                        ====o=oooooo######-
                                                                        -=====ooooo#######
                                                                        -=======oooooo###o
                                                                        -=========oo#####-
                                                                        .========o==o#@##.
                                                                         -=======ooooo##=
                                                                         .==========oooo-
                                                                         .==-=======ooo=.
                                                                          -==--======o==
                                                                          .==---========
                                                                          .==---=======.
                                                                           -==----=----
                                                                           .-----------
                                                                            -----------
"""

GIANT_ISOPOD = r"""
                                                                            .................
                                                                  ...--====================--------....
                                                             ..--==o=================================-----..
                                                         .--=ooooooooooo====================================---..
                                                      .==oooooooooooo====ooooooo=================================--.
                                                 ..-=oo##oooooooooooooooooooooooo=oooooooo==========================--..
                                               .-=ooo#####oooooooooooooooooooo##ooooooooooooo==========================--..
                                            .-=oooo#############ooooooooooo####oo=====ooo=========--========----=========---.
                                          .=ooo##############oooooooo#####ooooo=====oo===========-------=====-----====-==-==--.
                                        .=ooo################ooo######oooo###ooooooooooooo========------====--==-----------==---.
                                      .=ooo#####@###############@@@###ooooooooooo#oooooooooooooo======---==--------=---------==---.
                                    .=o##o###@@@########@@@@@@@@@@@####o###############ooooooooooo=========--------==-----------=--..
                                   -o#####@@@@##@@@@@@@@@@@@@@@@@@######@@##@@#############oo##oooooo========-=-------------------=--.
                                 .=o####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########@@@@##########oooo========-=----.-----------------..
                                .=#@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@@@@@@##@@@@@##oo######o#ooooooo========-..--...........--....
                              .=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o--=-=oo####@@@@@@####oooooooooooooo###ooo==--.....----................
                             .=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o..-====----=#@@@@@@##oooooooo#####o=.....    .-----.................-.
                            .o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o=....-oooooo#ooo#ooo@#o==o##o==oo#=-......-=-..-====--.................
                           .o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#===-----o#@@@#oooooooo#@###ooo#@o#@@#ooo=-.. ..=ooooo===----.......-==--.
                          -o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##oooo=-oo###@@@@@@#ooooooo#@@@###oooo#ooo=-..........---===oo======-=======ooo==.
                         -o#@@@@@@@@@@@@@@@@##########o==o#########o=##@@@@@@@##o==ooo#@@@@@@#o===o####o=-...............--------------========-.
                        -=##@@#######oooooo=ooo#@#####o-..=#@@@@@##o=-=#@#ooo=====-=o@@@@@@@@#ooo##=-oo##=@##oooo-=--=--............-------==oooo=.
                      .=o###oo=--...--=oooooo==##@###o-....-o###@@#oo==##oo====o##oo#ooo###oooooooo=---.=--=oooo@@@##o=-.................-----=--.
                     .-oo#o==--.......=ooooo===##@##oo=-....-o#######oo==--=o####@@@@######oooooooooo=-......--====oo#####=-...................---.
                   .-=ooo==--.........=ooooo===#####ooo=-....-o####oooo===---==#####@@###########@#---.....---====---..-=o####o=-...............
                   .==oo=--...........===ooo===#########oooo====oo#####oo===-...==ooooooo----=o==---...----===o====-...........-=o###o-......---.
                   .--===--.......--===ooooooooo#oo##ooo==-.....-########ooo==-...-=oooooo=-=o==--..-======ooo====-...................--=ooo=--.
                    .--==---===----....===oooo=o######ooo=-......-o#########oo=-........---.--.....=oooooooo=====-...-...--......-........   ..--==--.
                    .-------...........-o=oooooo#######ooo=-....---=##@#########o-.       .......-o######oo=====...--..---......--.-....            ..---.
                     ..................-ooooo#ooo#######ooo=-.......-o######oooo@#=-.     .....-o######oooo===-...--.----......--.......                 .--.
                        ...............-oooo####o#@@@####oo==-........ .o##oooo#@#=.        ..=#@@#==ooooooo=-.........-...............                     .--.
                          ..-........-..-oooo###o#######@#o==-.......   -o========-.          -###o=======-=-..........-...............                       ....
                           .--......-o=--=====o##oo######@#o=-......     .==----==--.        .-o####ooo===o=---......---..............                          ....
                             ....---..==-----==oooooooooo##oo-.....   .===----=-----.         -o###ooo=oo=oooo#o=-..---........   ........                         ..
                           ..-oooooo==-=o=--==----.-==oo###oo=.       ====-....----..         .=####oo#oooo#o####o=-...........            .......
                        .===---=======o=oo=----==----=======-.        =@@#=-.....---.          .=#@@@##oo#@oo#####o=.................    .....------===---.
                           -o#oo=-=-----====---.-=----====--..        #@@@o--.......            .=o##ooo####o######=-.........-----.............--====-.
                         .oooo=-----------=ooo==--==-------..         o#@@o=-.......             .=oooo##o#@o#o#@@#o-.-----..----==--...........---===o=-.
                        -oo==--.---.--..=o====-==---==---..           .#@#o=-.                      .......-###o###=-=o====----======-..  ........---===o=.
                      .-==--.---.. ...-o=--==--------===-.             =##o=-.                             .oo=o#@#===ooo====-------=-...........--...-oo=-.
                      -===-. ..     .=-.-ooo=---------...               o#oo=.                              .--=@@#=------====----==oo------........  .=oo=.
                      ----.           .=ooo=-.----.....                 .##oo=.                              .--=#o-.-....--=-....-ooo=-----...  ...    .--.
                      .-.             =oo==-........                     -o#o-.                               ..=#=--...............-o-------....        .-.
                     ...             -===--...                            .-oo.                                .oo----..............-=-...--.....        ...
                     ..             .===--..                                .o=.                               .o-.----..........   .-.  ..----...        ..
                     ..             .---...                                  .=-                              .==...............   .-.   ....--....
                                   .---..                                     .=-                             .-     ............  ...      ........
                                   .-.-..                                      ..                                      ...........           .......
                                    ....                                                                                 .........            .......
                                     ..                                                                                    ........            ......
                                     ..                                                                                       ......
                                     .                                                                                          .....
                                                                                                                                 .....
"""

BIRD_HOUSE = r"""
                  ========================================
                 [      T H E   B I R D   H O U S E      ]
                  ========================================
     __________________________________________________________________
    /                                                                  \
   /    ~ ~~~~~~~~~ ~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~~ ~~~~~~~~ ~~~~~~~      \
  /    (  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  )     \
 |     | / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ |      |
 |     |/\_//\_//\_//\_//\_//\_//\_//\_//\_//\_//\_//\_//\_//\_//\_/ |     ||
 |     |  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  || |      | 
 |     |  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  || |      | 
 |   /\   ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||   /\   | 
 |  /  \                                                              /  \  | 
 | /    \      , _ ,                    _._                      , _ ,/    \|  
 | | || |     (o.o)                    (o.O)  Pukeko            (o.o) | || ||  
 | | || |     /)__)  Macaw             /) ))             Potoo  /)__) | || ||  
 | | || |--,,--"  "---,,---------------" "-----------------------"  "-| || ||  
 | | || | /  \                                                        | || ||  
 | | || |/    \                                                       | || ||  
 | | || |      \____________________________________________________/ | || ||  
 | | || |      |                                                    | | || ||  
 | | || |      |                                                    | | || ||  
 | | || |      |                     _                              | | || ||  
 | | || |    _ |                   _('>                             | | || ||  
 | | || |   ( )|                _///  )   Shoebill                  ( ) || ||  
 | | || |   / \|               (___/_//                             / \ || ||  
 | | || |  /___\                 ||  ||                            /___\|| ||  
 | | || |   |_|~~~~~~~~~~~~~~~~~~||~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|_| || ||  
 | |____|____|__________________________________________________|____|__|__||
 |/________________________________________________________________________\|

"""

POTOO = r"""
                                                                           -=--.   -#@@@@@@#-
                                                              ..-=o@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-
                                                            .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.       =-
                                                          .-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o-.=@.o@@@#-
                                                        o@@@@@@@@@#@@@@@@@#@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##o
                                                   .-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@#@#@@@@@@@@@@@@@@@#@o
                                                  .@@@@@@@@@@@@@@@@@@@@o@o#####@@@@@@@@@@@@@@@####@@@@@#@@@#@@@@@@=
                                               .-=@@@@@#@@@@@@@@@@#o#@@#@@@@@@@@###@@@@@@@@#@@o#o#@#@o##o##@@@@@@@@@-.
                                            -=o#@@@@@@@@@@@@@@@@###@#@#@o#@o#o#o@#@##@@@@o@@@#o#o=o##@ooo###@#@@@@@@@#
                                            -@@#@@@@#@@@@##oo@#@@@@ooo@#@o####==###@#@@#o####@#@#o=o#@oo####@@###@@@@@
                                          .@@@@@@@@@##@@@@#o#=##@@@@@@@@##@#@@@#o#o@#@@@=-oo#oo#@@##o=#@o##@###@@@@@##
                                          -@@@@@@@@@@####o##oooo=@@@@@o@##@@@@@@@@@###o##oo-###=oo##@o#@##@@@#@@#@#o##
                                        .#@@@@@@@####@#o#######@##o@#@#@=#@@@@@@@@#@@@#o#@###====o@@=######@@####@##@@.
                                       .#@@@@####@##@@##@@#@@@@@@@#oo#@##@@@@@@@@@@@@@#=oo#o##=o==o@@@##=oo#@@#o#o@@@@#
                                      .@@oo@@#@@@@@#@@@@@@@###oo#o#@@@@@@@@@###@#@#@@@@##==o.###====@@o##@=o#@#@#@@@@@=
                                     =@@@o=o####@@@@@@@@@@@####@#oo=ooo#@@#@#############oo#o@@@#o#=##=@#@##o@#o@@@@@#
                                   .=@@#oo#o=o#@@@#@@@@#@@##oo##@@#@@@@@@@@#@=.. ... .o#o#o===o###@@#o####@@#####@@#@@
                                  .#@@=@@#oo@=o###o#@@@@@@@#@@@@@#######@@@- .========-..o@##@o=##o@@@@@@@@@o#o-#@@@@@
                                 -#@@@@######oo####o#@#@###@@@@@@#####o#@@. ..=---..----. -@##o@@@@@@@@#o#@@@@@@@##@#=
                               -#o@@@@@####oo=oo#o#o#o#@####@@#@@#@@@#@@@#..   ..  ...  . .ooo@@####@#@####@###@#---oo
                              .=#@oo#@@@@###oooo=####@@####o####o###o#@###= .       .  .. .o#########@@@@@@@@#@=... ..-
                            -@#o=o####@#=o==--===o##@oo@#oo=====##@###@@@#oo.         .. --o@@#@@@@@@@@@@@@@o#@@=....-
                          -@##=oo=oo@@o#=-==o=oo#=o#ooooo===--=ooo=ooo###o#o#o.       .-=#@@@##o#@@@@@@@@@@@@@#@@#-.-.
                       -#=#@@#==----=-o==#o##=ooooooo##o##o#oo==-o=-oo==oo==oo=oo#o=oo=o######@#####@@@@@@@@@@###@@#o
                    .#@#o#@@@#oo=--o#@#=-==o========o#=---===oo===#o=..-==oo====oo=-=o===oo=ooo#@@#@@@@@@####@###@@@=.
                   ==-##@@@@o==-=o##o###o#@#=-ooo=-.-=o===----=--=oo@@=......-==oo##@#####@####@@@##oo===o@@##@#o@@@@@-
                  .@@@@@o=#o--===#@@o#o#--=##o##o--=--o=oo=-=--oo#o=oo@@o-.............  ...........-==oo=o-----===o#@o
                -@@@@o=o=-o--=-#o#oo#oooooo=#@#@==-o#=o=-==--=ooo=--..--@@@o-..............................---..=o= .=..
               -@@@o-==--.=.---=#oooo####o#=ooo-. --==-=..-=---..-=-=o===o=@@@#=-......  .... ............--===-o=o.
              @@@#o=--=--..-.-oo####@#@@@@#o=-....==--=-=o==--.-==.-----ooo====@@@@#=.....    .........-----o#o##.-.
            -@@@@@=-===-.---=###@@@@@#@@@#=-=..-==-=-=-===---.-=--.=-o==--#oo=oo=-=o####=--.   ...-------====o##@..
           -@@@@@@o=---===o#@###o####@##@o--==-=oo==oo=-==-----.-..=-==--==o##oo#oo=oo--ooo=--. .------=====oooo@..
          .@@@@@@@----..-==o#######o#@@@#o-=##@=-oo=oo#=---..--=----o=-====#o==o#o=oooooo=.-=o=====ooooooooo##==@-
          .#@@@@@@-----.--o=#@@##@o##o###o=.==-=#o##--=-....------o=--=--=o=---===#ooo#oo====-.-o############=-=@#.
         =@@@@@@@@o--.--==oo@@@@#@@o#@#o=====o-=-=o##-.=.----....-----.-=---===o==o-oo===oo===o==.-####@@@##..-#@#-
         .@@@@@@@o==.--=o@o#o@@@@@@#o@@#@@#o-==-=.-=#oo=-----=-..-----.--.-----==-==----=oo=--=====--o###=.. =##ooo-
         o@@@@@###oo=-o=@@##@@@##@@##@#o=o#-.--..-.-=##--=o=..----.-...-...-..=---.-=---==--=-==-===--.=-=..o####=-..
        o@@@@@@@##=o===##@@@#@@@@@@@@@#@@@oo=#=.-.=--oo#==o-o=------..--..-..-..----..-..-------===oo-...-==###==...
       #@@@@@@#@oo==@#@@@@@@@@@@@#o@@#@@@@oooo##.......-=-ooo---.-....-.................-.....----=o-=-..==o=@@=
      =@@@@@@@@@@##oo#@@@@@@@@@@@@@@@@##o@#=o===-.--##-=-..=o--.........--.. .............-....----=====-==-o@@@.
     .@@@@@@#@@@@@#o=oo#@@@@@@#@@@@##oo#oooo#.-ooo@#oo=..--==.=---..--.---.. .......  .-..-=-.=--=o#o@#o---##@@@@.
     #@@@@@@@@@@@@@#=ooo##@#@@@#o@@#@##oo=oo-=ooo=#o=##o-o###o.--=-=-..-.............-. ....--=oo-=#@@@@o=-#@@@@@.
    #@@@@@@@@@@@@@@o-ooo#@o@@##@#@#oo#@o#o#@#@@####o-oo==o#@@#o-.. .....    . .---.----....-.-oo-=oo###@@oo@@@@@@#
   .@@@@@@@#==@@@##=o@@#@@o=##o@#o#@@@@@@@@@@@@@@@##o==o@oo####==..... .     .--.--===o-=-.oo=###o###o@@@#@##o@@@@
   -@@@@@@@@@@@@##==@@#oo--==##@@@@@@#@#@@@@@@@@@@@@@o#@@@#@@###=-.....    -o==o===-.====-=##oo##oo##=o@@@@@@@##@o
  .@@@@@@@@@@#@@#=-#####=o###o##@###@@@@##@@@@@@@@@@@@@@#oo=.-=-==..=.-...==o=ooo===o#oo==-===o#ooooo##o###@@@@@@.
 .@@@@@@#@@@##o#=.=#@##o===oo#=o#=o####@@@@@@@@#@#@#@###=o=--=oo=ooo=-..o--o##ooooo=oooo######==oo===o@##@@@@@@@@.
 #@@@@#@@@#o--o..=oo#o@@@#####o###@##o##@@#o#@@###@@@@##ooo====-.---=ooo=oo--#o=-=-=====o###@@@@@#@=o##o@@@#@@@@@.
-@@@##@##@@oo=...-#@=#=o##ooo##oooo=o#=o#@@o###@@@##oo###oo====-.--=oo=.=o#ooo#ooooooo#o==o#oo#@o#oo##@@#@#@@o@@@.
@@@@#oo@#o=#o.-.-=@@@@@#######o##@@@o=o@@@@@@@@@@###@##@@@#####ooo##@#=.=oo########=##o#@####o##@@#o-oooo##@@@#@@.
@@@@o-==###@o--#o#@#@#####oooo#@@@@@@@@@@@##@@@##oooo###==@#####@@##oo-==oo###@@@##o#o@##=oo##oo=o==-=o--=#=#@@@@.
@@@#@#=-.ooooo-o=@@@@@@@@@@@@@@@@#@##=###########@@@@@#o#@o######o#oo=o#@#@@@@#o@###oooo=#o#oooo=o==--...==oo@@@@=
@@@@@@##--oo###-o@@##@@@@o##@@##@@@@@@###oo######@#@@@@ooooo#####@@####@#@@@@@@###ooo@#oooo-==oo##o--..#o-=-oo@@@@
@@=@@#o-@#@@@@#-ooo#@@@@@#@###oo#ooo==#oo===o#@##@##########oooo##o=##=o##@@@@@@@##ooo#####@#oo##o#=-.o=@-.=-#@@@@.
###=oo=-.#@#==#o--=.=oo##@#@######ooooooooooo#@@@@@@@@@@###oo#oo#@#===o#@@@@@@#@@@####@@@#@@#@o=#o--.=-.-#o#@#@@@@.
@ooo=-o#.=o##o=--. .###o==o##o#oo##oooooo#####@@@@@@@@@#######o=-o==o#@@@@@@#####@@@@@@#@@o@###o##-.-##oo#o-oo@@@@.
@#=o=-#==o.-o#o--...==oooo###oooooo#ooo#o#####@@@@##@@@###o##==oooo=#@@@@@@@@@@o@##@#@@o@##@@@@@@=---#o@=#-=o@@@@.
#=.--=o#=-#-o@@o-..=o=oooo##oooooooo#ooooo#####@@@@@#o######o=ooo#o#@@#@#@@@@@@###@###o@@@##@@@@@-.-oo#==##=#@@@#
o=-#-..#@@#=.-=...=oo#oo#ooo==oooooooooooo#o###@@@@##@@@######o####@###o#o####ooooo#o#@#@@@@@@@@#. ..#o#@--o@@oo
#-=#o-o#@#@.o#=..=o@#oooo=o=o=#####ooooooo######o#@@##@@##ooo####oo#####oo#oo#oo=ooo##@@@#@@@@@#o-.. -##@=o@@@=
"""

MACAW = r"""
                                                                                                .
                                                                                           =o. .@#--oo=-..  .
                                                                                       o##@@@@#.@##@###########o-=-=#=o#-
                                                                                  .....##@@###@@#####o###################o-
                                                                              .--=@@@@###########o###oooooooooo#o###ooooo##o-
                                                                            .-o@@@@#@#######oooooooo#ooooo#ooooooooooooooo###o-
                                                                            =#@@@@######o#ooooooo#ooooo=oooooooooo##@#o====oo##-.
                                                                        .=o#@@@@@@##o##ooooooo===ooo========ooooooooooo=-===oooo=.
                                                                         =#######@##oo##oooo#o===--=====#@@@@@@@####@@@o-------==o.
                                                                       .-=##@@@###@###oo==oooooo==--==o@@@@o-o@@@@@@@@@#o--==###o-.
                                                                      -o##ooo#oo#o##oooo=-==ooooooo=o#@@@@@@@@@@@@@@@@@@o--o@@@@@@-
                                                                     -###o==-=========oooooo#ooooooo#@@@@@@@@@@@@@@@@@#o##@@@@@@@@@o
                                                                  .-=oooooo==o#####ooo=o==#o####o#oo#@@#@@@@@@@@@@@@@@@o=o#@@@@@@@@@o.
                                                                .-o#=--=o#@#oo#####@###=o=#o#######@@@@@@@@@@@@@@@@@@#===o#@@@@@@@@@@=
                                                            .-o##ooooooo######oo===##ooo=#o==o######@@@@@@@@@@@@@@@@o==-=o#@@@@@@@@@@@.
                                                          -o@#####ooo##o==oooo==oooooooo==ooo#######@@@@@@@@@@@@@@@#---===#@@@@@@@@@@@-
                                                     .-=o===ooo###@@@#@#oo=oo=ooo=o####oo===o=ooo###@@@@@@@@@@@#oooo-...-=o@@@@@@@@@@@.
                                                  .o#o..--=###@@@@@@@@@@@@o=oo=-oo==###oo@##=-=---=##@@@@@@@o-..---=oo-..-=#@@@@@@@@@@.
                                               .=-..-=oo@@#@@##@@#####@@@@@o--=--ooo=-=##oooo#o#o#oo##@@@#=---.....-=oo=. .#@@@@@@@@@o.
                                             .=..-########@@##@@@@#@@@#####oo=----=oo=o==oooo=-oo=oo=o#o-.......---=ooo=-. .o@@@@@@@@.
                                            --..-oo=oooo#@@#@@@@@@##@#######o==....-===-==-o###oo==o##oo=......----=o##o=.  .#@@@@@@-
                                          -=-.-o###@ooo@@@@@@@#####oooooo=oo===-.....-----..=#oo#==oo===-......---==ooo==o=--#@@@@@-
                                        -#=..o#==ooo#@@#@@@@####o###oooo======o=..-...-=oo=-..=-..===ooo-.--...........     .o#@@=.
                                      .@o.---o####o#@@@#@##oooooo=oooooo=-=====-....-.-=ooo=------.-=o=..---                oo=-.
                                   .=@o--.o###o####@@@oooooo======o###oo=-----..........==ooo=====----=--.  .             ....
                               -o#o##=-..-=oooo##o###oooo#oo=====o###ooo=---=----.--.......-----------.--               ...
                             .oo--o==-..=oooooo==##o==##oooooo===ooo#o==--=======---..........--...---
                                =@o=-.-=oo##ooo####ooooooooo##o-===ooo###o=--=====--...........------
                             .=@#==..--==ooooo==ooooooo=ooo#####ooooo#####=-=---===--..---....-----.
                           .==oo=o-.--==ooooo=o==oo#o=o#ooooo#######o#####=--===-----------.------
                           .==-o#=--=====ooo=o-==o#oooo####oo#######oooo#=----========----------.
                              -o==o===o==oooo#=o=ooo#####@@#########oo===--=========---------.-
                             -o=o#ooooo==#####o#oo####ooo##o#########oo===============----=---.
                            -o=o#oo##o=oo######@##@@#o###@##oo######ooo=====================--
                           .=oo#==o#o.ooo####o@####@#####o##oo######o=-=====================-.
                           =o=#o=#@@=-=##@#@@#@#=######@#####o#####o=-=============--======--.
                          -=-=o=#@@#=oo#@@#@@#@#o=o==o#@###ooo####o=-===ooooo==-===---=====-==
                         .==-oo#@@#o=###@@@@@#@#oo--=o#@@##=-=####o==ooooooooo=---=-====-====.
                        .=o=##o##ooo-=##@@@@@oo###==ooo@@##=-=###o==ooooo==oooo-..-==-==---==
                       .=oo@@###oo#==--=oo@@@#@###===oo#@##=-=##o=-=ooooooo====-.---=---..-oo.
                      .=##@@o##o#@#ooo==##@@@@@##o--=oo####=-=ooo-..=oooo##o===-----===..-- .
                    .-o##@@##@#o#@#oooo###@@@@###o--=ooo##o--=oo=-...-=ooooo=--------==-=-
                   -=###o@@#@@##@##oo######@#####---===oooo-------....-----====-----. .=.
                  -=ooooo##@@##@@@o=o######@####=...-==ooo==----=---......----..----
                 -=oo==o@@@@@##@@@=oo#ooooo##oo==--.----=ooo=====---.....---------.
                .oo#o=o@@#@@###@@#oooo====-=o--===---===ooo=======-=-....--.-----..
               -o#@#oo@@####oo#o#oooo==-----==o##o=--oo===========-=-.......---=#@@#o=-.       .--..
             .=####o#@@######o==oo==--=---==o####=--=o======-=====---........-o@@@@@@@#@@#@@#@@@@@@@@@@@@@o
            -###@###@@######o==ooo=-==---=o###@#oo=.========------=oo=-.....=##==oo#@@#@#@@@@@@@@@@##@@@#o-
          .=###@#o#@#######oo=ooo-===--==o####@##o--=====----..-o@@@@@@@@@@##@@@@##oo=o#@##@@@@@@@@@#oo=-.
         .o#=.=@##@######oo==oo==-==-===o#@###@@#o--o==---...-o#####o###@@@@#@@#==#@#o-=--##@@@#oo--=--.
        .o=. -###@######oo==oo=======o##===####@#=-===--..-#@@@####ooo==o@@@@###@#o=o#==-.o#@@o==-...    .
       .=-  .=##@######oo==========-=###=-.=#oo@#o--=--..-#@@@@#####@###oo#@@@@o#o=ooo=---#@@#=-       -@@@-
       .-.  .o@#####ooo=--==--===o=-=###ooo--o#oo=--.....#@@@@@@@@@@@@####==#@##o#o.=#==--==-=        .#@@@@@#.
       ... .o@#oo##ooo=----..---==-.=#####o==-=#oo==oo#@@@@@@@@@@@@@@@@@@@#o=ooo#o=-=o-... .-.        -#@@@@@#
        ...-@#oo#ooo=-...    ..-==..-o####o=====o#@@@@@@@@@@@@@@@@@@@@@@@@#o=-o@@#===-....-o-        .=##@@@@#.
"""

PUKEKO = r"""
                                                                                        ...---=====oo=oo=---..
                                                                                ..--===ooooo##oooooo=oooooooooo==-..
                                                                             ..=ooooooooooooooo==oo========ooooooooo=-.
                                                                         ..-oooooooooooooooo==============--==ooooo#@#o-.
                                                                     ..-oo##oooooooooooooo====---=====---==----===oo###o=.
                                                                   .-=ooooooo=o==o============-------==----==---=====oo=oo-.
                                                                 .-oooooo=oo==oo=======-=====--------------====----======oo-.
                                                               .-o##ooo==========-----==---==------------=-----------=====oo-.
                                                             .-o#oo=======oo===------==----==--==-----------------------==oo=.
                                                           .=oo==ooo==========---..------..----==---------------------====o=o-.
                                                         .===--==================-------..---------...------...---=----=====o=.
                                                       .-======--------------======---------..--------------...--------====ooo-.
                                                     .-o##o-------------.------=====---.--....-...----..---=--..--------==oooo=.
                                                    -@@@@@#=------..........-------===--......--------------.....--=----=oooooo.
                                                  .o@@@@#=---------......---..----------........---------=--.....------==oooooo-.
                                                 .#@@#o==----------...........------------.....----------=--.....------==oooooo-.
                                                -@@o=--------...............-..----------......----------==-----------=====ooo=-
                                              .o#=====---------...................-------.......----------------..-----=--===o=.
                                             .==-====-------.-..................---------......---..----------------------==oo-.
                                            ---==--=====----....................-..-----.......-....-----------------==--==ooo-.
                                          .======----------..................................-----.....-....------------===ooo-.
                                        .-=oo==-----------.....................................................---------===ooo-.
                                       .-=o==--....----------------..........................................----------===oooo-
                                       -==----.......   ...-------....................................--......----------==ooo=.
                                      .--...                .===---.........-................................-----------==ooo=.
                                                             .===--.......................................-------------===ooo-
                                                              -==--......................................---------------===o=.
                                                              .-=---.................................---------...-----=--==o=.
                                                                .-----...........................------...........-------==o-.
                                                                  .---....-..................--------..............-----===o-.
                                                                    ..............-...----------------................----==.
                                                                        .........-----------..........-.............-----==-
                                                                                    .-----.           ............-----=o=.
                                                                                    .------              .--......---..--.
                                                                                    .----==.              ........-----.
                                                                                     .---==-.               ....---...
                                                                                     .----==.                .--==-
                                                                                     .-----=-                .===o-
                                                                                     .-------                --===-
                                                                                     .-=====-               .---==-
                                                                                     .--====.               .--===-
                                                                                     .-====-                .-====-
                                                                                     .-====.                -=====-
                                                                                     .--===.               .-=====-
                                                                                     .---=-                .-=====-
                                                                                     .--==.                .--====-.
                                                                                     .-===.                .-=====-
                                                                                     -===-.                .=====o=.
                                                                                    .-====.                 -====o=.
                                                                                    .-====.                 -=-==o=.
                                                                                    -======.                .---==-
                                                                                   .=======oo=--===oo########o==oo-
                                                                                  .-======-=ooooooooooo====---==oo-
                                         .-----=----............       ......---==o==-====----.....          .--=o-
                                         .....--------=========oooooooooooo======-------==o-                 .==oo=
                                                       ...............-..--......=oo=----=@#-                .==oo=
                                                                              .=##o=----.-o@#.               .===o-
                                                                           .-#@##o-.     .-=##-              .===o=
                                                                        .-o###=-.         .-=#@#=--==-.      .===o=
                                                                     .-o##oo-.              .-o##ooooo##-.   .===o=.
                                                                   -o@@#o-.                    -o##=-==o@@=. .===oo.
                                                                .o#@#o-.                        .=##o---=#@@======o.
                                                             .=##o=.                              .-##o=o=oo=====oo-
                                                           -#@#o-                                    .=o==========#=
                                                        .=###-.                                        ..-=oo=---=o#o.
                                                     .-##o=.                                          ..=oo=------==o##o=..
                                                    .=oo-.                                        ..=ooo==----=#@@#==--==o##o=.
                                                                                            .--o##oo===--... .=#@@=.  ...---===ooo=-.
                                                                                    ..-==o##o===--...         -#@@-         ..---====oooo=--..
                                                                          ...--=o####oo==--...               .=#@#-               ...---=-===oooo=-...
                                                                  ...-oooooo======-....                      .=#@#.                      ...------===ooooo=..
                                                                .----=---.....                               .o##o.                             ...--=======o#=.
                                                                                                             -#@@=                                       ......
                                                                                                             -#@@-
                                                                                                             -#@#.
                                                                                                            .=#@=
                                                                                                            .o##-
                                                                                                            -@@o.
                                                                                                            =@@.
                                                                                                           .##=
                                                                                                          .o#=.
                                                                                                          -@#-
                                                                                                         .o=.
                                                                                                         ..
"""

SHOEBILL = r"""
                                                                ..-=oo#@@#oooo=ooo##@@@@@@@@#=-
                                                           .=#@@##oo###@@@@@@@@@@@@@@@@@@@@@@@@@@=.
                                                         -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o-..
                                                       .o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                                                     .=@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o-.
                                                   -##o#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o-..
                                                .=###@@@@@@@#@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                                              .-o####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@o-
                                            .=#####@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#oooo=.
                                          .-#####@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o==oo-
                                         .o########@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@=--.
                                     .-=#######@@##@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                                    -#@@o#######@@@##@@#@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@##@@@@@@@@@@o.
                                   .o@@#################@##@@@@@########@@@@@###@##@@@@@@@@@@@##@@##@@###@@@@#@@@@@@@@@@@@##@@@@@@@@@@@-
                                   .o#########ooo###############@@@@###############@@@@@@@@@@##@@@@@@@@#######@@@@@@@@#@##@#@@@@@@@@@@@-
                                   .o#oo##oo###oo########@@#######@@@#@@#####oo##########@@@@@###@###########@@@#####@######@@@@@@@@@@#.
                                   .o#o==o=oooooo####o###@@@#oo##@@@@@@@#########oo############@####@@@@##@@@@##########o=o@@@@@@@@@@@#.
                                   .o##o=======ooo####o#@@################@@@@@######oo##o###o##########@@@@@@@###oooo=--=#@@@@@@@@@@@@.
                                   .=o##o---====ooo####o##@@@#####o###########o#oooooooo#oooooo#####@@@@@@#@@@#oooo=----=####@@@@@@@@@#.
                                    =oooo=-.--===oooo###@##############@#######ooooooooooooo######@@@@@@#####oo=====--=oo########@@@@@o.
                                    -o#oo==---=--==ooooo##oooo#########ooooo#oo==oooo#########@@@@###@@@@@#oo=...-#o===oo@#######@@@@#=
                                    -o#ooo=--=oo-..-===ooooo####o#######oooo##@@ooooo###@@@@@##@@@@##@@###=-.  .=##oooooo############o.
                                    -ooooo=---=oo=-...-====oooooo#######oo###@@#@##########@@@@@@##oooooo=oooo#@@#oo#ooooo###########-
                                    -oooo==------=oooo=-========oooo#######@@@@@@@@@#####@@@@###@##ooo=-=---=---==oo###o###@@@#@@####=
                                    -o#oo===-----........---====oooo#####@@@#@@@@@@@@@@@@@@@####oo========-=o=====ooooooo###@@@@@@@###.
                                    =o#oo====---.-------...--=ooo##@@@@@@@#o##@@@@@@@@@@@@@@@@@##oooo==ooooo#####oo=-=o###@@##@@@@@@@@-
                                   .=oooo====-------=---.--=o####@#@@@@@@@#o==#@@@@@@@@@@@@@@@#@#o##ooooooooo#@@####oooo####@@@@@@@@@@o.
                                  .=oooooo====-==----------==--=oooo@@@@@@#o#=#@@@@@@@@@@@@@###oo##@@@@o==ooo##@####oooo######@@@@@@@@@.
                                  -ooooo======--=-=-----==oooo--=o#o@@@@@@#o=-#@@@@@@@@@@@@@@#####@@@@@@@@@@##ooo#ooooo#####@@#@@@@@@@@=
                                 .=ooooooooo====---==oooo=oooo=-==oo#@#@@@#===#@@@@@@@@@@@@@#@#@@@@@@o###@@@@@@@@#oooooo###@@@@@@@@@@@@o.
                                 -oooooooo=oo=====-==ooo=-=o##o-===o#@#@@@#==#@@@@@@@@@@@@@@@#@#@@@@@##@@##@@@@@@@@@#o##@@@@@@@@@@@#@@@#.
                                .-oo#ooooo==========ooooo==oo##=-====#@@@@@ooo#@@@@@@@@@@@@@@@oo@@@@@@##@@@o@@@@@@@@@####@@@@#@##@#@@@@#.
                                .-=oooooooo==oooooooooooooooo##o=o==o@@@@@#o=o@@@@@##@@@@@@@@@#oo@@@@@@@@@@@#@@@@##@@@##@@@@#@@@####@@@#.
                                .=ooooooooo=ooooooooooooooo#o##oo#ooo@@@@@oo=#@@@@@##@@@@@@@@#@##@@@@@@@@@@@@@@@@#oo@@########@@@@@####o.
                                .-==oooooo====o##o=oooo=oo####=o####o#@@@@@@#@@@@@@#o@@@@@@@@@@o@@@@@@@@@@@@@@@@@@#######@@##@@@@@###@@-
                                 .-==ooooooooooooooo#oo-oo####o#######@@@##@#@@@@@###@@@@@@@@@@##@@@@@@@#@@@@@@@@@##@@@###############=
                                  .-==ooo===ooooo####oo-oo##########@@@@@@@###@@@@oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########ooo-
                                   .--======ooooo####o==oo#####@@#o#@@@@@@######@@@#@@@@@@@@o@@@@@@@##@@@@@@@@@@@@@@@@@#ooo######oo=.
                                     .-======ooo=#@#oo-=o#####@@o=##@@@@@@###o#@@@@@@@@@@@@@oo@@@@@@@o#@@@@@@@@@@@@@@@@##oo#####o==.
                                      .-===o==ooo#@@o===oo##o###oo#@##@@@@###oo#@@#@@@@@@@@o==o@@@@@@@@@@@@@@@@#@@@@@@@#oo#####o=-.
                                        -=oooooo###o===oo#####oo#@@###@@@@#oooo#@@@@@@@@@@@@o#@@@@@@@@@@@@@@@@@#@@@@@@@######o==.
                                         -ooooooo#ooo==######ooo#@@###@@@@@oo=o#@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@####o=-.
                                         .-=====o###o=o#@@#@#####@###@@@@@@#o=##@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@###oo-.
                                          .==--=o###==##@@@@####@#@@@##@@@@#o=o#@@@@@@@@@@@@@@@@@@@@o#@@@@@@@@@@@@@@@@####o.
                                           .---=o###=oo#@@#####@@@@@@@#@@@@@#ooo#@@@@@@@@@@@@@@@@@@@@o#@@@@@@@@@@@@@@@###o.
                                            .---o##o=o###@@@####@@@@@@#@@@@@#=oo@@@@@@@@@@@@@@@@@@@#####@@@@@@@@@@@@@@##o.
                                             .--=##oooo##@@###@@@@@@@#@@@@@@#o##@@@@@@@@@#####@@@@@@#@@@@@@@@@@@@@@@@#ooo.
                                             .--=o#oo#o#@@@@##@@###@@#@@@@@@@oo#@@@@@@@@@@####@@@@@@@##@@@@@@@@@@@@@@o=o#.
                                              .-=o#ooo###o#@@@@@##@@@##@@@@@@###@@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@@@@#ooo=.
                                               .-=#ooo#o=o##@@@#####@@@@@@@@@#o#@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@#o#o-
                                                .=ooooooooo#@@@@@@###@#@@@@@@#o#@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@###=.
                                                 -oooooo#oo@@@@@@@@@#o#@@@@@#oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@=.
                                                 -=o=ooo###@@@@@@@###@##@@@@#oo#@@@@@@@@####@@@@@@@@@@@@@@@#@@@@@@###@@#.
                                                .-====ooo#####@@#####@##@@@@#=o@@@@@@@@@@##oo#@##@@@@@@@@@@@@@@@@@@##@@@=
                                                .=====oo######@####oo#@@@#@@#oo@@@@@@@@@@@@###@@@@o#@@@@@@@###@@####@##@@-
                                               .-ooo==ooo####@@@@@@@@@@@@@@@@oo@@@@@@@@@@@@@@##@#ooooo@@@@@@oo@@####@@#@@o
                                               -oooo==oooooo##@@@###@@#@@@@@@#o@@@@@@@@@@@@@@@###########@@@@#@@##@@@@@#@@-
                                              .=ooooo=oooooo####@###@@@@@@@@@##@@@@@@@@@@@@@@@@o#####oooo###@@@#o#@@@@@@#@o.
                                             .=oooooo=====oo##@@@@oo##@@@@@@@@@@#@@@@@@@@@@@@@@@#@@@##ooooooo@#o#@@@@@@@@@@o.
                                            .=oooo##oo======o#oooo=ooo#@@@@@#@@@@@@@@@@@@@@@@@@@@@@@#####ooo=#o#@@@@@@@@@@@@#.
                                           .=##oo####o=======ooo#o=oo#@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@######==oo##@@@@@@@@@@@@#-
                                           -#######ooo=--=--=oo########@@@@@@@@@@@@@@@@####@@#@@@@@@@@@@##o==o@@###@@@@@@@@@@@@=.
                                          -######oo=ooo===--==o=o@@@@@@@@@@@@##@@@@@@@@@#####@@@@@@@@@@@##oo#@@@#o#@@@@@@@@@@@@@#-
                                         -#######ooooooo==---==oo######@@@@@@@o@@@@@@@@@##@@@@#@@@@@@@@##ooo#@@@ooo#@@@@@@@@@@@@@@o=-..
                                        -o#o######oo##oo===--===oo####@@@@@@@@@@@@@@@@@@@@@@#oo#@@@@@@#o==o####@#o=#@@@@@@@@@@@@@@@#ooooo=-.
                                       -o########oo##oooo=======ooo####@@@@@@@@@@@@@@@@@@@@@@##@@@@@##o==######@@#o#@@@@@@@@@@@@@@@@@oooooooo-.
                                      -##########oo#ooooo========ooooo@@@#@@@@@@@@@@@@@@@@@@#@@@@@##o=oo####@#####o#@@@@@@@@@@@@@@@@@@#o==--=---.
                                     -#######oo#oo##o#ooo=====-===o==o@@#o#@@@@@@@@@@@@@@@@#=#@##oo=ooo##@@@#o####o#@@@@@@@@@@@@@@@@@@@#ooooooo=-.
                                   .-###############oo#ooooo========-=#@o=#@@@@@@@@@###@@@@#o##ooooooo###@@@@#######@@@@@@@@@@@@@@##@@@@#o###ooo==.
                                 .-o#############o##oo##ooooo=======--=o==o@@@@@@@@#o#oo#oooo==oooooo###@@@@@@#####@@@@@@@@@@@@@@@@#########oooooo#o.
                              .--=o#######o#####ooo####ooooooo====--=---===o#@@###@#=oo===--=oo=o=oo###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########o==o===-.
                           .----=oo#############ooooo##oooooooo=====----.---=o#ooo##===---=o====oooo###@@@@@@@@@@@@@@@@@@@@@@@@@@@###########o=oo==o#o=-.
                        .-=--.-=o#oo###o#o####oooo###ooooooooo======------.-==oo-==o=-====-====o##o#####@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@########oo===o#o=oo-
                      .--======oooooooo##o####ooooo##ooooo#ooooo======-----.-=ooo#==---=---=oooo########@@@@@@@@@@@@@@@@@@@@@@@@@@@#######oo####o====---=o=.
                    .-==-----==oooooooooooooooooo#oooo##o#ooooo==o======---------=o=-----===ooo####@@@@@@@#@@@@@@@@@@@@@@@@@@@@##@@###@@####oo####oo=-====oo=.
                ..--=----===--=ooooooooooooooooo#o####ooo#o#ooooooo=======------==---====oooooo####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########o==o#oo#o==ooooo=-..
             .-==-----====---oooooooooooo####ooo######oooo##oooooooo========------===o===ooo#oo####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######o##o#o-=##==#oo=========
          .--=-------=-==--===ooo=ooooooooo#ooooo######oooooooooooo=o========------=====ooo########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#############ooo==######oo==-===-
        .-------=----.-oo=====oo=oooooooooooooooo####o#oooooooooooo=o=============-===ooooo#########@@##@@@@@@@@@@@@@@@@@@@@@@@@@@#############oooooo####oooo=--=o
      ..-----=------.-==-=--ooo=oooooooooooooooooo#oo##oooooooooooooo=o==============oooooo########@@@@@@@@@@@@@@@@@@@@@@@@@@####@##############oooooo#oo#==oo=--=
"""

PENGUIN_PLUSH = r"""
                                .       .
                        .:.:::::        ...
                          ..:+#%+       ....
                            ..... =--   *%%%:
                            ........   %@@@@@
                             .......   :@%**#.
                             ..........=@%**#.
                            +++++=...+@@@@@@@:
                          **++++++++%#*#%%@%=
                         ******##**#@     ....
                        =%*#######%@@ .   ...:
                        %%%%%%%@@@@@@+.........
                       *%%%%%%@@@@@@@@...  .:::
                       %%%%%%%%@@@@@@@=..   .  .
                      -%%%%%%%%@@@@@@@%:..  .
                      #%%%%%%%@@@@@@@@@:..  .....
                      %%%%%%%%%@@@@@@@@:..  ......
                     .%%%%%%@%%@@@@@@@@-..   ...
                     +%%%%%%%%%%@@@@@@@%:..
                    :%%%%%%%%%%%@@@@@@@@@=.  . ....
                    =@@%%%%%@@@@@@@@@@@@@@@%-..  ...
                    :@@@%%%%%@@@@%@@@@@@@@@@@=.    .
                     +@@@@@@%@@@@%@@@@@@@@@@@+..
                      #@@@@@@@@%%%@@@@@@@@@@@*..
                       +%%@@@@@@%%@@@@@@@@@@@#:+
                 .........+%%@@%%%@@@%%@@@@@@@*
                  .:...         :+*#%%%%%%@@+
                                    ...:..:
                                  ..:::..::
                                          .
"""

KOALA_PLUSH = r"""
            :-**.*%#*+        :+*=:.             .*##*:
           =*+%@@%%%%++:-. +##**+*+*===:        *%%%#**+:
          =#%%%@@%%#%#=-:*%#****++==----+=  :**#%%%#***++:
          +%%%@%%%##**+##%#****+++=---:::--.:-=##***+*+==-
          ..#%%@%#**+#%%##*****++===::..-:--..=**##**+==-.
          *%%@@@%#*++###*++**+=      .::::::::--=++=======-
          %%%@@%#%%*+%#**- =+=         :::..::.:--========
          .-##%%%%#+=#**++=+++         .: ..::::---===+==
            -%%%#**++#**+==+++-        ....::::--=====::
              +*##*+ *+*+==+*+=*=    .-..:::::: .:.--
                  -   -++=-==++##*++++=::::::.
                    .-=*#%##*+=*#*+++=:::::--
                    ++**%%%%%####+============:
                   ++++#%%%%##%%%*#**+*+++===-
                  :++++=+*#######******++++=:::
               .***+++==-+##*****+*+*++++=::...::
               ***++++==--=#****++++++++-......:::
              =***+++=-:-::=*+++++=++==..........:.
              =**++++-:::::  -+=======::....:::::::
               +*++=---::::   .------:  .::::::::..
               +*+==--:::..              :--::.:-====---
             .*++++===++++-:             .-====-::::...:
              -=----::---:::-.          .===+---::: .
                   .........            :=-::::.
"""

TIGER_PLUSH = r"""
                         -=o====oo=.
                    .=====-=---..-=o#o.
              ..  .-=====---. .--..  .o#####o.
              ##o===--====.---. .-----=o######o  ..
            -##o===o===----..----=ooooo=-=#####o-    =@.
             ##=.-o==----------...-==..--.-o###@#      #-
             .o-==------------    -..-- .= -##@@@=.    -o
              #==----------==.    .----- --.=#@@@ .=o  ==
        . -  .#==ooo==--==o####o===---- -=- -#@@@#oo=-o#=====--
       .. -===@#o=oo=oo###@@@@@@#o=------- --#@@o-.-##o------==
              =#oo=oo######@@#@@@#-==---..--o#@#o==-=o=--===o=
               .####=ooo#########o=--------=###=###=.
                  -o####o#######=----==--==o##====o#
                   --=####ooooo######o---==ooo=---=o#-
                 .o---o##############o====--.=--=ooo##=
                .o==-----ooooooooo=---=----=oo-=ooooooo
                oo===--......-====---==--==-.=-==ooooooo
               .====--.......   ----==-----===.---===ooo
                =-==---.---.    ====------=o==-.---====
                  ..-.....      ====------===. ....-.
                                 -=---------
"""

GIRAFFE_PLUSH = r"""
                                             .-. ...
                                           .=---o=--=-
                                           .=--==-=---.
                                      o@@@#.o@@@@@@@@@@
                                      .@##@@@@@@@@@@@#
                                        -@@#oo@@@@@@@@
                                      .o====o@#o#@@@@@=
                                     -=o@##====-#@#@@@@.
                                    o==o@ooo=====o#o#@@@.
                                  -o==--#@o--#==o@@@@@@@=
                                 ==#o#o===#==  .-o#@@@@@.
                              .==oo=------=#        ...
                             .ooo#@#oo====o=
                             ==--=#o---==##.
                         .-@#==----@@#=-####
                     .-#=o#-----o#@#----=#@#
                    =o#o=#o=---o#@o=----==o#
                   o@=--o===o#==---=@#=-=ooo-
                 .#oo---o-==o=-----@@=--==o=-
                .=o=oo=--=o==ooo=oooo##@o=o#-
               .#o#o@oo=#o====@o-----=o#o@@#.
              .--======---...###===o#=--==@o
             -...===-=#@o-...=--=o@@o=-o=o#=
             .-..-==@#=o===oo=--==#@o---=#=.
                 -==o#=o.#####o====oo===o#@.
                 #@@@@@#.-#####oooo#o#@@@@@.
                 =@@@@@@.-@##@@@@@@@#@@@@@@.
                 -@@@@@@. .-.@@@@@@@@@@@@@@.
                 .-...-...  .@@@@@@@--.-o=-.
                  .----..    .-...---...---.
                               .-----
"""

MONKEY_PLUSH = r"""
                                     ...-----..
                               .=#@@@@@@@@##@##@@=.
                            -@@@@@@#@@#########oo##@-
                          .@@###@@@@########oo####o###.
                         #@@##@##########o##o##########==o=o-
                        o@###########@######o##########@#o#@@@-.
                 .=@@#=o@#######@@@@@@@@@@@@@@@@@@@@@##@@@@@@#@@.
               .@@@####@####o#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.
             -@##@@@@@@#####oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
            .=@@@@@@@@@###ooo#@@@@@@@@#.=@@@@@-.o@@@@@@@@@@@@@@@.
            .o@@@@@@@@@####o###o@@@@@@o=o@@@@@=-#@@@@@@@@@@@@#@#.
             .#@@@@@@@@#####o#ooooo#@@@@@@@@@@@@@@@o#@@#@#@@.=-
               =@#@@@@@@#####ooooo=@@@@@@@@@@@@@@@@##.  =o--.
                .###@@#@@o.##o#oo==@@@@@@@@@@@@@@@@#-.
                   .     .#oo=-ooooo=o@@@@@@@@@@o###oo#=.
                       o#oooo===----------==oooooooo#oo###-
                    .#o#o##oooo==oo#o=ooooooo#oo#oooooo#####-
    .o@@#@=       .#########oo==oo#######oo###oo##oooooo######.
   o##o#oo#=.    -@#######@@oooo######oo##o####oo####oooo######-
  =@###oooooo.  .@##@#@####o==#######o#ooooo#o#oooo###o-o#######o.
  -@#oooo==o==-.o@#########o-o#@##@#######ooo##o##o#o#o==ooo#####o.
   =@#ooo====o=@@@####oo#o#==############o##o##o#oo#ooo====o#######
    .=##oooo===@@####oooo##-=ooooooooo#ooo=#o####o#o#####=o#######@.
       .=##oooo@@@#####ooo#ooo##@####ooooo###o###oo####o###@#######
            .--o@##@#####oo=oo##o#@o####===o#ooo=#####o####@@@##@o.
                =@####@############o######oo===######oo####@=##-.
                 .=####@@@@###@##@o#########--o=@#o#oo#o####.
                     .....=o#############@@.  .=#@@@@######.
                            .#@@##o###@@@@-       ..-.
                               .-=ooo##=.
"""

ELEPHANT_PLUSH = r"""
                                             .-=ooo##o#=.
                                      ...-=oooooo=-=--==o.   ..
                                 .=#@##o=ooo###@o===--===..oo=##.
                             -##@@oo#oo========#@@#=-=oo-.o===#@-
                  -ooo#o###o====-===o=o===-===oo=o###@oo.#o=-o#@#-
               .o#oo===--=oo====.-=====oo===-==o===o=oo#o======o-
             -o#ooooo==--===--=o.-====.-=o===-=-========-=-====.
             =#oo====--========---==o#o=====-=-=---====----=oo=
             -#oooo=======ooooo=====oooooo#@@@@@@@@@@#--=o=oo-
            -@#@##ooo====ooooo-==oo=oo===oo#@@@@@@@o=======.
           =@####oo##oo===o#oo.-==o###oo=oooo###.....
          .#@#oooo==oo###ooo#--==------=o##.--=oo.
        .=#@#oooooo======o##=------==o##o-...--=o-
     --.o=#@@oo==-=o#o=====--=-======o=......---=o#=.
     .-...##ooo===o=--=#####o===o--==o=.......---===o#.
      ....oo===o=---.--o=-oo==o=====--oo-.......--==o##o
          =oo=----==--=====-=o======-===ooo=-...-=##=###.
          -#=oo--==ooo-==###o=-oo====-==oooo=o---=o#=#@#.
           -##o===ooooo##@o###-=ooo==---==o####-=oo=-..
             .oooo=ooooo###=#=-.-#o=======o=o#o.
                 .o####o####=.   .o#o=====o###-
                    .-o#=--.       .=o==ooo=.
"""

KEYCHAIN = r"""
                            ....
                        .-==-..--o=.
                       .--.       -=-
                       -=          ==
                       -=.        .=-
                        .=-.  ...-=-
                         ..-=ooo=..
                            .==-.
                             -=.
                            .-=-
                            ..o=
                            .-o=.
                     .....  ==.--  ..
                  .o###@@@=.-=-.-o#####o-
                .o#@@@@@o-.=#@#=--o@@@@@@#-.
               .=#@@@o=@@@@@@@@@@@@@o=@@@@#-.
               .-##o#@@@@@@@@@@@@@@@@@#=#@#-
                 .o@@@@@@@@@@@@@@@@@@@@@#-.
                .=@@@@@@@#..#@@#.-o@@@@@@o.
                -#@@@@@@@##===-=o@@=o@@@@@-
                -@@@@@@oo@@@@@@@@@@@oo@@@@=.
                -#@@@#=#@@@@@@@@@@@@@#@@@@-.
                .o@@@#=@@@@@@@@@@@@@@o#@@#-
                 .o@@@#oo#@@##@##@#==#@@#-.
                  .-#@@@##@@@o@#@@##@@@=.
                    .-#@@@@##@@@##@@#=.
                        .-ooo##oo=-.
"""

POSTCARD = r"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@##########@@@@@@@@@###############@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@################################@@@####@@@########@@@@@@@@@@@@@@@@@@@
@@@@@@@@@#########################@@####@@@@@@#@###@@@##########@@@@@@@@@@@@@@@@
@@@@@@##############################@@@@@@@@@@#@@#@@@@#############@@@@@@@@@@@@@
@@@@################################@@@@@@@@@@@@@@@@@@#############@@#@@@@@@@@@@
@@@@############################@@@@@@@@@@@@@@@@@@@@@@@###########@@@###@@@@@@@@
@@@@###############@###########@@@@@@@@@@@@@@@@@@@@@@@@@##########@@#@####@@@@@@
@@@@########@##################@@@@@@@@@@@@@@@@@@@@@@@@@#######@@@@@##@####@@@@@
@@@@##################@@####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@@@##@##@####@@@@
@@@@@#####################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@########@@@@@@@@#####@@@
@@@@@@@###################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@#@@############@@@@
@@@@@@@@@################@#=@@@@@@@@@@@@@@@@@@@@@@oo@#######################@@@@
@@@@@@@@@@@@@@@@##########@o#@@@@@@@@@@@@@@@@@@@@@#@#####################@@@@@@@
@@@@@@@@@@@@@@@@@##########@@@@@@@@@@@@@@@@@@@@@@@@@#################@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#######@@@@@@@@@@@@@@@@@@@@@@@@#######oo#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@#@@@@@@@@@ooo####@@@@@@@@@@@@@@@@@@@@@@@@####ooooo@@@@@@@@@@@@@@@@@@@@
@@@@@@@###=#@@@@@@@@@ooooo@@@@@@@@@@@@@@@@@@@@@@@@@ooooooooo@@@@@@@@@@@@@@@@@@@@
@@@@@@@@#o=@@@@@@@@@@oooo@@@@@@@@@@@@@@@@@@@@@@@@@@#ooooooo#@@@@@@@@@@@@@@##@@@@
@@@@#@@@o#o#@@@@@@@@@#ooo@@@@@@@@@@@@@@@@@@@@@@@@@@@ooooooo@@@@@@@@@#@@@@o@@@@@@
@@@@##@####o#@@@@@@@@#oo#@@@@@@@@@@@@@@@@@@@@@@@@@@#ooooooo@@@@##@@@=o@##@oo@@@@
@@@@#o#@o#o#o=o@@@@@@ooo@@@@@#@@@@@@@@@@@@@@@@@@@@@@oooooooo@@@##@@o=@#o@oo#@@@@
@@@@#o####oo##@#@@@@#ooo@@@@@#@@@@@@@@@@@@@@@@@#@@@@@ooooooo#@##oo##=o#ooo##@@@@
@@@@#o###@ooooo#ooo#oooo@@@@oo@@@@@@@@@@@@@@@@#o#@@@@#oooooooooooo#####oo###@@@@
@@@@#oo##oooo####ooooooo@@@#o=#@@@@@@@@@@@@@@@o=o@@@@#ooooooooooo##@##oo##o#@@@@
@@@@#ooo#ooooooo#ooooooo@@@oo=#@@@@@@@@@@@@@@o===@@@@#ooooooooooo#ooooo###o#@@@@
@@@@#oooo#oooooo##oooooo#@@oo=#@@@@@@@@@@@@@@o===#@@@ooooooooooo##oo=ooo#ooo@@@@
@@@@####o#ooooooo#ooooooo@@#==#@@@@@@@@@@@@@o====@@@oooooooooooo#oooooo##oo#@@@@
@@@@#oo#ooo=oooooooooooooo@#o@@@@@@@@@@@@@@#o===o@@ooooooooooooo##o=ooo#ooo#@@@@
@@@@#oo#oo#oooooo##ooooooooo=o@@@@@@@@@@@@@o========oooooooooooo##oooo#oooo#@@@@
@@@@#oo#@#####oooo#ooooooooo=o#@@@@@@@@@@@oo========ooooooo##oo##oooo##ooooo@@@@
@@@@###oooo#oooooo#oooooooooo#@@@#@@@@@@@#oooo======ooooooooooo####oo##ooooo@@@@
@@@@#ooooooo#ooooo#oooooooooo#@@@@@@@@@@@oooooooooooooooooooooo#ooooo#oooo=o@@@@
@@@@#o#oooooo#@oo#####o###@@@@@@@@@@@@@@#oo#@@@@@ooooo####oooooooooo#oooo=oo@@@@
@@@@ooooooooo####oo########oo###@@@@@@@@@@@@@@@@@@@ooooooooooo#ooooo#@#o#ooo@@@@
@@@@ooooooooo##oooo#oooooooo##@@@@@###@@@@@@@@@@@@@@#oooooo==o#=ooo##o#ooooo@@@@
@@@@ooooo=oo#ooooooo#ooooooo##@@@@@@#@@@@##@@@@@@@@@#oooooo=o#ooooo#####o==o@@@@
@@@@ooooo=ooooo#ooo##oooooo#@@@@@@@@@@@@@@@@@@@@@@@@#ooooo=o#@@@@@@@@@@=oooo@@@@
@@@@ooooooooooo#oooo#o=ooo=#@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@ooo@@@@
@@@@oooooo=o###oooooooooooo=oo#@@@@@@@@@@@@@@@@#o=o@@@@@o#@@@@##@@@@##@@@@##@@@@
@@@@oooooo=o#oooooooo##ooo=o==o@@@@@@@@@@@@@@#oooooo@@@@#@@@@#ooooo###@@@@#o@@@@
@@@@oo##o#o####@##@o####o#oo=o@@@@@@@@@@@@@o=ooooo=o@@@@#@@@@@oooo#ooo@@@@#o@@@@
@@@@ooooooo##o####o###oo=o==#@@@@oo##oo#@@@@oooo=oo@@@@##@@@@@#####oo@@@@@oo@@@@
@@@@ooooo#oo#o####o#####ooo@@@@@@@@@@@@oo@@@@@@@@@@@@@#o=oo@@@@@@@@@@@@@#ooo@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

TIGER_SHIRT = r"""
                                   ...-==o=-.         ..----..
                        ..--=====o###oo###################oo#o###ooo=--..
                  ..=o#####o#######oo######o##########################o######o=-..
              .-ooooooo######################o#ooo#####o###########################=.
           .-o#################################ooooooo################################o-.
       .-=####################################################################o###########=..
    .-o#oooo##################@###@@@@@@@@@@@@###@@@@@@@@@@@@@@@#########@@###################=.
.=ooooooooooooooo########@@@@@###@@###@@@@@@@@########@@@###@@@###@@@@@@@@#######################o=.
.-=oooo########################@###@@@@@@@@o=ooooo###=##o#####@@@@###@@@@#######@###@@###########o=.
 .=oo#############################@@###@@o=o..--#=====ooooooo=##@#@@##################@@########o=.
  .oo#ooo#################@@######@#o#@#ooooo##o==o-====-o#o==o#########@@######################o.
   .o#########################ooooo##@@o=o=o#o=#oo===oo@#.==#ooo#oooooo########################o.
    .ooo####################ooooooo##@##oo=o#=o-#o-=oo#=#-oo.##oooooooooo####################o=.
     -o####################o#oooo###@@#oooo@.=--==-===--==oo=.#@##ooooooooo##################o.
     .-oo=oooooo=-o######oo###oooo###@#o=o##.oo===oo=-==-oo#-.-####o###ooooo#####o==o######o.
       .-o==-...  -o##########oooo#o##oooo##.-o===oo=-===#-=-.o#@@###########oo##o.   ..=o=.
                  .o######oo###oooo##@#o==o###oo=========--===o@###############oo=-
                  .=o##########oooo####o==oo###oo=--===-ooo##o####################-
                  .=#########@##########o-===ooo=o===o=-ooo=o########o############-
                  .=###################@===o=--====---==o=-o###########oo#########-
                  .=#######ooooooooooo#@#o#====----===-.-ooo=#####################.
                  .-#####oooooooooooooo####o=..-=---==-....-=o####################.
                   -o######oooo======o#@o##o==-..=#@@#=---===####@#@@@@@@@#######o.
                   -o#####@@@##@@@#oooo#=##ooo=-=#@@@#======#@@@@@@@@######o#####o.
                   -ooo##@#@@##@@@@@@@@o=##oooo-o@@@@#==-=-o======ooooooo########-.
                   -oooooooooooo##@@@#==-#ooooo#@@@@@@@o=-=######################-
                   -oooooooo#oooooooooo-=oo===o@@@@@@@#=--o##ooo#####ooo########o-
                   -o#ooooooo=oo======-=##o---=#@@@@@@o--=##oooooooooo##########o.
                   .o##ooooo==oo########@#o-----o@@@@o=--#@#######oooooooo######o.
                   .ooo#####@@@########@@oo---..-o##o-===@####@@################o-
                   .o###@@@###########o#==o=....-o@#==--o#ooo####################=.
                   -o#####@#######ooooo===------=#o=-=---==oo###################oo.
                   .o######@####ooooooo========o##o========oo####################o-
                   .o###########o##oooooooooooooo#oooooooooooo###################o=
                   .o##############oooooooooooooooooooo#####o#################o###o
                   .o######ooo############o##############################o#####o##o.
                   .o####################o########################################o.
                   .o###################o##########################################.
                   -o#######o#o########oo###########################ooooo##o######o.
                   .----..---==--======-=o===================o==oooooo==ooooo=ooooo.
"""

SAFARI_SHIRT = r"""
                            .---==------=:
                          :*#*#%%%@%@@%%*##+=.
                   .-+#%%#***#@%%#***%%%*#+%@@%@@#+:
               :*%%%%%##%#*+%@%@@##*+#%*#@@@%@@@@@*%%%=
            .+%#*@@#***+%@@%#%#%@@@###%#%#**#%%@%%%%*%###.
           =#@@***#%%%%@%%%#%@@@%%%@@@@@%%%@%%%%%@%%%%#%@%+
         :##%%%%#*%%%%#%%%**#@@%##%%@%%%**##*%@@@@#@@**@@@@@=
       :*%%#@%%%%%%%@@%#@@%*%#%%%%@@%%@%%#*###%%%%@##*#@%%%%#%=
     .@%****#@@%%%@@%%%%%##%%%#+###@*%@**@@**%@@@%##**@%%%@*##%%:
     -#%%@@@@@#%#%%#***%@%%%###%%%%@@%@%@@***%%@%#%*+#*%%#%@@@@%=.
       .+%%@@%%@@**%%#*#*%#%%@@%%%#%#%%%%%@@@@%%@@%*%%%%@@@%%%:
          :%@@#****@@%%#%@@@%%*%#*@%%%*%@%#%%%@@%%*#=%%@@@%+.
             +@%: :%@%#@%@@%%####%@*%@*#@@%%%%%@@@@@..#@%.
                  -%%%%****%%@@@%%%@%%%%%%%@@%#@@@@@.
                  =#****#@@@@%%%#*#%#%@@@%%#%##@%%%@.
                  -*#@@%%%%%%@@@@@@@@@@@@%%%@@@@@@%%.
                  -%%%%%%%%*#%@%%#%@%@@**#@%@@@@@@%%.
                  =%@@%%%%%*%%#%#%@@@@@@%*##*#@@@@@@.
                  =@@@##%%%%%%@*#####@@@@@@@%@@@@@%%.
                  +@%#@@%@@@@%%%%%@%#%%%%#%%@#@@%%%%.
                  +%##*+*+*#%%%%%%#%@@%%#*%@@@%%**#*.
                  +@@@@%%##%%%%***%%%%#**##*+*@@%@@%.
                  +####**#####@%**@%***#%%%@@@@@@#*#.
                  #%*++@@%**#%@@%%##%%@###%####%%@@@.
                  .+%%%%#*@%%##**##%%#########**#%%+.
                           .::-=+++****++==:.
"""

GIRAFFE_SHIRT = r"""
                                           :++:               ::.
                              ..:--+%@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@%#+=-:.
                      :+**##%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@%@@%#*+=:
                  :*%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-
              .+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-
           .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.
       .=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:
    :*%@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%%%@@@%##+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-
*%%%%%@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%*===*@@%@%-=+=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.
-%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####%@@@%#=@*%@%%%%*#@#@@%%%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.
 =%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#***##@@@@@%%@+%%#*%@%*@*%@@@@@@%#*##%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
  +%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%#+=+@@@@#*@#+=+**++@@*%@@##==+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:
  .*@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@+-+@@#*+*#%***#@@#**#@@@--#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:
   .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*==%@%+#@@@#*+#@@@@%#@@*==*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:
    .*@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%@@@%#@@@*=#@@@@@%####@@@@@@*==#@@@%#%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.
     -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###*+#%*%####%@####%#%#*%%#%@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
      -#%%%%%%%%%%##@@@@@@@@@@@%#%@@@@@@@@@@@#=::*@%=#@@@*@@*.-+%@@@@@@@@@@@@@@@@@@@@@@@@@@%##%@@@@@#:
        -##*=:     .#@@@@@@@@@@@@@@%@@%%@@@@@@#+#@@@%%@@@%%@@++%@@@%%%@@@@@%%@@%%%@@@@%@@@:     .+%%.
                    +@@@@@@@@@@@%%%##%%@@@@%%@@%*@@#=#@@@*%@@#%%%@@@@@@@@@@@%%%%%%@@@@@@%%#.
                    -@@@@@@@@@@@@%%%%@@@@@@%%@@@*+*+@@@@@@#*@%@@@@@@%@@@@@%%%%%%%@@@@@@@@@%.
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@%=+%-+##+*@**@@@@@@@@@@@@@%%%%%@@@@@@@@@@@#.
                    -@@@@@@%#%##%@@@@%%%@@@@@@@@%*:%@@%@@@@=%@@@%@@@@@@@@@@@@@@@@@@@@@@@@@#.
                    -@@@@@@@%#%%@@@@%%@%%%@@@@@%%#+:#%%%@#:*@@@%%%%@%@@@@@@@@@@@@@@@@@@@@@*
                    :%@@@@@@@@@@@@@@##%%@@@@@@@@@%*=::-::=*+@@@%###%%@@@%@@@@@@@@@@@@@@@@@=
                    :#@@@@@@@@@@@@@@@@@@@@@#%@@@@@#-*++-#*-*%@@@%#%@@@@@@@@@@@@@@@@@@@@@@@-
                    .#@@@@@@@@@@@%%%%@@@@%@%%@@@@%%+#=*+=:+:#%@@@@@@@@@@@%%%@@@@@@@@@@@@@%=
                    .*@@@@@@@@@@@%#%@@@@@@@%%###@%:@@=+=-%%=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:
                     *@@@@@@@@@@@@@@@@@@@%@%%%#%@#++@@##%@#*%#@#%@@@@@@%###@@@@@@@@@@@@@@#.
                     +@@@@@@@@@@@@@%%%@@%%%@@%%@@#@@++%@==@@#@@@@@@@@##%%%##@@%%%%%@@@@@@+
                     +@@@@@@@@@@@@@@%@@@%#@@%%@@@++@+++%*@%-##@@@@@@@@@%%%%@@@%#%%@@@@@@@=
                     +@@@@@@@@@@@@@@@@%%@@@@%@@@@=-@@%%%%@+=**##@@@@@@@@@@@@@@@@@@@@@@@@@=
                     +@@@@@@@@@@@@@@%%%@@@%%%%@@%+-@@@@@@@@%@*%%@@%%%%@@@%%%%%%@@@@@@@@@@-
                     =@@@%@@@@@@@@@@@@%@@%%%%@@@%#%%+%@#***@#*@%%%%%%%@@@%%%%%%@@@@@@@@@@=
                     =%@@@@@@@@%%%@@%@@@@%%%%%@@%#@=-=#+==#@=-%%%%%%@@@@@@@@@@@@@@@@@@@@@+
                     +@@@@@@@@@@@@@@@@@@@@@@@@@@%+@%**@@@@@@**@@@@@@@@%%%@@@@@@@@@@@@@@@@%:
                     +@@@@@@@@@@@@@@@@###%@@@@@@%+-@@%@@@#+@##+%@@@@%%%@@@@@@@@@@@@@@@@@@@=
                     =@@@@@@@@@@@@@@@@%###%@@@%%#*--@@@@++#%@%=*##@@%###%%@@@@@@@@@@@@@@@@*
                     =%@@@@@@@@@@@@@@@@@%%@@@@@@%%+==*@@*#@@@*+**#@@@@@@@@@@@@@@@@@@@@@@@@#.
                     =@@@@@@@@@@@@@@@@@@@@@@@@@@%*@%##@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@%.
                     =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.
                     =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
                     =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                     +@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                     +@@@@@@@@@@@%@@@@@@@@@@%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=
                     .-=++++***#**++=====----=--==-======---::::::-===++++++=========--=+**:
"""

ESPRESSO = r"""
                                         .:-=*#*****###****###%%*+=-.
                                    .=+##%@@@@@@@@@@@%@%%%%%%%%%%@%%#+++++.
                                 -###@@@@@@@@@@@@@@@@@@@@%%%*+#######%%%%#+*@-
                               -+#@@@@@@@@@@@@@@@@@@@@@@@%@%%%%%%###******%%#+@@.
                             :+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%###***++++#%#*@*
                            -+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##*++++++*#@%@*
                           =+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##*++===+=#%@@
                           :%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##*++====+#@@
                           :=#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##*++=++*@@%
                      -*#@@@=+#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##*++++*#@@@%#*=
                  :*#@@@@@@@#=+*+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%##*+++#@@@@@%+****#@@#:
               :##@@@@@@@@%%%==++##**#@@@@@@@@@@%@@@@@@@@@@@@@@@@@%%%##*++*@@@%@@#-*%%%%###%@@@:
             =#%%@@@@@@@%#%%%=:-==+*#%@%*+**#@@@@%%%@@@@@@@@@%%%%%#++*#%@@@%%%%%+:-@@@%###%%@@@%*.
           =#%**##@%#####%@@#+...-===++**#%@@@@@####***+**+***###%%%%%%%%%%%%#-.:#@@@@%%%@@@%#@%**=
         :%@%+++*#**#%%@@%*+*+-.   .-===++++******#####################%%##-...:+######%##%%#%+##++*.
        =@@#****%@@@@%#**#%%#++:..      :-=+++++++***********########+=:. ....:-**############**#*=**.
       +@@#*##**#@####%%%%**++*=.              .:::-==++++==---:.         ...:-+*###########+*****=***
      :@%*+*@@@@@@@@@@@%#***==+=-.                                       ...:-=++**#**##*#**+=+#*=-:=*+
      #@#*+#@@@@@@@@@%@@@*+*@=---=..                                    ...:+=+==++**#%@%%*#*##*=-=--*#.
      @@**+++*@@@@@@@@@%*%@+---+*--:...                               ....-#%*@@@@@@@@%@%%###*++*+****#:
      %@%*#+++++#@@@@@@%@@=--+#=::::-..                             ....:-++%@@@%%%%%%###***+*#**#*+=*#:
      =@@#**+++*@@+**##@@+-=+#--:::-==:.                          .:-::-+-----=+**####******+****====*#.
      .@@@**+=+#@@++++@@@--=**-::-----:...       ...       .... ....:-++#*%*+=+%@@+=+**++***+****+*+*%-
       :@@@*+++*@@#+++@@@=--++:----::::...:-..               .....:+++*++**+++*@@@*++#*+****+**#****#=
        .@@@%==*%@@*++*@@+---=::::::.::.....=%%+=-:...   ...:--==--==-=+**+==+*%@@*%%%*+***++*##**+*-
          *@@@%++#@@#++#@@=-===-:::::.......:-......:::::::....:--:---======+*@@@*#%#+++*++=+##*+**.
            @@@@%*+%@@*++@@+-====::::::....................:::::::--=--=====#@@@**#%*++*==+*#*+*%-
              #@@@@#*#@@*=*@%+===+=:::::::........::.........::::-------=+%@@@*+*%%++==++***+##-
                -%@@@%**%@#+*%@#=--===-::::.:::.:::::.....::---------=+%@@@#**#%#==++#****#%+.
                   -%@@@%#*#%#++#%*=---====-------:-------------=+*%%%%*+=#@#*==*##*+*#%#+.
                       =#@%%##****===+==-----=++==-=----=====++*+====+*#**+**##***#%#*-
                           :=+**+*++==----------------------==========++***#%@@@%+:
                                 .:-++++=====-----------------======+++****=-.
                                           ..::----------------:::..
"""

AMERICANO = r"""
                                     .:+#%@@@@@@@@@@@@@@@@@@@@@@@@@@#*-.
                                   -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
                                  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#::..
                                   +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*@@@%*-.
                                   .::+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=:.--:-###+.
                                    .:::::::.:=*=#####***+=---:............   -%##=
                                    .::::::::.............................    :%%#*
                                    ....::::..............................   .=%#*=
                                    ..:...................................  .*%#@*.
                                     ...................................:+*##***=.
                                      ..................................+#%%@@+.
                                      ....................................:..
                                       ................................
                                       ................................
                                        ..............................
                                         ............................
                                          ..........................
                                           +*-:................:-++.
                                            -@@++========+*##+===:
                                             .*@==+%@@@@@@@@+=-.
"""

LATTE = r"""
                                                 .----=======--..
                                          .-o##@@@@@@@@@@@@@@@@@@@@@@@o-.
                                      .o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.
                                   .=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                                  =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
                                 =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
                                 o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                                 -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o.
                                   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.
                                   -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o-
                                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##o==-.
                                     #@@@@@@@@@@#@@@@@@@@@@@@@@@###o=======--==-..
                         .------------@@@@@@@@@@@@@@@@@@@@@####oo=====---=--===-=#o-.
                         .------------o@@@@@@@@@@@@@@@@@@@@###oo=====------=-----.=o#o-.
                          .-----------=@@@@@@@@@@@@@@@@@@@####oo===========------..==ooo=-
                          .------------#@@@@@@@@@@@@@@@@@@@###ooo=========--........-##ooo=-
                        .-...----------o@@@@@@@@@@@@@@@@@#####oooo========-.........-=oooooo-.
                       .-....-----------#@@@@@@@@@@@@@@@@@#####ooo=======-........-.-==ooo==o-.
                      .=.....-----.-o@@#@=@@@@@@@@@@@@@@@@#####ooo=======...----..----=======o-.
                      --......-o@@@@@o-...-@@@@@@@@@@@@@@#####ooo=====-----------------========.
                     .--.-=o#@@@@#=........-@@@@@@@@@@@@#####ooo==-----......--------------====-
                   .-=#@@@@###=.............-##o#@@@@@#####ooo===-----......-------------======-.
             ..=oo###@@@@@o..-------.........=o====oooo======-------#.............--------====--
          -ooooo#o###@o-......--------.--....-#==========--------=##o.............-------=======-
          o@##oo#=-.   =o-....-------------.....-===o==-----=---==-...............-----========-
                        =o-..---------------.......-===--------..................-----======-..
                         -#=.-------------------...............................-----======-..
                           =o-----------------------..........................-------==-...
                            .----------------------------------------------..-------..-..
                            .--------------------------------------------------..---..
                            -.........----------------------------------.......--..
                                      ...--....--......-..--...........-......
                                            ..-----------------........
"""

TEA = r"""
                                                  .-=oooo###ooo==-.
                                         .=o########################@@@##o=-
                                     -#@@############ooooooooooo#######@@@@@@@#=
                                  =@@@@####ooo========================ooo##@@@@@@@=
                               .#@@@@##oo=======ooooooooooooooooooooooooooooo##@@@@@#
                              =@@@@##o=====ooooooooooooooooooooooooooooooooooooo#@@@@@o
                             -#@@@#o====oooooooooooooooooooooooooooooooooooooooooo#@@@@o
                             =@@@#o===ooooooooooooooooooooooooooooooooooooooooooooo#@@@#.
                             =@@##==ooooooooooooooooooooooooooooooooooooooooooooooo#@@@#.
                             .#@#o==oooooooooooooooooooooooooooooooooooooooooooooo##@@@=
                           .-#@@@#ooooooooooooooooooooooooooooooooooooooooooooooo##@@@#=.
                        =#@@@@@@@@@#oooooooooooooooooooooooooooooooooooooooooooo#@@@###@@@#o-
                     -#@@@@@@@@@@######ooooooooooooooooooooooooooooooooooooooo#@@###oo@@@@@@@@#-
                   =@@@@@@@@@@@@@@#######o##ooooooooooooooooooooooooooooo####oooo#oo###@@@@@@@@@@o.
                 o@@@@@@@@@@@@@@@@#######ooo#o==#@@##oooooooooooo###@#o==oo===-=o@#ooo####@@@@@@@@@#
               .#@@@@@@@@@@@@@@@@@@######ooooooooooooooooooooo==ooooo====ooo=-=o#####o######@@@@@@@@@o
              =@@@@@@@@@@@@@@@@@@@########oooooooooooooo=oo==oooooooo==oooo=ooo#####@@o##oo##@@@@@@@@@#.
             -#@@@@@@@@@@@@@@@@@@@@@######ooooooo===oooooooo====ooooo==oooo=ooo####@@@@o--=oo#@@@@@@@@@#.
             o@@@@@@@@@@@@@@@@@@@@@@@#########o#oooooooooooooo====oooooooo=ooooo###@@@@#-..--o@@@@@@@@@@=
            .#@@@@@#@@@@@@@@@@@@@@@@@@#######oooooooo#oooooooooooooooooooooooo######@@@#-..-=##@@@@@@@@@o.
            .#@@@@@@@@@@@@@@@@@@@@@@@@@@@#####ooooooooooooooooooooooooooooooo##########o-=o###@@@@@@@@@@o
            .o@@@@####@@@@@@@@@@@@@@@@@@@@########o##oo###ooooooooo####ooooooooooooooo###@@###@@@@@@@@@@=
             -#@@@########@@@@@@@@@@@@@@@@@@@@##############o#######oooo##oo#o##########@@@@@@@@@@@@@@@o.
              =#@@#########@@@@@@@@@@@@@@@@@@@@#################ooooooooo##############@@@@@@@@@@@@@@@#-
               =##@##########@@@@@@@@@@@@@@@@@@#####oo#ooooooooo=====oo###############@@@@@@@@@@@@@@@#.
                 o#@@#########@@@@@@@@@@@@@@@@@@@####oooooooo===ooooo###############@@@@@@@@@@@@@@@#=
                   o#@@@########@@@@@@@@@@@@@@@@@@##################################@@@@@@@@@#@@@#=
                     =##@@@###@@@@@@@@@@@@@@@@@@@@@#################################@@@@@@#@@@#o-
                        =##@@@@@@#####@@@@@@@@@@@@@@##############################@@@@###@##o-
                           -o##@@@####@@####@@@@@@@@@@###########################@@##@##o=.
                               .-o###@@@@@@########@##############################oo=.
                                      -=o####@@@@@@#@@####################oooo=.
                                              ..--=======o=========---..
"""

DOUGHNUT = r"""
                                                   .==.
                                      .-=--....-#@@@#o#@@@@@@@@=...
                                   .-o#@@@@@@@@@@@##=o####@@@@@@#@@-..=-.
                                .#@@@@o@@o#@@@@@@@o=o@@@@@@@@@@@@@@@@@@@@@@@@@.
                            .-o@@@@@@@@@#@@@@#@@@@#o@#@@@#@@@@#o#@@@@@o@@#ooo@@=.
                          -=@@@@@@@@oo@@@@=.-o@@#=#@@@#o=-##@o=o@@@@@@#@@@@o=#@#@o.
                       ...o#@@@@@@#=#@o-=--===-=o=-#o#@@##o@#=#@@@##@@@@o=#@@o=#ooo#.
                   .-#@@###@@@#oo#=-@@==#=---ooo@#.-.--=-..--.-=#@#@o@@@@@##==##o=ooo-
                   -##ooo@@@@###oo=#@@@@#=@@=o###=..=#=...oo.oo-####=o====-=--=o@@=--o=....
                 -o==ooo=-.-o@#ooo===--==o###o...--......-oo=-..--o=--oo=-o@@@@@@o-=-o##=..
                -o==o##o==@#=oooo=====oooo.--==---..=o-..-...o#o#==@@@#=o##oo##@@o---=-.
               .#@#o#@@@#@@##@@#-...--=##o...........-=....-=-o@@######o=oo@ooo#@@#o#@@=.
              .#@#@@@@@##@o@#--o=..-=o##@@@#................--o@@##@@o=@#@@o=oo#@@@@@@@#o==.
              o@o-=-#@#=o@###@@@@@@=@@o=-.-..................-ooo#@@@@@#@o-=#oo@oo##@o...-..
             .oo-==o##o##=#@###o@#o@@o--.......----.--------...---o@o@#o=o=#o#o=o#@@o=#o==-=-.
             .--=ooo@@#@@@@@@#@@@@@o==#o-.ooo--..           .....--.o@@@@@@@@#=.-o@o--.-=..#@-
          .=#=--=#@@@#oo==o#@@#o@@oo@o..-===.               .-=.-o@@##@@@@#@@@#oooo-o@o-o##oo.
           .-=-#o=oo=o@@#-o##o-.o#@===##=--=-.               .--#@@@###@#o##o#@#-..--oo=-===o=.
           .-===o===#@@@@@@oo@@@@@@@#@#====.                 .=o@@@@@@##@#@#-.-==o#@@...==o#=..
           .-====-@@#@@#@@@@@#o##o=o@@@@@@o-.                .==#@oo==o@@@@#=o@@oo-#@o...--...-.
           .-oo==---=-o@@@@@@#@@@@@@@@@#-o@@=     . ....  .#oo@#@@@@@@#o##====-.-o-.#@=.----..--
            -ooo==--=o#o==o#@@#o@ooo#####@o=ooo@##o#@@##@@@@#o#@@@#@@@@o=-o#=...........----.-...
            .o#oo==--==--==##@#o=-o@#o@@@#@@#@@#o=o#@@@@@@@#oo#@@@#--#@o.=o=..=@@o......----.---
             =##oo==-------=o--=-=#==oo##@ooo@@@@#o@#o==oo=@@#ooo==@ooo==-..o@#o-......----.....
             .=##oo==------o--o=-o=...=@o-=##o==#o@oo==-===@@@o#@@@@@oo#@=............----.....
               -#@#o=--------.==-...----.-oooo=#@@#--oooo@@#@@@@@o-...-o#-...-......----=.
               .==##o=--------o#-.-------==-=----#@-o@@#oo=-=o--..oo-..--........------..
                .-=o#o--==---@@#@@---..-..-----..............-==-oo=.-----......-o#--..
                   .=oooo=====o==...........................-...=#=...---------..-....
                    .-=oooo======--.....-.-.................-----........-------..
                      .-==========------=---.........---.....------.......---..
                        ..--========----=----==========ooooo==-----------....
                           ..----==-.--==######################ooooo-...
                              ...---...----=o###############oo=-.
                                   ......----ooo==--.......
"""

SCONE = r"""
                                                    .-=o###@@@@@@@@@@@@##oo==o#####=-..
                                             .-o#@#@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@#@@@@o-.
                                           -@@##o##@@@#@@#@@@@@@#oo###@@@@@@@@@#@#@@@@@#@@@@@@@@o.
                                         -o###@@@@@@@@####@@@@@@@#@@@@@@@@#@@@@#oo#@@@@#@@@@@@@@@@@.
                                        -ooooooo=ooo##@###@@@##ooo##@###@@#@@@@@@@@@@@@@@@@@@@@@@@@@o
                                        =oooooooooo=-===o@@@@#@@@o#oo=oooo#o#@###@o####@@@@@@@@#@@@@@o.
                                        =ooooooooo#oo=oooooooo@@@##@@@==ooo###@@@@@@@o#@@@#@@@@@@@@@@@-
                                       .oo##oooooo=oo=ooooooo#ooooo=o#oooooo=ooo#@#oo#o#@@@@@@@#@@@@@@-
                                      .oo#o#ooooooooooo##ooooo#oooo==ooooooo##oooo##@###o@#@@@@@@@@@@@.
                                      -o=o#####o###ooooo#oooo#oooooooo#oooo##ooo##=o#######@@#@@@@@@@.
                                     -oooo=#########oo##o=#o######oo#o=oooo##oooo##ooo####o@@##@@@@@-
                                       .ooo#o=oo=#####o###oo####o##ooo#########o#o#####o#oo@@@@@@@@@.
                                      =@@@@@#####oo@#ooooo#o#####o#@#######o###ooo####@##@@@@@@@@@@-
                                     -#@@@@@@@@####@@@@@@#oooo###########o#o######oo#@@##@@@@@@@@#.
                                   .-=@@@@@@@@@@##@@@@@@@@@##o##o=o-===###o#############@@@@@@@@@.
                                   .-o@@@@@@@@@@@@@@@@@@@@@@@########oooo####o####@@@@@@@@@@@@@@@@.
                                   .=@@@@@@@@@@@@@@@@@@@@@@@@@ooo#####@@@@@@@@@@@@@@@@@@@@@@@@@o#@@-
                                   .=o@@@@@@@@@@@@@@@@@@@@@@@@#ooooo#@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@-
                                   .=-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#o@@@@o#@=
                                   .oo-o@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@oo====o=oooo@-
                                   .=o=--o@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@oo=@o----=====oo#@#=.
                                    =o#--.--oo#@@@#@@@@@@@@@@@@@@@@o=----=oo=---==oooo-----===o@@@=.
                                    =o##=-----------==oo@@@@@@@@@@#------.------===#@@@o===o#@@@@=
                                    -####o=---.---------#@@@@@@@#-----------=-=###@@@@@@#@###@@@@.
                                    -#####o==-----=-----=-==-----=----==--===o##@#@#@@@@@@@@#@@@=
                                    .o###o---==-==---=-========--===----o###@#@#@@@##@@@@o@@@@@@.
                                     -oo#o---------=---==o=---===--===o##o#@##o##@@@#o#@@@@@@@@.
                                      .ooo=---------==oo=-==oo=---==oo@@@@#@@@@@@@##o#@@#@#@@#.
                                        -ooo=----==o#####@#==--======o#o######@#@#oo####@@@#-.
                                          .o===-=o############=======##@#@##@#o##ooo####o-.
                                            ..-=oooo#oooo#####o=====o#ooo####=####oo#o-.
                                                .-=====o==oo##o=-==--=oooooooo#ooo=.
                                                     ...-===oo=----===o=====..
                                                              ..----..
"""

BUN = r"""
                                               ...--=o##@@-o@@@@@#-.....
                                       ..-=o#@@@@o=@@@#@@@#.@@@@##@@@@@#o#@#.
                                 .oo=#@#@@oo@@@@##o-=@@@###o@@@#o#@@#--=ooooo#ooo-.
                               .-@@@@@@@@o=#@@@@###@##@#@@#====--o#@@@#######ooo#o=.
                            .=@@@@@@@@@##=@@@@@#@@#o##o#@@o@#ooooooo##@#ooo=-o#ooo###=.
                          -#@@@@@@@###@@@#-#@@@@@@@@@@o#@@o--oo##ooo#==--.-=@#o#@#ooo##o-.
                        -@@@####@@@@@@@@#@#@@@@@@@@@@@@@@@####o===o##==oo===oo=ooo@#oo####=.
                      -#@@@@#-=@@@@@@@@#@@@@@@@@##@##@@@@#=@@=o=====.-==========--@@########=
                    .=@@@@@@@@@@@@@@@@@#@@@@@@@@@@@-o@oooooo============oo--=======oooo####@@#.
                   .o@@@@@-@@@@@@@@@@oo=-o@@@@@@@@@@=##oo==o=======o=oo==---=======oooo#####@@#-
                  .#@@@@@@@@@@@@@@@@@@@#oo@#@@@@@@@#ooo====o==#@o=-=-=============ooooo#######@#o.
                 .o@@@@@@@@@@@@@@@@@@@#@@@o@##@@@@###o=======#@o=-.---=========ooooooooo#oo######=.
                 =@@@@@@@@@@@@@@@@######@@#@####o==o===========--------===ooooo==ooooo#ooooo######-
                .@@@@@@@@@#@@@@@@@#######o###ooooo=o====================ooooooooooooooooooooo#####o.
                =@@#@####@@####@############o==ooooooo==============o===ooooooooooooooooooo#oo####o.
                #@@@@######@@####ooooo##oooooooooooooo============o==ooooooooooooooooooooooooo####o.
                #@@@@@@###########oooooooo####o#ooo==oo=====oo=o===o=====ooooooooooooooooooooo####o.
                #@@@@@@@@#########ooooooo##o#ooooooooo===oo=======oooooooooooo#oooooooooo#ooo#o###o.
                =@@@@@@@@@#####oo#oooooooooooooooooooo==============ooooooooooo#ooooooo##ooooo####-.
                .@@@@@@@@@@@#####o###oooooooooooooooooo==oo=ooo==o=o==oooooooooooooo#############o-
                 -@@@@@@@@@@@@@#####oo##ooooooooo#oooooooooooooooooooooooo#####ooo#o#############-.
                  .#@@@@#@##@####@#######ooooooooooooooooooooooooooooooooo######################-
                   .-#@@@@@###############o#########oooooooo#####oooo#######o##################-
                     .-o@@@@@##############################################ooo##ooooo########=.
                        ..o#@@@#####@####o###############################ooooooooooo######o-.
                            .-o###################oo##############oooooo#oooo###oooo###o=.
                               ..-o#################################oo#o###oooooooooo=..
                                    ..=ooooo#####o##oo##ooooooooooooooooooooooo===-.
                                          ....-------=====================--..
"""

PASTRY = r"""
                                                              .
                                                               .
                                                                -
                                                                -



                                                                  .
                                                            -=o###oo##
                                                         o#########=###
                                                     .o############o=##.
                                                    =###############oo#-
                                                     -#########oo#ooo----.
                                                     -#########oooo=.....-
                                         o#o#@@@##@@#@@########ooo-.-...    ...
                           .oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@####ooo=. --.    ....
                    =#@@@@@@@@@@@@@@@@#@@@@@@#@@@@@@@@@@@@@###ooo#-              =.
                 =@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@#@@@@@o-..        ..=###=
                 @@@@@@@@@@@@@@@@@@#@@@@@@#@@@#@@@@@@@@@@@@@@@@@@#@@@o.      .-oo#####-
                -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##ooo#########@o
                 o##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@o
                 -##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
                 .####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o
                  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####@@@=
                  ######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@#@@@##@@@#####@########oo#o###@@=
                  @@@#####@@@@@@@@@@@@@@@@@@#######################oooooooooooooooo#oo#@##@=
                -#@@@@######@@@@@@######################ooooooooooooooooooo=--oooooooo##@#@##=
             o##oo#@@@@######@@##################o#oooooooooooooooooooooooooooooooo=##@@@@@#####o
          =##ooooo##@@@@@@####@@#########ooooooooooooooooooooooo#oooooooooo#o#o###@#####@@@########-
        o#oooooooo###@@@@@#####@##oooooooooooooooooooooooo=ooooo#oooooo#######@@@@@@@#@@@@@##########=
      ##ooooooooo#####@@@@@@######ooooooooooooooooooooo#o##o#####oo##@@@@@@@@@@@@@@#@@@@@@@#o##########=
    =#oo=oooooo##@@@@###@@@@@@######oooooooooooooooooo#########oooo#@@@@@@@@@@@#######ooo#####oo####oo##o.
   o#o==oo=oooooo##@@@@##@@@@@##@###oooooooooo###o################@@@@@@####ooooooooooooo##ooo#ooooooooo##-
  ##o=ooooooooo####@@@@###@@@@@@###ooo##############@@@@@@#######@###ooooooooooooooo##oo###oooooooooooooo##=
 ##oooooooo#oo######@@@@####@@@@@############@###@@@@@@@@@#########oooooooooo###oo#oo##o#@@oooooooooooooo###.
o##ooooooo#oo########@@@@###@@@@@@#####@@##########o####oooo###ooo#o#oooo##################oooooooooooo######
##ooooooo#############@@@@@###@@@@@#@##oooooooooooooooooo#########@@###@@@@@@@@###ooooo###ooo==oo=ooooo######-
@#oooooo###########@####@@@@##@@##ooooooooooooooooo#######oooo##@@@@@@@@@@@@##ooooooooo###oooo=oooooooo######=
@##ooooo###########@@@###@@@@@@####oooooooooooo######@###o#o#oo#@##@@@@####oooooooooooo###oooooooooo#o#######=
@##ooooo###########@@@@###@@@@@#####oooo=o=o=####@@@@@@@@@##########oooooooooooooo=o==oo###o##oo#oo##########.
-@##################@@@###@@@@######oooo===oo@@@@@@@##o#o########oooooooooo==oooo###########################o
 =@#################@@@####@###@##########o#oooooooooooooooooooooo=====ooo##################################
  =@##################@@@#######@#o##ooooooooooooo==ooo=o====o====oo#######################################
    #@#################@@@@####@@####o==ooo=--=oooooo====oooo############################################o
     .@@@#################@@@#@@@##oooo==ooo=oooo#######################################################-
        #@@##################@#@###===ooo#############################################################-
          -#@@@##############@@####################################################################o.
             .o@@@###########@###################################################################-
                 -o#@@@@#####################################################################o.
                      -o#@@@@@##########################################################o=
                            -o###@@@@@############################################o=.
                                    -=oo#################################oo=-
                                                      ......
"""



def penguin_plush():
    while True:
        Clear()
        print(PENGUIN_PLUSH)
        time.sleep(0.5)
        Action = input('What would you like to do? (squish/leave): ').lower()
        if Action == 'squish':
            print('You squeezed the plush.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def koala_plush():
    while True:
        Clear()
        print(KOALA_PLUSH)
        time.sleep(0.5)
        Action = input('What would you like to do? (squish/leave): ').lower()
        if Action == 'squish':
            print('You squeezed the plush.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue        
def tiger_plush():
    while True:
        Clear()
        print(TIGER_PLUSH)
        time.sleep(0.5)
        Action = input('What would you like to do? (squish/leave): ').lower()
        if Action == 'squish':
            print('You squeezed the plush.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def giraffe_plush():
    while True:
        Clear()
        print(GIRAFFE_PLUSH)
        time.sleep(0.5)
        Action = input('What would you like to do? (squish/leave): ').lower()
        if Action == 'squish':
            print('You squeezed the plush.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def monkey_plush():
    while True:
        Clear()
        print(MONKEY_PLUSH)
        time.sleep(0.5)
        Action = input('What would you like to do? (squish/leave): ').lower()
        if Action == 'squish':
            print('You squeezed the plush.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def elephant_plush():
    while True:
        Clear()
        print(ELEPHANT_PLUSH)
        time.sleep(0.5)
        Action = input('What would you like to do? (squish/leave): ').lower()
        if Action == 'squish':
            print('You squeezed the plush.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def keychain():
    while True:
        Clear()
        print(KEYCHAIN)
        time.sleep(0.5)
        Action = input('What would you like to do? (inspect/leave): ')
        if Action == 'inspect':
            print('The keychain shines.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def postcard():
    while True:
        Clear()
        print(POSTCARD)
        time.sleep(0.5)
        Action = input('What would you like to do? (inspect/leave): ')
        if Action == 'inspect':
            print('The postcard looks bland.')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def tiger_shirt():
    while True:
        Clear()
        print(TIGER_SHIRT)
        time.sleep(0.5)
        Action = input('What would you like to do? (inspect/leave): ')
        if Action == 'inspect':
            print('The shirt looks okay...')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def safari_shirt():
    while True:
        Clear()
        print(SAFARI_SHIRT)
        time.sleep(0.5)
        Action = input('What would you like to do? (inspect/leave): ')
        if Action == 'inspect':
            print('The shirt looks okay...')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def giraffe_shirt():
    while True:
        Clear()
        print(GIRAFFE_SHIRT)
        time.sleep(0.5)
        Action = input('What would you like to do? (inspect/leave): ')
        if Action == 'inspect':
            print('The shirt looks okay...')
            time.sleep(1)
            continue
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def espresso():
    while True:
        global Inventory
        Clear()
        print(ESPRESSO)
        time.sleep(0.5)
        Action = input('What would you like to do? (drink/leave): ').lower()
        if Action == 'drink':
            print('You drank the espresso.')
            Inventory.remove('Silverback Espresso')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def americano():
    while True:
        global Inventory
        Clear()
        print(AMERICANO)
        time.sleep(0.5)
        Action = input('What would you like to do? (drink/leave): ').lower()
        if Action == 'drink':
            print('You drank the americano.')
            Inventory.remove('Anaconda Americano')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def latte():
    while True:
        global Inventory
        Clear()
        print(LATTE)
        time.sleep(0.5)
        Action = input('What would you like to do? (drink/leave): ').lower()
        if Action == 'drink':
            print('You drank the latte.')
            Inventory.remove('Pink Flamingo Latte')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def tea():
    while True:
        global Inventory
        Clear()
        print(TEA)
        time.sleep(0.5)
        Action = input('What would you like to do? (drink/leave): ').lower()
        if Action == 'drink':
            print('You drank the tea.')
            Inventory.remove('Toucan Tropical Tea')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def doughnut():
    while True:
        global Inventory
        Clear()
        print(DOUGHNUT)
        time.sleep(0.5)
        Action = input('What would you like to do? (eat/leave): ').lower()
        if Action == 'eat':
            print('You ate the doughnut.')
            Inventory.remove('Dugong Doughnut')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def scone():
    while True:
        global Inventory
        Clear()
        print(SCONE)
        time.sleep(0.5)
        Action = input('What would you like to do? (eat/leave): ').lower()
        if Action == 'eat':
            print('You ate the scone.')
            Inventory.remove('Sun Bear Scone')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def bun():
    while True:
        global Inventory
        Clear()
        print(BUN)
        time.sleep(0.5)
        Action = input('What would you like to do? (eat/leave): ').lower()
        if Action == 'eat':
            print('You ate the bun.')
            Inventory.remove('Oreo Panda Bun')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue
def pastry():
    while True:
        global Inventory
        Clear()
        print(PASTRY)
        time.sleep(0.5)
        Action = input('What would you like to do? (eat/leave): ').lower()
        if Action == 'eat':
            print('You ate the pastry.')
            Inventory.remove('Lion Claw Pastry')
            time.sleep(1)
            break
        elif Action == 'leave':
            break
        else:
            print('Something went wrong')
            time.sleep(0.5)
            continue

def search_inventory(): 
    while True:
        Clear()
        if len(Inventory) != 0:
            print(Inventory)
            return_to_zoo = input('Would you like search or exit inventory?: ')
            if return_to_zoo in ['exit','leave']:
                break
            elif return_to_zoo == 'search':
                inspect_item = input('What item would you like to inspect? (type exactly): ')
                if inspect_item in Inventory:
                    if inspect_item == 'Penguin Plush':
                        penguin_plush()
                        continue
                    elif inspect_item == 'Koala Plush':
                        Clear()
                        koala_plush()
                        continue
                    elif inspect_item == 'Elephant Plush':
                        Clear()
                        elephant_plush()
                        continue
                    elif inspect_item == 'Tiger Plush':
                        Clear()
                        tiger_plush()
                        continue
                    elif inspect_item == 'Monkey Plush':
                        Clear()
                        monkey_plush()
                        continue
                    elif inspect_item == 'Giraffe Plush':
                        Clear()
                        giraffe_plush()
                        continue
                    elif inspect_item == 'Python Zoo Keychain':
                        Clear()
                        keychain()
                        continue
                    elif inspect_item == 'Python Zoo Postcard':
                        Clear()
                        postcard()
                        continue
                    elif inspect_item == 'Safari Shirt':
                        Clear()
                        safari_shirt()
                        continue
                    elif inspect_item == 'Tiger Shirt':
                        Clear()
                        tiger_shirt()
                        continue
                    elif inspect_item == 'Giraffe Shirt':
                        Clear()
                        giraffe_shirt()
                        continue
                    elif inspect_item == 'Anaconda Americano':
                        Clear()
                        americano()
                        continue
                    elif inspect_item == 'Toucan Tropical Tea':
                        Clear()
                        tea()
                        continue
                    elif inspect_item == 'Pink Flamingo Latte':
                        Clear()
                        latte()
                        continue
                    elif inspect_item == 'Silverback Espresso':
                        Clear()
                        espresso()
                        continue
                    elif inspect_item == 'Dugong Doughnut':
                        Clear()
                        doughnut()
                        continue
                    elif inspect_item == 'Sun Bear Scone':
                        Clear()
                        scone()
                        continue
                    elif inspect_item == 'Lion Claw Pastry':
                        Clear()
                        pastry()
                        continue
                    elif inspect_item == 'Oreo Panda Bun':
                        Clear()
                        bun()
                        continue
                    else:
                        print('Something went wrong')
                        time.sleep(0.5)
                        continue
                else:
                    print(f"{inspect_item} is not in inventory")
                    time.sleep(1)
                    continue
            else:
                continue
        else:
            print('Your inventory is empty...')
            time.sleep(1)
            break
def gift_shop(): # done
    global Monkey_Plush_Count, Elephant_Plush_Count, Penguin_Plush_Count, Tiger_Plush_Count, Koala_Plush_Count, Giraffe_Plush_Count, Keychain_Count, Postcard_Count, Your_Money, Total_Cost, Inventory
    Cart = []
    while True:
        Clear()
        print(GIFT_SHOP.format(cost=f"{Total_Cost:05.2f}",money=f"{Your_Money:05.2f}"))
        Actions = input('What would you like to do? (add (to cart), view (cart), buy, leave): ').lower()
        if Actions in ['add', 'add to cart', 'add cart', 'addcart']:
            AddCartItem = input('Would you like to add? (plush, keychain, postcard, book, apparel): ').lower()
            if AddCartItem in ['plush']:
                print(rf"""There is 
{Penguin_Plush_Count} Penguin Plushies $6.95
{Tiger_Plush_Count} Tiger Plushies $10.38
{Elephant_Plush_Count} Elephant Plushies $9.56
{Koala_Plush_Count} Koala Plushies $8.76
{Giraffe_Plush_Count} Giraffe Plushies $8.59
{Monkey_Plush_Count} Monkey Plushies $9.99
in stock.""")
                AddPlushToCart = input('Please input plush name: ').lower()
                if AddPlushToCart in ['penguin', 'penguinplush', 'penguin plush']:
                    if Penguin_Plush_Count != 0:
                        Cart.append('Penguin Plush')
                        Total_Cost += 6.95
                        Penguin_Plush_Count -= 1
                        print(f"Added Penguin Plush to cart. There is {Penguin_Plush_Count} Penguin Plush(es) left.")
                        time.sleep(1)
                        continue
                    else:
                        print('There is no more Penguin Plushes in stock.')
                        time.sleep(1)
                        continue
                elif AddPlushToCart in ['tiger', 'tiger plush', 'tigerplush']:
                    if Tiger_Plush_Count != 0:
                        Cart.append('Tiger Plush')
                        Total_Cost += 10.38
                        Tiger_Plush_Count -= 1
                        print(f"Added Tiger Plush to cart. There is {Tiger_Plush_Count} Tiger Plush(es) left.")
                        time.sleep(1)
                        continue
                    else:
                        print("There is no more Tiger Plushes in stock.")
                        time.sleep(1)
                        continue
                elif AddPlushToCart in ['elephant', 'elephantplush', 'elephant plush']:
                    if Elephant_Plush_Count != 0:
                        Cart.append('Elephant Plush')
                        Total_Cost += 9.56
                        Elephant_Plush_Count -= 1
                        print(f"Added Elephant Plush to cart. There is {Elephant_Plush_Count} Elephant Plush(es) left.")
                        time.sleep(1)
                        continue
                    else:
                        print('There is no more Elephant Plushes in stock.')
                        time.sleep(1)
                        continue
                elif AddPlushToCart in ['koala', 'koala plush', 'koalaplush']:
                    if Koala_Plush_Count != 0:
                        Cart.append('Koala Plush')
                        Total_Cost += 8.76
                        Koala_Plush_Count -= 1
                        print(f"Added Koala Plush to cart. There is {Koala_Plush_Count} Koala Plush(es) left.")
                        time.sleep(1)
                        continue
                    else:
                        print('There is no more Koala Plushes in stock.')
                        time.sleep(1)
                        continue
                elif AddPlushToCart in ['giraffe', 'giraffeplush', 'giraffe plush']:
                    if Giraffe_Plush_Count != 0:
                        Cart.append('Giraffe Plush')
                        Total_Cost += 8.59
                        Giraffe_Plush_Count -= 1
                        print(f"Added Giraffe Plush to cart. There is {Giraffe_Plush_Count} Giraffe Plush(es) left.")
                        time.sleep(1)
                        continue
                    else:
                        print('There is no more Giraffe Plushes in stock.')
                        time.sleep(1)
                        continue
                elif AddPlushToCart in ['monkey' or 'monkeyplush' or 'monkey plush']:
                    if Monkey_Plush_Count != 0:
                        Cart.append('Monkey Plush')
                        Total_Cost += 9.99
                        Monkey_Plush_Count -= 1
                        print(f"Added Monkey Plush to cart. There is {Monkey_Plush_Count} Monkey Plush(es) left.")
                        time.sleep(1)
                        continue
                    else:
                        print('There is no more Monkey Plushes in stock.')
                        time.sleep(1)
                        continue
                else:
                    print('Returning...')
                    time.sleep(1)
                    continue           
            elif AddCartItem in ['keychain', 'key chain']:
                print(f"There is {Keychain_Count} Python Zoo Keychain(s) for $2.46 in stock...")
                AddKeyChainToCart = input('Would you like to add a Python Zoo Keychain to the cart? (y/n): ').lower()
                if AddKeyChainToCart == 'y':
                    Cart.append('Python Zoo Keychain')
                    Total_Cost += 2.46
                    Keychain_Count -= 1
                    print(f"Added Python Zoo Keychain to cart. There is {Keychain_Count} Keychain(s) left.")
                    time.sleep(0.75)
                    continue
                elif AddKeyChainToCart == 'n':
                    print('Returning...')
                    time.sleep(1)
                    continue
                else:
                    print('Something went wrong')
                    time.sleep(1)
                    continue
            elif AddCartItem in ['postcard', 'post', 'card', 'post card']:
                print(f'There is {Postcard_Count} Python Zoo Postcard(s) for $1.50 in stock...')
                AddPostcardToCart = input('Would you like to add a Python Zoo Postcard to the cart? (y/n): ').lower()
                if AddPostcardToCart == 'y':
                    Cart.append('Python Zoo Postcard')
                    Total_Cost += 1.50
                    Postcard_Count -= 1
                    print(f"Added Python Zoo Postcard to cart. There is {Postcard_Count} Postcard(s) left.")
                    time.sleep(1)
                    continue
                elif AddPostcardToCart == 'n':
                    print('Returning...')
                    time.sleep(0.75)
                    continue
                else:
                    print('Something went wrong')
                    time.sleep(0.75)
            elif AddCartItem in ['apparel','clothes','clothing','shirt','shirts']:
                print(f"""There is
{Safari_Apparel_Count} Safari shirt(s)
{Giraffe_Apparel_Count} Giraffe shirt(s)
{Tiger_Apparel_Count} Tiger shirt(s)
in stock...""")
                AddApparelToCart = input('Please input Apparel name: ').lower()
                if AddApparelToCart in ['safari','safarishirt','safari shirt','safari apparel','safariapparel']:
                    Cart.append('Safari Shirt')
                    Total_Cost += 9.99
                    Safari_Apparel_Count -= 1
                    print(f"Added Safari Shirt to cart. There is {Safari_Apparel_Count} Safari Shirt(s) left.")
                    time.sleep(1)
                    continue
                elif AddApparelToCart in ['giraffe','giraffe apparel','giraffeapparel','giraffeshirt','giraffe shirt']:
                    Cart.append('Giraffe Shirt')
                    Total_Cost += 9.99
                    Giraffe_Apparel_Count -= 1
                    print(f"Added Giraffe Shirt to cart. There is {Giraffe_Apparel_Count} Giraffe Shirt(s) left.")
                    time.sleep(1)
                    continue
                elif AddApparelToCart in ['tiger','tigershirt','tiger shirt','tiger apparel', 'tigerapparel']:
                    Cart.append('Tiger Shirt')
                    Total_Cost += 9.99
                    Tiger_Apparel_Count -= 1
                    print(f"Added Tiger Shirt to cart. There is {Tiger_Apparel_Count} Tiger Shirt(s) left.")
                    time.sleep(1)
                    continue
                else:
                    print('Something went wrong')
                    time.sleep(0.75)
                    continue


            else:
                print('Something went wrong')
                time.sleep(1)            



        elif Actions in ['buy', 'purchase','checkout']:
            if len(Cart) != 0:
                purchase = input(f"""You have the following in your cart:
{Cart}
would you like to checkout? (y/n): 
""")            
                if purchase == 'y':
                    if Your_Money >= Total_Cost:
                        Inventory.extend(Cart)
                        Your_Money -= Total_Cost
                        Total_Cost = 00.00
                        Cart = []
                        print(f"You have ${Your_Money} left...")
                        time.sleep(2)
                        continue
                    else:
                        print('You do not have enough money...')
                        time.sleep(2)
                        continue
            else:
                print('Your cart is empty...')
                time.sleep(1)
                continue

        elif Actions in ['view', 'viewcart','view cart']:
            if len(Cart) != 0:
                print(Cart)
                Remove_Answer = input('Would you like to remove an item from the cart? (y/n): ').lower()
                if Remove_Answer == 'y':
                    Remove = input('Which item would you like to remove? (type exactly): ')
                    if Remove in ['Monkey Plush', 'Elephant Plush', 'Tiger Plush', 'Giraffe plush', 'Penguin Plush', 'Koala Plush', 'Python Zoo Keychain', 'Python Zoo Postcard', 'Tiger Shirt', 'Giraffe Shirt', 'Safari Shirt']:
                        try: 
                            Cart.remove(Remove)
                        except ValueError:
                            print(f'Failed to remove {Remove} as it is not in the cart...')
                            time.sleep(1)
                            continue
                        print(f"{Remove} has been removed from the cart...")
                        if Remove == 'Monkey Plush':
                            Total_Cost -= 9.99
                            Monkey_Plush_Count += 1
                            continue
                        elif Remove == 'Penguin Plush':
                            Total_Cost -= 6.95
                            Penguin_Plush_Count += 1
                            continue
                        elif Remove == 'Koala Plush':
                            Total_Cost -= 8.76
                            Koala_Plush_Count += 1
                            continue
                        elif Remove == 'Giraffe Plush':
                            Total_Cost -= 8.59
                            Giraffe_Plush_Count += 1
                            continue
                        elif Remove == 'Elephant Plush':
                            Total_Cost -= 9.56
                            Elephant_Plush_Count += 1
                            continue
                        elif Remove == 'Tiger Plush':
                            Total_Cost -= 10.38
                            Tiger_Plush_Count += 1
                            continue
                        elif Remove == 'Python Zoo Keychain':
                            Total_Cost -= 2.46
                            Keychain_Count += 1
                            continue
                        elif Remove == 'Python Zoo Postcard':
                            Total_Cost -= 1.50
                            Postcard_Count += 1
                            continue
                        elif Remove == 'Tiger Shirt':
                            Total_Cost -= 9.99
                            Tiger_Apparel_Count += 1
                            continue
                        elif Remove == 'Giraffe Shirt':
                            Total_Cost -= 9.99
                            Giraffe_Apparel_Count += 1
                            continue
                        elif Remove == 'Safari Shirt':
                            Total_Cost -= 9.99
                            Safari_Apparel_Count += 1
                            continue
                    else: 
                        print(f'Failed to remove {Remove}.')
                        time.sleep(1)
                elif Remove_Answer == 'n':
                    print('Returning to gift shop')
                    time.sleep(1)
                    continue
                else:
                    print('Something went wrong.')
                    time.sleep(0.75)
                    continue
            else:
                print('Your cart is empty...')
                time.sleep(1)
                continue

        elif Actions in ['leave', 'exit', 'stop']:
            break

        else:
            print('something went wrong')
            continue
def tickets(): # done
    Clear()
    print(ZOO_ENTRANCE)
    time.sleep(1)
    print('You already paid for your ticket...')
    time.sleep(1)
    Go_Home = input('Would you like to go home? (y/n): ').lower()
    if Go_Home == 'y':
        print("You decided that you've had enough zoo time for the day and went home...")
        time.sleep(2)
        exit()
    elif Go_Home == 'n':
        print('You went back inside the zoo...')
        time.sleep(1)
    else:
        print('Invalid input.')
        print('Returning to zoo')
        time.sleep(1)
def cafe(): # done
    global Total_Cost, Your_Money
    Item_Cart = []
    while True:
        Clear()
        print(CAFE.format(items=f"{len(Item_Cart):02}",cost=f"{Total_Cost:05.2f}",money=f"{Your_Money:05.2f}"))
        Actions = input("What would you like to do? (add (to cart), view (cart), buy, leave): ")
        if Actions in ['add', 'add to cart', 'add cart', 'addcart']:
            AddOrderItem = input('The barista asks: What would you like to order? (type menu item): ').lower()
            if AddOrderItem in ['anaconda americano', 'anaconda', 'anacondaamericano','americano']:
                Item_Cart.append('Anaconda Americano')
                Total_Cost += 4.50
                print('Added Anaconda Americano to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['silverback espresso','espresso','silverbackespresso','silverback','gorilla']:
                Item_Cart.append('Silverback Espresso')
                Total_Cost += 4.00
                print('Added Silverback Espresso to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['pink flamingo latte','flamingo','latte','pink','pink flamingo','pinkflamingo','pinkflamingolatte']:
                Item_Cart.append('Pink Flamingo Latte')
                Total_Cost+= 5.25
                print('Added Pink Flamingo Latte to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['tropical','toucan','tea','tropicaltoucantea','toucan tropical tea','toucantropicaltea','tropical toucan tea','toucan tea']:
                Item_Cart.append('Toucan Tropical Tea')
                Total_Cost += 4.20
                print('Added Toucan Tropical Tea to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['dugong doughnut','dugong','doughnut','dugongdoughnut','donut','dugongdonut']:
                Item_Cart.append('Dugong Doughnut')
                Total_Cost += 3.50
                print('Added Dugong Doughnut to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['sunbear','sun','bear','sunbrearscone','scone','sun bear scone','bear']:
                Item_Cart.append('Sun Bear Scone')
                Total_Cost += 4.00
                print('Added Sun Bear Scone to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['oreo panda bun', 'oreo bun','panda','orea panda','oreo','oreopandabun','oreopanda']:
                Item_Cart.append('Oreo Panda Bun')
                Total_Cost += 4.50
                print('Added Oreo Panda Bun to order!')
                time.sleep(0.75)
                continue
            elif AddOrderItem in ['lion claw pastry','pastry','lion claw','lion','claw','lion pastry','lionpastry']:
                Item_Cart.append('Lion Claw Pastry')
                Total_Cost += 3.75
                print('Added Lion Claw Pastry to order!')
                time.sleep(0.75)
                continue
            else:
                print('Something went wrong')
                time.sleep(0.5)
                continue
        elif Actions in ['buy', 'purchase','checkout']:
            if len(Item_Cart) != 0:
                purchase = input(f"""You have the following in your order:
{Item_Cart}
would you like to checkout? (y/n): 
""")            
                if purchase == 'y':
                    if Your_Money >= Total_Cost:
                        Inventory.extend(Item_Cart)
                        Your_Money -= Total_Cost
                        Total_Cost = 00.00
                        Item_Cart = []
                        print(f"You have ${Your_Money} left...")
                        time.sleep(2)
                        continue
                    else:
                        print('You do not have enough money...')
                        time.sleep(2)
                        continue
            else:
                print('Your cart is empty...')
                time.sleep(1)
                continue
        elif Actions in ['view', 'viewcart','view cart']:
            if len(Item_Cart) != 0:
                print(Item_Cart)
                Remove_Answer = input('Would you like to remove an item from the order? (y/n): ').lower()
                if Remove_Answer == 'y':
                    Remove = input('Which item would you like to remove? (type exactly): ')
                    if Remove in ['Anaconda Americano','Silverback Espresso', 'Pink Flamingo Latte', 'Toucan Tropical Tea','Dugong Doughnut', 'Sun Bear Scone', 'Oreo Panda Bun', 'Lion Claw Pastry']:
                        try: 
                            Item_Cart.remove(Remove)
                        except ValueError:
                            print(f'Failed to remove {Remove} as it is not in the order...')
                            time.sleep(1)
                            continue
                        print(f"{Remove} has been removed from the cart...")
                        if Remove == 'Anaconda Americano':
                            Total_Cost -= 4.50
                            continue
                        elif Remove == 'Silverback Espresso':
                            Total_Cost -= 4.00
                            continue
                        elif Remove == 'Pink Flamingo Latte':
                            Total_Cost -= 5.25
                            continue
                        elif Remove == 'Toucan Tropical Tea':
                            Total_Cost -= 4.20
                            continue
                        elif Remove == 'Dugong Doughnut':
                            Total_Cost -= 3.50
                            continue
                        elif Remove == 'Sun Bear Scone':
                            Total_Cost -= 4.00
                            continue
                        elif Remove == 'Oreo Panda Bun':
                            Total_Cost -= 4.50
                            continue
                        elif Remove == 'Lion Claw Pastry':
                            Total_Cost -= 3.75
                            continue
                    else: 
                        print(f'Failed to remove {Remove}.')
                        time.sleep(1)
                elif Remove_Answer == 'n':
                    continue
                else:
                    print('Something went wrong.')
                    time.sleep(0.75)
                    continue
            else:
                print('Your order is empty...')
                time.sleep(1)
                continue
        elif Actions in ['leave', 'exit', 'stop']:
            break
        else:
            print('something went wrong')
            continue
def help_desk(): # done
    while True:
        Clear()
        print(HELP_DESK.format(Help_desk_text=Help_desk_attendent_lines[randint(0,7)]))
        print('What do you need help with? Commands, Locations, or Game information (code)?')
        Question = input('>').lower()
        if Question == 'commands':
            print('You must type the name of location or command you are trying to input almost exactly as I did not want to try to make the code adapt.')
            Return = input('Are you done looking at this information? (y/n): ')
            if Return == 'y':
                continue
            elif Return == 'n':
                print('Too Bad...')
                time.sleep(0.5)
                continue
            else:
                continue
        elif Question == 'locations':
            print('''The avaliable locations to travel to are:
Tickets, Gift Shop, Cafe
Fountain, Restrooms, Help Desk
The Reptiles, The Aquarium, The Sky Zone
Gate #1, Gate #2, The Savanna, The Forest''')
            Return = input('Are you done looking at this information? (y/n): ')
            if Return == 'y':
                continue
            elif Return == 'n':
                print('Too Bad...')
                time.sleep(0.5)
                continue
            else:
                continue
        elif Question in ['game information','info','game info']:
            print('''Most things are randomised when possible. 
Fountain, item, and animal graphics were made with an ascii image converter.
Your money is randomised from $35 to $80.
I tried to make the game have humor...
The entire file is about 6100 lines of code, about half are dedicated to graphics. The other half is code.
There is techincally a small secret in the Northern River.
Yes, I know a pelican eel could not survive in a aquarium at sea level pressure.
The file is very big, so that means there could be a bug somewhere that I do not know about.''')
            Return = input('Are you done looking at this information? (y/n): ')
            if Return == 'y':
                continue
            elif Return == 'n':
                print('Too Bad...')
                time.sleep(0.5)
                continue
            else:
                continue
        elif Question == 'leave':
            break
        else:
            continue
def fountain(): # done
    while True:
        global Your_Money
        Clear()
        print(FOUNTAIN)
        print('You walk up to the fountain...')
        Fountain_action = input('What would you like to do? (leave/admire/coin): ').lower()
        if Fountain_action == 'admire':
            print('You admire the fountain...')
            time.sleep(1)
            continue
        elif Fountain_action == 'coin':
            Toss_coin = input('Would you like to toss a quarter in? (y/n): ')
            if Toss_coin == 'y':
                print('You toss in a quarter...')
                Your_Money -= 0.25
                time.sleep(0.5)
                print(f"You have ${Your_Money:.2f} left...")
                time.sleep(0.75)
                continue
            elif Toss_coin == 'n':
                print('You decided to save your money...')
                time.sleep(1)
                continue
            else:
                print('Something went wrong')
                time.sleep(0.25)
                continue
        elif Fountain_action == 'jump':
            print('You elegantly leap into the fountain...')
            time.sleep(0.75)
            if randint(0,100) >= 93:
                print('You Found a Quarter in the fountain!')
                Your_Money += 0.25
                print(f'You have ${Your_Money:.2f} now!')
                time.sleep(1)
            else:
                pass
            print('You quickly get out of the fountain')
            time.sleep(1)    
            print('Somehow, no one saw you jump in...')
            time.sleep(1.5)
            continue
        elif Fountain_action == 'leave':
            break
        else:
            print('Something went wrong')
def restrooms(): # done
    Clear()
    print(RESTROOM)
    time.sleep(2)
    print('The Restrooms are "out of order for maintenence..."')
    time.sleep(1)
    print('You head back...')
    time.sleep(1.5)
def gate1(): # done
    while True:
        global GATE1_PASS
        Clear()
        print(GATE1)
        time.sleep(0.5)
        if GATE1_PASS == False:
            print('The security guard asks to see your ticket.')
            time.sleep(1)
            print('You flashed your ticket to him and he allows you to pass.')
            time.sleep(1.5)
            GATE1_PASS = True
            walk_through = input('Would you like to walk through? (y/n): ')
            if walk_through == 'y':
                time.sleep(1)
                print('He lets you walk through...')
                time.sleep(1)
                Clear()
                print('Travelling to The Savanna.')
                savanna()
                break
            elif walk_through == 'n':
                print('You decided to walk back to the main area.')
                time.sleep(1)
                break
            else:
                print('Something went wrong')
                time.sleep(0.75)
                continue
        if GATE1_PASS == True:
            print('The guard recognises you from earlier...')
            time.sleep(1)
            walk_through = input('Would you like to walk through? (y/n): ')
            if walk_through == 'y':
                time.sleep(2)
                print('He lets you walk through...')
                time.sleep(2)
                Clear()
                print('Travelling to The Savanna.')
                savanna()
                break
            elif walk_through == 'n':
                print('You decided to walk back to the main area.')
                time.sleep(1)
                break
            else:
                print('Something went wrong')
                time.sleep(0.75)
                continue    
        else:
            print('Something went wrong')
            continue
def gate2(): # done
    global GATE2_PASS
    while True:
        Clear()
        print(GATE2)
        time.sleep(0.5)
        if GATE2_PASS == False:
            print('The security guard asks to see your ticket.')
            time.sleep(1)
            print('You flashed your ticket to him and he allows you to pass.')
            time.sleep(1)
            GATE2_PASS = True
            walk_through = input('Would you like to walk through? (y/n): ')
            if walk_through == 'y':
                time.sleep(1)
                print('He lets you walk through...')
                time.sleep(1)
                Clear()
                print('Travelling to The Forest.')
                forest()
                break
            elif walk_through == 'n':
                print('You decided to walk back to the main area.')
                time.sleep(1)
                break
            else:
                print('Something went wrong')
                time.sleep(0.75)
                continue
        if GATE2_PASS == True:
            print('The guard recognises you from earlier...')
            time.sleep(1)
            walk_through = input('Would you like to walk through? (y/n): ')
            if walk_through == 'y':
                time.sleep(2)
                print('He lets you walk through...')
                time.sleep(2)
                Clear()
                print('Travelling to The Forest.')
                forest()
                break
            elif walk_through == 'n':
                print('You decided to walk back to the main area.')
                time.sleep(1)
                break
            else:
                print('Something went wrong')
                time.sleep(0.75)
                continue    
        else:
            print('Something went wrong')
            continue
def savanna(): # done
    while True:
        Clear()
        print(SAVANNA)
        time.sleep(0.5)
        travel_to = input('Where would you like to go?: ').lower()
        if travel_to == 'ocelot':
            time.sleep(0.5)
            see_ocelot()
            continue
        elif travel_to == 'pangolin':
            time.sleep(0.5)
            see_pangolin()
            continue
        elif travel_to in ['painted wolf','wolf', 'painted']:
            time.sleep(0.5)
            see_wolf()
            continue
        elif travel_to in ['black rhinoceros','black','rhinoceros','rhino','black rhino']:
            time.sleep(0.5)
            see_rhino()
            continue
        elif travel_to in ['gate', 'gate1', 'gate 1','leave']:
            Clear()
            print('Leaving Savanna...')
            time.sleep(1)
            break
        else:
            continue
def forest(): # done
    while True:
        Clear()
        print(FOREST)
        time.sleep(0.5)
        travel_to = input('Where would you like to go?: ').lower()
        if travel_to == 'lynx':
            time.sleep(0.5)
            see_lynx()
            continue
        elif travel_to == 'capybara':
            time.sleep(0.5)
            see_capybara()
            continue
        elif travel_to in ['silverback gorilla','gorilla','silver','silver gorilla']:
            time.sleep(0.5)
            see_gorilla()
            continue
        elif travel_to == 'wolverine':
            time.sleep(0.5)
            see_wolverine()
            continue
        elif travel_to == 'jaguar':
            time.sleep(0.5)
            see_jaguar()
            continue
        elif travel_to in ['gate', 'gate2', 'gate 2','leave']:
            Clear()
            print('Leaving Forest...')
            time.sleep(1)
            break
        else:
            continue
def reptile_house(): # done
    while True:
        Clear()
        print(REPTILE_HOUSE)
        time.sleep(0.5)
        travel_to = input('Where would you like to go?: ').lower()
        if travel_to == 'axolotl':
            time.sleep(0.5)
            see_axolotl()
            continue
        elif travel_to == 'jerboa':
            time.sleep(0.5)
            see_jerboa()
            continue
        elif travel_to in ['crocodile','indian crocodile','gharial crocodile','gharial','indian gharial crocodile']:
            time.sleep(0.5)
            see_indian_gharial()
            continue
        elif travel_to in ['newt','crested newt','danube crested newt']:
            time.sleep(0.5)
            see_newt()
            continue
        elif travel_to in ['amazon mata mata','mata','mata mata']:
            time.sleep(0.5)
            see_mata()
            continue
        elif travel_to in ['worm lizard','worm']:
            time.sleep(0.5)
            see_worm_lizard()
            continue
        elif travel_to in ['mountain','mountain chicken','chicken']:
            time.sleep(0.5)
            see_mountain_chicken()
            continue
        elif travel_to in ['sand boa','arabian sand boa','boa']:
            time.sleep(0.5)
            see_sand_boa()
            continue
        elif travel_to in ['burmese python','python']:
            time.sleep(0.5)
            see_python()
            continue
        elif travel_to in ["jackson's chamelon",'chameleon']:
            time.sleep(0.5)
            see_chameleon()
            continue
        elif travel_to in ['snake-necked turtle','snake necked turtle','snake turtle']:
            time.sleep(0.5)
            see_snake_turtle()
            continue
        elif travel_to in ['main entrance','leave']:
            Clear()
            print('Leaving Reptile House...')
            time.sleep(1)
            break
        else:
            continue
def aquarium():
    while True:
        Clear()
        print(AQUARIUM)
        time.sleep(0.5)
        travel_to = input('Where would you like to look?: ').lower()
        if travel_to == 'lamprey':
            time.sleep(0.5)
            see_lamprey()
            continue
        elif travel_to == 'sunfish':
            time.sleep(0.5)
            see_sunfish()
            continue
        elif travel_to in ['giant','isopod','giant isopod']:
            time.sleep(0.5)
            see_giant_isopod()
            continue
        elif travel_to in ['blue','dragon','blue dragon']:
            time.sleep(0.5)
            see_blue_dragon()
            continue
        elif travel_to in ['pelican','eel','pelican eel']:
            time.sleep(0.5)
            see_pelican_eel()
            continue
        elif travel_to == 'bichir':
            time.sleep(0.5)
            see_bichir()
            continue
        elif travel_to in ['manta','ray', 'manta ray']:
            time.sleep(0.5)
            see_manta_ray()
            continue
        elif travel_to in ['main entrance','leave']:
            Clear()
            print('Leaving Aquarium...')
            time.sleep(1)
            break
        else:
            continue
def bird_house(): # done
    while True:
        Clear()
        print(BIRD_HOUSE)
        time.sleep(0.5)
        travel_to = input('Where would you like to look?: ').lower()
        if travel_to == 'shoebill':
            time.sleep(0.5)
            see_shoebill()
            continue
        elif travel_to == 'pukeko':
            time.sleep(0.5)
            see_pukeko()
            continue
        elif travel_to == 'potoo':
            time.sleep(0.5)
            see_potoo()
            continue
        elif travel_to == 'macaw':
            time.sleep(0.5)
            see_macaw()
            continue
        elif travel_to in ['main entrance','leave']:
            Clear()
            print('Leaving Bird House...')
            time.sleep(1)
            break
        else:
            continue
while True:
    print('Zoom out terminal when viewing animals for the best experience!')
    h = input('Proceed?: ')
    print(ZOO_ENTRANCE,end='')
    time.sleep(1)
    print(f"You brought ${Your_Money:.2f} with you...")
    if randint(1,100) >= 92:
        print(f"It's your lucky day, as tickets are on sale for ${Sale_Ticket_Price}!")
        Answer = input(f'Would you like to buy a ticket for ${Sale_Ticket_Price}? (y/n): ')
        Sale = True
    else:
        print("Zoo ticket prices are kinda expensive nowadays...")
        Answer = input(f'Would you like to buy a ticket for ${Normal_Ticket_Price}? (y/n): ')
    
    if Answer == 'n':
        print("You Decided to come back to the zoo on another day...Maybe prices were too high, or maybe you didn't bring enough cash...Come Back Soon!")
        time.sleep(2.5)
        Clear()
        exit()
    elif Answer == 'y':
        Clear()
        if Sale == True:
            Your_Money -= Sale_Ticket_Price
        else:
            Your_Money -= Normal_Ticket_Price
        print(f"You have ${Your_Money:.2f} left...")
        print('Entering...')
        time.sleep(1.5)
        break
    else:
        Clear()
        continue
while True:
    Clear()
    print(ZOO_MAIN_AREA)
    Answer = input('Where you would like to go? (type location name, I for inventory): ').lower()
    Clear()
    if Answer == 'tickets':
        print('Travelling to Tickets')
        time.sleep(1)
        tickets()
    elif Answer in ['gift shop', 'giftshop', 'gift']:
        print('Travelling to Gift Shop')
        time.sleep(1)
        gift_shop()
    elif Answer == 'cafe':
        print('Travelling to Cafe')
        time.sleep(1)
        cafe()
    elif Answer == 'i':
        search_inventory()
    elif Answer in ['help desk','help']:
        print('Travelling to Help Desk')
        time.sleep(1)
        help_desk()
    elif Answer == 'fountain':
        print('Travelling to The Fountain')
        time.sleep(1)
        fountain()
    elif Answer in ['restroom','restrooms']:
        print('Travelling to The Restrooms')
        time.sleep(1)
        restrooms()
    elif Answer in ['gate2', 'gate 2']:
        print('Travelling to Gate 2')
        time.sleep(1)
        gate2()
    elif Answer in ['gate1', 'gate 1']:
        print('Travelling to Gate 1')
        time.sleep(1)
        gate1()
    elif Answer in ['the savanna', 'savanna', 'thesavanna']:
        if GATE1_PASS == False:
            print('You must talk to the guard at Gate 1 first...')
            print('Travelling to Gate 1.')
            time.sleep(2)
            gate1()
        elif GATE1_PASS == True:
            print('You must pass Gate 1 to enter...')
            print('Travelling to Gate 1.')
            time.sleep(2)
            gate1()
    elif Answer in ['the forest','forest','theforest']:
        if GATE2_PASS == False:
            print('You must talk to the guard at Gate 2 first...')
            print('Travelling to Gate 2.')
            time.sleep(2)
            gate2()
        elif GATE2_PASS == True:
            print('You must pass Gate 2 to enter...')
            print('Travelling to Gate 2.')
            time.sleep(2)
            gate2()
    elif Answer in ['reptiles','thereptiles','the reptiles']:
        print('Travelling to The Reptiles...')
        time.sleep(2)
        reptile_house()
    elif Answer in ['the aquarium', 'aquarium']:
        print('Travelling to Aquarium')
        time.sleep(2)
        aquarium()
    elif Answer in ['bird house','bird']:
        print('Travelling to Bird House')
        time.sleep(2)
        bird_house()
    elif Answer in ['northern river','river','northern']:
        print(WIP)
        time.sleep(2)
        print('This place is not finished yet...')
        time.sleep(1)
        print('This programmar sucks...')
        time.sleep(1.5)
    else:
        continue