"""20CE023 - KAVIRAJ DESAI
Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship."""
class Student:  # student class
    def __init__(self, rollNo, name):  # define roll number and name when the object of studnt is created
        self.rollNo = rollNo  # initialize roll number
        self.name = name  # initialize name

    def display(self):  # display method of student
        print(f'Student Roll No: {self.rollNo}')  # print roll number of student
        print(f'Student Name: {self.name}')  # print name of student


class Exam(Student):  # exam class
    def __init__(self, rollNo, name, subject):  # define roll number, name and subject
        super().__init__(rollNo, name)  # initialize  roll number and name from student class
        self.subject = subject  # initialize subject

    def display(self):  # display method of exam
        super().display()  # display roll number and name from student class
        for i in range(len(self.subject)):
            print(f'Subject {i + 1} Marks: {self.subject[i]}')  # print marks of subject


class Result(Exam):  # class result
    total_marks = 0

    def __init__(self, rollNo, name, subject):  # define roll number, name , subject
        super().__init__(rollNo, name, subject)  # initialize roll numer, name, subject from exam class
        self.total_marks = sum(subject)  # do sum of all marks

    def display(self):  # display method of result method
        super().display()  # display roll number, name and subject
        print(f'Total Marks: {self.total_marks}')


if __name__ == '__main__':
    student = Student(1, 'BHAVDEEP')
    student.display()
    print()

    exam = Exam(2, 'KAVIRAJ', [30, 29, 8])
    exam.display()
    print()

    result = Result(3, 'MAHARSHI', [11, 11, 13])
    result.display()
    print()