
print("---------------Q (4) -------")
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))



print("---------------Q (8) -------")
x = 15
if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")




print("---------------Q (10) -------")
total = 0
for n in [1,2,3,4,5]:
    total += n
print(total)



print("---------------Q (11) -------")

x = 10
x += 5
x *= 2
print(x)






print("---------------Q (12) -------")
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)



print("---------------Q (13) -------")
a = True
b = False
print(a and not b)




print("---------------Q (18) -------")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")





print("---------------Q (22) -------")
for i in range(1, 6, 2):
    print(i, end=" ")


print("(23)--------What does range(5) produce? [0, 1, 2, 3, 4]---------------")



print("---------------1. Variable Swap-------")

# 1. Variable Swap
# Write a Python program to swap two variables a = 10 and b = 20 without using a third variable. Print both values before and after swapping.

a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)




print("---------------# #2. FizzBuzz-------")
# #2. FizzBuzz
# Write a program that prints numbers from 1 to 30. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



print("---------------# #3. Grade Calculator-------")
# #3. Grade Calculator
# Write a function get_grade(marks) that returns: "A" (≥80), "B" (≥65), "C" (≥50), "F" (below 50). Call it with at least 3 different values.
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(get_grade(92))
print(get_grade(70))
print(get_grade(55))
print(get_grade(40))




print("---------------# 4. Even Numbers Sum-------")

# 4. Even Numbers Sum
# Using a for loop and range(), calculate and print the sum of all even numbers from 1 to 100.


total = 0

for i in range(2, 101, 2):
    total += i

print("Sum of even numbers:", total)



print("---------------# 5. Factorial Function-------")

# 5. Factorial Function
# Write a function factorial(n) that returns the factorial using a while loop. Test it with n=5 and n=0.

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(5))
print(factorial(0))

