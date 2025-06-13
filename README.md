# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan berhasil mencetak banyak lulusan berkualitas. Namun, dalam beberapa tahun terakhir, tingkat siswa yang tidak menyelesaikan pendidikannya (dropout) mengalami peningkatan yang signifikan.

Tingginya tingkat dropout menjadi tantangan besar karena dapat mencoreng reputasi institusi dan berdampak pada akreditasi serta kepercayaan publik. Oleh karena itu, institusi memiliki kebutuhan untuk mendeteksi secara dini siswa yang berpotensi dropout, sehingga dapat diberikan intervensi tepat waktu.

Untuk mendukung upaya tersebut, dilakukan analisis data untuk mengidentifikasi faktor-faktor utama yang berkontribusi terhadap dropout. Selain itu, dashboard visual juga dikembangkan untuk memudahkan pemantauan dan pengambilan keputusan berbasis data oleh pihak manajemen.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi masalah serius berupa meningkatnya jumlah siswa yang tidak menyelesaikan pendidikan (dropout). Fenomena ini berdampak negatif terhadap reputasi, akreditasi, serta target kelulusan institusi.

Jika tidak segera ditangani, kondisi ini dapat menurunkan kepercayaan masyarakat, menyebabkan kerugian finansial, serta menghambat pencapaian indikator kinerja institusi. Oleh karena itu, penting untuk memahami karakteristik dan faktor-faktor yang menyebabkan dropout agar dapat dilakukan tindakan preventif dan perbaikan sistem secara menyeluruh.

### Cakupan Proyek
#### Analisis dan Prediksi Employee Attrition dengan Python dan Google Looker Studio

##### Tujuan:
Membangun sistem analisis menyeluruh untuk memahami faktor-faktor yang memengaruhi tingkat dropout siswa dan membuat model prediksi apakah seorang siswa menyelesaikan pendidikannya atau tidak. Hasil akhir divisualisasikan dalam dashboard interaktif menggunakan Google Looker Studio.

##### Cakupan Proyek:
1.Data Understanding
Membaca dataset data.csv
Memahami struktur data 
melakukan pengecekan awal data seperti null & duplicate

2.Data Preparation / Preprocessing
Membaca dataset data.csv

Membersihkan data:
Menghapus baris yang tidak perlu
Encoding variabel kategorikal (Label encoding)
Feature selection

Eksplorasi data awal (EDA):
Distribusi data Status
Korelasi fitur terhadap Status
Melihat jumlah dropout tiap jurusan
Distribusi usia masuk berdasarkan status (BoxPlot)
Distribusi faktor ekonomi berdasarkan status

3.Modeling: Predictive Machine Learning
Menentukan target: apakah Dropout/Graduated

Model yang digunakan:
Random Forest

Splitting data: 
Train-Test split

Evaluasi model:
Accuracy, Precision, Recall, F1-score
Confusion Matrix

4.Dashboard Visualisasi (Google Looker Studio)
Menyambungkan Google Sheets hasil preprocessing ke Looker Studio

Menampilkan:
KPI utama (Total Siswa, Dropout Rate, Jumlah Dropout)
Visualisasi fitur terhadap Status (histogram)
### Persiapan

Sumber data yang kita dapatkan kali ini adalah data siswa dari Jaya Jaya Institut yang tidak menyelesaikan pendidikan(dropout), lulus(graduate) sesuai dengan nilai yang ada pada dataset,dataset ini memiliki banyak kolom yang dapat membantu kita menganalisis tingkat dropout pada Jaya Jaya Institut
berikut link dataset yang kita gunakan : (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment - Shell/Terminal (Download File):

```
1.Analysis and Modelling 
cd SUB-2-DICODING-EXPERT
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Business Dashboard
Dashboard ini dikembangkan untuk membantu pihak manajemen Jaya Jaya Institut dalam mengidentifikasi pola dan karakteristik siswa yang mengalami dropout.

Beberapa fitur penting dalam dashboard ini meliputi:

1.Total Siswa, Jumlah Dropout, dan Persentase Dropout: Menyediakan gambaran umum mengenai tingkat penyelesaian pendidikan di institusi.

2.Distribusi Dropout berdasarkan Gender, Status Debitur, Usia, dan Mode Aplikasi: Membantu dalam mengenali kelompok siswa yang lebih rentan mengalami dropout.

3.Dropout by Course: Menampilkan mata kuliah atau jurusan dengan tingkat dropout tertinggi.

4.Status vs Application Mode dan Rentang Usia: Memberikan insight tambahan berdasarkan segmentasi untuk mendukung kebijakan yang lebih tepat sasaran.

Dari visualisasi yang ditampilkan, terlihat bahwa dropout cukup signifikan pada kelompok usia tertentu dan pada jalur aplikasi tertentu. Dashboard ini berfungsi sebagai alat monitoring strategis yang memudahkan proses pengambilan keputusan berbasis data oleh pihak institusi.
berikut link untuk menuju dashboard saya: (https://lookerstudio.google.com/reporting/046860d8-f535-40dd-adaa-ed085a542369)

## Menjalankan Sistem Machine Learning
```
1.Prediksi (Melalui StreamlitCloud)
klik link berikut : https://sub2dicoding.streamlit.app/
isi data sesuai petunjuk
hasil prediksi akan muncul
```
```
2.Prediksi (Lewat Terminal)
cd SUB-2-DICODING-EXPERT
streamlit run app.py
isi data sesuai petunjuk
hasil prediksi akan muncul
```

## Conclusion
Berdasarkan hasil analisis data, ditemukan bahwa beberapa fitur memiliki kontribusi penting dalam menentukan status dropout siswa, antara lain:

1.Usia saat pendaftaran (Age_at_enrollment): Usia yang lebih tinggi meningkatkan risiko dropout.

2.Application_mode: Terdapat jalur masuk tertentu yang memiliki tingkat dropout lebih tinggi dibandingkan yang lain.

3.Gender: Terdapat perbedaan proporsi dropout antara siswa laki-laki dan perempuan.

4.Debtor: Siswa yang memiliki status debtor menunjukkan kecenderungan lebih tinggi untuk dropout, sehingga faktor ekonomi ini perlu menjadi perhatian khusus.

Faktor akademik menunjukkan hubungan yang kuat terhadap kemungkinan kelulusan. Semakin tinggi nilai dan jumlah curricular units yang disetujui atau diselesaikan, maka semakin besar kemungkinan siswa untuk lulus:

1.Curricular_units_2nd_sem_approved

2.Curricular_units_1st_sem_approved

3.Curricular_units_2nd_sem_grade

4.Curricular_units_1st_sem_grade

Faktor ekonomi juga memiliki peran penting:

1.Tuition_fees_up_to_date: Siswa yang selalu membayar biaya kuliah tepat waktu cenderung memiliki peluang kelulusan yang lebih tinggi.

2.Scholarship_holder: Siswa penerima beasiswa menunjukkan tingkat kelulusan yang lebih baik dibandingkan yang tidak menerima beasiswa.

Kesimpulan ini dapat menjadi dasar dalam menyusun strategi, seperti pemberian dukungan akademik tambahan dan bantuan keuangan, untuk menurunkan tingkat dropout di Jaya Jaya Institut.

### Rekomendasi Action Items
1. Pendekatan Personal dan Psikososial
  - Mentoring dan konseling untuk mahasiswa usia kerja (20-30 tahun).
  - Komunitas dukungan untuk mahasiswa laki-laki.
  - Exit interview bagi mahasiswa yang mengundurkan diri untuk menggali alasan utama dropout.
2. Pendekatan Finansial
  - Skema bantuan keuangan, keringanan cicilan, dan beasiswa khusus bagi mahasiswa debitur.
  - Sistem monitoring berkala terhadap performa akademik mahasiswa peminjam.
3. Pendekatan Akademik
  - Evaluasi kurikulum di program studi dengan angka dropout tinggi.
  - Early warning system untuk mendeteksi dini risiko dropout (berdasarkan absensi, nilai, dan partisipasi).
  - Pengembangan program kuliah malam/fleksibel untuk mahasiswa pekerja.
4. Pendekatan Penerimaan Mahasiswa Baru
  - Evaluasi jalur penerimaan mahasiswa yang menghasilkan dropout tinggi.
  - Perbaikan proses seleksi, pembekalan awal, dan orientasi akademik untuk mahasiswa baru dari jalur tersebut
