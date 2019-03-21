# Non moving creatures
# Taken from http://pi.math.cornell.edu/~lipa/mec/lesson6.html
square = [
    [1,1],
    [1,1]
]

boat = [
    [1,1,0],
    [1,0,1],
    [0,1,0]
]

loaf = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,1,0],
    [0,1,0,0]
]

ship = [
    [1,1,0],
    [1,0,1],
    [0,1,1]
]

# Dynamic Creatures
glider = [
    [1,1,1],
    [1,0,0],
    [0,1,0]
]

space_ship = [
    [0,1,0,0,1],
    [1,0,0,0,0],
    [1,0,0,0,1],
    [1,1,1,1,0]
]

f_pentomino = [
    [0,1,1],
    [1,1,0],
    [0,1,0]
]

# Replicator taken from http://www.conwaylife.com/wiki/HighLife
replicator = [
  [0,0,1,1,1],
  [0,1,0,0,1],
  [1,0,0,0,1],
  [1,0,0,1,0],
  [1,1,1,0,0]
]

stick = [
    [1,1,1]
]

# Dictionary of creatures to be imported
creatures = {
    'square': square,
    'boat' : boat,
    'loaf': loaf,
    'ship': ship,
    'glider': glider,
    'space_ship' : space_ship,
    'F-pentomino' : f_pentomino,
    'replicator' : replicator,
    'stick' : stick
}
