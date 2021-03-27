"""
Создайте класс, описывающий человека (создайте метод, выводящий
информацию о человеке).

На его основе создайте класс Студент (переопределите метод вывода
информации).

Создайте класс Группа, который содержит список из объектов класса
Студент. Реализуйте методы добавления, удаления студента и метод поиска
студента по фамилии. Определите для Группы метод __str__() для
возвращения списка студентов в виде строки.
"""


class Human:
    
    def __init__(self, gender, firstname, patronymic, lastname, year_of_birth):
        self.gender = gender
        self.firstname = firstname
        self.patronymic = patronymic
        self.lastname = lastname
        self.year_of_birth = year_of_birth

    def __str__(self):
        return f"Human: gender={self.gender}, firstname={self.firstname}, patronymic=" + \
        f"{self.patronymic}, lastname={self.lastname}, year_of_birth={self.year_of_birth}"

class Student(Human):

    def __init__(self, gender, firstname, patronymic, lastname, year_of_birth, group_id):
        super().__init__(gender, firstname, patronymic, lastname, year_of_birth)
        self.group_id = group_id

    def __str__(self):
        return f"Student: gender={self.gender}, firstname={self.firstname}, patronymic=" + \
             f"{self.patronymic}, lastname={self.lastname}, year_of_birth={self.year_of_birth}" + \
             f", group_id={self.group_id}"

class Group:

    def __init__(self, group_id):
        self.group_id = group_id
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)

    def remove_student(self, student):
        self.students_list.remove(student)

    def search_student(self, last_name):
        for elem in self.students_list:
            if elem.lastname == last_name:
                print("Студент найден!")
                print(elem)
                break
        else:
            print(f"Студента '{last_name}' нет в списке группы!")
    
    def __str__(self):
        result_list = ""
        for elem in self.students_list:
            result_list += str(elem) + "\n"
        return f"Group: {self.group_id}" + "\n" + result_list

student_1 = Student("М", "Иван", "Иванович", "Иванов", 1984, "Grp-123")
student_2 = Student("М", "Петр", "Петрович", "Петров", 1999, "Grp-123")
student_3 = Student("Ж", "Ольга", "Андреевна", "Бойко", 2002, "Grp-123")
print(student_1)
print(student_2)
print(student_3)
print()
group_1 = Group("Grp-123")
group_1.add_student(student_1)
group_1.add_student(student_2)
group_1.add_student(student_3)
group_1.remove_student(student_2)
group_1.search_student("Попович")
print()
print(group_1)
