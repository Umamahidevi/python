#Task 1: User Info Manager (Functions + Dictionary)

def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

# Store users
users = []
users.append(create_user("Uma", 25, "developer"))
users.append(create_user("Sai", 30, "manager"))
users.append(create_user("Kavya", 22, "designer"))

# Print all users
print("User List:")
for user in users:
    print(user)

# Task 2: Dynamic Calculator (*args)

def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

# Example
result = calculate_total(10, 20, 30, 40)
print("Total:", result[0])
print("Average:", result[1])

#Task 3: Keyword Config System (**kwargs)

def system_config(**settings):
    print("System Configuration:")
    for key, value in settings.items():
        print(f"{key}: {value}")

# Example
system_config(mode="debug", version="3.0", user="Uma")

#Task 4: Factorial Service (Recursion)

def factorial(n):
    if n < 0:
        return "Error: Negative numbers not allowed"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example
print("Factorial:", factorial(3))

#Task 5: Memory Optimization (Generator)

def square_generator(n):
    for i in range(n):
        yield i * i

# Normal list
square_list = [i * i for i in range(5)]

# Generator
square_gen = square_generator(5)

print("List:", square_list)
print("Generator values:", list(square_gen))

print("Type of list:", type(square_list))
print("Type of generator:", type(square_generator(5)))

#Task 6: Exception Handling Module

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")

# Task 7: File Handling
# Writing to file

file = open("team_data.txt", "w")

for user in users:
    file.write(str(user) + "\n")

print("File closed after writing?", file.closed)
file.close()
print("File closed now?", file.closed)

# Reading file
file = open("team_data.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)

file.close()
print("File closed after reading?", file.closed)