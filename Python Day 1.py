print("Welcome to Python! Ruby")


# 1. Variables

name = "Ruban"
age = 25
height = 5.9
salary = 50000
is_employed = True
print(name, age, height, salary, is_employed)


# 2. Data Types

a=10          # Integer
b=5.5         # Float
c="Ruby"     # String
d=True        # Boolean

print(type(a), type(b), type(c), type(d))


# 3. Type Casting

x="100"
y=float(x)
print(y, type(y))

z=int(10.5)
print(z, type(z))

num = 50
s=str(50)
print(s, type(s))

n=int("200")
print(50 + n)

# 4. Input & Output

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("Hello", name)
print("You are", age, "years old and", height, "m tall.")


# Normal way
print("Your name is", name, "and your age is", age)

# f-string (modern way)
print(f"Your name is {name} and your age is {age}")


# 5. Eg ;


#1. Store your name, age, and salary in variables and print them.

name = "RubanKumar"
age = 25
salary = 50000

print(f"Name: {name}, Age: {age}, Salary: {salary}")


#2. Convert an integer num = 50 into float and string.

num = 50
num_float = float(num)
num_str = str(num)
print(num_float, type(num_float))
print(num_str, type(num_str))
print(num + int(num_str))


#3. Ask user:
#    name
#    2 numbers → add them and print result.

name = input("Enter your name: ")
num1 = int(input("Enter first number: "))   
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
print(f"Hello {name}, the sum of {num1} and {num2} is {sum_result}.")   

#4. Print the following using f-string:
#    Your name is __ and your age is __.  
print(f"Your name is {name} and your age is {age}.")
#    The sum of __ and __ is __.
print(f"The sum of {num1} and {num2} is {sum_result}.")
#    The multiplication of __ and __ is __.
mul_result = num1 * num2
print(f"The multiplication of {num1} and {num2} is {mul_result}.")
#    The division of __ and __ is __.

div_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
print(f"The division of {num1} and {num2} is {div_result}.")    
#    The subtraction of __ and __ is __.
sub_result = num1 - num2        
print(f"The subtraction of {num1} and {num2} is {sub_result}.")
#    The modulus of __ and __ is __.
mod_result = num1 % num2 if num2 != 0 else "undefined (modulus by zero)"
print(f"The modulus of {num1} and {num2} is {mod_result}.") 
#    The floor division of __ and __ is __.
floor_div_result = num1 // num2 if num2 != 0 else "undefined (floor division by zero)"
print(f"The floor division of {num1} and {num2} is {floor_div_result}.")        

#    The exponentiation of __ and __ is __.
exp_result = num1 ** num2                       

print(f"The exponentiation of {num1} and {num2} is {exp_result}.")
#    The average of __ and __ is __.
avg_result = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is {avg_result}.") 
#    The maximum of __ and __ is __.
max_result = max(num1, num2)            

print(f"The maximum of {num1} and {num2} is {max_result}.")
#    The minimum of __ and __ is __.            

min_result = min(num1, num2)
print(f"The minimum of {num1} and {num2} is {min_result}.")     
