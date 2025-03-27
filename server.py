
'''Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

@app.route('/emotionDetector/<dict:detect_emotion>', methods = ('GET','POST'))
def emotion_detector(emotion):
    result = request.get.args()

@app.route('/')
def render_page():
    return render_template("index.html")