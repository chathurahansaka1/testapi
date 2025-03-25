from flask import Flask, request, jsonify
from scraper import generate_image

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    image_url = generate_image(text)
    return jsonify({"image_url": image_url})

if __name__ == "__main__":
    app.run(debug=True)
