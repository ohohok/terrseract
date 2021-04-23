import cv2
import pytesseract
import numpy as np


class ImageTableOCR(object):

    # 初始化
    def __init__(self):
        ImagePath = '/home/ubuntu/PycharmProjects/terrseract/ocr1.png'
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

        h, w = self.gray.shape

        # 横向直线列表
        horizontal_lines = []
        for i in range(h - 1):
            # 找到两条记录的分隔线段，以相邻两行的平均像素差大于120为标准
            if abs(np.mean(blur[i, :]) - np.mean(blur[i + 1, :])) > 120:
                # 在图像上绘制线段
                horizontal_lines.append([0, i, w, i])
                cv2.line(self.image, (0, i), (w, i), (0, 255, 0), 2)  # 绿色，三个像素宽度

        horizontal_lines = horizontal_lines[1:]
        print(horizontal_lines)
        return horizontal_lines


def main():
    ImageTableOCR().HorizontalLineDetect()


if __name__ == '__main__':
    main()
