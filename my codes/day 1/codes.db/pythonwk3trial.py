#basic if statement
temperature = 30
if temperature > 25:
    print("its a hot day!")
elif temperature > 15:
    print('its a warm day!')
else:
    print('its a cold day!')

#example 2 grading system
#taking input from user
grade = int(input('Enter your garde:'))
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')





 #control flow is the order in which a code is to be executed.
 # we have for and while loops
 # conditionals are if, else, elif
 #concatenatwe is linking 

bill = 2500

discount1 = 100
if bill > 2000:
    print('bill is greater than 2000')
    final_bill = bill - discount1 
print('final bill:' + str(final_bill))

#functions allows one to write a reusable block of code
#function is a block of code used to perform a specific task

def myFunction(x, y):
    sum = a + b
    print('sum')

myFunction(2 , 5)

a = 2
b = 5
#a, b are variables containing those numbers
