import numpy as np

arrayTest = np.zeros((10, 10))
print(arrayTest)


def addcell(array, x, y):
    array[x, y] = 1
    return


def gameoflife(array):
    for i in range(array.size):
        for j in range(array.size):

            if (array[i, j] == 1):
                total = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i + k < (array.size -1) and i + k >= 0 and
                                j + l < (array.size -1) and j + l >= 0):
                            total = total + array[i + k, j + l]

                if total <= 2:
                    array[i, j] = 0

                elif total >= 4:
                    array[i, j] = 0

            else:
                total = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i + k < array.size and i + k >= 0 and
                                j + l < array.size and j + l >= 0):
                            total = total + array[i + k, j + l]

                if total == 3:
                    array[i, j] = 1

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
