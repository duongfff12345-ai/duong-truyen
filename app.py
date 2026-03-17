import edge_tts
import asyncio
import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

OUTPUT_FILE = "voice.mp3"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_audio", methods=["POST"])
def create_audio():

    text = request.form["text"]
    voice_type = request.form["voice"]

    voice = "vi-VN-HoaiMyNeural"
    rate = "+0%"
    pitch = "+0Hz"

    if voice_type == "nu_truyen":
        voice = "vi-VN-HoaiMyNeural"
        rate = "-5%"
        pitch = "+20Hz"

    elif voice_type == "nu_ke":
        voice = "vi-VN-HoaiMyNeural"
        rate = "+0%"
        pitch = "+0Hz"

    elif voice_type == "nu_bac":
        voice = "vi-VN-HoaiMyNeural"
        rate = "-10%"
        pitch = "+10Hz"

    elif voice_type == "nu_nam":
        voice = "vi-VN-HoaiMyNeural"
        rate = "+5%"
        pitch = "+5Hz"

    elif voice_type == "nam_tram":
        voice = "vi-VN-NamMinhNeural"
        rate = "-5%"
        pitch = "-20Hz"

    elif voice_type == "nam_ke":
        voice = "vi-VN-NamMinhNeural"
        rate = "+0%"
        pitch = "+0Hz"

    elif voice_type == "nam_bac":
        voice = "vi-VN-NamMinhNeural"
        rate = "-10%"
        pitch = "-10Hz"

    elif voice_type == "nam_nam":
        voice = "vi-VN-NamMinhNeural"
        rate = "+5%"
        pitch = "-5Hz"

    elif voice_type == "nu_halazy":
        voice = "vi-VN-HoaiMyNeural"
        rate = "-7%"
        pitch = "+18Hz"

    elif voice_type == "nu_story_youtube":
        voice = "vi-VN-HoaiMyNeural"
        rate = "-12%"
        pitch = "+8Hz"

    async def generate():
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate=rate,
            pitch=pitch
        )
        await communicate.save(OUTPUT_FILE)

    asyncio.run(generate())

    return render_template("index.html", audio=True)


@app.route("/download")
def download():
    return send_file(OUTPUT_FILE, as_attachment=True)


# QUAN TRỌNG CHO RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
