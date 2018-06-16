# This will be the main parent class that will hold name, salary, and department
class Employee:

    print("Part Time Employees:")
    count = 0
    salary_total = 0

# here we set everthing for the name, salary, and department
    def __init__(self, employee_name, employee_salary, employee_dept):

        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.employee_dept = employee_dept
        Employee.count += 1
        Employee.salary_total += employee_salary

    def display(self):
        print("------------------")
        print("Name:", self.employee_name)
        print("Salary:", self.employee_salary)
        print("Department:", self.employee_dept)

# this is only for full time employees it also uses the Employee class
class full_time(Employee):

    count = 0
    FTsalary = 0

    def __init__(self, employee_name, employee_salary, employee_dept, employee_city):
        super().__init__(employee_name, employee_salary, employee_dept)
        self.employee_city = employee_city
        full_time.count += 1
        full_time.FTsalary += employee_salary

    def display(self):

        Employee.display(self)
        print("Employee's City:", self.employee_city)

# this is a manager class which will also use the Employee class
class Manager(Employee):
    count = 0

    def __init__(self,employee_name, employee_salary, employee_dept, employee_exp):
        super().__init__(employee_name, employee_salary ,employee_dept)   # Use of super call
        self.employee_exp = employee_exp
        Manager.count += 1

    def display(self):
        print(" ")
        print("Manager details")
        Employee.display(self)
        print("Manager Experience:", self.employee_exp, "years")

# the applicants class does not use employee class since they are not employees and dont use all the
# stuff in the employee class
class Applicants:
    def __init__(self, applicants_name, applicants_ID, applicants_location):
        self.applicants_name = applicants_name
        self.applicants_ID = applicants_ID
        self.applicants_location = applicants_location

    def display(self):
        print("Applicant name:", self.applicants_name)
        print("Applicant ID:", self.applicants_ID)
        print("Applicant job location:", self.applicants_location)

# The recruiter even though is an employee we dont need it to be using the employee class
# this is becasue it only needs to take in 2 things name and department
class Recruiter:

    count = 0

    def __init__(self, recruiter_name, recruiter_dept):

        self.recruiter_name = recruiter_name
        self.recruiter_dept = recruiter_dept
        Recruiter.count += 1

    def display(self):
        print("Interview Schedule:")
        print("Recruiter name:", self.recruiter_name)
        print("Recruiter dept:", self.recruiter_dept)
# the interview class will use recruiter and applicant becasue it needs info from both classes
class Interview(Recruiter,Applicants):
    def __init__(self,recruiter_name,recruiter_dept, applicants_name, applicants_ID, applicants_location):
        Recruiter.__init__(self, recruiter_name, recruiter_dept)
        Applicants.__init__(self, applicants_name, applicants_ID, applicants_location)
    def display(self):
        Recruiter.display(self)
        Applicants.display(self)

# here we start to enter in names, salary, and jobs
# after it is all entered in we are then able to print


employee1 = Employee("Tom", 100000, "Software Engineer")
employee2 = Employee("Megan",60000,"Human Resources")
employee3 = Employee("Mike",55000,"Social Media Manager")


employee4 = full_time("Tim",80000,"IOS Developer","Kansas City, Missouri")

employee5 = full_time("Katy",35000,"Sales","Austin, Texas")

employee6 = Manager("John",150000,"CEO",20)

applicant1 = Applicants("Matt",884,"Dallas, Texas")

interview1=Interview("John","CEO","Matt",884,"Dallas, Texas")

employee1.display()
employee2.display()
employee3.display()

print("")
print("Fulltime employees list:")

employee4.display()
employee5.display()
employee6.display()

print("------------------")
print("Job Applicant details:")
applicant1.display()

print("------------------")
interview1.display()
print("------------------")

print("Total number of employees:", Employee.count, "---", "Average salary of all employees:", (Employee.salary_total//Employee.count))
print("------------------")
print("Total number of fulltime employees:", full_time.count, "---", "The average salary of fulltime employees:", (full_time.FTsalary//full_time.count))

print("-------------------")
print("Total number of Managers:", Manager.count, "---", "Total number of Recruiters:", Recruiter.count)