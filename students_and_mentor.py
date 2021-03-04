class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_mntr(self, mentor, course, grade):
        if isinstance(mentor, lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
                mentor.grade.append(grade)
            else:
                mentor.grades[course] = [grade]
                mentor.grade.append(grade)
        else:
            print( 'Ошибка')

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname + "\nКурсы в процессе изучения: " + ",".join(self.courses_in_progress) + "\nЗавершенные курсы: " + ",".join(self.finished_courses) + "\nСредняя оценка за домашние задания: " + " , ".join(self.avg_grade)

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.avg_grades = []

class lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.avg_grade = []
        self.grade = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname + "\nСредняя оценка за лекции: " + " ".join(self.avg_grade)


class reviwer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.total_grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                self.total_grades[course] += [grade]
            elif course in self.total_grades:
                student.grades[course] = [grade]
                self.total_grades[course] += [grade]
            else:
                student.grades[course] = [grade]
                self.total_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)