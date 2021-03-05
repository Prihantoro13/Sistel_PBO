class student():
    def nama(self):
        print("nama    :", self.full_name)
        
    def get_age (self):
        print("umur    :", self.age)
    def get_hobby (self):
        print("hobby   :", self.hobby)
    def get_alamat (self):
        print("alamat  :", self.alamat)
toro = student()

toro.full_name = "Toro Mendes"
toro.age = "20"
toro.hobby = "Chilling in bed with some indie music"
toro.alamat = "Bekasi"

toro.nama()
toro.get_age()
toro.get_hobby()
toro.get_alamat()