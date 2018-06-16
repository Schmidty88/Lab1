import numpy as np
# this is setting up an array of 15 with integers between  0 and 20 only
x = np.random.randint(0, 20, 15)

print("List:" + str(x))

count = np.bincount(x)

largest = 0
setter = 0
counter = 0

while counter < len(count):
    if count[counter] >= largest:
        largest = count[counter]
        setter = count[counter]
    counter += 1

print("Largest Frequency " + str(x[setter]))