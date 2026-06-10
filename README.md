# 📊 Open Source Analytics: Issue Frequency & Contributor Diversity in pandas

Analisis dinamika kontribusi open-source pada repositori **pandas-dev/pandas** menggunakan data *closed issues* dan *merged pull requests*. Proyek ini memodelkan frekuensi issue yang mengikuti **distribusi Poisson** dan mengukur **keberagaman kontributor** (*contributor diversity*) untuk memahami faktor-faktor yang mempengaruhi produktivitas dan keberlanjutan proyek open-source.

---

## 🎯 Project Description

Proyek ini bertujuan untuk menganalisis pola aktivitas dan kolaborasi dalam repositori open-source pandas. Dengan memanfaatkan:

- **Issue frequency** yang mengikuti distribusi Poisson
- **Contributor diversity** yang diukur menggunakan Shannon/Simpson index

Proyek ini membangun model statistik dan simulasi dalam **tiga lapisan utama**:

| Layer | Tujuan |
|-------|--------|
| **Estimation** | Mengestimasi rata-rata issue per minggu dan tingkat keberagaman kontributor |
| **Inference** | Menguji perbedaan diversity antara periode high vs low issue frequency |
| **Simulation** | Memproyeksikan diversity di masa depan berdasarkan parameter historis |

Data diperoleh melalui **GitHub API** crawling, mencakup informasi temporal, identitas kontributor, dan asosiasi mereka dengan proyek (MEMBER, CONTRIBUTOR, NONE).

---

## 🔬 Research Questions

### 1. Estimation Layer
Berapa probabilitas sebuah PR di-merge, dan seberapa tidak pasti estimasi tersebut?

### 2. Inference / Testing Layer
Apakah rata-rata jumlah komentar berbeda secara signifikan antara PR yang merged vs unmerged?

### 3. Simulation Layer
Berapa probabilitas sebuah issue butuh lebih dari 30 hari untuk ditutup?

---

## 📈 Key Findings

## EDA

Data telah dibersihkan dan divisualisasikan.

Temuan utama:
- Probabilitas PR di-merge sekitar **63.4%** →  (Member B, Q1)
- PR unmerged cenderung punya lebih banyak komentar → diuji Member D (Q2)
- **6.9%** issue butuh lebih dari 30 hari untuk ditutup → disimulasi Member E (Q3)

## Estimation

Dari analisis estimasi pada Q1, diperoleh:

| Metode | Nilai θ |
|---|---|
| MLE Bernoulli (θ̂ = k/n) | ≈ 0.6337 |
| Mode Beta Posterior | ≈ 0.6337 |
| Mean Beta Posterior | ≈ 0.6334 |

**Kesimpulan Q1:**  
Probabilitas sebuah PR di-merge di `pandas-dev/pandas` diestimasi sebesar **≈ 63.4%** dengan tingkat ketidakpastian yang rendah (kurva posterior sempit). Nilai ini akan diteruskan ke **Member C (Inference Analyst)** untuk konstruksi confidence interval dan credible interval terhadap parameter θ ini.

## Inference

[cite_start]Berdasarkan hasil inferensi menggunakan *Confidence Interval* 95%[cite: 85, 86], kita dapat menjawab pertanyaan penelitian (Q2):
* Rata-rata jumlah komentar pada PR yang berstatus `merged` diproyeksikan berada pada interval **[1.14 sampai 1.34]**.
* Rata-rata jumlah komentar pada PR yang berstatus `unmerged` diproyeksikan berada pada interval **[1.96 sampai 2.29]**.

Karena kedua interval tersebut **[tidak saling tumpang tindih]**, maka dapat disimpulkan bahwa **[terdapat]** perbedaan yang signifikan secara statistik pada antusiasme/diskusi (jumlah komentar) antara PR yang diterima (merged) dan ditolak/ditutup (unmerged).

## Hypothesis

Hasil pengujian menunjukkan bahwa PR yang berstatus *unmerged* memiliki rata-rata komentar sebesar 2,1246, lebih tinggi dibandingkan PR yang berstatus *merged* yang memiliki rata-rata komentar sebesar 1,2380. Hal tersebut berarti PR yang tidak berhasil di-merge cenderung melibatkan diskusi yang lebih panjang atau lebih banyak *feedback* dari maintainer dan kontributor lain. Beberapa faktor dari banyaknya komentar bisa dari adanya revisi yang belum terselesaikan atau kualitas kode yang perlu perhatian lebih lanjut dari maintainer. Hasil ini menunjukkan bahwa tingginya jumlah komentar dapat menjadi indikator awal adanya hambatan dalam proses review. Oleh karena itu, informasi ini dapat dimanfaatkan maintainer untuk mengidentifikasi PR yang berpotensi mengalami kesulitan dan juga untuk memberikan *feedback* yang lebih terarah.

## Simulation
Data dimanipulasi sesuai kebeutuhan sebelum melakukan simulasi.

Temuan utama:
- Metode Monte Carlo sangat cocok untuk simulasi ini karna tidak terikat urutan proses dan tidak berkaitan dengan durasi.
- Hasil simulasi menunjukkan bahwa kemungkinan issue akan di tutup dalam waktu lebih dari 30 hari adalah sekitar *~6.9-7.5%* berubah-ubah karena simulasi mengambil sampel random setiap kali di jalankan.


---


## How To Run
```bash
pip install pandas matplotlib numpy
python namaFile.py
```


## Team Table
| Nama                   | NIM          |
|------------------------|--------------|
| Raynar Usman Annafis   | 1519625013   | 
| Zaky Aditya Susanto    | 1519625023   |
| Bethelina Imanuella Y  | 1519625014   |
| Kirana Cinta Mentari   | 1519625021   | 
| Luqman                 | 1519625072   | 
