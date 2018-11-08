import csv
import numpy as np 
from PIL import Image
import math
import glob


# 1st image load
i = Image.open('2011.03_2011.04.jpg')
pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size

# 2nd image load
i2 = Image.open('2011.05_2012.04.jpg')
pixels2 = i2.load() # this is not a list, nor is it list()'able
width2, height2 = i2.size


# Extract RGB values for each pixel
all_pixels1 = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels1.append(cpixel)

all_pixels2 = []
for x in range(width2):
    for y in range(height2):
        cpixel2 = pixels2[x, y]
        all_pixels2.append(cpixel2)

# convert list to numpy array 
array1 = np.array(all_pixels1)
array2 = np.array(all_pixels2)

# Subtract value for both array and store in variable
result = np.subtract(array1, array2)

#calculate using formula
list2 = []
def calculate(numberOfArray):
	for element in numberOfArray:
		data = element * element
		squared_root = math.sqrt(sum(data))
		list2.append(squared_root)

finalResult = calculate(result)

#save to csv
with open('result.csv', 'w') as csvFile3:
    writer3 = csv.writer(csvFile3)
    writer3.writerow(list2)

csvFile3.close()
