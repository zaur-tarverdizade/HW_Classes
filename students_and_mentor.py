class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = []

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

    def avrg_rd(self):
        for name_course, grade in self.grades.items():
            average_grade = sum(grade) / len(grade)
            self.avg_grade.append(name_course + " -> " + str(average_grade))

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

    def avrg_rd(self):
        for name_course, grade in self.grades.items():
            average_grade = sum(grade) / len(grade)
            self.avg_grade.append(name_course + " -> " + str(average_grade))

    def com(self, mentor):
        if isinstance(mentor, lecturer):
            if sum(mentor.grade) / len(mentor.grade) > sum(self.grade) / len(self.grade):
                print("Учитель с большей оценкой: " + mentor.name + mentor.surname)
            elif sum(mentor.grade) / len(mentor.grade) < sum(self.grade) / len(self.grade):
                print("Учитель с большей оценкой: " + self.name + self.surname)
            else:
                return "Одинаковый"

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

    def avg_ttl_grds(self, course):
        if course in self.total_grades:
            print("Средняя оценка за д/з по курсу "  + course + ": " + str(sum(self.total_grades.get(course))/len(self.total_grades.get(course)) ))

    def avg_grade(self,student, course):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                average_grade = sum(student.grades[course])/len(student.grades[course])
                print(average_grade)
        else:
            print("Ошибка")

    def comp(self, student1, student2, name_course):
        if isinstance(student1, Student) and isinstance(student2, Student) and name_course in self.courses_attached and name_course in student1.courses_in_progress and name_course in student2.courses_in_progress:
            if sum(student1.grades[name_course]) / len(student1.grades[name_course]) > sum(student2.grades[name_course]) / len(student2.grades[name_course]):
                print("Студент с большей оценкой по курсу " + name_course +  " : " + student1.name + ' ' + student1.surname)

            elif sum(student1.grades[name_course]) / len(student1.grades[name_course]) < sum(student2.grades[name_course]) / len(student2.grades[name_course]):
                print("Студент с большей оценкой по курсу " + name_course +  " : " + student2.name + ' ' + student2.surname)

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname

 
HPotter = Student('Harry', 'Potter')
HPotter.courses_in_progress += ['Python']
HPotter.courses_in_progress += ['Git']
HPotter.courses_in_progress += ['Java']
HPotter.courses_in_progress += ['MatLab']
HPotter.finished_courses += ["Введение в программирование"]

RWeasley = Student('Ronald', 'Weasley')
RWeasley.courses_in_progress += ['Python']
RWeasley.courses_in_progress += ['Java']
RWeasley.finished_courses += ["Введение в программирование"]
RWeasley.courses_in_progress += ['Git']
RWeasley.courses_in_progress += ['MatLab']

SSnape = reviwer('Severus', 'Snape')
SSnape.courses_attached += ['Python']
SSnape.courses_attached += ['Hub']

HSlughorn = reviwer('Horace' , 'Slughorn')
HSlughorn.courses_attached += ['Java']

MMcConnagal = lecturer('Minevra', 'McConnagal')
MMcConnagal.courses_attached += ['Git']

RLupin = lecturer('Remus', 'Lupin')
RLupin.courses_attached += ['MatLab']
