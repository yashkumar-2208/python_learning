class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    #This is Instance method (default)
    def print_info(self):
        info = f"The name is: {self.name} and the salary is: {self.salary}"
        print(info)

e1 = Employee("Jack", 100000)
e2 = Employee("John", 200000)

e1.print_info()
e2.print_info()
print(Employee.company)



print("--------")

class my_info:

    company_1 = "Google"
    company_2 = "Apple"

    def __init__(self, name, salary, skills):
        self.name = name 
        self.salary = salary
        self.skills = skills


    def print_info(self):
        a = f"My name is: {self.name} and my salary is: {self.salary} and my skills are: {self.skills}"
        print(a)


    @staticmethod #after using @staticmethod we are all good to go without using self func. And self is not automatically passed.
    def sum(a,b): 
        return a+b
    
    @classmethod
    def print_company(cls):
        print(cls.company_1)

    @classmethod
    def change_company(cls, new_company):
        cls.company_1 = new_company


e1 = my_info("Yash Kumar", 1200, "Python, AL/ML, GenAI")
e1.print_info()
print(my_info.company_1)
print(my_info.company_2)

print(e1.sum(4,60))

e1.print_company()

e1.change_company("Microsoft")


e1.print_company()











        

        