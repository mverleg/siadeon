
"""
	What if gravitational and inertial mass would be different?
	http://worldbuilding.stackexchange.com/questions/3396/different-gravitational-and-inertial-mass
"""

from numpy import empty, sqrt
from matplotlib.pyplot import subplots, show


mass = [
	# gravitational; inertial
	(1., 1., 'normal'),
	(5., 1., 'new iron'),
	(1., 5., 'new copper'),
]

g = 0.1
fig, ax = subplots()

for grav, inert, label in mass:
	x, y = 0, 0
	px, py = sqrt(2 / inert), sqrt(2 / inert)
	Xs, Ys = [x], [y]
	for t in range(1000):
		Fg = - g * grav
		a = Fg / inert
		py += a
		x += px
		y += py
		Xs.append(x)
		Ys.append(y)
		if y < 0:
			break
	ax.plot(Xs, Ys, label = label)
	ax.set_yticks([])

ax.legend()

if __name__ == '__main__':
	show()


