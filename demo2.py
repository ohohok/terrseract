import cv2
from hyperlpr import HyperLPR_PlateRecogntion
while True:
    file_name = input('图片名：')
    image = cv2.imread(file_name)
    H_P = HyperLPR_PlateRecogntion(image)
    car_num = H_P[0][0]
    print(car_num)

