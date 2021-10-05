#! python

"""

if you want to break out of the loop, but continue on to further iterations,
you can use continue. (see example2b.py)
"""

players = ("Guile", "Cammy", "Ryu", "Ken", "Chun-Li")

# here, i is the indexing variable.  All the tuple members will take turns being i
for i in players:
    # this checks to see if the current tuple member is Ryu and then
    # breaks out of the current iteration, but continues on to the rest of
    # the loop
    if i == "Ryu":
        continue
    print("===")
    print( i + " is going to the mall")
    print("---")
else:
    # a For loop can optionally end with an else:
    # the else indicates a block of code to be run if the loop has no more members
    print("That is the end!")