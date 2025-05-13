# Q1
class Rectangle():
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return  2* (self.width + self.height)
rect = Rectangle(int(input("1.Kenar")), int(input("2.Kenar")))

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# Q2

class School():
    def __init__(self,name,foundation_year):
        self.name=name
        self.foundation_year=foundation_year
        self.students=[]
        self.teachers={}
    def  add_new_student(self, student_name, student_class):
        self.students.append({"name":student_name, "class": student_class})
    def  add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name]=branch
    def view_student_list(self):
        print("Student List:")
        for student in self.students:
            print(f"Name: {student['name']}, Class: {student['class']}")
    def view_teacher_list(self):
        print("Teacher List:")
        for teacher, branch in self.teachers.items():
            print(f"Name: {teacher}, Major: {branch}")
school = School(input("Okul Ismini girin"),int(input("Foundation year")))
school.add_new_student(input("Isim girin"), input("Sinif girin"))
school.add_new_student(input("Isim girin"), input("Sinif girin"))
school.add_new_teacher(input("Isim girin"), input("Brans"))
school.add_new_teacher(input("Isim girin"), input("Brans"))
        
school.view_student_list()
school.view_teacher_list()

# Q3

class Shape():
    def __init__(self, width,height):
        self.width=width
        self.height=height
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    def calculate_area(self):
        return self.width*self.height
class Square(Shape):
    def __init__(self, width):
        super().__init__(width,width)
    def area_calculate(self):
        return self.width*self.width
