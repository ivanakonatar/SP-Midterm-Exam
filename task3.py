"""
Write a class Person that has general attributes about person like name, surname, date of birth,
address. Override __str__ function in order to print name and the surname of the person.

Write a class Employee that extends the Person class and adds attributes company, position,
years_employed and base_salary. Employee class should override __str__ method and print
the data about the company and position. Employee class should have method get_salary() that
returns actually salary of the employee by adding 1% of the base salary on top of the base
salary for each year spent in company. Employee class should have method get_tax() that returns
how much tax should be paid for the employee by using formula actual salary + 70% of the actual
salary. Employee class should have class variable num_of_employees that keeps track about the
number of existing employees.

Write a class Freelancer that extends the Person class and adds attributes skills and reviews.
Both skills and reviews should be lists. List skills represents list of the skills offered by
Freelancer. List reviews represents quality marks (review starts) valued from 1 - 5 for each
project done by Freelancer. Freelancer class should override __str__ method and print the skill set
and average rating for the Freelancer. Frellancer class should have method get_rating() that returns
 average rating based on all reviews.

"""

class Person:

    def __init__(self,name, surname, date_of_birth, address):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.address = address

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Employee:

    num_of_employees = 0
    def __init__(self,name, surname, date_of_birth, address, company, position, years_employed, base_salary):
        Person.__init__(name,surname,date_of_birth,address)
        self.company = company
        self.position = position
        self.years_employed = years_employed
        self.base_salary = base_salary
        Employee.num_of_employees += 1
    def __str__(self):
        return "{} {}".format(self.company,self.position)

    def get_salary(self):
        return self.base_salary + (self.base_salary * (1/100) * self.years_employed)

    def get_tax(self):
        return  self.get_salary() + (self.get_salary() * 70/100)



class Freelancer(Person):

    def __init__(self,name, surname, date_of_birth, address,skills = [], reviews =[]):
        Person.__init__(name,surname,date_of_birth,address)

        self.skills = skills
        self.reviews = reviews

    def __str__(self):
        return "{} {}".format(self.get_rating(),self.skills)

    def get_rating(self):
        return sum(self.reviews)/len(self.reviews)













