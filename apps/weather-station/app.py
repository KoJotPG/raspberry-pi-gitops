from flask import Flask, render_template_string
import requests
import psutil

app = Flask(__name__)

def get_weather():
    # Przykład dla Warszawy (szerokość: 52.23, długość: 21.01)
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&current_weather=true"
    try:
        response = requests.get(url).json()
        return response['current_weather']
    except:
        return None

@app.route('/')
def index():
    weather = get_weather()
    cpu_temp = "N/A"
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            cpu_temp = round(int(f.read()) / 1000, 1)
    except:
        pass

    return render_template_string("""
    <div style='text-align:center; font-family:sans-serif; background:#f0f2f5; padding:50px;'>
        <div style='background:white; display:inline-block; padding:20px; border-radius:15px; shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h2>Stacja Pogodowa Raspberry Pi</h2>
            <hr>
            <p>Temperatura CPU: <b style='color:red;'>{{ cpu_temp }}°C</b></p>
            {% if weather %}
                <p>Pogoda na zewnątrz: <b style='color:blue;'>{{ weather.temperature }}°C</b></p>
                <p>Prędkość wiatru: {{ weather.windspeed }} km/h</p>
            {% else %}
                <p>Nie udało się pobrać danych pogodowych.</p>
            {% endif %}
        </div>
    </div>
    """, cpu_temp=cpu_temp, weather=weather)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)