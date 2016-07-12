# Instructions
# Create an empty set named showroom. Add four of your favorite car model names to the set.
cars = {'Nissan Sentra', 'Ford Escape', 'Chevy Camaro', 'Honda Civic'}
# Print the length of your set.
print(len(cars))
# Pick one of the items in your show room and add it to the set again.
cars.update({'Nissan Sentra'})
# Print your showroom. Notice how there's still only one instance of that model in there.
print(cars)
# Using update(), add two more car models to your showroom with another set.
cars.update({'Nissan Altima', 'Toyota Camry'})
print(cars)
# You've sold one of your cars. Remove it from the set with the discard() method.
cars.discard('Chevy Camaro')
print(cars)
# Acquiring more cars: Now create another set of cars in a variable junkyard. Someone who
# owns a junkyard full of old cars has approached you about buying the entire inventory. In
# the new set, add some different cars, but also a few that are the same as in the showroom set.
junkyard_cars = {'Nissan Altima', 'Ford Escape', 'Subaru Outback', 'Nissan Xterra', 'Jeep Wrangler'}
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
multiples = cars.intersection(junkyard_cars)
print(multiples)
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard
# into your showroom.
merged_cars = cars | junkyard_cars #same as cars.union(junkyard_cars)
print(merged_cars)
# Use the discard() method to remove any cars that you acquired from the junkyard that you
# don't want in your showroom.
merged_cars.discard('Subaru Outback')
print(merged_cars)
