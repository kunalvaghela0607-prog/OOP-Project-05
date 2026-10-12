def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter numbers only.")


class Employee :
  
    def __init__(job,
                 __Employee_id = None, 
                 Name = None,
                 Age = None,
                 __Salary = None,):
        job.__employee_id = __Employee_id
        job.name = Name
        job.age = Age
        job.__salary = __Salary
    def display(job):
        print(f"ID:{job.__employee_id}")
        print(f"Name:{job.name}")
        print(f"Age:{job.age}")
        print(f"Salary:{job.__salary}")

    def setdata(job):
        job.__employee_id = input("Enter Employee ID: ")
        job.name = input("Enter Name: ")
        job.age = read_int("Enter Age: ")
        job.__salary = read_int("Enter Salary: ")

    def getdata(job):
        print()
        print(f"Employee Create with Name : {job.name},age : {job.age}",
              f"ID:{job.__employee_id}, salary: ₹ {job.__salary},")
        print()

    def __del__(job):

        print()

class Person:
    
    def __init__(job, name=None, age=None):
        job.name = name
        job.age = age
 
    def display(job):
        print(f"Name: {job.name}")
        print(f"Age: {job.age}")
 
    def setdata(job):
        job.name = input("Enter Name: ")
        job.age = read_int("Enter Age: ")
        print()
 
    def getdata(job):
        print(f"Person created with name: {job.name} and age: {job.age}.")
        print()

class Manager (Employee) :
    def __init__(job,
                 __Employee_id = None, 
                 Name = None,
                 Age = None,
                 __Salary = None,
                 department = None):
        super().__init__(__Employee_id,Name,Age,__Salary)
        job.department =  department

    def display(job):
        super().display()
        print(f"Department : {job.department}")

    def setdata(job):
        super().setdata()
        job.department = input("Enter Your department : ")
        print()
    def getdata(job):
        print(
            f"Manager created with name: {job.name}, age: {job.age}, "
            f"ID: {job._Employee__employee_id}, salary: ₹ {job._Employee__salary}, and "
            f"department: {job.department}."
        )
        print()  

class Developer (Employee):
    
    def __init__(job, name=None, age=None, employee_id=None, salary=None, programming_language=None):
        super().__init__(employee_id, name, age, salary)
        job.programming_language = programming_language

    def display(job):
        super().display()
        print(f"Programming Language : {job.programming_language}")

    def setdata(job):
        super().setdata()
        job.programming_language = input("Enter Programming Language: ")
        print()     
        
    def getdata(job):
        print(
            f"Developer created with name: {job.name}, age: {job.age}, "
            f"ID: {job._Employee__employee_id}, salary: ₹ {job._Employee__salary}, and "
            f"programming language: {job.programming_language}."
        )
        print()
print("--- Python OOP Project: Employee Management System ---")
print()
 
obj = obj1 = obj2 = obj3 = None
 
while True:
    print("Choose an operation: ")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")
    print()
 
    choice = read_int("Enter your choice: ")
    print()
    if choice == 1:
        print("-----Creating a Person-----")
        print()
        obj = Person()
        obj.setdata()
        obj.getdata()
  

    elif choice == 2:
        
        print("-----Creating an Employee-----")
        print()
        obj1 = Employee()
        obj1.setdata()
        obj1.getdata()
 
    elif choice == 3:
        
        print("-----Creating a Manager-----")
        print()
        obj2 = Manager()
        obj2.setdata()
        obj2.getdata()
 
    elif choice == 4:
        
        print("-----Creating a Developer-----:")
        print()
        obj3 = Developer()
        obj3.setdata()
        obj3.getdata()


    elif choice == 5:

        print("Show details of:")
        print()
        print("Choose an object:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")
        print()
        choice = read_int("Enter your choice: ")
        print()
        if choice == 1:
            print("--Details of Person:--")
            if obj is None:
                print("Person not created yet..")
            else:
                obj.display()
            print()
 
        elif choice == 2:
            print("--Details of Employee:--")
            if obj1 is None:
                print("Employee not created yet..")
            else:
                obj1.display()
            print()
 
        elif choice == 3:
            print("--Details of Manager:--")
            if obj2 is None:
                print("Manage not created yet...")
            else:
                obj2.display()
            print()
 
        elif choice == 4:
            print("--Details of Developer:--")
            if obj3 is None:
                print("Developer not created yet..")
            else:
                obj3.display()
            print()
 
        else:
            print("Invalid choice. Please try again.")
            print()
 
    elif choice == 6: 
        print("Exiting the system. All resources have been successfully cleared.") 
        print("See you soon Goodbyy!") 
        break

    else:
        print("Invalid choice. Please try again.")
        print()