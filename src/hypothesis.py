import numpy as np
from scipy import stats

def z_test_two_sample(x_bar1, x_bar2, sigma1, sigma2, n1, n2, alternative='two-sided', alpha=0.05):
    """
    Menghitung Uji Z Dua Sampel untuk Membandingkan Rata-rata Dua Populasi.
    Reference: Tsun (2020), p. 309
    """
    # Rumus Tsun (2020) p. 309
    pooled_se = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    z_stat = (x_bar1 - x_bar2) / pooled_se
    
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(np.abs(z_stat)))
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
        
    decision = "Reject H0" if p_value <= alpha else "Fail to reject H0"
    
    return {
        "z_stat": float(z_stat),
        "p_value": float(p_value),
        "decision": decision
    }
