# Project Report: AI Video Script Generator

**Task ID:** AI-CM-007  
**Student Code:** DAS010027  
**Domain:** Content Creation & Marketing Generative AI

## 1. Objective
The objective is to develop a tool that helps content creators draft platform-specific video scripts with hooks, structured content, calls to action, timing estimates, and production/marketing suggestions.

## 2. Implementation
The application uses Python for the script generation engine and Flask to serve a web interface. A platform configuration specifies the script sections and speaking rate. Reusable templates generate the hook, introduction, main content, problem/solution, offer, and CTA. The interface lets users choose a platform, tone, audience, goal, hook style, and CTA style.

## 3. Features
- Six output formats: YouTube, YouTube Shorts, Instagram Reels, TikTok, explainer, and promotional video.
- Word count and section-level duration estimation.
- B-roll, scene direction, sound cue, title, thumbnail, description, and SEO tag suggestions.
- Copy and text export.
- Flask JSON generation endpoint and health endpoint.

## 4. Timing logic
For each section, the system counts words and estimates duration with:

**Duration in seconds = (word count ÷ words per minute) × 60**

The configured rate is 150 words per minute for most formats and 160 for short-form formats. The estimate does not account fully for pauses, visual-only sequences, or editing.

## 5. Limitations and future work
The current version is template-based rather than an LLM-powered generator. Some suggestions are reusable patterns and may require human editing for accuracy, originality, and brand voice. Future work could add a verified LLM API, NLTK tokenization, saved script history, language selection, and automated evaluation of script readability.

## 6. Conclusion
The project demonstrates a complete Python web application for structured script drafting and platform-aware content planning. The output should be reviewed by a creator before publication.
