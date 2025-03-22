# Define a class to represent an employee
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"Employee(name={self.name}, position={self.position})"

# Define a class to represent a department
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.sub_departments = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_sub_department(self, department):
        self.sub_departments.append(department)

    def __repr__(self):
        return f"Department(name={self.name}, employees={len(self.employees)}, sub_departments={len(self.sub_departments)})"

# Define a class to represent a company
class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_hierarchy(self):
        print(f"Company: {self.name}")
        self._display_departments(self.departments, indent=2)

    def _display_departments(self, departments, indent):
        for department in departments:
            print(" " * indent + f"Department: {department.name}")
            for employee in department.employees:
                print(" " * (indent + 2) + f"Employee: {employee.name}, Position: {employee.position}")
            if department.sub_departments:
                self._display_departments(department.sub_departments, indent + 2)

# Example usage
my_company = Company("Tech Innovators")

# Create departments
sales_department = Department("Sales")
hr_department = Department("Human Resources")

# Add employees to departments
sales_department.add_employee(Employee("Alice", "Sales Manager"))
sales_department.add_employee(Employee("Bob", "Sales Associate"))
hr_department.add_employee(Employee("Charlie", "HR Manager"))

# Create sub-department and add to HR
recruitment_department = Department("Recruitment")
hr_department.add_sub_department(recruitment_department)
recruitment_department.add_employee(Employee("David", "Recruiter"))

# Add departments to the company
my_company.add_department(sales_department)
my_company.add_department(hr_department)

# Display the hierarchy
my_company.display_hierarchy()
