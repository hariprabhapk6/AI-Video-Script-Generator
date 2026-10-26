# Scriptly — AI Video Script Generator

**Internship Task:** AI-CM-007  
**Student Code:** DAS010027  
**Domain:** Content Creation & Marketing Generative AI

Scriptly is a responsive Flask web application that creates structured, template-powered video scripts for YouTube, YouTube Shorts, Instagram Reels, TikTok, explainer videos, and promotional ads.

## Features
- Platform-specific section structure and estimated speaking time
- Hook styles: question, problem, promise, and story
- Main content, introduction, problem/solution, offer, and CTA sections
- Word counts and per-section timing estimates
- B-roll, scene direction, music and sound-effect cues
- Title and thumbnail suggestions
- SEO description and tags
- Copy and export generated scripts as a text file
- JSON response endpoint; no database or paid API key required

## Tech stack
Python, Flask, lightweight regular-expression NLP utilities, HTML, CSS, JavaScript, NLTK and Pandas listed as learning/extension dependencies.

> Current generation is rule/template-based and does not call an LLM. Describe it accurately in demos. A real LLM integration can be added later with an API key.

## Run on Windows
1. Install Python 3.10+.
2. Extract this project folder and open it in VS Code.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt and run:
```bat
.venv\Scripts\activate.bat
```

5. Install dependencies:
```powershell
python -m pip install -r requirements.txt
```

6. Start the app:
```powershell
python app.py
```

7. Open `http://127.0.0.1:5000` in your browser.

## API
- `GET /` — web interface
- `POST /generate` — accepts JSON fields `topic`, `platform`, `tone`, `audience`, `goal`, `hook_type`, `cta_type`
- `GET /health` — health check

Example:
```json
{
  "topic": "Python tips for beginners",
  "platform": "instagram_reel",
  "tone": "casual",
  "audience": "college students",
  "goal": "teach useful coding habits",
  "hook_type": "question",
  "cta_type": "comment"
}
```

## Screenshots for submission
Capture at least five screenshots after running the app:
1. Empty/home screen
2. Settings filled before generation
3. Generated script and section timing
4. B-roll, scene direction, and sound cue suggestions
5. Title, thumbnail, and SEO suggestions

## Demo outline
1. Introduce AI-CM-007 and the project objective.
2. Generate one YouTube script.
3. Generate one Instagram Reel or TikTok script.
4. Explain hooks, CTAs, word counts, and timing estimation.
5. Show B-roll, titles, thumbnails, SEO tags, and export.
6. Explain that timing is estimated from word count and configured words-per-minute.

## Timing formula
`estimated seconds = word count / words per minute × 60`

Timing is an estimate, not a guarantee; delivery speed, pauses, and editing affect actual video length.

## Task reference
Add the official internship task page URL here before submission, if available. Submit the GitHub repository and demo link in the internship blog post under **Task Submit**, using the required title format.
