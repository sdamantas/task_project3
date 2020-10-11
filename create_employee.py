import re
from database import *


class Employee():

    def __init__(self, first_name: str, last_name: str, annual_salary: float, years_employed: int, email: str,
                 feedback: int, role: str):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.years_employed = years_employed
        self.email = email
        self.feedback = feedback
        self.role = role

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.role}, {self.annual_salary}, {self.feedback}, {self.years_employed}, {self.email}'

    @classmethod
    def create_from_string(cls, employee_string: str):
        first_name, last_name, role, annual_salary, years_employed, feedback, email = employee_string.split(",")
        annual_salary, feedback, years_employed = float(annual_salary), int(feedback), int(years_employed)
        if cls.validate_email(email):
            return cls(first_name, last_name, role, annual_salary, feedback, years_employed, email)

    @staticmethod
    def validate_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        return False


new_Empl = Employee.create_from_string("johnathanas,johns,CTO,200.0,32,20,johnotonasss@gmail.com")
print(new_Empl)
