
"""
	- is there a realistic way to make days longer than nights?
	- 2 or 3 moons in eliptical orbits
	- phase locked planets are kind of cliche
	---
	- new idea: 8 shape orbit around two stars
	-
"""

from numpy import array, arange, zeros, copy, linspace
from numpy.linalg import norm
from numpy.random import randn
from matplotlib.pyplot import subplots, show


class CelestialBody():

	def __init__(self, name = 'Blob', mass = 1., radius = 1, x = None, p = None):
		self.name = name
		self.mass = mass
		self.radius = radius
		x = randn(3) if x is None else copy(x)
		p = randn(3) if x is None else copy(p)
		self.xhist = []
		self.jumpto(x, p)

	def jumpto(self, x, p = None):
		self.x = x
		if p is not None:
			self.p = p
		self.log()
		return self

	def log(self):
		self.xhist.append(copy(self.x))

	def step(self, F, dt = 1.):
		""" dp = m*dv = m*a*t = F*t """
		self.p += F * dt
		self.x += self.p
		self.log()


G = 10.; dt = 0.1; N = 200
bodies = [
	CelestialBody(name = 'Alpha', mass = 20, x = array([+10., 0., 0.]), p = array([0., -5., 0.])),
	CelestialBody(name = 'Beta',  mass = 10, x = array([-10., 0., 0.]), p = array([0., +5., 0.])),
	#CelestialBody(name = 'Earth', mass = 1,  x = array([0, 0, 0])),
]

for t in linspace(0, N * dt, N):
	#print 't = %.2f' % t
	for body in bodies:
		""" calculate gravitational force """
		body.F = zeros(3)
		for other in bodies:
			if other is not body:
				r = other.x - body.x
				body.F += G * other.mass * body.mass / norm(r)**3 * r
	for body in bodies:
		body.step(body.F, dt)


fig, ax = subplots()
for body in bodies:
	x, y = array(body.xhist)[:, 0:2].T
	ax.plot(x, y, 'x', label = body.name)
ax.legend()
print len(bodies[0].xhist)
#ax.set_xlim([-15, 15])
#ax.set_ylim([-15, 15])

if __name__ == '__main__':
	show()


