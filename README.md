# Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis Divide and Conquer
> Tugas Kecil IF2211 Strategi Algoritma
> 
> Oleh:<br>
> 1. 13522061 Maximilian Sulistiyo<br>
> 2. 13522088 Muhamad Rafli Rasyiidin<br>
> 
> Sekolah Teknik Elektro dan Informatika<br>
> Institut Teknologi Bandung<br>
> Semester IV Tahun 2023/2024

## Table of Contents
* [Deskripsi Singkat](#deskripsi-singkat)
* [Deskripsi Permasalahan](#deskripsi-permasalahan)
* [Libraries Used](#libraries-used)
* [Setup](#setup)
* [Usage](#usage)
* [Links](#links)
<!-- * [License](#license) -->


## Deskripsi Singkat
Pada tugas kecil ini kami ditugaskan untuk membuat kurva bezier menggunakan strategi Divide and Conquer. Dalam penyelesaian masalah ini digunakan bahasa python. Program ini menerima input jumlah titik kontrol, titik kontrol sejumlah yang sudah diinput, dan juga iterasi yang diinginkan. Kemudian program ini secara otomatis menampilkan hasil akhir dari kurva bezier yang diminta.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Deskripsi Permasalahan
Kurva Bézier merupakan kurva yang sering digunakan dalam desain grafis, animasi, dan manufaktur. Dalam pembuatannya kurva ini memiliki N titik kontrol dimana setiap titik kontrol akan dihubungkan dengan sebuah kurva. Untuk pembentukannya kurva bézier dapat menggunakan sebuah persamaan parametrik, namun seiring bertambahnya titik maka persamaan pun semakin panjang dan kompleks. Oleh karena itu dibutuhkan solusi lain, dalam hal ini menggunakan algoritma Divide and Conquer, dengan harapan akan memiliki efisiensi yang lebih baik.


## Libraries Used
Berikut adalah library yang dipakai
- matplotlib            3.8.1
- tkinter               8.6.12
- numpy                 1.26.4
- time
- math


## Setup
Pastikan seluruh library yang dipakai sudah ter-install dalam device anda. Jikabelum maka anda dapat meng-install nya dengan cara run command di bawah ini

```shell
pip install -r src/requirements.txt
```


## Usage
Untuk menjalankan program maka anda memiliki dua pilihan:
- Menggunakan CLI : Cara ini **DISARANKAN** untuk iterasi yang berjumlah banyak. Cara run program berbasis CLI maka anda cukup menjalankan command di bawah di root directory project ini

```shell
python src/main.py
```

-Menggunakan GUI : Cara ini dapat digunakan agar mempermudah visualisasi input dan juga plot. Cara run program berbasis GUI maka anda cukup menjalankan command di bawah di root directory project ini

```shell
python src/gui.py
```

## Links
- [Spesifikasi Tugas Kecil 2 IF2211 Strategi Algoritma 2023/2024](https://docs.google.com/document/d/161qTQR5PzjQUIsoLO00A0Rp1dvsahrXY2Dk-fSmJl2o/edit).
- [Laporan [email std]](https://docs.google.com/document/d/1vaaxxt-4EWhpEPAtTjvysETvmU4RrV2bjP1D0OY8O9o/edit)