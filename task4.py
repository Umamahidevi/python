#Mini Project 1: Employee Management System
#Concepts: Dictionary, List, Functions

employees = []

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    emp = {"name": name, "age": age, "role": role, "salary": salary}
    employees.append(emp)
    print("Employee added!\n")

def display_employees():
    print("\nEmployee List:")
    for emp in employees:
        print(emp)

def update_employee():
    name = input("Enter employee name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = float(input("Enter new salary: "))
            print("Updated successfully!")
            return
    print("Employee not found")

def delete_employee():
    name = input("Enter employee name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("Deleted successfully!")
            return
    print("Employee not found")

# Main loop
while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

#Mini Project 2: Student Report Card
#Concepts: Dictionary, Functions, Formatting
# Function to calculate grade

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
# Function to generate report card
def report_card():
    print("\n===== Student Report Card =====")
    
    name = input("Enter student name: ")
    
    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))
    
    total = m1 + m2 + m3
    average = total / 3
    grade = calculate_grade(average)
    
    print("\n Report Card")
    print("-" * 30)
    print(f"Name     : {name}")
    print(f"Subject1 : {m1}")
    print(f"Subject2 : {m2}")
    print(f"Subject3 : {m3}")
    print("-" * 30)
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")
    print("-" * 30)
#  Main Loop
while True:
    print("\n1. Generate Report Card")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        report_card()
    elif choice == '2':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

#Mini Project 3: Shopping Cart System
#Concepts: List, Dictionary, Loop

cart = []

def add_item():
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    cart.append({"name": name, "price": price, "qty": qty})
    print("Item added!\n")

def remove_item():
    name = input("Enter product to remove: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            print("Item removed!")
            return
    print("Item not found")

def show_cart():
    total = 0
    print("\nCart Items:")
    for item in cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(f"{item['name']} - {item['qty']} x {item['price']} = {subtotal}")
    
    print("Total Bill:", total)
 # Main Loop
while True: 
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Show Cart")
    print("4. Exit")            
    choice = input("Enter choice: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        show_cart()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

# Mini Project 4: Login & User Validation 
# Concepts: Dictionary, Condition

users = {
    "admin": "1234",
    "uma": "abcde",
    "sai": "sai123"
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
    else:
        print("Invalid Credentials")
# Main Loop
while True:
    print("\n1. Login")
    print("2. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        login()
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

# Mini Project 5: Unique Visitor Counter
# Concepts: Set

visitors = set()

while True:
    name = input("Enter visitor name (or type 'exit'): ")
    
    if name.lower() == 'exit':
        break
    
    visitors.add(name)
    print(" Visitor added!\n")

print("\n--- Unique Visitors ---")
for v in visitors:
    print(v)

print(f"\nTotal Unique Visitors: {len(visitors)}")


# Mini Project 6: String Formatter Tool Concepts: String Formatting 

# Taking input from user
name = input("Enter your name: ")
product = input("Enter product name: ")

# Formatted sentence
sentence = f"Hello {name}, thank you for purchasing {product}!"
print("\nFormatted Sentence:")
print(sentence)

# Padding outputs
print("\nPadded Outputs:")

# Left aligned
print("\nLeft Align:")
print(sentence.ljust(60, '-'))

# Right aligned
print("\nRight Align:")
print(sentence.rjust(60, '-'))

# Center aligned
print("\nCenter Align:")
print(sentence.center(60, '-'))

 #Mini Project 7: Bank Account System
#Concepts: Functions, Dictionary
# Bank Account System

account = {}

def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    account["name"] = name
    account["balance"] = balance
    print("Account created successfully!")

def deposit():
    amount = float(input("Enter deposit amount: "))
    account["balance"] += amount
    print("Amount deposited!")

def withdraw():
    amount = float(input("Enter withdraw amount: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

def check_balance():
    print(f"Current Balance: {account['balance']}")

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Check Balance 5.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

# Mini Project 8: Voting System
# Concepts: Dictionary, Loop    
# Voting System

votes = {
    "Uma": 0,
    "Sai": 0,
    "Kavya": 0
}

while True:
    print("\nCandidates:", list(votes.keys()))
    choice = input("Enter candidate name to vote (or 'exit'): ")

    if choice.lower() == 'exit':
        break
    elif choice in votes:
        votes[choice] += 1
        print("Vote added!")
    else:
        print("Invalid candidate!")

# Display results
print("\nVoting Results:")
for candidate, count in votes.items():
    print(candidate, ":", count)

# Winner
winner = max(votes, key=votes.get)
print("Winner is:", winner)

#Mini Project 9: Course Enrollment System
#Concepts: List + Dictionary
# Course Enrollment System

students = {}

def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(',')
    students[name] = courses
    print("Student added!")

def update_courses():
    name = input("Enter student name: ")
    if name in students:
        courses = input("Enter new courses: ").split(',')
        students[name] = courses
        print("Courses updated!")
    else:
        print("Student not found!")

def display_students():
    for name, courses in students.items():
        print(f"{name}: {', '.join(courses)}")

while True:
    print("\n1.Add 2.Update 3.Display 4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_courses()
    elif choice == '3':
        display_students()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
# Mini Project 10: Number Utility Tool
# Concepts: Functions, Formatting
# Number Utility Tool

num = int(input("Enter a number: "))

# Conversions
print("\nConversions:")
print("Binary:", bin(num))
print("Octal :", oct(num))
print("Hex   :", hex(num))

# Formatting
print("\nFormatted Number:")
print(f"With commas: {num:,}")

# Scientific notation
print("Scientific notation: {:.2e}".format(num))
