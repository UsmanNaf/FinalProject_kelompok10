import numpy as np
import scipy.stats as st

def confidence_interval(theta_hat, sigma, n, confidence=0.95):
    """Membangun Confidence Interval umum menggunakan Z-Score."""
    alpha = 1 - confidence
    z_score = st.norm.ppf(1 - alpha / 2)
    margin_of_error = z_score * (sigma / np.sqrt(n))
    
    return theta_hat - margin_of_error, theta_hat + margin_of_error

def ci_bernoulli(k, n, confidence=0.95):
    """Membangun CI untuk data probabilitas/proporsi (Sukses/Gagal)."""
    theta_hat = k / n
    sigma = np.sqrt(theta_hat * (1 - theta_hat))
    alpha = 1 - confidence
    z_score = st.norm.ppf(1 - alpha / 2)
    margin_of_error = z_score * (sigma / np.sqrt(n))
    
    return theta_hat - margin_of_error, theta_hat + margin_of_error

def ci_poisson(data, confidence=0.95):
    """Membangun CI untuk data hitungan/cacah (misal: jumlah komentar)."""
    data = np.array(data)
    n = len(data)
    theta_hat = np.mean(data) # MLE untuk Poisson adalah rata-rata
    
    alpha = 1 - confidence
    z_score = st.norm.ppf(1 - alpha / 2)
    margin_of_error = z_score * np.sqrt(theta_hat / n)
    
    return theta_hat - margin_of_error, theta_hat + margin_of_error

def credible_interval(alpha_param, beta_param, confidence=0.95):
    """Membangun Credible Interval (Bayesian) menggunakan distribusi Beta."""
    alpha_level = 1 - confidence
    lower_bound = st.beta.ppf(alpha_level / 2, alpha_param, beta_param)
    upper_bound = st.beta.ppf(1 - alpha_level / 2, alpha_param, beta_param)
    
    return lower_bound, upper_bound