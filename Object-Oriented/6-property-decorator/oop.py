
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @fullname.setter
    def fullname(self,value):
        self.first,self.last=value.split(' ')


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp1.fullname="Nabin Singh"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
