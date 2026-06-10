# AI Usage Log — stat-audit-FinalProject_Group10-sti-2025

## Summary

| Member | Role | Tools | ~% Code AI-Assisted | Interpretation Cells AI-Assisted? |
| ------ | ---- | ----- | ------------------- | --------------------------------- |
| Kirana Cinta Mentari | Data Engineer | Claude | ~70% | No |
| Raynar Usman Annafis | Estimation Analyst | Claude, DeepSeek, Gemini | ~65% | Yes |
| Bethelina Imanuella Yesaya | Hypothesis Analyst | Gemini, ChatGPT | ~80% | Yes |
| Zaky Aditya Susanto | Computation Analyst | Gemini, ChatGPT | ~70% | No |

---

## Per-Member Detail

### Member A — Kirana Cinta Mentari

| # | Task | Tool | Prompt | How the Output Was Used | How Do You Evaluate the Output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Membuat script crawling data issues dan pull request dari GitHub API | Claude | "Saya punya tugas sebagai Data Engineer dan perlu mengambil data dari GitHub API untuk repo pandas-dev/pandas. Bantu saya buat script Python yang bisa crawling issues dan PR secara otomatis tanpa menggunakan input(), lengkap dengan pagination dan rate limit handling" | Output menghasilkan script `collect_data.py` yang langsung bisa dijalankan otomatis, dengan pagination dan pembuatan folder `data/raw/` secara otomatis | Mengecek hasil crawling dengan memverifikasi jumlah data dan struktur CSV yang dihasilkan |
| 2 | Import library dan load dataset untuk EDA | Claude | "Bantu aku import library yang dibutuhkan untuk EDA dan load data dari issues_clean.csv dan pr_clean.csv" |Output menginisialisasi library `pandas`, `matplotlib`, `seaborn` dan memuat data dari direktori `data/raw/` | Memverifikasi dataset berhasil dimuat dengan mengecek shape dan kolom |
| 3 | Cleaning dataset issues dan PR  | Claude | "Bantu aku membersihkan dataset issues dan PR. pilih kolom yang penting, hapus duplikat, dan konversi format tanggal" | Output memberikan kode cleaning yang kemudian disesuaikan dengan kolom data aktual | Mengecek nilai null dan tipe data setelah cleaning untuk memastikan hasilnya benar |
| 4 | Membuat visualisasi untuk ketiga research questions | Claude | "Bantu aku buat tiga visualisasi: bar chart untuk distribusi PR merged vs unmerged, boxplot untuk perbandingan komentar, dan histogram untuk waktu penyelesaian issue" | Output menghasilkan kode visualisasi yang disesuaikan dengan data aktual | Menjalankan visualisasi dan memverifikasi hasilnya sesuai dengan data |
| 5 | Debug error library matplotlib dan seaborn | Claude | "Muncul error ModuleNotFoundError saat import matplotlib di notebook. Gimana cara fixnya?" | Output memberikan perintah install yang tepat untuk menyelesaikan error | Menjalankan ulang notebook setelah install dan memastikan error teratasi |

---

### Member B — Raynar Usman Annafis

| # | Task | Tool | Prompt | How the Output Was Used | How Do You Evaluate the Output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Set up project structure, import required libraries, and reference data from `issues_clean.csv` and `pr_clean.csv` | DeepSeek | "Saya memiliki tugas kuliah sebagai Estimation Analyst. Sebelum melakukan estimasi, tolong bantu saya mengimport library yang dibutuhkan dan bantu saya mereferensikan data berdasarkan `issues_clean.csv` dan `pr_clean.csv`." | The output initialized core libraries (`pandas`, `sys`, `os`, `numpy`, `matplotlib.pyplot`, `scipy.stats`) and established a router path from `estimator.py` — which contains all predefined estimation formulas — as the central data reference point. | Verified that the router path correctly pointed to `estimator.py`, and tested a success indicator to confirm the path was resolved and executed successfully. |
| 2 | Import core estimation formulas: MLE Derivation, Beta Posterior, and Likelihood Visualisation | DeepSeek | "Berdasarkan data yang telah direferensikan, lakukan analisis estimasi menggunakan pendekatan MLE Derivation, Beta Posterior, dan Likelihood Visualisation. Formula disesuaikan dengan spesifikasi pada repository (Formula Accuracy Formula dan Source Modules)." | The formulas were imported from `estimator.py`, specifically: `mle_bernoulli`, `log_likelihood_bernoulli`, `mle_poisson`, `log_likelihood_poisson`, and `beta_posterior`. | After loading the data and filtering between merged and unmerged pull requests, the formulas were applied to the filtered datasets to validate correctness and alignment with expected estimation outputs. |
| 3 | Debug minor errors related to data reference loading and `plt` command execution | DeepSeek, Gemini | "Saya mengalami masalah pada referensi data yang gagal diproses dan perintah `plt` yang tidak berjalan dengan benar." | The output provided fixes for the incorrect library configuration and the faulty router path in `estimator.py`. | Re-analyzed the corrected code manually and re-ran the full script to confirm that the improvements resolved both issues successfully. |

---

### Member D — Bethelina Imanuella Yesaya

| # | Task | Tool | Prompt | How the Output Was Used | How Do You Evaluate the Output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Membuat kode Two-Sample Z-Test | Gemini | "bantu saya membuat kode Two-Sample Z-Test di python" | Digunakan sebagai dasar kode untuk melakukan uji hipotesis pada data PR merged dan unmerged | Menjalankan kode dan memastikan hasil yang keluar sesuai dengan data yang dianalisis |
| 2 | Menjelaskan konsep statistik | ChatGPT | "jelaskan apa itu p-value, Two-Sample Z-Test, Two-Tailed Test, dll" | Digunakan untuk membantu memahami konsep yang digunakan dalam analisis | Membandingkan penjelasan dengan materi dari PPT |
| 3 | Perbaikan kode Python | ChatGPT | "bantu saya merapikan kode python berikut" | Digunakan untuk membuat kode lebih rapi dan menampilkan informasi tambahan yaitu standar deviasi | Menjalankan ulang kode dan memastikan hasilnya tetap sama seperti sebelumnya |
| 4 | Menjelaskan hasil uji hipotesis | ChatGPT | "bantu saya menjelaskan hasil Z-test dan p-value yang diperoleh" | Digunakan untuk menyusun penjelasan hasil uji dan interpretasi | Dicocokkan dengan output yang dihasilkan program dan mencoba memahami dan menjelaskan menggunakan bahasa sendiri |

---

### Member E — Zaky Aditya Susanto

| # | Task | Tool | Prompt | How the Output Was Used | How Do You Evaluate the Output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Memahami Metode Apa yang akan digunakan diantara tiga metode (Monte Carlo, MCMC, Bloom Filter) | Gemini | "Menurut lu, metode apa yang paling cocok untuk melakukan simulasi data pull request yang di close lebih dari 30 hari diantara tiga metode ini : Monte Carlo, MCMC, dan Bloom Filter?" | Digunakan sebagai referensi dan pendukung pengambilan keputusan | Membandingkan hasil jawaban AI dengan materi yang diberikan di teams. |
| 2 | Visualisasi persebaran hasil simulasi | ChatGPT | "Buatkan visualisasi dengan diagram bar untuk hasil dari kode simulasi berikut" | Digunakan untuk memvisualisasikan hasil simulasi | Mereview hasil kode dan kebersihan kode |

---

## Group Reflection (150–300 words)

Penggunaan AI dalam kelompok kami mengalami evolusi yang signifikan selama tiga minggu jalannya proyek. Pada awal proses, kami cenderung menggunakan instruksi standar yang sederhana, namun seiring berjalannya waktu, kami mulai menerapkan teknik instruksi yang lebih matang dan terstruktur. Selain itu, kelompok kami juga mengembangkan kebiasaan baru untuk selalu mengevaluasi serta memvalidasi kembali setiap respons yang dihasilkan oleh AI sebelum digunakan dalam laporan utama.

Secara umum, AI mampu bekerja dengan sangat baik dalam memberikan wawasan baru serta membantu pembuatan visualisasi data melalui kode program. Hasil visualisasi tersebut dinilai sangat layak pakai berkat dukungan kombinasi instruksi yang mendalam dari anggota kelompok. Meskipun demikian, AI masih memiliki keterbatasan yang memerlukan perbaikan signifikan, terutama pada bagian pembuatan kode penjelajahan web atau crawling serta pembersihan data. Pada tahapan ini, instruksi yang kurang detail sering kali membuat hasil dari AI menjadi kurang maksimal, sehingga kami harus melakukan proses debugging secara manual untuk menyempurnakan alur kode tersebut.

Di sisi lain, walaupun sebagian besar tahapan proyek terlihat bergantung pada AI, ada momen tertentu di mana kami secara sadar memilih untuk tidak menggunakannya sama sekali. Momen tersebut terjadi pada saat kami menyusun bagian kesimpulan dan temuan utama. Beberapa anggota kelompok memilih untuk merumuskan bagian ini secara manual tanpa bantuan AI. Keputusan ini diambil karena kami merasa penyusunan kesimpulan akan jauh lebih baik jika menggunakan bahasa dan pemikiran sendiri. Langkah ini tidak hanya menjaga orisinalitas tulisan agar tidak terkesan kaku, tetapi juga menjadi sarana untuk memantapkan pemahaman mendalam kelompok kami terhadap seluruh hasil analisis yang telah dikerjakan.
