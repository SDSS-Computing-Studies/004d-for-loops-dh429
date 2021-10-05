#! python

"""
We can cycle through all of the members of a tuple using a for... loop.
The for loop uses an indexing variable that stores the current tuple
member and can be accessed within the block

if you want to break out of the for loop, you can use break at any point
in the block.  All future iterations are skipped and the loop exits at
the current point (see example2a.py)

if you want to break out of the loop, but continue on to further iterations,
you can use continue. (see example2b.py)
"""

players = ("Guile", "Cammy", "Ryu", "Ken", "Chun-Li")

for i in players:
    """ 
    here, i is the indexing variable.  
    All the tuple members will take turns being i
    """
    print("===")
    print( i + " is going to the mall")
    print("---")
    print("\n")