class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} makan nasi.")


class ManusiaMilenial(Manusia):
    def __init__(self, nama):
        super().__init__(nama)
        self.email = None

    def makan(self):
        print(f"{self.nama} makan nasi sambil scroll HP.")  # contoh override

    def set_email(self, email):
        self.email = email


# Membuat objek programmer
programmer = ManusiaMilenial('Eka')
programmer.set_email('Eka@test.com')
programmer.makan()

# Membuat objek petani
petani = ManusiaMilenial('Putra')
petani.set_email('putra@test.com')
petani.makan()
