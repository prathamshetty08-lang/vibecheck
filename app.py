from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion_detector import predict_emotion
from preprocess import preprocess
import json
import nltk
nltk.download('punkt_tab', quiet=True)

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:3000",  # local testing
    "https://vibecheck-frontend-lyart.vercel.app"  # your Vercel frontend
])

# Load your lastfm_results.json once at startup
with open("lastfm_results.json") as f:
    mood_tracks = json.load(f)

# Health check route (GET)
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# Main prediction endpoint (POST)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Check if text is provided
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    text = data["text"]
    
    try:
        # Step 1: Detect emotion
        emotion, confidence = predict_emotion(text)
        
        # Step 2: Get tracks for that emotion
        tracks = mood_tracks.get(emotion, [])
        
        # Step 3: Return as JSON
        return jsonify({
            "emotion": emotion,
            "confidence": float(confidence),
            "tracks": tracks
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)