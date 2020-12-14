class buku:
    nama = ''
    alamat = ''
    judul = ''

    def __init__(self, judul): # method constructor
        self.judul = judul

    def get_nama(self, nama):
        self.nama = nama

    def get_alamat(self, alamat):
        self.alamat = alamat

    def hasil(self):
        print('judul buku adalah %s\nnama peminjam %s\nalamat peminjam %s' % (self.judul, self.nama, self.alamat))


p = buku('surat cinta untuk starla')
p.get_nama('asdar')
p.get_alamat('bontonompo')
p.hasil()
print(' ')

p = buku('dilan 1990')
p.get_nama('adit')
p.get_alamat('pallangga')
p.hasil()
