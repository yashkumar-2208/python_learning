class Employee:
    
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond
        
    def get_salary(self):
        return self.salary
        
    def get_name(self):
        return self.name
    
    def get_bond(self):
        return self.bond

e1 = Employee(34000, "Jhon Doe", "4 years bond")
print(e1.get_salary())
print(e1.get_name())
print(e1.get_bond())




class myresume:

    def __init__(self, name, experience, skills, courses, degree, projects):
        self.name = name
        self.experience = experience
        self.skills = skills 
        self.courses = courses 
        self.degree = degree
        self.projects = projects

    def get_name(self):
        return self.name
        
    def get_experience(self):
        return self.experience

    def get_skills(self):
        return self.skills
        
    def get_courses(self):
        return self.courses

    def get_degree(self):
        return self.degree

    def get_projects(self):
        return self.projects

        

a = myresume('My name is Yash Kumar', "I'm having 3 years of experience.", "My skills are: \n- Python \n- Artificial Intellience \n- Machine Learning \n- Generative AI \n- Communication sills", "I'm having B.Tech degree from Doon University, Deharadun, UttraKhand", "Courses i've done: \n- Python from Code With Harry \n- AL/ML from Harvard University \n- GenAI from MIT.", "My projects: \n- AI Automation \n- Vidsnap AI (Reel generator) \n- LLM Model \n- Weather forecasting from API")
print(a.get_name())
print(a.get_experience())
print(a.get_skills())
print(a.get_courses())
print(a.get_degree())
print(a.get_projects())
