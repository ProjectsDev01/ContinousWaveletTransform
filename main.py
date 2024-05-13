# import numpy as np
# import matplotlib.pyplot as plt
# import pywt
# import cv2
# import os
# from tkinter import filedialog
# import tkinter as tk
# 
# def wavelet_transform(image_path, wavelet='haar', level=2):
#    Wczytanie obrazu
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# 
#   Zastosowanie falkowej transformacji dyskretnej dla pierwszej falki
    # coeffs_wavelet1 = pywt.wavedec2(img, wavelet, level=level)
# 
#    Wizualizacja współczynników
    # fig, axs = plt.subplots(1, level+2, figsize=(12, 6))
# 
#    Wyświetlenie oryginalnego obrazu
    # axs[0].imshow(img, cmap='gray')   
    # axs[0].set_title('Original Image')
    # axs[0].axis('off')
# 
    # for i in range(1, level+2):
#        Zastosowanie odwrotnej transformacji falkowej dla pierwszej falki
        # reconstructed_img_wavelet1 = pywt.waverec2(coeffs_wavelet1[:i+1], wavelet)
# 
#        Wyświetlenie zrekonstruowanego obrazu na danym poziomie dla pierwszej falki
        # axs[i].imshow(reconstructed_img_wavelet1.astype(np.uint8), cmap='gray') #
        # axs[i].set_title(f'Level {i}')
        # axs[i].axis('off')
# 
#        Porównanie zrekonstruowanego obrazu na 3 poziomie z obrazem oryginalnym
        # if i == 3:
            # pixel_diff = np.abs(img - reconstructed_img_wavelet1)
            # fig_diff, ax_diff = plt.subplots(figsize=(6, 6))
            # ax_diff.imshow(pixel_diff.astype(np.uint8), cmap='gray')
            # ax_diff.set_title('Pixel Difference - Level 3 vs. Original')
            # ax_diff.axis('off')
            # plt.show()
# 
    # plt.tight_layout()
    # plt.show()
# 
# def select_image():
#    Tworzenie interfejsu użytkownika Tkinter
    # root = tk.Tk()
    # root.withdraw()  # Ukrycie głównego okna
# 
#    Wybieranie pliku obrazu
    # file_path = filedialog.askopenfilename(initialdir=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images'),
                                        #    title="Select an Image",
                                        #    filetypes=[("Image Files", "*.jpg; *.jpeg; *.png; *.bmp")])
# 
    # if file_path:
#        Wywołanie funkcji do transformacji falkowej dla wybranego obrazu
        # wavelet_transform(file_path, wavelet='haar', level=3)
# 
#Wywołanie funkcji do wyboru obrazu
# select_image()

# Using the PyWavelets module
#biorthagonal wavelets
from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import os
import pywt
plt.rcParams['figure.figsize'] = [16, 16]
plt.rcParams.update({'font.size': 18})

A = imread(os.path.join('ContWavTr/images/wallpaper.jpg'))
B = np.mean(A, -1); # Convert RGB to grayscale
## Wavelet decomposition (2 level)
n = 2
w = 'db1'
coeffs = pywt.wavedec2(B,wavelet=w,level=n)

# normalize each coefficient array
coeffs[0] /= np.abs(coeffs[0]).max()
for detail_level in range(n):
    coeffs[detail_level + 1] = [d/np.abs(d).max() for d in coeffs[detail_level + 1]]

arr, coeff_slices = pywt.coeffs_to_array(coeffs)



plt.imshow(arr,cmap='gray',vmin=-0.25,vmax=0.75)
plt.show()