from flask import Flask, render_template_string, jsonify
import psutil

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>System Monitor</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: sans-serif; background: #2c3e50; color: white; text-align: center; }
        .card { background: #34495e; padding: 20px; margin: 20px; border-radius: 10px; display: inline-block; width: 200px; }
        h1 { color: #ecf0f1; }
        .value { font-size: 2em; color: #e74c3c; }
    </style>
</head>
<body>
    <h1>System Monitor</h1>
    <div class="card"><h3>CPU Usage</h3><div class="value">{{ cpu }}%</div></div>
    <div class="card"><h3>RAM Usage</h3><div class="value">{{ ram }}%</div></div>
    <div class="card"><h3>Temperature</h3><div class="value">{{ temp }}°C</div></div>
    <p>Data refreshes every 5 seconds.</p>
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

    return render_template_string(HTML_TEMPLATE, cpu=cpu, ram=ram, temp=temp)

@app.route('/api')
def api():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    try:
        temp = open("/sys/class/thermal/thermal_zone0/temp").read()
        temp = round(int(temp) / 1000, 1)
    except:
        temp = "N/A"
    return jsonify(cpu=cpu, ram=ram, temp=temp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)