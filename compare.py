import csv
import numpy as np 
from PIL import Image
import math
import glob

# list down path in directories
txtfiles = []
for file in glob.glob('*.jpg'):
	print(file)


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


# Save in CSV file
# with open('data.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(all_pixels1)

# csvFile.close()

# with open('data2.csv', 'w') as csvFile2:
#     writer2 = csv.writer(csvFile2)
#     writer2.writerows(all_pixels2)

# csvFile2.close()

with open('result.csv', 'w') as csvFile3:
    writer3 = csv.writer(csvFile3)
    writer3.writerow(list2)

csvFile3.close()


# im = Image.open('2.jpg')

# pix = im.load()

# width, height = im.size

# csvData = list(im.getdata())

# import PIL
# from PIL import Image
# FILENAME='1.jpg' #image can be in gif jpeg or png format 
# im=Image.open(FILENAME).convert('RGB')
# pix=im.load()
# w=im.size[0]
# h=im.size[1]
# for i in range(w):
#   for j in range(h):
#     print(pix[i,j])
#     
#     
#     


