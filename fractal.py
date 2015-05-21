import matplotlib
matplotlib.use('Agg')
from collections import deque
import matplotlib.pyplot as plt

def count(dq, item):
  return sum(elem == item for elem in dq)

LEN = 2
WID = 1
GRID = 100
NUMIT = 50000

plt.axis([-GRID, GRID, -GRID, GRID])
root = plt.Line2D((0,0), (0, LEN), lw=WID)
plt.gca().add_line(root)
endpoints = deque([(0, 0, 'v'), (0, LEN, 'v')])

for i in range(0, NUMIT-1):
  p = endpoints.popleft()
  if p[2] == 'v': #end of vertical line
    a = (p[0]-LEN/2, p[1], 'h')
    b = (p[0]+LEN/2, p[1], 'h')
  if p[2] == 'h': #end of horizontal line
    a = (p[0], p[1]-LEN/2, 'v')
    b = (p[0], p[1]+LEN/2, 'v')
  branch = plt.Line2D((a[0], b[0]), (a[1], b[1]), lw=WID)
  plt.gca().add_line(branch)
  #print "Plotting hline from", a[:2], "to", b[:2]
  if count(endpoints, a) == 1:
    endpoints.remove(a)
  else:
    endpoints.append(a)
  if count(endpoints, b) == 1:
    endpoints.remove(b)
  else:
    endpoints.append(b)

plt.savefig("fractal"+str(NUMIT)+".png")
plt.show()
