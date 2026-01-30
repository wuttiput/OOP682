from models.classroom import Classroom
from models.student import student

oop = Classroom('OOP')
oop.add_student(student(1, 'Alice', 20, 'S1001'))
oop.add_student(student(2, 'Bob', 22, 'S1002'))
print(f'จำนวนนักเรียนที่ลงทะเบียน {len(oop)} คน')
oop.add_student(student(3, 'Charlie', 21, 'S1003'))
print(f'จำนวนล่าสุด {len(oop)} คน')
print('student in the classroom:')
for i in range(len(oop)):
    print(oop.__getiem__(i))