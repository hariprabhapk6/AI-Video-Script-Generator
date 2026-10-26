from flask import Flask, render_template, request, jsonify, send_file
from generator import VideoScriptGenerator
from io import BytesIO
import json

app = Flask(__name__)
generator = VideoScriptGenerator()

@app.route("/")
def index():
    return render_template("index.html", platforms=generator.platform_configs)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or request.form.to_dict()
    topic = (data.get("topic") or "").strip()
    if len(topic) < 2:
        return jsonify({"error": "Please enter a topic with at least 2 characters."}), 400
    platform = data.get("platform", "youtube")
    if platform not in generator.platform_configs:
        return jsonify({"error": "Please select a supported platform."}), 400
    result = generator.generate_script(
        topic=topic,
        platform=platform,
        tone=data.get("tone", "engaging"),
        audience=(data.get("audience") or "general audience").strip(),
        goal=(data.get("goal") or "educate and engage").strip(),
        hook_type=data.get("hook_type", "auto"),
        cta_type=data.get("cta_type", "subscribe")
    )
    return jsonify(result)

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json(silent=True) or {}
    content = data.get("formatted_script", "")
    if not content:
        return jsonify({"error": "Generate a script first."}), 400
    return send_file(BytesIO(content.encode("utf-8")), mimetype="text/plain",
                     as_attachment=True, download_name="video_script.txt")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "AI Video Script Generator"})

if __name__ == "__main__":
    app.run(debug=True)
