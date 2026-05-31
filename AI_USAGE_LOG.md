# AI Usage Log — [Project Name]

## Summary

| Member | Role | Tools | ~% Code AI-Assisted | Interpretation Cells AI-Assisted? |
| ------ | ---- | ----- | ------------------- | --------------------------------- |
| Raynar Usman Annafis | Estimation Analyst | Claude, DeepSeek, Gemini | ~65% | Yes |
| ... | | | | |

---

## Per-Member Detail

### Member B — Raynar Usman Annafis

| # | Task | Tool | Prompt | How the Output Was Used | How Do You Evaluate the Output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Set up project structure, import required libraries, and reference data from `issues_clean.csv` and `pr_clean.csv` | DeepSeek | "Saya memiliki tugas kuliah sebagai Estimation Analyst. Sebelum melakukan estimasi, tolong bantu saya mengimport library yang dibutuhkan dan bantu saya mereferensikan data berdasarkan `issues_clean.csv` dan `pr_clean.csv`." | The output initialized core libraries (`pandas`, `sys`, `os`, `numpy`, `matplotlib.pyplot`, `scipy.stats`) and established a router path from `estimator.py` — which contains all predefined estimation formulas — as the central data reference point. | Verified that the router path correctly pointed to `estimator.py`, and tested a success indicator to confirm the path was resolved and executed successfully. |
| 2 | Import core estimation formulas: MLE Derivation, Beta Posterior, and Likelihood Visualisation | DeepSeek | "Berdasarkan data yang telah direferensikan, lakukan analisis estimasi menggunakan pendekatan MLE Derivation, Beta Posterior, dan Likelihood Visualisation. Formula disesuaikan dengan spesifikasi pada repository (Formula Accuracy Formula dan Source Modules)." | The formulas were imported from `estimator.py`, specifically: `mle_bernoulli`, `log_likelihood_bernoulli`, `mle_poisson`, `log_likelihood_poisson`, and `beta_posterior`. | After loading the data and filtering between merged and unmerged pull requests, the formulas were applied to the filtered datasets to validate correctness and alignment with expected estimation outputs. |
| 3 | Debug minor errors related to data reference loading and `plt` command execution | DeepSeek, Gemini | "Saya mengalami masalah pada referensi data yang gagal diproses dan perintah `plt` yang tidak berjalan dengan benar." | The output provided fixes for the incorrect library configuration and the faulty router path in `estimator.py`. | Re-analyzed the corrected code manually and re-ran the full script to confirm that the improvements resolved both issues successfully. |

---

## Group Reflection (150–300 words)

_How did your group's use of AI evolve over three weeks? What did AI handle well? Where did output need significant correction? Was there a moment you chose **not** to use AI — and why?_

