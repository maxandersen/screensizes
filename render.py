import matplotlib.pyplot as plt
from numpy.random import rand
from matplotlib.patches import Rectangle
import csv
import time
from collections import namedtuple

cmap = plt.cm.hot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

ax.set_xlim(0, 10000)
ax.set_ylim(0, 3000)

#plt.ion()
#plt.show()


data = []
Point = namedtuple('Point', 'w h amount')
with open('sizes.csv', 'rb') as csvfile:
    sizereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sizereader:
        dimension = row[0].split('x')
        amount = float("0." + row[1]) # fix this to be right mapping
        w = int(dimension[0])
        h = int(dimension[1])
        data.append(Point(w,h,amount))


for p in data:
    #print h,w
    ax.add_artist(Rectangle(xy=(0, 0),
                        color=cmap(50),        # I did c**2 to get nice colors from your numbers
                        width=p.w, height=p.h, fill=False, alpha=0.01, lw=1))      # Gives a square of area h*h
        
        #plt.draw()
        #time.sleep(0.10)
        
#plt.draw()

plt.show()
