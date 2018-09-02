import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def addcell(arrayTest, x, y):
    arrayTest[x, y] = 1
    return


arrayTest=np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])




def animate(data):
    global arrayTest
    arrayNew = np.zeros((arrayTest[0, :].size, arrayTest[0, :].size))

    for row in range(arrayTest[0, :].size):
        for column in range(arrayTest[0, :].size):

            if (arrayTest[row, column] == 1):
                total = 0
                for rangRow in range(-1, 2):
                    for rangeColumn in range(-1, 2):
                        if (row + rangRow < (arrayTest[0, :].size) and row + rangRow >= 0 and
                                column + rangeColumn < (arrayTest[0, :].size) and column + rangeColumn >= 0):
                            total = total + arrayTest[row + rangRow, column + rangeColumn]
                if total == 4 or total == 3:
                    arrayNew[row, column] = 1

            else:
                total = 0
                for rangRow in range(-1, 2):
                    for rangeColumn in range(-1, 2):
                        if (row + rangRow < (arrayTest[0, :].size) and row + rangRow >= 0 and
                                column + rangeColumn < (arrayTest[0, :].size) and column + rangeColumn >= 0):
                            total = total + arrayTest[row + rangRow, column + rangeColumn]
                if total == 3:
                    arrayNew[row, column] = 1

    mat.set_data(arrayNew)
    arrayTest = arrayNew
    return [mat]


fig, ax = plt.subplots()
mat = ax.matshow(arrayTest)
ani = animation.FuncAnimation(fig, animate, interval=1000, save_count=50)


plt.show()
