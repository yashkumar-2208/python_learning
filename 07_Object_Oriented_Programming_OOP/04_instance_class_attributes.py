class Employee:
    company = "Company: Google"

    def __init__(self, salary, name, experience, skills):

        self.salary = salary
        self.name = name
        self.experience = experience
        self.skills = skills

    def get_salary(self):
        return "Salary: 8000000"
    
    def get_name(self):
        return "Name: Yash Kumar "
    
    def get_experience(self):
        return "Experience: 2 years"
    def get_skills(self):
        return "Skills: Python, AI, ML, GenAI"
    
e1 = Employee(8000000, "Yash Kumar", "2 years of experience", "Skills: Python, AI, ML, GenAI")
print(e1.get_name())
print(e1.get_salary())
print(e1.get_experience())
print(e1.get_skills())
print(Employee.company)

# Object introspection
print(dir(e1))


