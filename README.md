# Lumigram

[![Live Demo](https://img.shields.io/badge/Demo-Vercel-black?style=for-the-badge&logo=vercel)](https://lumigram.vercel.app/)

A full-featured social media web application built with Django, Django REST Framework, and modern frontend templates.

🌐 **Live URL:** [https://lumigram.vercel.app/](https://lumigram.vercel.app/)

## ✨ Features
- **Feed & Posts:** Create, view, like, comment, and share image and video posts with custom filters and post analytics.
- **Reels:** Short video reel feed with continuous playback, likes, and comments.
- **Direct Messaging (Messenger):** Send text, shared posts, and images.
- **Audio Features:** Audio transcriptions, voice translation, and audio search support.
- **Explore & Search:** Explore trending media, user profiles, and hashtag feeds.
- **User Authentication:** Registration, profile personalization, notifications, and profile privacy controls.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- `pip` and `virtualenv`

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/syedafraz2005-png/Lumigram.git
   cd Lumigram
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv env
   # On Windows:
   .\env\Scripts\activate
   # On Linux/macOS:
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r Lumigram/requirements.txt
   ```

4. **Run migrations (optional if using included SQLite DB):**
   ```bash
   python Lumigram/manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python Lumigram/manage.py runserver 0.0.0.0:8000
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.
