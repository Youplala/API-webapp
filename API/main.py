import os
from flask import Flask, jsonify, request
from transformers import pipeline
import json

app = Flask(__name__)

model_path = "./beto-emotion"


@app.route('/')
def classify():
  # Your function
  classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
  return jsonify(classify("i like this i love it"))

@app.route('/run', methods = ['POST']) 
def run():
  classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
  user_data = json.loads(str(request.get_json()))
  
  try:
    api = str(user_data["api_key"])
    text = str(user_data["input"])
    if api != "mysupersecret":
      return jsonify({"status": 'Authentification error: API key not valid'})
    elif len(text) <= 2:
      return jsonify({"status": 'Input error: No text or text too short'})
  except:
    return jsonify({"status": 'API not responding'})
  return jsonify(classify(text))
  
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
