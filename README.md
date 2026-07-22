# VibeCheck

A mood-based music recommender that detects your emotion from text and suggests matching songs from Last.fm.

## Tech Stack
- **Frontend**: React + Vite (deployed on Vercel)
- **Backend**: Flask + gunicorn (deployed on Render)
- **Emotion Detection**: HuggingFace transformers (distilbert)
- **Music API**: Last.fm

## Live Demo
https://vibecheck-frontend-lyart.vercel.app

## How to Run Locally

### Backend
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
export LASTFM_API_KEY=your_key
export LASTFM_API_SECRET=your_secret
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Features
- Detect emotions (joy, sadness, anger, fear, love, surprise)
- Get 5 Last.fm songs matching the emotion
- Click songs to open Last.fm page

## Deployed URLs
- Frontend: https://vibecheck-frontend-lyart.vercel.app
- Backend: https://vibecheck-tcoz.onrender.com
