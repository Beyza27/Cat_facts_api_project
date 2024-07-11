# -*- coding: utf-8 -*-
"""Cat_Facts_Api_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sr8FBKlcG2lrGiKp8jB_YfieK5UL5QxQ
"""

import requests
import matplotlib.pyplot as plt

# Cat Facts API URL'si
url = 'https://catfact.ninja/fact'

# API'ye GET isteği gönder
response = requests.get(url)

# İsteğin başarılı olup olmadığını kontrol et
if response.status_code == 200:
    # JSON yanıtını ayrıştır
    data = response.json()
    # Kedilerle ilgili bilgiyi yazdır
    cat_fact = data['fact']
else:
    cat_fact = None

# Çıktıyı görselleştirmek
if cat_fact:
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.text(0.5, 0.5, cat_fact, ha='center', va='center', fontsize=12, wrap=True)
    ax.set_axis_off()
    plt.title("Kedi Bilgisi")
    plt.show()
else:
    print(f"Veri alınamadı: {response.status_code}")