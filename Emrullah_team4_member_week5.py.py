#Soru 1
class Rectangle:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def area(self):
        return self.genislik * self.yukseklik

    def perimeter(self):
        return 2 * (self.genislik + self.yukseklik)


dikdortgen = Rectangle(5, 7)
print("Alan:", dikdortgen.area())
print("Çevre:", dikdortgen.perimeter())



#Soru 2
class Okul:
    def __init__(self, isim, kurulus_yili):
        self.isim = isim
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = []
        self.ogretmenler = {}

    def add_new_student(self, student_name, sinif):
        self.ogrenciler.append({"isim": student_name, "sinif": sinif})

    def add_new_teacher(self, teacher_name, branch):
        self.ogretmenler[teacher_name] = branch

    def view_student_list(self):
        print("Öğrenci Listesi:")
        for ogrenci in self.ogrenciler:
            print(f"{ogrenci['isim']} - Sinif: {ogrenci['sinif']}")

    def view_teacher_list(self):
        print("Öğretmen Listesi:")
        for isim, brans in self.ogretmenler.items():
            print(f"{isim} - Branş: {brans}")


okul = Okul("Atatürk Lisesi", 1995)
okul.add_new_student("Ali", "10-A")
okul.add_new_student("Zeynep", "9-B")
okul.add_new_teacher("Ahmet Hoca", "Matematik")
okul.add_new_teacher("Fatma Hoca", "Türkçe")

okul.view_student_list()
okul.view_teacher_list()

#3. Soru
class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Rectangle(Sekil):
    def calculate_area(self):
        return self.genislik * self.yukseklik

class Square(Sekil):
    def calculate_area(self):
        return self.genislik * self.genislik

# Örnek kullanim
dikdortgen = Rectangle(4, 6)
kare = Square(5, 5)

print("Dikdörtgen Alani:", dikdortgen.calculate_area())
print("Kare Alani:", kare.calculate_area())




#Soru 4
class Vehicle:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

class SUV(Vehicle):
    def __init__(self, marka, model, yil, dort_cekis):
        super().__init__(marka, model, yil)
        self.dort_cekis = dort_cekis

class SportCar(Vehicle):
    def __init__(self, marka, model, yil, max_speed):
        super().__init__(marka, model, yil)
        self.max_speed = max_speed


arazi_araci = SUV("Toyota", "Land Cruiser", 2020, True)
spor_araba = SportCar("Ferrari", "F8", 2023, 340)

print("Arazi Araci:", arazi_araci.marka, arazi_araci.model, arazi_araci.yil, "4x4:", arazi_araci.dort_cekis)
print("Spor Araba:", spor_araba.marka, spor_araba.model, spor_araba.yil, "Maks Hiz:", spor_araba.max_speed)

#soru 5
class Musteri:
    def __init__(self, isim, soyisim, tc_kimlik, telefon):
        self.isim = isim
        self.soyisim = soyisim
        self.tc_kimlik = tc_kimlik
        self.telefon = telefon

    def display_information(self):
        print("Müşteri Bilgileri:")
        print(f"İsim: {self.isim} {self.soyisim}")
        print(f"TC: {self.tc_kimlik}")
        print(f"Telefon: {self.telefon}")

class Hesap:
    def __init__(self, musteri, hesap_no, bakiye=0):
        self.musteri = musteri
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def deposit(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatirildi.")

    def money_check(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi.")
        else:
            print("Yetersiz bakiye!")

    def display_balance(self):
        print(f"Hesap Bakiyesi: {self.bakiye} TL")


musteri1 = Musteri("Ayşe", "Yilmaz", "12345678901", "0532 123 45 67")
hesap1 = Hesap(musteri1, "987654321")

musteri1.display_information()
hesap1.deposit(1000)
hesap1.money_check(300)
hesap1.display_balance()