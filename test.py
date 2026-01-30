from models.student import student
from models.staff import staff
from models.person import Person


student_obj = student(1, 'Alice', 20, 'S1001')
staff_obj = staff(2, 'Bob', 35, 'ST2001')

def get_person_info(person):
    return f'Name: {person.name}, Age: {person.age}'

print(get_person_info(student_obj))

