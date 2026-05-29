class Employee:
    company = "HP"

    def get_salary(self):
        return 34000
    
e = Employee()
print(e.get_salary())

e2 = Employee
print(e2.company)