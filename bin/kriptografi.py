class Orang:
    def __init__(self, id_1, id_2):
        self.private_key = self.generate_keys(id_1, id_2)[0]
        self.public_key = self.generate_keys(id_1, id_2)[1]
        self.n = id_1* id_2

    def generate_keys(self, p, q):
        n = p * q
        Pn = (p-1)*(q-1)
        key = []
        for i in range(2, Pn):
            gcd = self.euclid(Pn, i)
            if gcd == 1:
                key.append(i)
        e = int(313)
        r, d = self.exteuclid(Pn, e)
        return [e,d]

    def mengirim_pesan(self, penerima, pesan):
        pesan_terenkripsi = (pesan**penerima.public_key) % penerima.n
        print("pesan yang dikirim (ciphertext) :", pesan_terenkripsi)
        penerima.menerima_pesan(pesan_terenkripsi)

    def menerima_pesan(self, pesan_terenkripsi):
        pesan_terdekripsi = (pesan_terenkripsi**self.private_key) % self.n
        print("pesan terdekripsi :",pesan_terdekripsi)

    def euclid(self, m, n):
        if n == 0:
            return m
        else:
            r = m % n
            return self.euclid(n, r)

    def exteuclid(self, a, b):
        r1 = a
        r2 = b
        s1 = int(1)
        s2 = int(0)
        t1 = int(0)
        t2 = int(1)
        while r2 > 0:
            q = r1//r2
            r = r1-q * r2
            r1 = r2
            r2 = r
            s = s1-q * s2
            s1 = s2
            s2 = s
            t = t1-q * t2
            t1 = t2
            t2 = t
        if t1 < 0:
            t1 = t1 % a
        return (r1, t1)

class Pesan:
    konten = []
    def __init__(self, konten):
        for i in konten:
            self.konten.append(i)

amry = Orang(3, 357611)
reza = Orang(2, 349337)

pesan = 10110
print('pesan asli (plain text) : ', pesan)
print('\namry -> reza')
amry.mengirim_pesan(reza, pesan)
print('\nreza -> amry')
reza.mengirim_pesan(amry, pesan)