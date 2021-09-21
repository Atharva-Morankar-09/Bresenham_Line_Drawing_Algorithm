
#BRESENHAM LINE DRAWING ALGORITHM

import matplotlib.pyplot as plt
print("STARTING POINTS")
x1, y1 = map(int, input().split())
print("ENDING POINTS")
x2, y2 = map(int, input().split())

X_coordinates = [x1]
Y_coordinates = [y1]
dx = x2-x1
dy = y2-y1
Pk = 2*dy-dx
print(" i     |   Pk   |   Pk+1  |   Xk+1   |   Yk+1  |   Plot    ")
print("       |        |         |     %d   |   %d    |   (%d,%d)    " % (x1, y1, x1, y1))
for i in range(dx):
    if Pk < 0:
        Pkn = Pk+(2*dy)
        x1+= 1
        print(" %d     |   %d   |   %d    |   %d     |    %d   | (%d,%d)  " % (i, Pk, Pkn, x1, y1, x1, y1))
        Pk = Pkn

    else:
        Pkn = Pk + (2*dy - 2*dx)
        x1+= 1
        y1+= 1
        print(" %d     |   %d   |   %d    |   %d     |    %d   | (%d,%d)  " % (i, Pk, Pkn, x1, y1, x1, y1))
        Pk = Pkn
    X_coordinates.append(x1)
    Y_coordinates.append(y1)
    X = (X_coordinates[0], X_coordinates[-1])
    Y = (Y_coordinates[0], Y_coordinates[-1])
    #plt.grid(True)

plt.title("BRESENHAM LINE")
plt.ylabel("Y-AXIS")
plt.xlabel("X-AXIS")
plt.plot(X, Y, 'lightblue', linewidth="1")
plt.scatter(X_coordinates, Y_coordinates, color='BLACK', s=25)
plt.show()


