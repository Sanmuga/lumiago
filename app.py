from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

EMOTIONS = ["Happy", "Sad", "Neutral", "Angry", "Surprised"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file received"}), 400

    audio = request.files['audio']
    filename = os.path.join("temp_audio.wav")
    audio.save(filename)

    # Simulate emotion detection with random choice
    detected_emotion = random.choice(EMOTIONS)

    return jsonify({"emotion": detected_emotion})

if __name__ == '__main__':
    app.run(debug=True)
