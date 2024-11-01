from ultralytics import YOLO
import cv2
import requests

# custom script
from lib import calcScore


def yolov8_predict(results):
    results = results[0].numpy()
    return 0


if __name__ == "__main__":
    # read YOLOv8n model
    model = YOLO("yolov8n.pt")
    results = model.predict(
        "images/ph01.jpg",
        save=True,
        save_crop=True,
        imgsz=640,
        conf=0.5,
    )
