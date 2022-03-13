from abc import abstractmethod, ABC

#Class
class bangun_ruang(ABC):
    
    #Abstract Method
    @abstractmethod
    def volume(self):
        pass

    
class Kubus(bangun_ruang):

    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
            """Method untuk menghitung
            luas lingkaran"""
            print("Volume:", self.sisi * self.sisi * self.sisi)
                   
        
class Balok(bangun_ruang):

    def __init__(self, panjang, lebar, tinggi):
        self.panjang = pankang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def volume(self):
        print("Volume:", self.panjang * self.lebar * self.tinggi)