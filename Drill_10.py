
# 1. Assign an integer to a variable
myInt =int(5) 

# 2. Assign a string to a variable
myString = 'Hello world of python'

# 3. Assign a float to a variable
myFloat = float(15.5)

# 4. Use the print function and .format() notation to print out the varalbe you assigned
print ('The integer is {}, the string is {}, the float is {}'.format(myInt, myString, myFloat))

# 5. Use each of these operators +, -, *, /, +=, =, %

x = 12
y = 24
z = 4
print (x - z)
print (x + y)
print (y / z)
print (z * x)
print (x % 5)

while x < 16:
    print x
    x += 1

# 6. Use logical operators: and, or, not

runnerOne = float(9.5)
runnerTwo = float(12.0)
slowestRunner = float(13.0)
me = float(14.0)
if runnerOne > 0 and runnerOne< 10 :
    print "The frist runner is FAST!"

if runnerTwo > 10.5 or runnerTwo < 14:
    print "The second runner is avrage"

if not slowestRunner > 14.0:
    print 'All runners are faster than me!'

# 7. Use of conditional statements: if, elif, else

if me < 10.0:
    print "I am the fastest runner!"
elif me <= 12.0 and me >= 10.0:
    print "I run at an average competitive speed"
else:
    print "I am too slow and I need to train more."

# 8. Use of a while loop
a = 24
while a < 30:
    print x
    a += 2

# 9. Use of for loop
for b in range (10,15):
    print b

# 10. Create a list and iterate through that list using a for loop to print each item out on a new line 
newCars = ['jeep', 'accord', 'civic', 'sentra', 'altima', 'focus', 'lancer']
for car in newCars:
    print car

# 11. Create a tuple and iterate through it using a for loop to print each item out on a new line
newPlayers = ('jack', 'james', 'anna', 'ray', 'sara', 'trish')

for player in newPlayers:
    print player

# 12. define a function that returns a string variable
def dinner():
    return "Dinner is ready at 6:30 P.M. Don't be Late!"

# 13. call the function you defined above and print the result to the shell.
print dinner() 






