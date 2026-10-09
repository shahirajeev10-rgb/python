# QUESTION:
# A small pond starts with a single water lily pad covering 1 square meter.
# Each day, the area covered by lily pads doubles (1, 2, 4, 8, ...).
# The total surface area of the pond is 500 square meters.
#
# How many days will it take for the lily pads to cover the ENTIRE pond?
#
# Write a while loop to calculate and print the answer in the format:
# days = <number>
# ==============================================================================

# Write your code below:



pads = 1
days = 0
while pads <=500:
    pads = pads * 2
    days = days + 1

print(f"days = {days}")    


