from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)

# گرفتن توکن از محیط امن Render
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        question = request.json["question"]
        output = replicate.run(
            "meta/llama-2-7b-chat",
            input={
                "prompt": question,
                "system_prompt": "You are a helpful assistant.",
                "temperature": 0.7,
                "max_new_tokens": 100
            }
        )
        return jsonify({"answer": "".join(output)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # اجرای سرور روی پورت مناسب برای Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))