# IF2250-2023-K03-08-MangaTracker

## Nama dan Deskripsi Aplikasi
Aplikasi ini diberi nama Manga Tracker, Aplikasi ini merupakan aplikasi desktop yang digunakan untuk memudahkan pengguna untuk melakukan pencatatan terhadap manga yang dibacanya. Pengguna dapat mengisi informasi mengenai manga yang dibacanya, pengguna juga dapat mengedit atau menambahkan informasi mengenai manga yang dibacanya.Aplikasi ini dibuat untuk M. Farel Darendra R. dan sebagai tugas di mata kuliah IF2250 Rekayasa Perangkat Lunak pada semester genap di tahun akademik 2023/2024.

## Fitur Aplikasi
Aplikasi yang dibuat memiliki fitur-fitur sebagai berikut
1. Menampilkan manga yang dibaca berdasarkan status
2. Menambahkan manga baru ke database
3. Menghapus manga
4. Melakukan pencarian manga berdasarkan judul manga
5. Mengubah detail informasi dari sebuah manga

## Cara Menjalankan Aplikasi
1. Program dijalankan pada sistem operasi Windows. Pastikan sudah memasang compiler Python pada perangkat Anda
2. Pada root folder aplikasi, install dependencies `pip install -r requirements.txt`
3. Pindah ke folder MangaTracker `cd src/MangaTracker`
4. Jalankan program `flet run`

## Daftar Modul yang Diimplementasikan dan Pembagian Tugasnya
1. Modul Menu Utama: Jimly Nur Arif, M. Roihan, Hafizh Ananta Akbari
2. Modul Tambah Manga: M. Roihan,  Jimly Nur Arif, Samy Muhammad Haikal, Rayhan Ridhar Rahman 
3. Modul Lihat Manga: Jimly Nur Arif, M. Roihan
4. Fitur Edit Manga (ubahan manga):  Samy Muhammad Haikal, Jimly Nur Arif, M. Roihan
5. Fitur Unit Testing: Samy Muhammad Haikal, Yosef Rafael Joshua

## Daftar Tabel Basis Data dan Atributnya
1. Manga (
    judul VARCHAR(32) NOT NULL ,
    status ENUM('ongoing','finished','wishlist') NOT NULL,
    chapter INT,
    chapter_count INT NOT NULL,
    added_date DATE,
    last_read DATE,
    personal_notes VARCHAR(100),
    PRIMARY KEY (judul)
);

2. genre_manga (
    judul VARCHAR(32) NOT NULL,
    genre VARCHAR(32) , 
    PRIMARY KEY (judul,genre), 
    FOREIGN KEY (judul) REFERENCES Manga(judul)
)

## Pembuat Aplikasi
| NIM | Nama Lengkap |
| ------ | ---------- |
| 13522123 | Jimly Nur Arif |
| 13522132 | Hafizh Hananta Akbari |
| 13522133 | Yosef Rafael Joshua |
| 13522151 | Samy Muhammad Haikal |
| 13522152 | Muhammad Roihan |
| 13522160 | Rayhan Ridhar Rahman  |

## Ucapan Terima kasih
Puji dan syukur kami panjatkan kepada Tuhan Yang Maha Esa, karena tanpa-Nya, tugas ini tidak dapat diselesaikan. Kepada M. Farel Darendra R. yang telah mendampingi dalam proses asistensi pembuatan dokumen dari aplikasi ini. 