class Employee:
    
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (salary / 50)
            salary += overtime_amount
        return salary
    
    def assign_department(self, department):
        self.emp_department = department
    
    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

emp1 = Employee(1, "John", 50000, "Marketing")

emp1.print_employee_details()

emp1.assign_department("Sales")

emp1.print_employee_details()

salary = emp1.calculate_emp_salary(emp1.emp_salary, 60)
print("Salary with overtime:", salary)