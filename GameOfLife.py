import numpy as np

arrayTest = np.zeros((10, 10))



def addcell(array, x, y):
    array[x, y] = 1
    return


def gameoflife(array):
    for row in range(array.size):
        for column in range(array.size):

            if (array[row, column] == 1):
                total = 0
                for rangRow in range(-1, 2):
                    for rangeColumn in range(-1, 2):
                        if (row + rangRow < (array.size -1) and row + rangRow >= 0 and
                                column + rangeColumn < (array.size -1) and column + rangeColumn >= 0):
                            total = total + array[row + rangRow, column + rangeColumn]

                if total <= 2:
                    array[row, column] = 0

                elif total >= 4:
                    array[row, column] = 0

            else:
                total = 0
                for rangRow in range(-1, 2):
                    for rangeColumn in range(-1, 2):
                        if (row + rangRow < (array.size -1) and row + rangRow >= 0 and
                                column + rangeColumn < (array.size -1) and column + rangeColumn >= 0):
                            total = total + array[row + rangRow, column + rangeColumn]

                if total == 3:
                    array[row, column] = 1

    return array


addcell(arrayTest, 3, 4)
addcell(arrayTest, 5, 6)
addcell(arrayTest, 2, 4)
addcell(arrayTest, 1, 4)
addcell(arrayTest, 9, 2)
addcell(arrayTest, 7, 4)
addcell(arrayTest, 9, 4)

print(arrayTest)

gameoflife(arrayTest)

print(arrayTest)
