from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)
os.environ["REPLICATE_API_TOKEN"] = "توکن خودت اینجا"

@app.route("/ask", methods=["POST"])
def ask():
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

if __name__ == "__main__":
    app.run()