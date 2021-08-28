import random
import datetime
from customer import Customer
atm =Customer(id)
class ATMcard:
    def __init__(self,defaultPin,defaultBalance):
        self.defaultPin = defaultPin
        self.defaulBalance = defaultBalance
    def cekPinAwal(self):
        return self.defaultPin
    def cekSaldoAwal(self):
        return self.defaulBalance

while True:
    id = int(input('Masukkan pin anda : '))
    trial = 0

    while  (id != int(atm.checkPin()) and trial<3):
        id = int(input("Pin anda salah. SilakanMasukkan lagi: "))
        trial += 1

        if trial == 3 :
            print('ERROR')
            exit()     
    while True:
        print('Selamat Datang')
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 -Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        pilihanUser = int(input('\n Silahkan Masukkan Pilihan : '))
        if pilihanUser == 1:
            print("\nSaldo anda sekarang: Rp. "+ str(atm.checkBalance())+' \n')
        elif pilihanUser == 2:
            jumlah = float(input("Masukkan jumlah pengambilan : "))
            verify_withdraw =input("Konfirmasi: Anda akan melakukan debet dengan nominalberikut ? y/n "+str(jumlah) +" ")
            if verify_withdraw =="y":
                print("Saldo awal anda adalah: Rp. "+str(atm.checkBalance()))
            else:
                break
            if jumlah < atm.checkBalance() :
                atm.debet(jumlah)
                print('sisa saldo : '+str(atm.debet(jumlah)))
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silakan lakukan penambahan nominal saldo")
        elif pilihanUser == 3:
            jumlahSimpan = float(input("Masukkan jumlah penyimpanan : "))
            verify_deposit =input("Konfirmasi: Anda akan melakukanpenyimpanan dengan nominal berikut ? y/n "+str(jumlahSimpan) +"")
            if verify_deposit == 'y':
                atm.simpan(jumlahSimpan)
                print("Saldo anda sekarang adalah: Rp."+str(atm.checkBalance()) +"\n" )
            else :
                break
        elif pilihanUser == 4:
            oldPin = input("masukkan nomor pin lama")
            if oldPin == atm.checkPin() :
                newPin = input("masukkan nomor pin baru : ")
                confirmNewPin = input("mohon konfirmasi pin baru anda ")
                if newPin == confirmNewPin :
                    print("Selamat, pin baru berhasil dibuat")
                else: 
                    print('pin tidak sesuai !!')
            else:
                break
        elif pilihanUser == 5:
            print("Resi tercetak otomatis saat anda keluar. \n Harapsimpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()
        else :
            print("ERROR !!!")
            print("pilihan tidak tersedia")

