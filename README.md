# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Nah, Anda diminta untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya.Mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa. 

### Permasalahan Bisnis
Banyak siswa yang tidak menyelesaikan pendidikannya/dropout.

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
saya membuat dashboard ini untuk membantu mengidentifikasi kelompok siwa yang tidak menyelesaikan pendidikannya, sehingga institut dapat mengambil langkah strategis untuk mengurangi tingkat siswa yang tidak menyelesaikan pendidikannya dan memperbaiki sistem internal nya.
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
Setelah analisis yang dilakukan saya menemukan bahwa beberapa penyebab dari meningkatnya Dropout pada institut ialah Age_at_enrollment, Application_mode, Gender, Debtor memiliki tingkat korelasi rendah dengan Status yang berarti masalah dropout berdasarkan fitur tersebut dan yang membuat siswa tidak dropout ialah faktor nilai(semakin tinggi semakin Lulus): Curricular_units_2nd_sem_approved, Curricular_units_1st_sem_approved, Curricular_units_2nd_sem_grade, Curricular_units_1st_sem_grade. Faktor ekonomi(Jika iya maka semakin Lulus): Tuition_fees_up_to_date, Scholarship_holder.

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
