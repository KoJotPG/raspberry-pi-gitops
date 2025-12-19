from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = redis.get('hits')
    return f"""
    <div style='text-align:center; padding-top:50px; font-family:sans-serif;'>
        <h1>Licznik odwiedzin Redis</h1>
        <p style='font-size: 2em;'>Ta strona została odwiedzona <b>{counter}</b> razy.</p>
        <p><small>Dane zapisane trwale w bazie Redis na Raspberry Pi</small></p>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)