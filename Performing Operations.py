# Performing Operations -

# Operators and their Operations

# + -> Addition
# - -> Subtractions
# / -> Division
# % -> Modulus
# // -> Floor division
# ** -> Exponent

# ********Arithmetic operations**********

a = 8
b = 2

print('Addition:\t', a, '+', b, '=', a + b)
print('Subtractions:\t', a, '-', b, '=', a - b)
print('Division:\t', a, '/', b, '=', a / b)
print('Modulus:\t', a, '%', b, '=', a % b)
print('Floor Division:\t', a, '//', b, '=', a // b)
print('Exponent:\t', a, '**', b, '=', a ** b, '\n')

# ************Assigning Values*********
print("The below is to assigning the values in python ->\n")

print('Assign Values:\t\t\t\t', 'a = ', a, '\t b= ', b)
a += b
print('Add & Assign:\t\t\t\t', 'a=', a, " ", '8+=2')
a -= b
print('Subtract & Assign:\t\t\t', 'a=', a, " ", '10-=2')
a *= b
print('Multiplicate & Assign:\t\t', 'a=', a, " ", '8*=2')
a /= b
print('Divide & Assign:\t\t\t', 'a=', a, " ", '8/=2', '\n')

# ****Comparing values*******

print("The below is to Comparing the values in python ->\n")

nil = 0
num = 0
max = 1
cap = 'A'
low = 'a'

print('Equality: \t', nil, '==', num, nil == num)
print('Equality: \t', cap, '==', low, cap == low, "The ascii values are different")
print('Inequality: \t', nil, '!=', max, nil != max)
print('Greater than: \t', nil, '>', max, nil > num)
print('Less than: \t', nil, '<', max, nil < num)
print('Greater than or Equal to: \t', nil, '>=', num, nil >= num)
print('Less than or Equal to: \t', max, '<=', num, nil <= num, '\n')

print("The below is to Assessing the logic in python ->\n")

# These are
# and -> Logical AND
# or -> logical OR
# not -> Logical NOT

a = True
b = False

print('\nFor AND ->')
print('a and a =', a and a)
print('a and b =', a and b)
print('b and b =', b and b)

print('\nFor OR ->')
print('a or a =', a or a)
print('a or b =', a or b)
print('b or b =', b or b)

print('\nFor NOT ->')
print('not a =', not a)
print('not b =', not b, '\n')

print("The below is to Examining condition in python ->\n")

a = 1
b = 2
print('one' if(a==b) else 'not one')
# Check even odd

# s = int(input("Enter a value: "))
# if(s % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

max = a if (a>b) else b # This is an conditional Expression
print(max)


print("The below is Setting Precedence logic in python ->\n")
"""
We will be doing These things lator on

"""

print("The below is to Casting data types logic in python ->\n")

# The operations can be formed


# int(x) -> x to int
# float(x) -> x to float
# str(x) -> x to string
# chr(x) ->  int x to char
# unichr(x) -> int x to unicode character
# ord(x) -> int x to its integer value
# hex(x) -> int x to hexdecimal
# oct(x) -> int x to octal string

m = input("Enter a number:") # The input takes the input as String format always
n = input("Enter a new number:")

sum = m + n
print('\n Data type sum:', sum, type(sum))
# the below is in int cast


sum = int(m) + int(n)
print(sum, type(sum))

# try above then print

print("The below is to Manipulating bits logic in python ->\n")

