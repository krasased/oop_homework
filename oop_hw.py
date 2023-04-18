class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.avg_rate = None
        self.grades = {}
        self.courses_attached = []
        self.name = name
        self.surname = surname


    def __avg_rate__(self):
        len, sum_ = 0, 0
        for cor in self.grades.keys():
            len += len(self.grades[cor])
            sum_ += sum(self.grades.values())
        return sum_ / len
        

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_01 = Student('St_1_Name', 'St_1_Sur', 'unknown')
student_01.courses_in_progress += ['Python']
student_01.finished_courses += ['C+']

student_02 = Student('St_2_Name', 'St_2_Sur', 'unknown')
student_02.courses_in_progress += ['Python', 'C+']
student_02.finished_courses += ['Java']

reviewer_01 = Reviewer('Rev_1_Name', 'Rev_1_Sur')
reviewer_01.courses_attached += ['Python', 'C+', 'Java']

reviewer_02 = Reviewer('Rev_2_Name', 'Rev_2_Sur')
reviewer_02.courses_attached += ['Python', 'C+', 'Java']

lecturer_01 = Lecturer('Dr.', 'Programmer')
lecturer_02 = Lecturer('Mrs.', 'Speaker')


reviewer_01.rate_hw(student_01, 'Python', 10)
reviewer_01.rate_hw(student_02, 'Python', 20)
reviewer_02.rate_hw(student_01, 'Python', 30)
reviewer_02.rate_hw(student_02, 'Python', 40)


student_01.rate_lect(lecturer_01, 'Python', 4)
student_01.rate_lect(lecturer_02, 'Python', 5)
student_02.rate_lect(lecturer_01, 'Python', 6)
student_02.rate_lect(lecturer_02, 'Python', 7)

import gc

for obj in gc.get_objects():
    if isinstance(obj, Reviewer):
        print(obj)



for obj in gc.get_objects():
    if isinstance(obj, Lecturer):
        print(obj)
