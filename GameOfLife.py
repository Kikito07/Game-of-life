import matplotlib.pyplot as plt
import numpy as np

def addcell(array, x, y):
    array[x, y] = 1
    return


def gameoflife(array):
    arrayNew = np.zeros((10, 10))
    for row in range(array[0, :].size):
        for column in range(array[0, :].size):

            if (array[row, column] == 1):
                total = 0
                for rangRow in range(-1, 2):
                    for rangeColumn in range(-1, 2):
                        if (row + rangRow < (array[0, :].size) and row + rangRow >= 0 and
                                column + rangeColumn < (array[0, :].size) and column + rangeColumn >= 0):
                            total = total + array[row + rangRow, column + rangeColumn]
                if total == 4 or total == 3:
                    arrayNew[row, column] = 1

            else:
                total = 0
                for rangRow in range(-1, 2):
                    for rangeColumn in range(-1, 2):
                        if (row + rangRow < (array[0, :].size) and row + rangRow >= 0 and
                                column + rangeColumn < (array[0, :].size) and column + rangeColumn >= 0):
                            total = total + array[row + rangRow, column + rangeColumn]
                if total == 3:
                    arrayNew[row, column] = 1

    return arrayNew

arrayTest = np.zeros((10, 10))
fram=0

addcell(arrayTest, 3, 5)
addcell(arrayTest, 3, 6)
addcell(arrayTest, 3, 7)
addcell(arrayTest, 4, 4)
addcell(arrayTest, 4, 5)
addcell(arrayTest, 4, 6)

fig, ax = plt.subplots()

while fram<50:
    ax.imshow(arrayTest)
    arrayTest=gameoflife(arrayTest)
    ax.set_title("frame {}".format(fram))
    fram=fram+1
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)
