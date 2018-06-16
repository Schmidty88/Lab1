# lab 1.3
# combo toolkit allows easy coding combinations, found after spending hours trying to
# hard code if statements, this is way easier

from itertools import combinations

# itertools uses the combinations to iterate through and find matches ([index], choose 3)

input = list(combinations([4,5,8,2,-4,9,-8,1,3],3))

# variables, and index for parsing through the input_int

triplets = []

ind = 0

length = len(input)

# for loop iterates through index, sum(input_int[ind]) == 0 stops when it finds a
# three integer combination with a total sum of zero

for i in range(length):
    if sum(input[ind]) == 0:
        triplets.append(input[ind])
    ind += 1


print("The following triplets are: ", triplets)