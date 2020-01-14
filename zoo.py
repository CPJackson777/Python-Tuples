# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("lions", "tigers", "bears", "beavers", "monkeys", "pythons", "frogs", "fish", "elephants", "rhinos")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
print(zoo.index("tigers"))

# Determine if an animal is in your tuple by using value in tuple syntax.
# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
#     # Print that the animal was found
animalToFind = "bears"
if animalToFind in zoo:
    print(f'{animalToFind} are found.')

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
