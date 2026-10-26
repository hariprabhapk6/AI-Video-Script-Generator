"""Template-based video script generation with lightweight NLP utilities."""
import random
import re
from datetime import datetime
from collections import Counter

class VideoScriptGenerator:
    def __init__(self):
        self.platform_configs = {
            "youtube": {"label":"YouTube", "wpm":150, "duration":"5–10 minutes", "sections":["hook","intro","main_content","cta"]},
            "youtube_short": {"label":"YouTube Shorts", "wpm":150, "duration":"30–60 seconds", "sections":["hook","content","cta"]},
            "instagram_reel": {"label":"Instagram Reels", "wpm":160, "duration":"15–60 seconds", "sections":["hook","content","cta"]},
            "tiktok": {"label":"TikTok", "wpm":160, "duration":"15–180 seconds", "sections":["hook","content","cta"]},
            "explainer": {"label":"Explainer Video", "wpm":150, "duration":"1–3 minutes", "sections":["hook","problem","solution","cta"]},
            "promotional": {"label":"Promotional Ad", "wpm":150, "duration":"30–120 seconds", "sections":["hook","problem","solution","offer","cta"]}
        }
        self.hooks = {
            "question": ["Have you ever wondered how {topic} can make a difference?","What if you could understand {topic} without the confusion?","Are you ready to discover a smarter way to approach {topic}?"],
            "problem": ["Struggling with {topic}? You're not alone.","Stop making {topic} harder than it needs to be.","If {topic} feels confusing, this is for you."],
            "promise": ["In this video, you'll learn practical ways to approach {topic}.","Stay with me to discover three useful takeaways about {topic}.","By the end, you'll have a clearer plan for {topic}."],
            "story": ["Let's start with a familiar situation involving {topic}.","Imagine facing a challenge with {topic}—where would you begin?","Every useful lesson starts with a question about {topic}."]
        }
        self.ctas = {
            "subscribe": "If this helped you, subscribe for more practical videos and turn on notifications.",
            "comment": "What is your biggest question about {topic}? Share it in the comments.",
            "share": "Share this video with someone who would find {topic} useful.",
            "follow": "Follow for more simple, actionable content about {topic}."
        }
        self.broll = [
            "Show a close-up of the presenter introducing the topic.",
            "Use a screen recording to demonstrate the main idea.",
            "Overlay keywords while the narrator explains each point.",
            "Cut to relevant real-world footage illustrating the concept.",
            "Use a simple diagram or animated steps to summarize the process.",
            "Add a brief recap card with the key takeaway."
        ]

    @staticmethod
    def clean_topic(topic):
        return re.sub(r"\s+", " ", topic).strip()

    @staticmethod
    def word_count(text):
        return len(re.findall(r"\b[\w'-]+\b", text))

    @staticmethod
    def fmt_time(seconds):
        seconds = max(0, int(round(seconds)))
        return f"{seconds // 60}:{seconds % 60:02d}"

    def generate_script(self, topic, platform="youtube", tone="engaging",
                        audience="general audience", goal="educate and engage",
                        hook_type="auto", cta_type="subscribe"):
        topic = self.clean_topic(topic)
        cfg = self.platform_configs[platform]
        if hook_type == "auto" or hook_type not in self.hooks:
            hook_type = random.choice(list(self.hooks.keys()))
        hook = random.choice(self.hooks[hook_type]).format(topic=topic)
        intro = (f"Today we're exploring {topic} for {audience}. "
                 f"Our goal is to {goal}, using clear explanations and practical examples.")
        points = [
            (f"Start with the basics", f"Explain what {topic} means in plain language and why it matters to {audience}."),
            ("Make it practical", f"Walk through one realistic example of {topic}. Keep the explanation {tone} and easy to follow."),
            ("Avoid a common mistake", f"Point out one misconception about {topic}, then explain a more useful approach."),
            ("Recap the takeaway", f"Summarize the main lesson and give viewers one small action they can try today.")
        ]
        content = "\n".join([f"{i+1}. {heading}: {detail}" for i, (heading, detail) in enumerate(points)])
        problem = f"Many people approach {topic} without a clear plan. That can make the process feel harder than it needs to be."
        solution = f"Break {topic} into manageable steps, practise with a real example, and review what works. Choose one action you can take today."
        offer = f"If you want to take the next step with {topic}, use this video as your starting point and build from there."
        cta = self.ctas.get(cta_type, self.ctas["subscribe"]).format(topic=topic)
        section_text = {}
        for section in cfg["sections"]:
            section_text[section] = {
                "hook": hook, "intro": intro, "main_content": content,
                "content": content, "problem": problem, "solution": solution,
                "offer": offer, "cta": cta
            }[section]
        timings = {}
        total_words = 0
        total_seconds = 0
        for name, text in section_text.items():
            words = self.word_count(text)
            seconds = words / cfg["wpm"] * 60
            timings[name] = {"word_count": words, "duration_seconds": round(seconds, 1),
                             "duration_formatted": self.fmt_time(seconds)}
            total_words += words
            total_seconds += seconds
        broll = random.sample(self.broll, 4)
        titles = [
            f"{topic.title()}: A Simple Guide",
            f"How to Understand {topic.title()}",
            f"{topic.title()} Explained in Practical Steps",
            f"3 Things to Know About {topic.title()}"
        ]
        description = f"Learn about {topic} with clear explanations and practical takeaways. This video is designed for {audience}."
        tags = list(dict.fromkeys(re.findall(r"[A-Za-z0-9]+", topic.lower()) + ["howto", "learning", "tips", "explained"]))
        thumbnail = [f"Big readable text: “{topic.title()} Explained”", "Use one clear focal image and strong contrast", "Keep the design uncluttered and mobile-friendly"]
        formatted = self.format_script(topic, cfg["label"], section_text, timings, broll, titles, total_seconds, total_words)
        return {
            "topic": topic, "platform": platform, "platform_label": cfg["label"], "tone": tone,
            "script": section_text, "timings": timings, "total_duration_seconds": round(total_seconds, 1),
            "total_duration_formatted": self.fmt_time(total_seconds), "total_words": total_words,
            "broll_suggestions": broll, "scene_directions": ["[ON CAMERA] Presenter delivers the hook directly to camera.",
              "[CUTAWAY] Show the example while narration continues.", "[ON SCREEN TEXT] Highlight the key takeaway."],
            "sound_cues": ["[MUSIC] Light upbeat instrumental under the opening.", "[SFX] Soft transition sound between major sections.",
              "[MUSIC] Lower background volume during spoken explanation."],
            "title_suggestions": titles, "thumbnail_suggestions": thumbnail,
            "seo_description": description, "seo_tags": tags, "formatted_script": formatted,
            "generated_at": datetime.now().isoformat(timespec="seconds")
        }

    def format_script(self, topic, platform, script, timings, broll, titles, seconds, words):
        lines = [f"VIDEO SCRIPT: {topic.title()}", "="*52, f"Platform: {platform}",
                 f"Estimated duration: {self.fmt_time(seconds)}", f"Total words: {words}", ""]
        for name, text in script.items():
            lines.extend([f"{name.replace('_',' ').upper()} [{timings[name]['duration_formatted']}]", "-"*36, text, ""])
        lines.extend(["B-ROLL SUGGESTIONS", *[f"- {x}" for x in broll], "", "TITLE IDEAS", *[f"- {x}" for x in titles]])
        return "\n".join(lines)
