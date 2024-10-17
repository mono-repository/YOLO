#
from ultralytics import YOLO
import cv2
import requests

# もしライブラリが読み込めた場合、メッセージを表示する
# if YOLO:
#     print("YOLO is available.") OK


def yolov8_predict(results):
    results = results[0].numpy()

    # print(results)
    print(results)
    return 0


if __name__ == "__main__":
    print("Hello, YOLO!")
    # read YOLOv8n model
    model = YOLO("yolov8n.pt")
    results = model("https://ultralytics.com/images/zidane.jpg", save=False)
    yolov8_predict(results)

    