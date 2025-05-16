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
rectangle =Rectangle(4,5)
sequare = Square(5)
print("Rectangle Area: ", rectangle.calculate_area())
print("Square Area : ", sequare.area_calculate())

# Q4
class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model =model
        self.year =year
class SuvVehicle(Vehicle):
    def __init__(self, make, model, year,four_wheel):
        super().__init__(make, model, year)
        self.four_wheel =four_wheel

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed=max_speed
suv_vhicle= SuvVehicle("Toyota","Rav4",2025,True)
sport_vhicle=SportsCar("BMW",328, 2025, 250)

print(f"Off-Road Vhicle: Make: {suv_vhicle.make},Model: {suv_vhicle.model}, Year : {suv_vhicle.year}, Four Wheel Drive:  {suv_vhicle.four_wheel} ")

print(f"Sport Vhicle: Make: {sport_vhicle.make},Model: {sport_vhicle.model}, Year : {sport_vhicle.year}, Four Wheel Drive:  {sport_vhicle.max_speed} ")


# Q5

class Customer:
    def __init__(self,name,surname,tc_identification,phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone
 
    def musteri_bilgileri (self):
        return f"Name: {self.name},  Surname: {self.surname},  TR ID Number:  {self.tc_identification}, Telephone Number: {self.phone}"
class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone,customer,account_number):
        super().__init__(name, surname, tc_identification, phone)
        self.customer=customer
        self.account_number=account_number
        self.balance=0.0
    def deposit(self, amount):
        self.balance+=amount
        print(f"Depozit: {amount}, Bakiye : {self.balance}")
    def money_check(self, amount):
        if amount <=self.balance:
            self.balance -=amount
            print(f"Cekilen: {amount}. Yeni bakiye: {self.balance}")
        else:
            print("Yeterli bakiye yok")

    def display_balance(self):
        print(f" Mevcut bakiye:{self.balance} ")


account = Account("Ali", "Veli", "12345678901", "05551234567", "TR123456")
print(account.musteri_bilgileri())

account.deposit(1000)
account.display_balance()
account.money_check(300)
account.display_balance()
account.money_check(800)
