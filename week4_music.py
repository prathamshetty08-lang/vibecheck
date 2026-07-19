import requests
import json
import os
from emotion_detector import predict_emotion

# Use environment variable - store your API key there
# export LASTFM_API_KEY='your-key-here'
API_KEY = os.environ.get("LASTFM_API_KEY")

if not API_KEY:
    print("ERROR: LASTFM_API_KEY environment variable not set")
    print("Run: export LASTFM_API_KEY='your-api-key'")
    exit(1)

def fetch_tracks(tag="happy", limit=5):
    """
    Fetch top tracks for a given mood tag from Last.fm
    
    Returns list of dicts with:
    - song: track name
    - artist: artist name
    - cover_image: album art URL (None if unavailable)
    - url: Last.fm track page URL
    """
    url = "https://ws.audioscrobbler.com/2.0/"

    params = {
        "method": "tag.gettoptracks",
        "tag": tag,
        "api_key": API_KEY,
        "format": "json",
        "limit": limit
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"API error for tag '{tag}': {e}")
        return []

    tracks = []

    # Handle empty results
    if "tracks" not in data or "track" not in data["tracks"]:
        print(f"No tracks found for mood: {tag}")
        return []

    for track in data["tracks"]["track"][:limit]:
        # Safely fetch cover image
        cover_image = None
        try:
            if "image" in track and track["image"]:
                # Get the largest image (usually last in array)
                cover_image = track["image"][-1].get("#text")
        except:
            cover_image = None

        tracks.append({
            "song": track.get("name", "Unknown"),
            "artist": track.get("artist", {}).get("name", "Unknown"),
            "cover_image": cover_image,
            "url": track.get("url", "")
        })

    return tracks


# ===== INTERACTIVE TEST (for quick testing) =====
print("=== Interactive Test ===")
user_text = input("How are you feeling today? ")
emotion, score = predict_emotion(user_text)
print(f"\nDetected emotion: {emotion}")
print(f"Confidence: {score:.2%}\n")

tracks = fetch_tracks(emotion)
if tracks:
    print(f"Top 5 tracks for {emotion}:")
    for i, track in enumerate(tracks, 1):
        print(f"{i}. {track['song']} - {track['artist']}")
        if track['cover_image']:
            print(f"   Cover: {track['cover_image']}")
        print(f"   URL: {track['url']}\n")


# ===== SYSTEMATIC TEST - ALL 6 EMOTIONS (for assignment submission) =====
print("\n" + "="*60)
print("Testing all 6 emotions for Week 4 submission...")
print("="*60 + "\n")

moods = ["joy", "sadness", "anger", "fear", "love", "surprise"]
all_results = {}

for mood in moods:
    print(f"Fetching tracks for: {mood}...")
    all_results[mood] = fetch_tracks(mood, limit=5)
    print(f"  ✓ Got {len(all_results[mood])} tracks\n")

# Save to JSON
output_file = "lastfm_results.json"
with open(output_file, "w") as f:
    json.dump(all_results, f, indent=2)

print(f"✓ Results saved to {output_file}")
print("\nSample output (joy):")
for i, track in enumerate(all_results["joy"][:3], 1):
    print(f"{i}. {track['song']} - {track['artist']}")