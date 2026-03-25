"""
Independent verification of SSGEOS conjuntclust6p-2000-2024 claims.
Author: Şira Nur Uysal
Date: 2026-03
"""

from scipy import stats
import numpy as np

# -----------------------------------------------
# 1. Background probability check
# -----------------------------------------------
total_days = 9132  # 2000-2024
total_eq = 371     # M7.0+ (USGS)
daily_rate = total_eq / total_days

# Poisson: P(>=1 EQ in 9-day window)
lambda_9 = daily_rate * 9
p_at_least_one = 1 - np.exp(-lambda_9)
print(f"Günlük M7.0+ oran: {daily_rate:.6f}")
print(f"9 günlük pencerede en az 1 deprem olasılığı (Poisson): {p_at_least_one:.6f}")
print(f"SSGEOS'un değeri: 0.306245")
print(f"Fark: {abs(p_at_least_one - 0.306245):.6f}")
print()

# -----------------------------------------------
# 2. Binomial test: 6/6 clusters matched
# -----------------------------------------------
n_clusters = 6
k_success = 6
p_background = p_at_least_one

binom_p = stats.binom.sf(k_success - 1, n_clusters, p_background)
print(f"Binom testi (6/6 eşleşme): p = {binom_p:.8f}")
print(f"SSGEOS'un değeri: 0.00082493")
print()

# -----------------------------------------------
# 3. Multiple testing problem
# -----------------------------------------------
print("=" * 50)
print("ÇOKLU TEST SORUNU")
print("=" * 50)
# Adjustable parameters in SSGEOS methodology:
# - Minimum cluster size: 4, 5, 6, 7, 8 (5 options)
# - Time window: 1-10 days each side (10 options)
# - Magnitude threshold: 6.0, 6.5, 7.0, 7.5 (4 options)
# - Center body: helio/geo + planet combos (~7 options)
# - Time period: various start/end dates (~3 options)
# Conservative estimate: 5 × 10 × 4 × 7 × 3 = 4,200 combinations
n_tests_conservative = 60  # very conservative
n_tests_realistic = 4200

bonferroni_conservative = min(binom_p * n_tests_conservative, 1.0)
bonferroni_realistic = min(binom_p * n_tests_realistic, 1.0)

print(f"Düzeltilmemiş p-değeri: {binom_p:.6f}")
print(f"Bonferroni (60 test, çok muhafazakâr): {bonferroni_conservative:.4f}")
print(f"Bonferroni (4200 test, gerçekçi): {bonferroni_realistic:.4f}")
print(f"α=0.05 eşiği aşılır mı (60 test)? {'EVET' if bonferroni_conservative > 0.05 else 'HAYIR'}")
print()

# -----------------------------------------------
# 4. 1940-2024 extended analysis is meaningless
# -----------------------------------------------
print("=" * 50)
print("1940-2024 GENİŞLETİLMİŞ ANALİZ SORUNU")
print("=" * 50)
# M6.5+ earthquakes: ~125/year average
# 9-day window probability for M6.5+
eq_per_year_65 = 125
daily_rate_65 = eq_per_year_65 / 365.25
lambda_9_65 = daily_rate_65 * 9
p_65 = 1 - np.exp(-lambda_9_65)
print(f"M6.5+ günlük oran: {daily_rate_65:.4f}")
print(f"9 günde en az 1 M6.5+ deprem olasılığı: {p_65:.4f} ({p_65*100:.1f}%)")
print(f"29 denemede beklenen eşleşme: {29 * p_65:.1f}")
print(f"SSGEOS'un bulgusu: 25/29 eşleşme")
print(f"Beklentinin ALTINDA: {29 * p_65 - 25:.1f} eksik eşleşme")
print()

# -----------------------------------------------
# 5. Tidal force comparison
# -----------------------------------------------
print("=" * 50)
print("GELGİT KUVVETİ KARŞILAŞTIRMASI")
print("=" * 50)
# Tidal force ~ M / d^3
# Moon: M=7.35e22 kg, d=3.84e8 m
# Venus (closest): M=4.87e24 kg, d=3.82e10 m (0.26 AU)
# Jupiter (closest): M=1.90e27 kg, d=5.88e11 m (3.93 AU)
# Sun: M=1.99e30 kg, d=1.496e11 m

def tidal(M, d):
    return M / d**3

moon = tidal(7.35e22, 3.84e8)
venus = tidal(4.87e24, 3.82e10)
jupiter = tidal(1.90e27, 5.88e11)
sun = tidal(1.99e30, 1.496e11)

print(f"Ay gelgit kuvveti (normalize): 1.000")
print(f"Güneş / Ay: {sun/moon:.4f}")
print(f"Venüs / Ay: {venus/moon:.7f} ({venus/moon*100:.5f}%)")
print(f"Jüpiter / Ay: {jupiter/moon:.7f} ({jupiter/moon*100:.5f}%)")
print(f"Venüs, Ay'ın {venus/moon*100:.4f}%'i kadar gelgit etkisi üretir.")
print(f"Jüpiter, Ay'ın {jupiter/moon*100:.5f}%'i kadar gelgit etkisi üretir.")
