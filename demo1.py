from PIL import Image
from pytesseract import pytesseract


def image_str():
    context = pytesseract.image_to_string(Image.open('/home/ubuntu/PycharmProjects/terrseract/myfontlab.normal.exp1.png'), lang='chi_sim')
    # context = pytesseract.image_to_string(Image.open('/home/ubuntu/PycharmProjects/terrseract/ocr1.png'), lang='chi_sim')
    print(context)
    with open('annimal.txt', 'w', ) as f:
        
        f.write(context)


image_str()
