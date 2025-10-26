# ====================================================
# =                     Library                      =
# ====================================================
# Import library yang diperlukan untuk sistem
import os  # Untuk operasi sistem seperti clear screen
from prettytable import PrettyTable  # Untuk membuat tabel tampilan data
import pwinput  # Untuk input password yang tersembunyi
import json  # Untuk membaca dan menulis file JSON
import time  # Untuk delay waktu
from datetime import date  # Untuk mendapatkan tanggal saat ini

# ====================================================
# =-------------------- JSON ------------------------=
# ====================================================

# ====================================================
# =- - - - - - - - DataReservasi.json - - - - - - - -=
# ====================================================
# ====================================================
# =             JSON Simpan Data Tamu                =
# ====================================================
def buat_ubah_hapusdata(data):
    # Simpan data reservasi ke file JSON dengan indentasi untuk readability
    with open("DataReservasi.json", "w") as file:
        json.dump(data, file, indent=4)

# ====================================================
# =             JSON Baca Tamu Hotel                 =
# ====================================================
def baca_reservasi():
    # Baca data reservasi dari file JSON
    # Exception handling: Jika file tidak ada atau JSON error, kembalikan list kosong
    try:
        with open("DataReservasi.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataReservasi.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []

# ====================================================
# =- - - - - - - - DataCheckList.json - - - - - - - -=
# ====================================================
# ====================================================
# =           JSON Cek Status Kamar Hotel            =
# ====================================================
def baca_checklist():
    # Baca data status kamar dari file JSON
    # Exception handling: Jika file tidak ada atau JSON error, kembalikan list kosong
    try:
        with open("DataCheckList.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataCheckList.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []

# ====================================================
# =          JSON Update Status Kamar Hotel          =
# ====================================================
def update_checklist(kamar, status):
    # Update status kamar tertentu di data checklist
    data = baca_checklist()
    for item in data:
        if item["Kamar"] == int(kamar):
            item["Status"] = status  # Ubah status (Tersedia/Ditempati)
            break
    with open("DataCheckList.json", "w") as file:
        json.dump(data, file, indent=4)

# ====================================================
# =- - - - - - - DataHarga.json - - - - - - - - - - -=
# ====================================================
# ====================================================
# =             JSON Harga Kamar Hotel               =
# ====================================================
def baca_harga():
    # Baca data harga kamar dari file JSON
    # Exception handling: Jika file tidak ada atau JSON error, kembalikan list kosong
    try:
        with open("DataHarga.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataHarga.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []

# ====================================================
# =                Mencari Harga Kamar               =
# ====================================================
def get_harga_kamar(kamar):
    # Hitung harga kamar berdasarkan nomor kamar
    # Kamar 1-5: Rp 300.000 (lantai 1), Kamar 6-10: Rp 600.000 (lantai 2)
    if 1 <= kamar <= 5:
        return 300000
    elif 6 <= kamar <= 10:
        return 600000
    else:
        return None  # Jika kamar tidak valid

# ====================================================
# =- - - - - - - DataKaryawan.json - - - - - - - - - =
# ====================================================
# ====================================================
# =              Melihat Akun Karyawan               =
# ====================================================
def loginkaryawan():
    # Baca data akun karyawan dari file JSON
    # Exception handling: Jika file tidak ada atau JSON error, kembalikan list kosong
    try:
        with open("DataKaryawan.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataKaryawan.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []

# ====================================================
# =              Tambah Akun Karyawan                =
# ====================================================
def tambahkaryawan(data2):
    # Simpan data akun karyawan ke file JSON
    with open("DataKaryawan.json", "w") as file:
        json.dump(data2, file, indent=4)

# ====================================================
# =- - - - - - - DataManager.json - - - - - - - - - -=
# ====================================================
# ====================================================
# =              Melihat Akun Manager                =
# ====================================================
def loginmanager():
    # Baca data akun manager dari file JSON
    # Exception handling: Jika file tidak ada atau JSON error, kembalikan list kosong
    try:
        with open("DataManager.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataManager.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []

# ====================================================
# =              Tambah Akun Manager                 =
# ====================================================
def tambahmanager(data1):
    # Simpan data akun manager ke file JSON
    with open("DataManager.json", "w") as file:
        json.dump(data1, file, indent=4)

# ====================================================
# =- - - - - - - DataKostumer.json - - - - - - - - - =
# ====================================================
# ====================================================
# =                Melihat Saldo                     =
# ====================================================
def loginkostumer():
    # Baca data akun kostumer dari file JSON
    # Exception handling: Jika file tidak ada atau JSON error, kembalikan list kosong
    try:
        with open("DataKostumer.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataKostumer.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []

# ====================================================
# =                Menambah Saldo                    =
# ====================================================
def saldokostumer(data_kostumer):
    # Simpan data saldo kostumer ke file JSON
    with open('DataKostumer.json', 'w') as file:
        json.dump(data_kostumer, file, indent=4)

# ====================================================
# =              Tambah Akun Kostumer                =
# ====================================================
def tambahkostumer(data3):
    # Simpan data akun kostumer ke file JSON
    with open("DataKostumer.json", "w") as file:
        json.dump(data3, file, indent=4)

# ====================================================
# =------------------- TABEL ------------------------=
# ====================================================

# ====================================================
# =                 Tabel Reservasi                  =
# ====================================================
def tabel_reservasi():
    # Tampilkan tabel reservasi menggunakan PrettyTable
    data = baca_reservasi()
    if not data:
        print("Tidak ada reservasi.")
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Reservasi Hotel"
    tabel.field_names = ["No", "Nama Tamu", "Nomor Kamar", "Durasi (hari)", "Total Harga"]
    for res in data:
        tabel.add_row([res["No"], res["Nama Tamu"], res["Nomor Kamar"], res["Durasi"], f"Rp {res['Total Harga']:,}"])
    print(tabel)

# ====================================================
# =               Tabel Status Kamar                 =
# ====================================================
def tabel_checklist():
    # Tampilkan tabel status kamar menggunakan PrettyTable
    data = baca_checklist()
    tabel = PrettyTable()
    tabel.title = "Status Kamar"
    tabel.field_names = ["Kamar", "Status"]
    for item in data:
        tabel.add_row([item["Kamar"], item["Status"]])
    print(tabel)

# ====================================================
# =                 Tabel Harga Kamar                =
# ====================================================
def tabel_harga():
    # Tampilkan tabel harga kamar menggunakan PrettyTable
    data = baca_harga()
    if not data:
        print("Data harga tidak tersedia.")
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Harga Kamar"
    tabel.field_names = ["No", "Nomor Kamar", "Lantai", "Harga per Malam"]
    for res in data:
        tabel.add_row([res["No"], res["Kamar"], res["Lantai"], res["Harga"]])
    print(tabel)

# ====================================================
# =                 Struk Pembelian Kamar            =
# ====================================================
def struk_harga(nama_tamu, kamar, durasi, harga_per_malam, total):
    # Tampilkan struk pembelian kamar
    os.system("cls")
    tanggal = date.today()
    lantai = 1 if kamar <= 5 else 2  # Hitung lantai berdasarkan nomor kamar 
    print("====================================================")
    print("=                Pembelian Kamar                   =")
    print("====================================================")           
    print(f"    Nama            : {nama_tamu}                  ")
    print(f"    Tanggal         : {tanggal}                    ")
    print(f"    Lantai Kamar    : {lantai}                     ")
    print(f"    Harga Per Malam : Rp {harga_per_malam:,}       ")  # Format harga dengan koma 
    print(f"    Durasi          : {durasi} Hari                ")
    print("====================================================")
    print(f"=   Total            : Rp {total:,}                ")  # Format total dengan koma 
    print("====================================================")
    print("= Terima Kasih atas Kunjungan Anda!                =")
    print("= Silakan Simpan Struk Ini sebagai Bukti.          =")
    print("====================================================")
    time.sleep(5)

# ====================================================
# = - - - - - - - - - LOGIN AKUN - - - - -  - - - - -=
# ====================================================
def sistemlog():
    # Sistem login untuk semua role (Manager, Karyawan, Kostumer)
    # Menggunakan counter percobaan untuk batas maksimal 10 kali
    percobaan = 0
    while True:
        try:
            data1 = loginmanager()
            data2 = loginkaryawan()
            data3 = loginkostumer()
            nama = input("Username: ").lower()  # Input username, ubah ke lowercase untuk fleksibilitas
            password = pwinput.pwinput("Password: ").lower()  # Input password, ubah ke lowercase untuk fleksibilitas 
            if nama == "keluar" or password == "keluar":
                break  # Keluar jika input "keluar"
            
            # Cek login untuk Manager
            for item in data1:   
                if nama == item["Username"].lower() and password == item["Password"].lower():  # Matching dengan lowercase 
                    print("\nLogin sukses!")
                    input("Enter...")
                    menu("Manager")
                    return
                    
            # Cek login untuk Karyawan
            for item in data2:
                if nama == item["Username"].lower() and password == item["Password"].lower():  # Matching dengan lowercase 
                    print("\nLogin sukses!")
                    input("Enter...")
                    menu("Karyawan")
                    return
            
            # Cek login untuk Kostumer
            for item in data3:
                if nama == item["Username"].lower() and password == item["Password"].lower():  # Matching dengan lowercase
                    print("\nLogin sukses!")
                    input("Enter...")
                    menukostumer(nama)
                    return

            # Jika login gagal, tambah percobaan dan penalti waktu
            percobaan += 1
            print("\nUsername atau password salah coba lagi! (10 Maksimal)")
            print(f"Percobaan {percobaan}")
            if percobaan == 10:
                print("Percobaan penuh anda di keluarkan!")
                time.sleep(10)
                break
            elif percobaan % 9 == 0:
                print("Tunggu 90 detik untuk mencoba lagi")
                time.sleep(90)
            elif percobaan % 6 == 0:
                print("Tunggu 60 detik untuk mencoba lagi")
                time.sleep(60)
            elif percobaan % 3 == 0:
                print("Tunggu 30 detik untuk mencoba lagi")
                time.sleep(30)
            input("Enter...\n")

        except ValueError:
            print("Input harus angka!")
            input("Enter...")
        except KeyError:
            print("Error Tidak ada di Data")
            input("Enter...")
        except KeyboardInterrupt:
            print("\nProses dibatalkan pengguna.")
            input("Enter...")
            print("Keluar dari sistem...")
        except Exception as e:
            print(f"Terjadi error tak terduga: {e}")
            input("Enter...")

# ====================================================
# = - - - - - - - - - TAMBAH AKUN - - - - - - - - - -=
# ====================================================
def registrasi():
    # Fungsi registrasi akun baru untuk Manager, Karyawan, atau Kostumer
    while True:
        try:
            data1 = loginmanager()
            data2 = loginkaryawan()
            data3 = loginkostumer()
            os.system("cls")
            print("====================================================")
            print("=                Registrasi Akun                   =")
            print("====================================================")        
            print("=            1.     Manager                        =")
            print("=            2.     Karyawan                       =")
            print("=            3.     Kostumer                       =")
            print("=            4.     Kembali Halaman Login          =")
            print("====================================================")
            
            pilihan = input("Masukkan pilihan : ")
            
            if pilihan == "1":  # Registrasi Manager
                username_baru = input("Masukkan username baru untuk Manager: ").lower()  # Ubah ke lowercase untuk konsistensi 
                password_baru = pwinput.pwinput("Masukkan password baru: ").lower()  # Ubah ke lowercase untuk konsistensi
                if len(password_baru) < 4:
                    print("Password minimal 4 karakter!")
                    input("Enter untuk kembali...")
                    continue
                akun_baru = {"Username": username_baru, "Password": password_baru}  # Manager tidak perlu E-Money 
                data1.append(akun_baru)
                tambahmanager(data1)
                print("\nRegistrasi sukses! Akun Manager baru telah ditambahkan.")
                input("Enter untuk kembali...")
                log()
            
            elif pilihan == "2":  # Registrasi Karyawan
                username_baru = input("Masukkan username baru untuk Karyawan: ").lower()  # Ubah ke lowercase untuk konsistensi 
                password_baru = pwinput.pwinput("Masukkan password baru: ").lower()  # Ubah ke lowercase untuk konsistensi 
                if len(password_baru) < 4:
                    print("Password minimal 4 karakter!")
                    input("Enter untuk kembali...")
                    continue
                akun_baru = {"Username": username_baru, "Password": password_baru}
                data2.append(akun_baru)
                tambahkaryawan(data2)
                print("\nRegistrasi sukses! Akun Karyawan baru telah ditambahkan.")
                input("Enter untuk kembali...")
                log()
                return

            elif pilihan == "3":  # Registrasi Kostumer
                username_baru = input("Masukkan username baru untuk Kostumer: ").lower()  # Ubah ke lowercase untuk konsistensi
                password_baru = pwinput.pwinput("Masukkan password baru: ").lower()  # Ubah ke lowercase untuk konsistensi
                if len(password_baru) < 4:
                    print("Password minimal 4 karakter!")
                    input("Enter untuk kembali...")
                    continue

                while True:  # Loop untuk memilih tipe akun
                    tipe = input("Pilih tipe akun (VIP/Reguler): ").lower()  # Ubah ke lowercase untuk fleksibilitas 
                    if tipe in ["vip", "reguler"]:
                        break
                    else:
                        print("Tipe akun harus 'VIP' atau 'Reguler'. Coba lagi.")
                e_money = 0
                akun_baru = {"Username": username_baru, "Password": password_baru, "E-Money": e_money, "Tipe": tipe.capitalize()}  # Ubah ke capitalize untuk konsistensi
                data3.append(akun_baru)
                tambahkostumer(data3)
                print(f"\nRegistrasi sukses! Akun Kostumer {tipe.capitalize()} baru telah ditambahkan.")  # Tampilkan tipe dengan capitalize
                input("Enter untuk kembali...")
                log()

            elif pilihan == "4":  # Kembali ke login
                log()
                break
            else:  # Pilihan tidak valid
                print("Pilihan tidak valid.")
                input("Enter untuk lanjut...")
        except ValueError:
            print("Input harus angka!")
            input("Enter...")
        except KeyError:
            print("Error Tidak ada di Data")
            input("Enter...")
        except KeyboardInterrupt:
            print("\nProses dibatalkan pengguna.")
            input("Enter...")
            print("Keluar dari sistem...")
        except Exception as e:
            print(f"Terjadi error tak terduga: {e}")
            input("Enter...")

# ====================================================
# =----------------- FUNGSI UTAMA -------------------=
# ====================================================
def menu(role):
    # Fungsi utama menu berdasarkan role (Manager atau Karyawan)
    while True:
        os.system("cls")
        print("====================================================")
        print("=              Sistem Reservasi Hotel              =")
        print("====================================================")
        
        # Menu untuk Manager
        if role == "Manager":
            print("====================================================")
            print("=            1.     Tambah Reservasi               =")           
            print("=            2.     Lihat Reservasi                =")
            print("=            3.     Ubah Reservasi                 =")
            print("=            4.     Hapus Reservasi                =")
            print("=            5.     Lihat Ketersediaan Kamar       =")
            print("=            6.     Kembali Halaman Login          =")
            print("====================================================")
            
        # Menu untuk Karyawan
        elif role == "Karyawan":
            print("====================================================")         
            print("=            1.     Lihat Reservasi                =")
            print("=            2.     Lihat Ketersediaan Kamar       =")
            print("=            3.     Kembali Halaman Login          =")
            print("====================================================")
        else:
            return  # Keluar jika role tidak valid
        
        try:
            pilihan = int(input("\nMasukkan pilihan: "))  # Input pilihan sebagai integer
            data = baca_reservasi()  # Baca data reservasi
            
            # Sistem untuk Manager
            if role == "Manager":
                if pilihan == 1:  # Tambah Reservasi
                    if len(data) >= 10:  # Cek batas maksimal reservasi
                        print("\nMaaf, semua kamar penuh (maksimal 10).")
                        input("Enter untuk lanjut...")
                        continue
                    checklist = baca_checklist()  # Baca data kamar
                    kamar_tersedia = []  # List kamar tersedia
                    for item in checklist:
                        if item["Status"] == "Tersedia":
                            kamar_tersedia.append(item["Kamar"])
                    if not kamar_tersedia:
                        print("\nTidak ada kamar tersedia.")
                        input("Enter untuk lanjut...")
                        continue
                    print(f"\nKamar tersedia: {kamar_tersedia}")
                    nama_tamu = input("Nama Tamu: ")
                    while True:
                        try:
                            kamar = int(input("Nomor Kamar (dari tersedia): "))
                            if kamar not in kamar_tersedia:
                                print("Kamar tidak tersedia! Coba lagi.")
                                continue
                            break
                        except ValueError:
                            print("Input harus angka!")
                    durasi = int(input("Durasi (hari): "))
                    harga_per_malam = get_harga_kamar(kamar)
                    total = durasi * harga_per_malam
                    no = len(data) + 1
                    data.append({
                        "No": no,
                        "Nama Tamu": nama_tamu,
                        "Nomor Kamar": kamar,
                        "Durasi": durasi,
                        "Total Harga": total
                    })
                    update_checklist(kamar, "Ditempati")
                    buat_ubah_hapusdata(data)
                    print(f"\nReservasi berhasil! Total: Rp {total:,}")
                    
                elif pilihan == 2:  # Lihat Reservasi
                    tabel_reservasi()
                    
                elif pilihan == 3:  # Ubah Reservasi
                    tabel_reservasi()
                    if not data:
                        input("Enter untuk lanjut...")
                        continue
                    while True:
                        try:
                            idx = int(input("Nomor Reservasi untuk diubah: ")) - 1
                            if 0 <= idx < len(data):
                                break
                            else:
                                print("Nomor tidak valid!")
                        except ValueError:
                            print("Input harus angka!")
                            
                    data[idx]["Nama Tamu"] = input("Nama Tamu baru: ")
                    kamar_lama = data[idx]["Nomor Kamar"]
                    kamar_baru_input = input("Nomor Kamar baru : ")
                    if kamar_baru_input:
                        try:
                            kamar_baru = int(kamar_baru_input)
                            checklist = baca_checklist()
                            kamar_tersedia = []
                            for item in checklist:
                                if item["Status"] == "Tersedia":
                                    kamar_tersedia.append(item["Kamar"])
                            if kamar_baru in kamar_tersedia:
                                update_checklist(kamar_lama, "Tersedia")
                                update_checklist(kamar_baru, "Ditempati")
                                data[idx]["Nomor Kamar"] = kamar_baru
                            else:
                                print("Kamar baru tidak tersedia!")
                                input("Enter untuk lanjut...")
                                continue
                        except ValueError:
                            print("Kamar baru harus angka!")
                            input("Enter untuk lanjut...")
                            continue
                    data[idx]["Durasi"] = int(input("Durasi baru: "))
                    data[idx]["Total Harga"] = data[idx]["Durasi"] * get_harga_kamar(data[idx]["Nomor Kamar"])
                    buat_ubah_hapusdata(data)
                    print("\nReservasi diubah!")
                    
                elif pilihan == 4:  # Hapus Reservasi
                    tabel_reservasi()
                    if not data:
                        input("Enter untuk lanjut...")
                        continue
                    while True:
                        try:
                            idx = int(input("Nomor Reservasi untuk dihapus: ")) - 1
                            if 0 <= idx < len(data):
                                break
                            else:
                                print("Nomor tidak valid!")
                        except ValueError:
                            print("Input harus angka!")
                    kamar = data[idx]["Nomor Kamar"]
                    del data[idx]
                    
                    nomor = 1
                    for res in data:
                        res["No"] = nomor
                        nomor += 1

                    update_checklist(kamar, "Tersedia")
                    buat_ubah_hapusdata(data)
                    print("\nReservasi dihapus!")
                    
                elif pilihan == 5:  # Lihat Ketersediaan Kamar
                    tabel_checklist()
                    
                elif pilihan == 6:  # Kembali ke Login
                    log()
                    break
            
            # Sistem untuk Karyawan
            elif role == "Karyawan":
                if pilihan == 1:  # Lihat Reservasi
                    tabel_reservasi()
                elif pilihan == 2:  # Lihat Ketersediaan Kamar
                    tabel_checklist()
                elif pilihan == 3:  # Kembali ke Login
                    log()
                    break
                else:
                    print("Pilihan tidak valid!")
            
            input("\nEnter untuk lanjut...")
            
        except ValueError:
            print("Input harus angka!\n")
            input("Enter...")
        except KeyError:
            print("Error Tidak ada di Data\n")
            input("Enter...")
        except KeyboardInterrupt:
            print("\nProses dibatalkan pengguna.")
            input("Enter...")
        except Exception as e:
            print(f"Terjadi error tak terduga: {e}")
            input("Enter...")

# ====================================================
# =------------------ KOSTUMER ----------------------=
# ====================================================
def menukostumer(nama_tamu):
    # Fungsi menu untuk kostumer
    data_kostumer = loginkostumer()
    money = {"E-Money": 0, "Tipe": "Reguler"}
    for item in data_kostumer:
        if item["Username"] == nama_tamu:
            money["E-Money"] = item["E-Money"]
            money["Tipe"] = item.get("Tipe", "Reguler")
            break
    saldo = money["E-Money"]
    tipe_akun = money["Tipe"]
    while True:
        try:
            os.system("cls")
            print("====================================================")
            print("=              Menu Kostumer                       =")
            print("====================================================")
            print("=            1.     Pesan Kamar                    =")
            print("=            2.     Tambah Saldo E-Money           =")
            print("=            3.     Lihat Saldo E-Money            =")
            print("=            4.     Kembali Halaman Login          =")
            print("====================================================")
            pilihan = int(input("Masukkan pilihan: "))
            
            if pilihan == 1:  # Pesan Kamar
                while True:
                    pesan = input("\nIngin memesan? (Iya/Keluar): ").lower()
                    if pesan == "keluar":
                        break
                    elif pesan == "iya":
                        os.system("cls")
                        tabel_harga()
                        tabel_checklist()
                        data_res = baca_reservasi()
                        if len(data_res) >= 10:
                            print("Maaf, hotel penuh!")
                            input("Enter...")
                            continue

                        checklist = baca_checklist()
                        kamar_tersedia = []
                        for item in checklist:
                            if item["Status"] == "Tersedia":
                                kamar_tersedia.append(item["Kamar"])

                        if not kamar_tersedia:
                            print("Tidak ada kamar tersedia!")
                            input("Enter...")
                            continue

                        print(f"\nKamar tersedia: {kamar_tersedia}")
                        nama_tamu_input = input("\nNama Anda: ").capitalize()  # Ubah ke capitalize untuk konsistensi nama 

                        while True:
                            try:
                                kamar = int(input("Pilih Kamar: "))
                                if kamar not in kamar_tersedia:
                                    print("Kamar tidak tersedia! Coba lagi.")
                                    continue
                                break
                            except ValueError:
                                print("Input harus angka!")

                        while True:
                            try:
                                durasi = int(input("Durasi (hari): "))
                                break
                            except ValueError:
                                print("Input harus angka!")

                        harga_str = get_harga_kamar(kamar)
                        harga_per_malam = int(harga_str)
                        total = durasi * harga_per_malam

                        # Diskon untuk VIP
                        if tipe_akun == "VIP":
                            diskon = total * 0.15
                            total -= diskon
                            print(f"Selamat! Sebagai akun VIP, Anda mendapat diskon 15%: Rp {diskon}")

                        if saldo >= total:
                            saldo -= total
                            money["E-Money"] = saldo
                            saldokostumer(data_kostumer)
                            no = len(data_res) + 1
                            data_res.append({
                                "No": no,
                                "Nama Tamu": nama_tamu_input,
                                "Nomor Kamar": kamar,
                                "Durasi": durasi,
                                "Total Harga": total
                            })
                            update_checklist(kamar, "Ditempati")
                            buat_ubah_hapusdata(data_res)
                            print(f"Saldo Anda sekarang: Rp {saldo}\n")
                            print(f"\nPemesanan berhasil! Total: Rp {total}. Hubungi staff untuk konfirmasi.")
                            struk_harga(nama_tamu_input, kamar, durasi, harga_per_malam, total)
                            input("Enter...")
                            break
                        else:
                            print("Uang Tidak Cukup")
                            input("Enter...")
                            break
            elif pilihan == 2:  # Tambah Saldo
                while True:
                    tambah = int(input("Masukkan jumlah saldo yang ingin ditambah: "))
                    if tambah <= 50000 or tambah > 1000000:  # Validasi: minimal 50K dan maksimal 1jt
                        print("Penambahan Saldo E-Money harus minimal Rp 50000 hingga Rp 1Jt")
                        input("Enter...")
                        continue
                    saldo += tambah
                    money["E-Money"] = saldo
                    saldokostumer(data_kostumer)
                    print("Saldo berhasil ditambahkan!")
                    print(f"Saldo Anda sekarang: Rp {saldo:,}")
                    input("Enter...")
                    break
            elif pilihan == 3:  # Lihat Saldo
                print(f"Saldo Anda: Rp {saldo:,}")
                input("Enter...")
            elif pilihan == 4:  # Kembali ke Login
                log()
            else:
                print("Input invalid!")
                input("Enter...")

        except ValueError:
            print("Input harus angka!")
            input("Enter...")
        except KeyError:
            print("Error Tidak ada di Data")
            input("Enter...")
        except KeyboardInterrupt:
            print("\nProses dibatalkan pengguna.")
            input("Enter...")
            print("Keluar dari sistem...")
        except Exception as e:
            print(f"Terjadi error tak terduga: {e}")
            input("Enter...")

# ====================================================
# =                   Login Sistem                   =
# ====================================================

def log():
    # Fungsi untuk menu login utama (pilih role atau registrasi)
    while True:
        try:
            os.system("cls")
            print("# ====================================================")
            print("# =               Login Sistem                       =")
            print("# ====================================================")
            print("=            1.     Manager                          =")
            print("=            2.     Karyawan                         =")
            print("=            3.     Kostumer                         =")
            print("=            4.     Buat Akun                        =")
            print("=            5.     Keluar                           =")
            print("======================================================")
            pilihan = int(input("Masukkan pilihan: "))
            
            if pilihan == 1:  # Pilih login Manager
                while True:
                    os.system("cls")
                    print("====================================================")
                    print("=                   Login Manager                  =")
                    print("====================================================")
                    print("=           Ketik 'Keluar' Untuk Kembali           =")
                    print("====================================================")
                    sistemlog()
                    break
            elif pilihan == 2:  # Pilih login Karyawan
                while True:
                    os.system("cls")
                    print("====================================================")
                    print("=                   Login Karyawan                 =")
                    print("====================================================")
                    print("=           Ketik 'Keluar' Untuk Kembali           =")
                    print("====================================================")
                    sistemlog()
                    break
            elif pilihan == 3:  # Pilih login Kostumer
                os.system("cls")
                print("====================================================")
                print("=                   Login Kostumer                 =")
                print("====================================================")
                print("=           Ketik 'Keluar' Untuk Kembali           =")
                print("====================================================")
                sistemlog()
                break
            elif pilihan == 4:  # Pilih registrasi akun
                registrasi()
                break
            elif pilihan == 5:  # Keluar dari sistem
                print("Keluar dari sistem...")
                time.sleep(1)
                os._exit(0)
            else:
                print("Input invalid!")
                input("Enter...")
        except ValueError:
            print("Input harus angka!")
            input("Enter...")
        except KeyError:
            print("Error Tidak ada di Data")
            input("Enter...")
        except KeyboardInterrupt:
            print("\nProses dibatalkan pengguna.")
            input("Enter...")
            print("Keluar dari sistem...")
        except Exception as e:
            print(f"Terjadi error tak terduga: {e}")
            input("Enter...")
            
# ====================================================
# =                     Mulai                        =
# ====================================================

log()  # Jalankan fungsi log untuk memulai program