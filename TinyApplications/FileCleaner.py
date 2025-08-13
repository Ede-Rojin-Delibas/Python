"""
Created in: 27th of June 2025 at 20:11 PM

author: Ede Rojin DELİBAŞ"""

import os

#1.Hedef klasöre git
FOLDER_PATH=input("Enter the folder path: ")
os.chdir(FOLDER_PATH) 
#2.Dosyaları tara
extention= input("Enter the file extension to clean (e.g., .txt, .json): ")
found = False #dosya bulunup bulunmadığını kontrol etmek için
for dosya in os.listdir():
    
    if os.path.splitext(dosya)[1] == extention:
        os.remove(dosya)
        found = True
if not found:
    print(f"Klasörde bu {extention} uzantıda bir dosya bulunamadı!")
else:
    print(f"Klasörde bu {extention} uzantılı dosyalar temizlendi!")



