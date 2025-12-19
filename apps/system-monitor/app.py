from flask import Flask, render_template_string
import psutil
import socket

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Berry Monitor</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: sans-serif; background: #2c3e50; color: white; text-align: center; }
        .card { background: #34495e; padding: 20px; margin: 20px; border-radius: 10px; display: inline-block; width: 200px; }
        h1 { color: #ecf0f1; }
        .value { font-size: 2em; color: #e74c3c; }
    </style>
</head>
<body>
    <h1>System Monitor: {{ hostname }}</h1>
    <div class="card"><h3>CPU</h3><div class="value">{{ cpu }}%</div></div>
    <div class="card"><h3>RAM</h3><div class="value">{{ ram }}%</div></div>
    <div class="card"><h3>TEMP</h3><div class="value">{{ temp }}°C</div></div>
    <p>Dane odświeżają się co 5 sekund.</p>
</body>
</html>
"""


@app.route('/')
def index():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    try:
        temp = open("/sys/class/thermal/thermal_zone0/temp").read()
        temp = round(int(temp) / 1000, 1)
    except:
        temp = "N/A"

    return render_template_string(HTML_TEMPLATE,
                                  cpu=cpu, ram=ram, temp=temp,
                                  hostname=socket.gethostname())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)