class Aritmatika :
    def jumlahkan(self, x, y):
        return x + y

    def kurangi(self, x, y):
        return x - y

    def kali(self, x, y):
        return x * y

    def bagi(self, x, y):
        return x / y

aritmatika = Aritmatika()
print("Penjumalahn 5 dan 3 adalah: "+ str(aritmatika.kali(5, 3)))