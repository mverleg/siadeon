
'''
	# hexagonal game grid
	# using axial coordinates (at 60 deg)
	# (0, 0) at the center
	# grid should be hexagon-periodic
	# http://www.redblobgames.com/grids/hexagons/
'''

# divisable into clusters that can be changed (with restart?) of unequal size,
#	perhaps the most efficient way is rhombus clusters as boundaries are clear
#	(simply a < x < a + L) with easy matching to neighbours
# for the world, it doesn't matter what the internal representation is, because
#	anything flat periodic can be represented on any reriodic lattice (e.g. rhombic
#	internal could be displayed as a square or hexagon on world view map

''' tests '''
def test_cell_count(L):
	assert L <= 200, 'for performance reasons, use test for L <= 200'
	''' count extra cells in each new layer '''
	total = 0
	for q in range(-L, L + 1):
		for r in range(-L, L + 1):
			if abs(q + r) <= L:
				total += 1
	return total

''' functions '''
def cell_count(L):
	return 3 * (L**2 + L) + 1

'''
	names adopted from article (q const for |, r const for \)
	the third coordinate s = - q - r is redundant
	note the grid is not filled, e.g. (1, L) does not exist
	points exist if abs(q + r) < L
'''
L = 3
print 'size %d; %d cells' % (L, cell_count(L))
Q = range(-L, +L + 1)
R = range(-L, +L + 1)
print Q

# should I store both an array mapping position to object and the position for each object? which is primary and which is derived? can there be multiple objects on a position?

if __name__ == '__main__':
	for L in range(201):
		print L, cell_count(L), test_cell_count(L), cell_count(L) == test_cell_count(L)

