# Create an empty set named showroom.

showroom = set()

# Add four of your favorite car model names to the set.

showroom = { 'Porsche 911 GT3 RS', 'Toyota Supra', 'Nissan GT-R', 'Audi R8' }

# Print the length of your set.

print(showroom)

# Pick one of the items in your show room and add it to the set again.

showroom.add('Toyota Supra')

# Print your showroom. Notice how there's still only one instance of that model in there.

print(showroom)

# Using update(), add two more car models to your showroom with another set.

another_showroom = set()
another_showroom = { 'Ford Focus RS', 'Mazda Speed3'}
showroom.update(another_showroom)
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.

showroom.discard('Mazda Speed3')
print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = set()
junkyard = { 'Honda Civic', 'Toyota Camry', 'Mazda 3', 'Toyota Supra', 'Audi R8'}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.

print(showroom.intersection(junkyard))


# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

x = showroom.union(junkyard)
showroom = x


# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

showroom.discard('Mazda 3')