# ==============================================================================
# QUESTION:
# A biology experiment starts with a single bacterium in a Petri dish.
# Every hour, the number of bacteria doubles (1, 2, 4, 8, ...).
#
# How many hours will it take for the total population to exceed 1,000,000 bacteria?
#
# Write a while loop to calculate and print the answer in the format:
# hours = <number>
# ==============================================================================

# Write your code below:

hours = 0
bacteria = 1

while bacteria <= 1000000:
 hours = hours + 1
 bacteria = bacteria * 2
 

print(f"hours = {hours}")