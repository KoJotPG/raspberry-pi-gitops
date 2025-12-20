from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = redis.get('hits')
    return f"""
    <div style='text-align:center; padding-top:50px; font-family:sans-serif;'>
        <h1>Redis Visit Counter</h1>
        <p style='font-size: 2em;'>This page has been visited <b>{counter}</b> times.</p>
        <p><small>Data stored persistently in Redis on Raspberry Pi</small></p>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)