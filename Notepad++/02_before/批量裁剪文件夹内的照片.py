from PIL import Image
import os
fin = r'C:\\Users\\Administrator\\Desktop\\1\\9-59'
fout = r'C:\\Users\\Administrator\\Desktop\\1\\test1'
for file in os.listdir(fin):
    file_fullname = fin + '/' +file
    img = Image.open(file_fullname)
    # a = [1860, 0, 2560, 2160]
    # a = [1860, 540, 2560, 1500]

    # a = [400, 0, 800, 1000]
    # a = [1400, 0, 2560, 1200]
    # a = [1350, 0, 2560, 2160]

    # a = [1700, 0, 2560, 2160]
    # a = [1700, 300, 2560, 1300]

    # a = [1700, 0, 2560, 2160]
    # a = [1700, 400, 2560, 1400]

    # a = [2100, 0, 2560, 2160]
    # a = [2100, 900, 2560, 1400]

    # a = [1100, 0, 1700, 1300]

    a = [1800, 400, 2560, 1400]



    box = (a)
    roi = img.crop(box)
    out_path = fout + '/' + file
    roi.save(out_path)