from flask import Flask, render_template
import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

model_json_file = r"D:\wetransfer_zip_2024-02-22_0704\Accident-Detection-System-main\Accident-Detection-System-main\model.json"
model_weights_file = r"D:\wetransfer_zip_2024-02-22_0704\Accident-Detection-System-main\Accident-Detection-System-main\model_weights.h5"

if not os.path.exists(model_json_file):
    print(f"Error: '{model_json_file}' not found.")
    exit()

if not os.path.exists(model_weights_file):
    print(f"Error: '{model_weights_file}' not found.")
    exit()
 
model = AccidentDetectionModel(model_json_file, model_weights_file)
font = cv2.FONT_HERSHEY_SIMPLEX

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_accident')
def detect_accident():
    video_path = r"D:\wetransfer_zip_2024-02-22_0704\Accident-Detection-System-main\Accident-Detection-System-main\Demo2.mp4"
    video = cv2.VideoCapture(video_path)  # for camera use video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if pred == "Accident":
            prob_percentage = round(prob[0][0] * 100, 2)
            detection_info = f"Accident detected with probability: {prob_percentage}%"
            return detection_info  # This will stop the video processing and return the detection info

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
