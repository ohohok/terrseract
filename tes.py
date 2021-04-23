import cv2

from PIL import Image
from pytesseract import pytesseract


def image_str():
    context = pytesseract.image_to_string(Image.open("./cv_cut_thor.jpg"), lang='chi_sim')
    print(context)
    with open('annimal.txt', 'w', ) as f:
        f.write(context)




class ImageTableOCR(object):

    # 初始化
    def __init__(self):
        ImagePath = '/home/ubuntu/PycharmProjects/terrseract/动物B5.jpg'
        # 读取图片
        self.image = cv2.imread(ImagePath, 1)
        # 把图片转换为灰度模式
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # print(self.gray)

    # 横向直线检测
    def HorizontalLineDetect(self):

        # 图像二值化
        ret, thresh1 = cv2.threshold(self.gray, 240, 255, cv2.THRESH_BINARY)
        # 进行两次中值滤波
        blur = cv2.medianBlur(thresh1, 3)  # 模板大小3*3
        blur = cv2.medianBlur(blur, 3)  # 模板大小3*3

        print(self.gray.shape)
        cropped = self.gray[280:345, 310:666]  # 裁剪坐标为[y0:y1, x0:x1]

        print(cropped)

        cv2.imwrite("./cv_cut_thor.jpg", cropped)
        image_str()

ImageTableOCR().HorizontalLineDetect()