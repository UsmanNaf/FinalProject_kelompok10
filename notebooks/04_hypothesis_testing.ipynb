import pandas as pd
import numpy as np
from scipy import stats

url_link_raw = "https://raw.githubusercontent.com/UsmanNaf/stat-audit-FinalProject_Group10-sti-2025/refs/heads/main/data/clean/pr_clean.csv"

# Load data
df_pr = pd.read_csv(url_link_raw)
print(f"Data berhasil dimuat. Total baris data: {len(df_pr)}")

# Pisahkan data berdasarkan status PR
comments_merged = df_pr[df_pr['status'] == 'merged']['comments']
comments_unmerged = df_pr[df_pr['status'] == 'unmerged']['comments']

# Statistik deskriptif
x_bar1 = comments_merged.mean()
x_bar2 = comments_unmerged.mean()

n1 = len(comments_merged)
n2 = len(comments_unmerged)

sigma1 = comments_merged.std()
sigma2 = comments_unmerged.std()

# Two-Sample Z-Test
pooled_se = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
z_stat = (x_bar1 - x_bar2) / pooled_se
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

# Output
print("\n" + "=" * 60)
print("HASIL OUTPUT PENGUJIAN TWO-SAMPLE Z-TEST")
print("=" * 60)

print(f"PR Merged")
print(f"  Mean              : {x_bar1:.4f}")
print(f"  Std. Deviation    : {sigma1:.4f}")
print(f"  Sample Size (n1)  : {n1}")

print()

print(f"PR Unmerged")
print(f"  Mean              : {x_bar2:.4f}")
print(f"  Std. Deviation    : {sigma2:.4f}")
print(f"  Sample Size (n2)  : {n2}")

print("-" * 60)
print(f"Z-Statistic         : {z_stat:.4f}")
print(f"P-Value             : {p_value:.4e}")
print(f"Decision            : {'Reject H0' if p_value < 0.05 else 'Fail to Reject H0'}")
print("=" * 60)
