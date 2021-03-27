"""
Модифицируйте класс Группа (задание прошлой лекции) так, чтобы при
попытке добавления в группу более 10-ти студентов, было возбужденно
пользовательское исключение. Таким образом нужно создать еще и
пользовательское исключение для этой ситуации. И обработать его.
"""


class MoreThan10StudentsError(Exception):
        
    def __init__(self):
        super().__init__()
        self.message = "Невозможно добавить нового студента в группу - уже 10 есть!"

    def __str__(self):
        return self.message

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
        try:
            if len(self.students_list) == 10:
                raise MoreThan10StudentsError
        except MoreThan10StudentsError as err:
            print(err)
        else:
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
student_4 = Student("Ж", "Татьяна", "Петровна", "Чуйко", 1998, "Grp-123")
student_5 = Student("Ж", "Юлия", "Олеговна", "Тимошенко", 1989, "Grp-123")
student_6 = Student("М", "Дмитрий", "Тарасович", "Фокин", 1955, "Grp-123")
student_7 = Student("М", "Виктор", "Петрович", "Махно", 1988, "Grp-123")
student_8 = Student("Ж", "Надежда", "Федоровна", "Лапина", 1989, "Grp-123")
student_9 = Student("М", "Олег", "Петрович", "Ложкин", 1978, "Grp-123")
student_10 = Student("М", "Тимур", "Петрович", "Каплин", 1971, "Grp-123")
student_11 = Student("Ж", "Елена", "Петровна", "Бабкина", 1991, "Grp-123")
print("1", student_1)
print("2", student_2)
print("3", student_3)
print("4", student_4)
print("5", student_5)
print("6", student_6)
print("7", student_7)
print("8", student_8)
print("9", student_9)
print("10", student_10)
print("11", student_11)
print()
group_1 = Group("Grp-123")
group_1.add_student(student_1)
group_1.add_student(student_2)
group_1.add_student(student_3)
group_1.add_student(student_4)
group_1.add_student(student_5)
group_1.add_student(student_6)
group_1.add_student(student_7)
group_1.add_student(student_8)
group_1.add_student(student_9)
group_1.add_student(student_10)
print()
print(group_1)
group_1.add_student(student_11)
