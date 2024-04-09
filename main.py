import numpy as np
import matplotlib.pyplot as plt
import pywt
import cv2
import os
from tkinter import filedialog
import tkinter as tk

def wavelet_transform(image_path, wavelet='haar', level=1):
    # Wczytanie obrazu
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Zastosowanie falkowej transformacji dyskretnej
    coeffs = pywt.wavedec2(img, wavelet, level=level)

    # Wizualizacja współczynników
    fig, axs = plt.subplots(1, level+2, figsize=(12, 6))

    # Wyświetlenie oryginalnego obrazu
    axs[0].imshow(img, cmap='viridis')
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    for i in range(1, level+2):
        # Zastosowanie odwrotnej transformacji falkowej
        reconstructed_img = pywt.waverec2(coeffs[:i+1], wavelet)

        # Wyświetlenie zrekonstruowanego obrazu na danej poziomie
        axs[i].imshow(reconstructed_img.astype(np.uint8), cmap='gray')
        axs[i].set_title(f'Level {i}')
        axs[i].axis('off')

    plt.tight_layout()
    plt.show()

def select_image():
    # Tworzenie interfejsu użytkownika Tkinter
    root = tk.Tk()
    root.withdraw()  # Ukrycie głównego okna

    # Wybieranie pliku obrazu
    file_path = filedialog.askopenfilename(initialdir=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images'),
                                           title="Select an Image",
                                           filetypes=[("Image Files", "*.jpg; *.jpeg; *.png; *.bmp")])

    if file_path:
        # Wywołanie funkcji do transformacji falkowej dla wybranego obrazu
        wavelet_transform(file_path, wavelet='haar', level=3)

# Wywołanie funkcji do wyboru obrazu
select_image()
