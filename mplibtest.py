import matplotlib.pyplot as pyplot
import numpy as np

# Generate some data...
arrayTest = np.zeros((10, 10))

def addcell(array, x, y):
    array[x, y] = 1
    return

addcell(arrayTest, 3, 4)
addcell(arrayTest, 5, 6)
addcell(arrayTest, 2, 4)
addcell(arrayTest, 1, 4)
addcell(arrayTest, 9, 2)
addcell(arrayTest, 7, 4)
addcell(arrayTest, 9, 4)

pyplot.imshow(arrayTest)
pyplot.show()

print(arrayTest)
