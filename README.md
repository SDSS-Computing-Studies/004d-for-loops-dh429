## SDSS Computing Studies Python Assignment
### Assignment #004b For Loops (Total Marks 15)

Objectives:
* new variable type: tuple
* use for loop to iterate through members of a tuple
* use for loop to iterate over a sequence of integers
* continue can be used to skip over and keep iterating
* exit from a for loop using break

For loops are useful when you want to repeat a section of code a set number of
times.  The number of times can be determined by a fixed number or by a collection
of data.

For loops are one of the most useful structures in programming, as it can be used
to cycle through large amounts of data, processing each entry until you get to the
end.

We can also use code that allows us to treat for loops like a while loop, and
vice versa!

### Using a TUPLE
We are going to mention a new variable type here: the TUPLE
example1.py
A tuple is a set of data that is defined as having multiple values or members.
It is defined just like a regular variable, but uses brackets to define the 
beginning and end of the tuple: 

Another way to use a tuple is to cycle through all of the members of a tuple 
using a *for* loop
example2.py

### Using a range
You can also cycle through a *for* loop using a range of numbers
example3.py
The indexing variable starts with an initial value, and continues until the
indexing value reaches the ending value.


### Note: A for loop can't be empty
If for some reason you need to execute no commands inside a for loop,
you need to use the command "pass"

example:

for i in range(3,5):
    pass
print("All done!")

### XX Tasks

##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points) 

###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of a single if with multiple
logical operators
(2 points)

##### Task 3
Given a typle that contains a series of numbers, list all the ones that are
divisible by 5
(2 points)


###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

##### Problem 2
Calculate the factorial of a number. 
A factorial is defined as:
5! = 1 * 2 * 3 * 4 * 5
5! = 120

3! = 1 * 2 * 3
3! = 6

##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

