#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

number = input("Enter a number:")
number = int(number)

base = 1

add = "1"

for i in range(number):
    if i == 0:
        add = add + "1"
        add = int(add)
    else:
        base = base + add
        add = str(add)
        add = add + "1"
        add = int(add)

print(f"the sum of the series is {base}")
