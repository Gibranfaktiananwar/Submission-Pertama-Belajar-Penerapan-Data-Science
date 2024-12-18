# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di berbagai wilayah. Meskipun telah berkembang pesat, perusahaan ini masih menghadapi tantangan besar dalam pengelolaan karyawan. Salah satu masalah utamanya adalah tingginya *attrition rate* rasio karyawan yang keluar dibandingkan total karyawan yang mencapai lebih dari 10%. Tingginya tingkat *attrition* ini menunjukkan kesulitan perusahaan dalam mempertahankan karyawannya, yang dapat memengaruhi produktivitas, meningkatkan biaya rekrutmen, dan mengganggu stabilitas operasional.

### Permasalahan Bisnis

1. Berapa persentase tingkat attrition di perusahaan ini?
2. Seberapa pengaruh kerja overtime (lembur) dalam tingkat penurunan karyawan?
3. Faktor-faktor yang mempengaruhi tingkat Attrition pada Jaya Jaya Maju?

### Cakupan Proyek

1. Analisis Data: Menganalisa data karyawan Jaya Jaya Maju yang sudah dikumpulkan untuk mencari tau faktor-faktor penyebab penurunan karyawan
2. Visualisasi dan Pelaporan: Menunjukan per Key Performance Indicator (kpi) yang ada untuk menganalisa apa yang menyebabkan hal penurunan karyawan bisa terjadi dan juga dilaporkan ke HR dengan ada nya Dashboard yang dibuat.
3. Rekomendasi aksi : Memberikan beberapa rekomendasi agar tingkat penurunan karyawan bisa terus ditekan.

### Persiapan

Sumber data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).


Setup environment:

* Setup conda environment:

```
conda create --name proyek-human-resources python==3.9.15
```

* Install requirements library:

```
pip install -r requirements.txt
```

* Run Predict :

```
python prediction.py
```

## Business Dashboard

Dashboard ini dibuat untuk memberikan pemahaman menyeluruh kepada tim HR mengenai faktor-faktor yang memengaruhi keputusan karyawan untuk keluar dari perusahaan per Key Performance Indicatornya.

* Mengidentifikasi department apa yang memiliki tingkat Attrition tertinggi.
* Seberapa berpengaruh faktor kerja ovetime terhadap tingkat attrition
* Dapat Mengambil tingkatan atau keputusan untuk menekan jumlah Attrition.

![gibran_faktian-dashboard](https://github.com/user-attachments/assets/502102c2-bbec-4ef3-95e4-5cc8bf98f382)


## Conclusion

1. Berapa persentase tingkat attrition di perusahaan ini?
   
![image](https://github.com/user-attachments/assets/0ae1d793-bbc1-41cc-b211-84e4b8b4b70a)

Jawaban : Tingkat attrition di perusahaan ini mencapai sekitar 16%. Yang berarti, satu dari enam karyawan meninggalkan perusahaan, yang menunjukkan bahwa tingkat keluar karyawan tergolong tinggi.

2. Seberapa pengaruh kerja overtime (lembur) dalam tingkat penurunan karyawan?

![image](https://github.com/user-attachments/assets/28f49105-b377-43c4-b29e-795f6040fa9e)

Jawaban : Sangat berpengaruh. Berdasarkan data, karyawan lebih banyak merasa bahwa bekerja di perusahaan Jaya Jaya Maju ini sering Overtime.

3. Faktor-faktor yang mempengaruhi tingkat Attrition pada Jaya Jaya Maju?

![image](https://github.com/user-attachments/assets/80156d80-7faa-43c4-8369-2b6d050236ce)


Jawaban : Overtime dan Marital Status menjadi faktor tertinggi yang mempengaruhi para karyawan untuk meninggalkan Perusahaan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Berikan Environment kerja yang nyaman : hal ini bisa dari mulai mempekerjakan orang-orang yang supportive hingga memberikan fasilitas yang membuat nyaman para pekerjanya.
- Kurangi waktu kerja overtime : sesuaikan lagi beban pekerjaan yang diberi para karyawan agar tidak merasa stress karena pekerjaan yang numpuk.
- Berikan tools / alat-alat penunjang pekerjaan : pada department Research & Development memiliki tingkat Attrition tertinggi, mungkin dikarenakan tools atau alat-alat penunjang pekerjaan mereka masih belum memadai.

Dengan menerapkan rekomendasi ini, perusahaan diharapkan mampu menekan tingkat attrition, meningkatkan kinerja karyawan, serta memperkuat efisiensi dan stabilitas operasional secara menyeluruh.

Berikut link akses Tableau : [Jaya Jaya Maju]([https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee](https://public.tableau.com/app/profile/gibran.faktian.anwar/viz/Dicoding-JayaJayaMaju/Dicoding-JayaJayaMaju)) 
