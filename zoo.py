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
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"
# Create a variable for the animals in your zoo tuple, and print them to the console.
(animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10) = zoo
for str in zoo:
    print(str)

# Convert your tuple into a list.
zoo = list(zoo)
print(zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(["kangaroos", "llamas", "giraffs"])
print(zoo)

# Convert the list back into a tuple.
zoo = tuple(zoo)
print(zoo)