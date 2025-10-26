# 🏨 Hotel Reservation System

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-Educational-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*Sistem Manajemen Reservasi Hotel Modern Berbasis CLI*

</div>

---

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Arsitektur Sistem](#-arsitektur-sistem)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Instalasi](#-instalasi)
- [Struktur Data](#-struktur-data)
- [Panduan Penggunaan](#-panduan-penggunaan)
- [Sistem Harga & Diskon](#-sistem-harga--diskon)
- [Keamanan](#-keamanan)
- [Alur Kerja Sistem](#-alur-kerja-sistem)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)

---

## 🎯 Tentang Proyek

Hotel Reservation System adalah aplikasi manajemen hotel yang komprehensif, dirancang untuk mempermudah operasional hotel dengan sistem berbasis role. Aplikasi ini menyediakan interface yang intuitif untuk mengelola reservasi, ketersediaan kamar, dan transaksi pembayaran melalui sistem E-Money terintegrasi.

### Mengapa Proyek Ini?

- ✅ **Sederhana namun Powerful** - CLI yang mudah digunakan dengan fitur lengkap
- ✅ **Role-Based Access** - Pemisahan hak akses untuk keamanan
- ✅ **Real-time Updates** - Sinkronisasi data instant via JSON
- ✅ **Payment Integration** - Sistem E-Money untuk transaksi mudah
- ✅ **Loyalty Program** - Diskon otomatis untuk member VIP

---

## 🌟 Fitur Utama

### 👔 Manager Dashboard

```
┌─────────────────────────────────────┐
│      MANAGER CONTROL PANEL          │
├─────────────────────────────────────┤
│ ✓ Tambah Reservasi Baru             │
│ ✓ Lihat Semua Reservasi             │
│ ✓ Edit Detail Reservasi             │
│ ✓ Hapus Reservasi                   │
│ ✓ Monitor Ketersediaan Kamar        │
│ ✓ Full System Access                │
└─────────────────────────────────────┘
```

**Kemampuan Manager:**
- Kontrol penuh atas semua reservasi hotel
- Ubah atau batalkan booking kapan saja
- Monitoring real-time status 10 kamar
- Manajemen akses dan audit trail

### 👨‍💼 Karyawan Dashboard

```
┌─────────────────────────────────────┐
│       KARYAWAN PORTAL               │
├─────────────────────────────────────┤
│ ✓ View Reservasi Aktif              │
│ ✓ Cek Status Kamar                  │
│ ✓ Informasi Tamu                    │
│ ✓ Read-Only Access                  │
└─────────────────────────────────────┘
```

**Kemampuan Karyawan:**
- Akses informasi untuk melayani tamu
- Verifikasi ketersediaan kamar
- Bantuan check-in/check-out
- Tidak dapat mengubah data sensitif

### 🎫 Kostumer Portal

```
┌─────────────────────────────────────┐
│       CUSTOMER SELF-SERVICE         │
├─────────────────────────────────────┤
│ 🏠 Pesan Kamar Online               │
│ 💰 Top-up E-Money                   │
│ 💳 Cek Saldo                        │
│ 🎁 Diskon VIP 15%                   │
│ 🧾 Struk Digital Otomatis           │
└─────────────────────────────────────┘
```

**Kemampuan Kostumer:**
- Booking mandiri tanpa perlu staff
- Pembayaran instant via E-Money
- Struk otomatis sebagai bukti
- Program loyalitas VIP

---

## 🏗️ Arsitektur Sistem

### Diagram Alur Data

```
┌─────────────┐
│   User CLI  │ (Interface)
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Python Engine  │ (Logic Layer)
│  - Validasi     │
│  - Kalkulasi    │
│  - Auth         │
└────────┬────────┘
         │
         ▼
┌──────────────────────────────┐
│      JSON Database           │
├──────────────────────────────┤
│ • DataReservasi.json         │
│ • DataCheckList.json         │
│ • DataHarga.json             │
│ • DataManager.json           │
│ • DataKaryawan.json          │
│ • DataKostumer.json          │
└──────────────────────────────┘
```

### Komponen Utama

1. **Authentication Layer** - Sistem login multi-role dengan security
2. **Business Logic** - Perhitungan harga, validasi, dan rules
3. **Data Persistence** - JSON-based storage untuk portabilitas
4. **User Interface** - CLI dengan PrettyTable untuk visualisasi

---

## 💻 Persyaratan Sistem

### Minimum Requirements

| Komponen | Spesifikasi |
|----------|-------------|
| **Python** | 3.7 atau lebih tinggi |
| **RAM** | 512 MB (Recommended: 1 GB) |
| **Storage** | 50 MB ruang kosong |
| **OS** | Windows 7+, Linux, macOS 10.12+ |
| **Terminal** | UTF-8 support untuk tampilan tabel |

### Python Libraries

```
prettytable >= 3.9.0  # Untuk tabel data yang indah
pwinput >= 1.0.3      # Password input tersembunyi
```

---

## 📦 Instalasi

### Langkah 1: Persiapan Environment

```bash
# Clone atau download repository
cd hotel-reservation-system

# Cek versi Python (pastikan 3.7+)
python --version
```

### Langkah 2: Install Dependencies

**Opsi A - Menggunakan pip:**

```bash
pip install prettytable pwinput
```

**Opsi B - Menggunakan requirements.txt:**

Buat file `requirements.txt`:

```text
prettytable==3.9.0
pwinput==1.0.3
```

Kemudian install:

```bash
pip install -r requirements.txt
```

### Langkah 3: Verifikasi Instalasi

```bash
python -c "import prettytable, pwinput; print('✓ Semua library terinstall')"
```

### Langkah 4: Siapkan File JSON

Sistem akan otomatis membuat file JSON jika belum ada, tetapi Anda bisa membuat struktur awal:

**DataCheckList.json** (Status kamar):
```json
[
  {"Kamar": 1, "Status": "Tersedia"},
  {"Kamar": 2, "Status": "Tersedia"},
  {"Kamar": 3, "Status": "Tersedia"},
  {"Kamar": 4, "Status": "Tersedia"},
  {"Kamar": 5, "Status": "Tersedia"},
  {"Kamar": 6, "Status": "Tersedia"},
  {"Kamar": 7, "Status": "Tersedia"},
  {"Kamar": 8, "Status": "Tersedia"},
  {"Kamar": 9, "Status": "Tersedia"},
  {"Kamar": 10, "Status": "Tersedia"}
]
```

**DataHarga.json** (Harga kamar):
```json
[
  {"No": 1, "Kamar": 1, "Lantai": 1, "Harga": "Rp 300.000"},
  {"No": 2, "Kamar": 2, "Lantai": 1, "Harga": "Rp 300.000"},
  {"No": 3, "Kamar": 3, "Lantai": 1, "Harga": "Rp 300.000"},
  {"No": 4, "Kamar": 4, "Lantai": 1, "Harga": "Rp 300.000"},
  {"No": 5, "Kamar": 5, "Lantai": 1, "Harga": "Rp 300.000"},
  {"No": 6, "Kamar": 6, "Lantai": 2, "Harga": "Rp 600.000"},
  {"No": 7, "Kamar": 7, "Lantai": 2, "Harga": "Rp 600.000"},
  {"No": 8, "Kamar": 8, "Lantai": 2, "Harga": "Rp 600.000"},
  {"No": 9, "Kamar": 9, "Lantai": 2, "Harga": "Rp 600.000"},
  {"No": 10, "Kamar": 10, "Lantai": 2, "Harga": "Rp 600.000"}
]
```

---

## 📊 Struktur Data

### Entity Relationship Diagram

```
┌──────────────┐          ┌──────────────┐
│  Reservasi   │          │   CheckList  │
├──────────────┤          ├──────────────┤
│ No           │◄────────►│ Kamar        │
│ Nama Tamu    │          │ Status       │
│ Nomor Kamar  │          └──────────────┘
│ Durasi       │                 │
│ Total Harga  │                 │
└──────────────┘                 │
       │                         │
       │                         │
       ▼                         ▼
┌──────────────┐          ┌──────────────┐
│   Kostumer   │          │    Harga     │
├──────────────┤          ├──────────────┤
│ Username     │          │ No           │
│ Password     │          │ Kamar        │
│ E-Money      │          │ Lantai       │
│ Tipe         │          │ Harga        │
└──────────────┘          └──────────────┘
```

### Detail Struktur Database

#### 1. DataReservasi.json

**Purpose:** Menyimpan semua informasi reservasi aktif

**Schema:**
```json
{
  "No": Integer,           // ID unik reservasi (auto-increment)
  "Nama Tamu": String,     // Nama lengkap tamu
  "Nomor Kamar": Integer,  // 1-10
  "Durasi": Integer,       // Jumlah hari menginap
  "Total Harga": Integer   // Harga total setelah diskon
}
```

**Contoh Data:**
```json
[
  {
    "No": 1,
    "Nama Tamu": "Ahmad Santoso",
    "Nomor Kamar": 3,
    "Durasi": 2,
    "Total Harga": 600000
  },
  {
    "No": 2,
    "Nama Tamu": "Siti Nurhaliza",
    "Nomor Kamar": 7,
    "Durasi": 3,
    "Total Harga": 1800000
  }
]
```

#### 2. DataCheckList.json

**Purpose:** Real-time status ketersediaan kamar

**Schema:**
```json
{
  "Kamar": Integer,       // Nomor kamar (1-10)
  "Status": String        // "Tersedia" atau "Ditempati"
}
```

**Status Flow:**
```
[Tersedia] ─(booking)─> [Ditempati] ─(checkout)─> [Tersedia]
```

#### 3. DataKostumer.json

**Purpose:** Akun dan saldo customer

**Schema:**
```json
{
  "Username": String,     // Unique identifier
  "Password": String,     // Minimum 4 karakter
  "E-Money": Integer,     // Saldo dalam Rupiah
  "Tipe": String         // "VIP" atau "Reguler"
}
```

**Contoh:**
```json
[
  {
    "Username": "john_doe",
    "Password": "pass123",
    "E-Money": 2000000,
    "Tipe": "VIP"
  },
  {
    "Username": "jane_smith",
    "Password": "secure456",
    "E-Money": 500000,
    "Tipe": "Reguler"
  }
]
```

#### 4. DataManager.json & DataKaryawan.json

**Purpose:** Kredensial login staff

**Schema:**
```json
{
  "Username": String,
  "Password": String
}
```

---

## 📖 Panduan Penggunaan

### 🚀 Menjalankan Aplikasi

```bash
# Windows
python main.py

# Linux/macOS
python3 main.py
```

### 1️⃣ Menu Utama

Saat aplikasi dimulai, Anda akan melihat:

```
====================================================
=               Login Sistem                       =
====================================================
=            1.     Manager                        =
=            2.     Karyawan                       =
=            3.     Kostumer                       =
=            4.     Buat Akun                      =
=            5.     Hapus Akun                     =
=            6.     Keluar                         =
====================================================
```

### 2️⃣ Registrasi Akun Baru

**Flow Diagram:**

```
Start
  │
  ▼
Pilih Role ──┬── Manager ──┐
             ├── Karyawan ─┤
             └── Kostumer ─┘
                           │
                           ▼
               Input Username & Password
                           │
                           ▼
          [Kostumer Only] Pilih Tipe
               ┌────────┴────────┐
               │                 │
             VIP             Reguler
               │                 │
               └────────┬────────┘
                        │
                        ▼
                 Akun Dibuat ✓
```

**Langkah-langkah:**

1. Pilih menu **"4. Buat Akun"**
2. Pilih tipe akun (Manager/Karyawan/Kostumer)
3. Masukkan username (akan diubah ke lowercase)
4. Masukkan password (minimal 4 karakter)
5. Khusus Kostumer: Pilih tipe **VIP** atau **Reguler**

**Contoh Interaksi:**

```
Masukkan pilihan: 4

====================================================
=                Registrasi Akun                   =
====================================================
=            1.     Manager                        =
=            2.     Karyawan                       =
=            3.     Kostumer                       =
=            4.     Kembali Halaman Login          =
====================================================
Masukkan pilihan: 3

Masukkan username baru untuk Kostumer: customer123
Masukkan password baru: ****
Pilih tipe akun (VIP/Reguler): vip

✓ Registrasi sukses! Akun Kostumer VIP telah ditambahkan.
```

### 3️⃣ Login Sistem

**Security Flow:**

```
Input Credentials
       │
       ▼
Check Username ─[NOT FOUND]─> Error + Counter++
       │                             │
   [FOUND]                           │
       │                             ▼
       ▼                      [10 attempts?]
Check Password ─[WRONG]──────────────┤
       │                             │
   [CORRECT]                      [YES]
       │                             │
       ▼                             ▼
  Grant Access               Lock Account
```

**Percobaan Login:**

| Percobaan | Penalty |
|-----------|---------|
| 1-2 | Tanpa delay |
| 3, 6, 9 | 30s, 60s, 90s delay |
| 10 | Akun terkunci (exit) |

### 4️⃣ Booking Kamar (Kostumer)

**Complete Booking Flow:**

```
Login Kostumer
      │
      ▼
Pilih "Pesan Kamar"
      │
      ▼
Sistem Tampilkan:
├─ Daftar Harga
├─ Status Kamar
└─ Kamar Tersedia
      │
      ▼
Input Nama Tamu
      │
      ▼
Pilih Nomor Kamar
      │
      ▼
Input Durasi (hari)
      │
      ▼
Sistem Hitung Total
      │
      ├─[VIP]─> Apply Diskon 15%
      │
      ▼
Cek Saldo E-Money
      │
      ├─[Cukup]─────> Proses Pembayaran
      │                      │
      │                      ▼
      │              Update Status Kamar
      │                      │
      │                      ▼
      │              Tampilkan Struk
      │                      │
      │                      ▼
      │              Booking Sukses ✓
      │
      └─[Tidak Cukup]─> Error: Saldo Kurang
```

**Contoh Booking:**

```
====================================================
=              Daftar Harga Kamar                  =
====================================================
┌────┬──────────────┬────────┬──────────────────┐
│ No │ Nomor Kamar  │ Lantai │ Harga per Malam  │
├────┼──────────────┼────────┼──────────────────┤
│ 1  │      1       │   1    │   Rp 300.000     │
│ 2  │      2       │   1    │   Rp 300.000     │
│ .. │     ..       │  ..    │      ..          │
│ 10 │     10       │   2    │   Rp 600.000     │
└────┴──────────────┴────────┴──────────────────┘

Kamar tersedia: [1, 3, 5, 7, 9]

Nama Anda: Budi Santoso
Pilih Kamar: 7
Durasi (hari): 3

[VIP Member Detected]
Harga Normal: Rp 1.800.000
Diskon 15%: Rp 270.000
─────────────────────────────
Total Bayar: Rp 1.530.000

Saldo Anda: Rp 2.000.000
Sisa Saldo: Rp 470.000

✓ Pemesanan berhasil!
```

### 5️⃣ Manajemen Reservasi (Manager)

**CRUD Operations:**

#### CREATE - Tambah Reservasi

```python
# Input:
nama_tamu = "Sarah Johnson"
kamar = 5          # Lantai 1
durasi = 4         # hari

# Kalkulasi:
harga_per_malam = 300000
total = 4 × 300000 = 1200000

# Output:
reservasi_baru = {
    "No": 1,
    "Nama Tamu": "Sarah Johnson",
    "Nomor Kamar": 5,
    "Durasi": 4,
    "Total Harga": 1200000
}
```

#### READ - Lihat Reservasi

```
====================================================
=           Daftar Reservasi Hotel                 =
====================================================
┌────┬─────────────────┬──────────────┬──────────┬──────────────┐
│ No │   Nama Tamu     │ Nomor Kamar  │  Durasi  │ Total Harga  │
├────┼─────────────────┼──────────────┼──────────┼──────────────┤
│ 1  │ Ahmad Santoso   │      3       │  2 hari  │  Rp 600.000  │
│ 2  │ Siti Nurhaliza  │      7       │  3 hari  │ Rp 1.800.000 │
│ 3  │ Budi Prasetyo   │      2       │  1 hari  │  Rp 300.000  │
└────┴─────────────────┴──────────────┴──────────┴──────────────┘
```

#### UPDATE - Ubah Reservasi

```
Scenario: Perpanjangan durasi menginap

Before:
- Durasi: 2 hari
- Total: Rp 600.000

Manager Input:
- Durasi baru: 5 hari

After:
- Durasi: 5 hari
- Total: Rp 1.500.000 (recalculated)
- Status: "Reservasi diubah!"
```

#### DELETE - Hapus Reservasi

```
Process Flow:
1. Tampilkan daftar reservasi
2. Manager pilih No reservasi
3. Sistem hapus data
4. Update status kamar → "Tersedia"
5. Reindex nomor reservasi
```

### 6️⃣ E-Money Management

**Top-up Process:**

```
Current Balance: Rp 500.000
                    │
                    ▼
         Input Jumlah Top-up
                    │
         ┌──────────┴──────────┐
         │                     │
    [< Rp 50K]           [> Rp 1Jt]
         │                     │
      ERROR               ERROR
         │                     │
         └──────────┬──────────┘
                    │
            [Rp 50K - 1Jt]
                    │
                    ▼
         Update Saldo + Save
                    │
                    ▼
    New Balance: Rp 500K + Top-up
```

**Validasi:**
- Minimum top-up: **Rp 50.000**
- Maximum top-up: **Rp 1.000.000**
- Saldo tidak ada batas maksimum

---

## 💰 Sistem Harga & Diskon

### Layout Hotel

```
┌─────────────────────────────────────────┐
│            LANTAI 2 (Premium)           │
│    Harga: Rp 600.000/malam              │
├─────┬─────┬─────┬─────┬─────┐           │
│  6  │  7  │  8  │  9  │ 10  │           │
└─────┴─────┴─────┴─────┴─────┘           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│            LANTAI 1 (Standard)          │
│    Harga: Rp 300.000/malam              │
├─────┬─────┬─────┬─────┬─────┐           │
│  1  │  2  │  3  │  4  │  5  │           │
└─────┴─────┴─────┴─────┴─────┘           │
└─────────────────────────────────────────┘
```

### Kalkulasi Harga

**Formula:**
```
Total = Harga_Per_Malam × Durasi × (1 - Diskon)
```

**Tabel Perhitungan:**

| Kamar | Lantai | Harga/Malam | Durasi | Tipe | Diskon | Total |
|-------|--------|-------------|--------|------|--------|-------|
| 3 | 1 | Rp 300K | 2 hari | Reguler | 0% | **Rp 600K** |
| 3 | 1 | Rp 300K | 2 hari | VIP | 15% | **Rp 510K** |
| 8 | 2 | Rp 600K | 3 hari | Reguler | 0% | **Rp 1.8Jt** |
| 8 | 2 | Rp 600K | 3 hari | VIP | 15% | **Rp 1.53Jt** |

### Program VIP

**Benefit VIP Member:**

```
┌────────────────────────────────────┐
│         VIP MEMBERSHIP             │
├────────────────────────────────────┤
│ ✓ Diskon 15% setiap booking        │
│ ✓ Berlaku untuk semua tipe kamar   │
│ ✓ Tidak ada minimum pembelian      │
│ ✓ Diskon otomatis teraplikasi      │
└────────────────────────────────────┘
```

**Contoh Penghematan:**

```
Booking 1:
- Kamar: 10 (Premium)
- Durasi: 5 hari
- Reguler: Rp 3.000.000
- VIP: Rp 2.550.000
- HEMAT: Rp 450.000 💰

Booking 2:
- Kamar: 3 (Standard)
- Durasi: 7 hari
- Reguler: Rp 2.100.000
- VIP: Rp 1.785.000
- HEMAT: Rp 315.000 💰
```

---

## 🔒 Keamanan

### Multi-Layer Security

```
┌────────────────────────────────────────┐
│      LAYER 1: Authentication           │
│  - Username/Password validation        │
│  - Case-insensitive login              │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│      LAYER 2: Password Security        │
│  - Hidden input (pwinput)              │
│  - Minimum 4 characters                │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│      LAYER 3: Brute Force Protection   │
│  - Max 10 login attempts               │
│  - Progressive delays (30s/60s/90s)    │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│      LAYER 4: Admin Protection         │
│  - Admin password untuk hapus akun     │
│  - Password: "unmul123"                │
└────────────────────────────────────────┘
```

### Login Security Timeline

```
Attempt 1-2:  Instant retry
    ↓
Attempt 3:    Wait 30 seconds ⏱️
    ↓
Attempt 4-5:  Instant retry
    ↓
Attempt 6:    Wait 60 seconds ⏱️⏱️
    ↓
Attempt 7-8:  Instant retry
    ↓
Attempt 9:    Wait 90 seconds ⏱️⏱️⏱️
    ↓
Attempt 10:   ACCOUNT LOCKED 🔒
```

### Data Security

**JSON File Protection:**

```python
# Contoh Exception Handling
try:
    with open("DataReservasi.json", "r") as file:
        return json.load(file)
except FileNotFoundError:
    # Buat file baru jika hilang
    return []
except json.JSONDecodeError:
    # Handle file corrupt
    print("File rusak, restore backup")
    return []
```

---

## 🔄 Alur Kerja Sistem

### Complete System Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     APPLICATION START                        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
              ┌──────────────────┐
              │   Main Menu      │
              └────────┬─────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
    ┌────────┐   ┌──────────┐  ┌──────────┐
    │Manager │   │Karyawan  │  │Kostumer  │
    └───┬────┘   └────┬─────┘  └────┬─────┘
        │             │             │
        │             │             ▼
        │             │      ┌──────────────┐
        │             │      │ E-Money Mgmt │
        │             │      └──────┬───────┘
        │             │             │
        ▼             ▼             ▼
    ┌─────────────────────────────────┐
    │      Reservation System         │
    ├─────────────────────────────────┤
    │ • Create Booking                │
    │ • View Rooms                    │
    │ • Update Data                   │
    │ • Generate Receipt              │
    └────────────┬────────────────────┘
                 │
                 ▼
        ┌────────────────┐
        │  JSON Storage  │
        │  Auto-sync     │
        └────────────────┘
```

### Booking Workflow Detail

```
START
  │
  ├─→ [Manager/Karyawan Path]
  │   │
  │   ├─→ Manual Input
  │   ├─→ Select Room
  │   ├─→ Set Duration
  │   └─→ Save Reservation
  │
  └─→ [Kostumer Path]
      │
      ├─→ Check Balance
      │   └─→ [Insufficient] → Top-up → Retry
      │
      ├─→ Select Room
      │   └─→ View Prices & Availability
      │
      ├─→ Calculate Total
      │   └─→ [VIP] → Apply 15% Discount
      │
      ├─→ Process Payment
      │   ├─→ Deduct Balance
      │   └─→ Update Room Status
      │
      ├─→ Generate Receipt
      │
      └─→ Confirmation ✓
```

---

## 🐍 Penjelasan Program Python

### Struktur Kode Keseluruhan

Program ini terdiri dari beberapa komponen utama yang saling terintegrasi:

```
main.py
├── Import Libraries (baris 1-8)
├── Fungsi JSON Operations (baris 10-150)
│   ├── DataReservasi
│   ├── DataCheckList
│   ├── DataHarga
│   ├── DataKaryawan
│   ├── DataManager
│   └── DataKostumer
├── Fungsi Tampilan Tabel (baris 152-200)
├── Fungsi Utilitas (baris 202-280)
├── Fungsi Login & Registrasi (baris 282-450)
├── Menu Sistem (baris 452-700)
└── Main Execution (baris 702)
```

### 1. Import Libraries

```python
import os  # Untuk operasi sistem seperti clear screen
from prettytable import PrettyTable  # Untuk membuat tabel tampilan data
import pwinput  # Untuk input password yang tersembunyi
import json  # Untuk membaca dan menulis file JSON
import time  # Untuk delay waktu
from datetime import date  # Untuk mendapatkan tanggal saat ini
```

**Penjelasan Detail:**

| Library | Fungsi Utama | Contoh Penggunaan |
|---------|--------------|-------------------|
| `os` | Operasi sistem operasi | `os.system("cls")` - clear screen Windows |
| `prettytable` | Membuat tabel ASCII art | Menampilkan data reservasi dalam format tabel |
| `pwinput` | Input password tersembunyi | `pwinput.pwinput("Password: ")` - input tanpa echo |
| `json` | Parse dan serialize JSON | `json.load()`, `json.dump()` |
| `time` | Fungsi waktu dan delay | `time.sleep(30)` - delay 30 detik |
| `datetime.date` | Tanggal untuk struk | `date.today()` - tanggal hari ini |

---

### 2. Fungsi-Fungsi JSON Operations

#### A. Fungsi untuk DataReservasi.json

**📝 buat_ubah_hapusdata(data)**

```python
def buat_ubah_hapusdata(data):
    with open("DataReservasi.json", "w") as file:
        json.dump(data, file, indent=4)
```

**Cara Kerja:**
1. Menerima parameter `data` (list of dictionaries)
2. Membuka file `DataReservasi.json` dalam mode write
3. Menulis data ke file dengan format JSON yang rapi (indent=4)
4. File otomatis tertutup setelah selesai

**Contoh Penggunaan:**
```python
# Data reservasi baru
reservasi = [
    {
        "No": 1,
        "Nama Tamu": "John Doe",
        "Nomor Kamar": 5,
        "Durasi": 3,
        "Total Harga": 900000
    }
]

# Simpan ke file
buat_ubah_hapusdata(reservasi)

# File DataReservasi.json akan berisi:
# [
#     {
#         "No": 1,
#         "Nama Tamu": "John Doe",
#         "Nomor Kamar": 5,
#         "Durasi": 3,
#         "Total Harga": 900000
#     }
# ]
```

**📖 baca_reservasi()**

```python
def baca_reservasi():
    try:
        with open("DataReservasi.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataReservasi.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []
```

**Cara Kerja:**
1. Mencoba membuka dan membaca file JSON
2. Jika file tidak ada → return list kosong `[]`
3. Jika file corrupt/invalid JSON → return list kosong `[]`
4. Jika sukses → return data sebagai Python list

**Flow Diagram:**
```
baca_reservasi()
      │
      ▼
Buka file "DataReservasi.json"
      │
      ├─[File Exists]──→ Parse JSON ──→ Return data
      │
      ├─[File Not Found]──→ Print warning ──→ Return []
      │
      └─[JSON Error]──→ Print error ──→ Return []
```

#### B. Fungsi untuk DataCheckList.json

**🔍 baca_checklist()**

```python
def baca_checklist():
    try:
        with open("DataCheckList.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataCheckList.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []
```

**Struktur Data yang Dibaca:**
```json
[
  {"Kamar": 1, "Status": "Tersedia"},
  {"Kamar": 2, "Status": "Ditempati"},
  {"Kamar": 3, "Status": "Tersedia"}
]
```

**✏️ update_checklist(kamar, status)**

```python
def update_checklist(kamar, status):
    data = baca_checklist()
    for item in data:
        if item["Kamar"] == int(kamar):
            item["Status"] = status
            break
    with open("DataCheckList.json", "w") as file:
        json.dump(data, file, indent=4)
```

**Cara Kerja Step-by-Step:**

```python
# Contoh: Update kamar 5 menjadi "Ditempati"
update_checklist(5, "Ditempati")

# Step 1: Baca data saat ini
data = [
    {"Kamar": 1, "Status": "Tersedia"},
    {"Kamar": 5, "Status": "Tersedia"},  # ← Target
    {"Kamar": 10, "Status": "Ditempati"}
]

# Step 2: Loop dan cari kamar yang sesuai
for item in data:
    if item["Kamar"] == 5:  # Ketemu!
        item["Status"] = "Ditempati"  # Update status
        break  # Keluar dari loop

# Step 3: Data setelah update
data = [
    {"Kamar": 1, "Status": "Tersedia"},
    {"Kamar": 5, "Status": "Ditempati"},  # ✓ Berubah
    {"Kamar": 10, "Status": "Ditempati"}
]

# Step 4: Simpan kembali ke file
```

**Visualisasi:**
```
Before:
┌────────┬───────────┐
│ Kamar  │  Status   │
├────────┼───────────┤
│   5    │ Tersedia  │ ← Update this
└────────┴───────────┘

After:
┌────────┬───────────┐
│ Kamar  │  Status   │
├────────┼───────────┤
│   5    │ Ditempati │ ✓
└────────┴───────────┘
```

#### C. Fungsi untuk DataHarga.json

**💵 get_harga_kamar(kamar)**

```python
def get_harga_kamar(kamar):
    if 1 <= kamar <= 5:
        return 300000
    elif 6 <= kamar <= 10:
        return 600000
    else:
        return None
```

**Logic Tree:**
```
Input: kamar = ?
        │
        ├─[1 ≤ kamar ≤ 5]──→ Return 300000 (Lantai 1)
        │
        ├─[6 ≤ kamar ≤ 10]──→ Return 600000 (Lantai 2)
        │
        └─[Lainnya]──→ Return None (Invalid)
```

**Contoh:**
```python
harga_1 = get_harga_kamar(3)   # 300000 (Lantai 1)
harga_2 = get_harga_kamar(8)   # 600000 (Lantai 2)
harga_3 = get_harga_kamar(15)  # None (Invalid)

# Perhitungan booking
durasi = 4
kamar = 7
total = durasi * get_harga_kamar(kamar)
# total = 4 * 600000 = 2400000
```

#### D. Fungsi untuk Login Systems

**🔐 loginkaryawan(), loginmanager(), loginkostumer()**

Ketiga fungsi ini memiliki struktur yang sama:

```python
def loginkaryawan():
    try:
        with open("DataKaryawan.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File DataKaryawan.json tidak ditemukan. Membuat file kosong.")
        return []
    except json.JSONDecodeError:
        print("Error membaca JSON.")
        return []
```

**Return Format:**
```python
# loginmanager() returns:
[
    {"Username": "admin1", "Password": "pass123"},
    {"Username": "admin2", "Password": "secure456"}
]

# loginkaryawan() returns:
[
    {"Username": "staff1", "Password": "staff123"},
    {"Username": "staff2", "Password": "staff456"}
]

# loginkostumer() returns:
[
    {
        "Username": "customer1",
        "Password": "cust123",
        "E-Money": 1000000,
        "Tipe": "VIP"
    },
    {
        "Username": "customer2",
        "Password": "cust456",
        "E-Money": 500000,
        "Tipe": "Reguler"
    }
]
```

---

### 3. Fungsi Tampilan dengan PrettyTable

#### 📊 tabel_reservasi()

```python
def tabel_reservasi():
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
```

**Cara Kerja:**

**Step 1 - Baca Data:**
```python
data = [
    {"No": 1, "Nama Tamu": "John", "Nomor Kamar": 3, "Durasi": 2, "Total Harga": 600000},
    {"No": 2, "Nama Tamu": "Jane", "Nomor Kamar": 7, "Durasi": 3, "Total Harga": 1800000}
]
```

**Step 2 - Buat Tabel:**
```python
tabel = PrettyTable()
tabel.title = "Daftar Reservasi Hotel"
tabel.field_names = ["No", "Nama Tamu", "Nomor Kamar", "Durasi (hari)", "Total Harga"]
```

**Step 3 - Tambah Rows:**
```python
# Loop pertama
tabel.add_row([1, "John", 3, 2, "Rp 600,000"])

# Loop kedua
tabel.add_row([2, "Jane", 7, 3, "Rp 1,800,000"])
```

**Step 4 - Output:**
```
+-----------------------------+
|  Daftar Reservasi Hotel     |
+----+------------+-------------+----------+--------------+
| No | Nama Tamu  | Nomor Kamar | Durasi   | Total Harga  |
+----+------------+-------------+----------+--------------+
| 1  | John       |      3      | 2 hari   | Rp 600,000   |
| 2  | Jane       |      7      | 3 hari   | Rp 1,800,000 |
+----+------------+-------------+----------+--------------+
```

**Format Number dengan Koma:**
```python
# Formatting rupiah dengan pemisah ribuan
harga = 1800000
formatted = f"Rp {harga:,}"  # "Rp 1,800,000"

# Breakdown:
# f"..." → f-string (formatted string)
# {harga:,} → format dengan koma sebagai thousand separator
```

#### 🏨 tabel_checklist()

```python
def tabel_checklist():
    data = baca_checklist()
    tabel = PrettyTable()
    tabel.title = "Status Kamar"
    tabel.field_names = ["Kamar", "Status"]
    for item in data:
        tabel.add_row([item["Kamar"], item["Status"]])
    print(tabel)
```

**Output Example:**
```
+----------------+
|  Status Kamar  |
+-------+----------+
| Kamar | Status   |
+-------+----------+
|   1   | Tersedia |
|   2   | Ditempati|
|   3   | Tersedia |
|   4   | Tersedia |
|   5   | Ditempati|
|   6   | Tersedia |
|   7   | Ditempati|
|   8   | Tersedia |
|   9   | Tersedia |
|  10   | Ditempati|
+-------+----------+
```

---

### 4. Sistem Login dan Autentikasi

#### 🔑 sistemlog()

Ini adalah fungsi login utama dengan security features:

```python
def sistemlog():
    percobaan = 0
    while True:
        try:
            data1 = loginmanager()     # Baca data manager
            data2 = loginkaryawan()    # Baca data karyawan
            data3 = loginkostumer()    # Baca data kostumer
            
            nama = input("Username: ").lower()
            if nama == "keluar":
                break
                
            password = pwinput.pwinput("Password: ").lower()
            if password == "keluar":
                break
            
            # Cek login untuk Manager
            for item in data1:   
                if nama == item["Username"].lower() and password == item["Password"].lower():
                    print("\nLogin sukses!")
                    input("Enter...")
                    menu("Manager")
                    return
            
            # Cek login untuk Karyawan
            for item in data2:
                if nama == item["Username"].lower() and password == item["Password"].lower():
                    print("\nLogin sukses!")
                    input("Enter...")
                    menu("Karyawan")
                    return
            
            # Cek login untuk Kostumer
            for item in data3:
                if nama == item["Username"].lower() and password == item["Password"].lower():
                    print("\nLogin sukses!")
                    input("Enter...")
                    menukostumer(nama)
                    return

            # Login gagal
            percobaan += 1
            print(f"\nUsername atau password salah! (Percobaan {percobaan}/10)")
            
            # Progressive delay
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
```

**Flow Diagram Detail:**

```
START sistemlog()
        │
        ▼
  Inisialisasi percobaan = 0
        │
        ▼
  ┌─────────────────┐
  │  LOOP FOREVER   │
  └────────┬────────┘
           │
           ▼
  Baca semua data JSON
  (Manager, Karyawan, Kostumer)
           │
           ▼
  Input Username (lowercase)
           │
           ├─[username == "keluar"]──→ BREAK
           │
           ▼
  Input Password (hidden, lowercase)
           │
           ├─[password == "keluar"]──→ BREAK
           │
           ▼
  ┌───────────────────────────────┐
  │   Cek di data1 (Manager)      │
  ├───────────────────────────────┤
  │ Loop setiap item:             │
  │   if username & password match│
  │      → menu("Manager")        │
  │      → RETURN                 │
  └───────────┬───────────────────┘
              │ [Not Found]
              ▼
  ┌───────────────────────────────┐
  │   Cek di data2 (Karyawan)     │
  ├───────────────────────────────┤
  │ Loop setiap item:             │
  │   if username & password match│
  │      → menu("Karyawan")       │
  │      → RETURN                 │
  └───────────┬───────────────────┘
              │ [Not Found]
              ▼
  ┌───────────────────────────────┐
  │   Cek di data3 (Kostumer)     │
  ├───────────────────────────────┤
  │ Loop setiap item:             │
  │   if username & password match│
  │      → menukostumer(nama)     │
  │      → RETURN                 │
  └───────────┬───────────────────┘
              │ [Not Found]
              ▼
     percobaan += 1
     Print error message
              │
              ▼
     ┌──────────────────┐
     │  Cek percobaan   │
     └────────┬─────────┘
              │
              ├─[== 10]──→ Lock & Exit
              ├─[% 9 == 0]──→ Sleep 90s
              ├─[% 6 == 0]──→ Sleep 60s
              ├─[% 3 == 0]──→ Sleep 30s
              └─[Lainnya]──→ Continue
              │
              └──────→ LOOP KEMBALI
```

**Contoh Login Matching:**

```python
# Data Manager
data1 = [
    {"Username": "admin", "Password": "admin123"}
]

# User input
nama = "ADMIN"  # ← Note: uppercase
password = "Admin123"  # ← Note: mixed case

# Konversi ke lowercase
nama = nama.lower()  # "admin"
password = password.lower()  # "admin123"

# Matching
for item in data1:
    if "admin" == item["Username"].lower() and "admin123" == item["Password"].lower():
        # ✓ MATCH!
        menu("Manager")
        return
```

**Progressive Delay Logic:**

```python
# Contoh skenario
percobaan = 1  # 1 % 3 = 1 → No delay
percobaan = 2  # 2 % 3 = 2 → No delay
percobaan = 3  # 3 % 3 = 0 → Sleep 30s ⏱️
percobaan = 4  # 4 % 3 = 1 → No delay
percobaan = 5  # 5 % 3 = 2 → No delay
percobaan = 6  # 6 % 6 = 0 → Sleep 60s ⏱️⏱️
percobaan = 7  # 7 % 3 = 1 → No delay
percobaan = 8  # 8 % 3 = 2 → No delay
percobaan = 9  # 9 % 9 = 0 → Sleep 90s ⏱️⏱️⏱️
percobaan = 10 # → LOCKED! 🔒
```

---

### 5. Fungsi Menu Utama

#### 🎛️ menu(role)

Fungsi ini menampilkan menu berdasarkan role user:

```python
def menu(role):
    while True:
        os.system("cls")
        print("====================================================")
        print("=              Sistem Reservasi Hotel              =")
        print("====================================================")
        
        if role == "Manager":
            print("=            1.     Tambah Reservasi               =")           
            print("=            2.     Lihat Reservasi                =")
            print("=            3.     Ubah Reservasi                 =")
            print("=            4.     Hapus Reservasi                =")
            print("=            5.     Lihat Ketersediaan Kamar       =")
            print("=            6.     Kembali Halaman Login          =")
            
        elif role == "Karyawan":
            print("=            1.     Lihat Reservasi                =")
            print("=            2.     Lihat Ketersediaan Kamar       =")
            print("=            3.     Kembali Halaman Login          =")
```

**Contoh Operasi: Tambah Reservasi (Manager)**

```python
if pilihan == 1:  # Tambah Reservasi
    # Step 1: Cek kapasitas
    if len(data) >= 10:
        print("\nMaaf, semua kamar penuh (maksimal 10).")
        input("Enter untuk lanjut...")
        continue
    
    # Step 2: Ambil daftar kamar tersedia
    checklist = baca_checklist()
    kamar_tersedia = []
    for item in checklist:
        if item["Status"] == "Tersedia":
            kamar_tersedia.append(item["Kamar"])
    
    # Step 3: Validasi ketersediaan
    if not kamar_tersedia:
        print("\nTidak ada kamar tersedia.")
        input("Enter untuk lanjut...")
        continue
    
    # Step 4: Input data tamu
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
    
    # Step 5: Kalkulasi harga
    harga_per_malam = get_harga_kamar(kamar)
    total = durasi * harga_per_malam
    
    # Step 6: Simpan reservasi
    no = len(data) + 1
    data.append({
        "No": no,
        "Nama Tamu": nama_tamu,
        "Nomor Kamar": kamar,
        "Durasi": durasi,
        "Total Harga": total
    })
    
    # Step 7: Update status kamar
    update_checklist(kamar, "Ditempati")
    
    # Step 8: Simpan ke file
    buat_ubah_hapusdata(data)
    
    print(f"\nReservasi berhasil! Total: Rp {total:,}")
```

**Visualisasi Proses:**

```
┌──────────────────────────────────────┐
│  TAMBAH RESERVASI - FLOW DIAGRAM     │
└──────────────────────────────────────┘

1. Cek Kapasitas
   ├─ [Full (10/10)]──→ Error: Hotel Penuh
   └─ [Available]──→ Lanjut

2. Load Kamar Tersedia
   DataCheckList.json
   ├─ Kamar 1: Tersedia   ✓
   ├─ Kamar 2: Ditempati  ✗
   ├─ Kamar 3: Tersedia   ✓
   └─ → kamar_tersedia = [1, 3, ...]

3. Input & Validasi
   ┌─────────────────────┐
   │ Nama: "John Doe"    │
   │ Kamar: 3            │ ← Harus dari list tersedia
   │ Durasi: 2 hari      │
   └─────────────────────┘

4. Kalkulasi
   kamar = 3 (Lantai 1)
   harga_per_malam = 300000
   durasi = 2
   ────────────────────────
   total = 2 × 300000 = 600000

5. Simpan Data
   data.append({
     "No": 1,
     "Nama Tamu": "John Doe",
     "Nomor Kamar": 3,
     "Durasi": 2,
     "Total Harga": 600000
   })

6. Update Status
   Kamar 3: Tersedia → Ditempati

7. Write to JSON
   DataReservasi.json ✓
   DataCheckList.json ✓
```

---

### 6. Menu Kostumer dengan E-Money

#### 💳 menukostumer(nama_tamu)

```python
def menukostumer(nama_tamu):
    data_kostumer = loginkostumer()
    money = {"E-Money": 0, "Tipe": "Reguler"}
    
    # Load saldo user
    for item in data_kostumer:
        if item["Username"] == nama_tamu:
            money["E-Money"] = item["E-Money"]
            money["Tipe"] = item.get("Tipe", "Reguler")
            break
    
    saldo = money["E-Money"]
    tipe_akun = money["Tipe"]
```

**Contoh Proses Booking dengan VIP Discount:**

```python
# Scenario: VIP user booking kamar premium
nama_tamu_input = "Jane Doe"
kamar = 8  # Lantai 2
durasi = 3
tipe_akun = "VIP"
saldo = 2000000

# Kalkulasi dasar
harga_per_malam = get_harga_kamar(kamar)  # 600000
total = durasi * harga_per_malam  # 3 × 600000 = 1800000

# Apply diskon VIP
if tipe_akun == "VIP":
    diskon = total * 0.15  # 1800000 × 0.15 = 270000
    total -= diskon  # 1800000 - 270000 = 1530000
    print(f"Diskon 15%: Rp {diskon:,}")  # "Diskon 15%: Rp 270,000"

# Validasi saldo
if saldo >= total:  # 2000000 >= 1530000 ✓
    saldo -= total  # 2000000 - 1530000 = 470000
    money["E-Money"] = saldo
    
    # Update ke file
    saldokostumer(data_kostumer)
    
    # Buat reservasi
    no = len(data_res) + 1
    data_res.append({
        "No": no,
        "Nama Tamu": nama_tamu_input,
        "Nomor Kamar": kamar,
        "Durasi": durasi,
        "Total Harga": total
    })
    
    # Update status kamar
    update_checklist(kamar, "Ditempati")
    
    # Simpan reservasi
    buat_ubah_hapusdata(data_res)
    
    # Tampilkan struk
    struk_harga(nama_tamu_input, kamar, durasi, harga_per_malam, total)
```

**Flow dengan Decision Tree:**

```
START Booking
      │
      ▼
Check Saldo: Rp 2.000.000
      │
      ▼
Select Kamar 8 (Premium)
Durasi: 3 hari
      │
      ▼
Calculate Base Price
3 × Rp 600.000 = Rp 1.800.000
      │
      ▼
Check Tipe Akun
      │
      ├─[Reguler]──→ Total = Rp 1.800.000
      │
      └─[VIP]──┐
               ▼
         Apply Diskon 15%
         Rp 1.800.000 × 0.15 = Rp 270.000
               │
               ▼
         Total = Rp 1.530.000 💰
               │
               ▼
         Check Saldo >= Total
               │
               ├─[NO]──→ Error: Saldo Kurang
               │
               └─[YES]──┐
                        ▼
                  Deduct Balance
                  Rp 2.000.000 - Rp 1.530.000
                  = Rp 470.000
                        │
                        ▼
                  Save Reservation
                        │
                        ▼
                  Update Room Status
                  Kamar 8: Tersedia → Ditempati
                        │
                        ▼
                  Generate Receipt
                        │
                        ▼
                  BOOKING SUCCESS ✓
```

---

### 7. Struk Pembelian

#### 🧾 struk_harga()

```python
def struk_harga(nama_tamu, kamar, durasi, harga_per_malam, total):
    os.system("cls")
    tanggal = date.today()
    lantai = 1 if kamar <= 5 else 2
    
    print("====================================================")
    print("=                Pembelian
