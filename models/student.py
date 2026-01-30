from models.person import Person

class student(Person):
    def __init__(self,pid, name, age,student_id):
        super().__init__(pid,name, age)
        self.student_id = student_id

    def __str__(self):
        return super().__str__() + f', StudentID: {self.student_id}'