#Q1

class Rectangle():
    def __init__(self,genislik,yukseklik):
        self.genislik=genislik
        self.yukseklik=yukseklik
        
    def alan(self):
        return self.genislik*self.yukseklik
    
    def cevre(self):
        return 2*(self.genislik+self.yukseklik)
    
cevre1=Rectangle(5,7)
print("Alani:",cevre1.alan())
print("cevre:",cevre1.cevre())

#Q2

class School():
    
    def __init__(self,name, foundation_year):
        self.name=name
        self.foundation_year=foundation_year
        self.students=[]
        self.teachers={}
        
    def add_new_student(self,student_name,student_class):
        
        student={"isim":student_name,"sinif":student_class}
        self.students.append(student)
        
        
    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name]=branch
        
    def view_student_list(self):
        print("ogrenci listesi:")
        for student in self.students:
            print(f"-{student['isim']}({student['sinif']}.sinif)")
    
    def view_teacher_list(self):
        print("Ogretmen listesi:")
        for teacher,branch in self.teachers.items():
            print(f"-{teacher}:{branch}")


okul=School("Barbaros Lisesi",1990)

okul.add_new_student("Ali Veli",10)
okul.add_new_student("Kel Mel",11)

okul.add_new_teacher("Mehmet Ad","Turkce")
okul.add_new_teacher("Adnan abi","Matematik")

okul.view_student_list()
okul.view_teacher_list()    
    



#Q3

class Shape():
    def __init__(self,genislik,yukseklik):
        self.genislik=genislik
        self.yukseklik=yukseklik
        
class Rectangle(Shape):         
    def calculate_area(self):
        return self.genislik*self.yukseklik

class Square(Shape):
    def calculate_area(self):
        return self.genislik*self.yukseklik
    
dikdortgen=Rectangle(5,10)
print("Dikdortegnin Alani:",dikdortgen.calculate_area())

kare =Rectangle(5,10)
print("Karenin Alani:",kare.calculate_area())


#Q4

class Vehicle():
    tur="Arac"
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil
        
        
class SUV(Vehicle):
    jip="Arazi araci"
    def arazi(self,dort_ceker_mi):
        self.dort_ceker_mi=dort_ceker_mi
        return "{} markasinin {} isimli modeli {} yilinda uretilmistir. '{}' olan bu otomobil '{}' sinifinda yer almaktadir ve {} dir. ".format(
            self.marka,self.model, self.yil, self.jip,self.tur,"4x4" if self.dort_ceker_mi else "2x4")
        
class Sportscar(Vehicle):
    sporoto="Spor Araba"
    def hizli(self,max_hiz):
        self.max_hiz=max_hiz
        return "{} markasinin {} isimli modeli {} yilinda uretilmistir.'{}' olan bu otomobil '{}' sinifinda yer almaktadir ve maksimum hizi {} dir. ".format(
            self.marka,self.model, self.yil,self.sporoto,self.tur,self.max_hiz
        )
        
arazi_araci=SUV("Range Rover","Discovery", 2020)
print(arazi_araci.arazi(True))

hizliarac=Sportscar("Lamborghini","Aventador",2020)
print(hizliarac.hizli(340))



#Q5

class Musteri():
    def __init__(self,isim,soyisim,tc_no,tel):
        self.isim=isim
        self.soyisim=soyisim
        self.tc_no=tc_no
        self.tel=tel
        
    def bilgi_goruntule(self):
        print("Musteri bilgileri:")
        print(f"isim:{self.isim}")
        print(f"soyisim:{self.soyisim}")
        print(f"tc:{self.tc_no}")
        print(f"tel:{self.tel}")    
            
        
class Hesap():
    def __init__(self, musteri,hesap_no,bakiye):
        self.musteri=musteri
        self.hesap_no=hesap_no
        self.bakiye=bakiye
        
    def musteri_goruntule(self):
        self.musteri.bilgi_goruntule()
    
    def para_ekle(self,yatirilan):
        self.bakiye+=yatirilan
        print(f"{yatirilan} hesaba yatirildi.")
        
    def para_cek(self,cekilen):
        if self.bakiye>=cekilen:
            self.bakiye-=cekilen
            print(f"{cekilen} hesaptan cekildi")
        else:
            print("Yetersiz bakiye...")
    def bakiye_goruntule(self):
        print(f"Bakiyeniz:{self.bakiye}")
        
musteri1=Musteri("Ali","Veli","1213341","06343444")

hesap1=Hesap(musteri1,"43534535",1000)

hesap1.musteri_goruntule()

hesap1.para_ekle(500)

hesap1.para_cek(750)

hesap1.bakiye_goruntule()

hesap1.para_cek(2000)
    
        
        
