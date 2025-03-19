from flask import Flask, jsonify
import json

app = Flask(__name__)

# Endpoint pour récupérer les tweets
@app.route('/tweets', methods=['GET'])
def get_tweets():
    try:
        with open("Data/tweets.json", "r", encoding="utf-8") as file:
            tweets = json.load(file)
        return jsonify(tweets)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
