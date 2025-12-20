from flask import Flask, render_template_string
import requests
from datetime import datetime

app = Flask(__name__)


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&current=temperature_2m,precipitation,wind_speed_10m&timezone=auto"
    try:
        response = requests.get(url).json()
        return response
    except:
        return None


@app.route('/')
def index():
    data = get_weather()

    if data:
        current = data.get('current', {})
        weather_info = {
            "city": "Kraków",
            "time": datetime.now().strftime("%H:%M:%S"),
            "temp": current.get('temperature_2m'),
            "precipitation": current.get('precipitation'),
            "wind": current.get('wind_speed_10m'),
            "lat": data.get('latitude'),
            "lon": data.get('longitude'),
            "elevation": data.get('elevation')
        }
    else:
        weather_info = None

    return render_template_string("""
    <div style='text-align:center; font-family:sans-serif; background:#f0f2f5; padding:50px;'>
        <div style='background:white; display:inline-block; padding:30px; border-radius:15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align:left;'>
            <h2 style='text-align:center; margin-top:0;'>Weather Station</h2>
            <hr>
            {% if w %}
                <p><b>City:</b> {{ w.city }}</p>
                <p><b>Time:</b> {{ w.time }}</p>
                <p><b>Temperature:</b> <span style='color: #e67e22; font-weight:bold;'>{{ w.temp }}°C</span></p>
                <p><b>Precipitation:</b> {{ w.precipitation }} mm</p>
                <p><b>Wind:</b> {{ w.wind }} km/h</p>
                <p><b>Location Coordinates:</b> {{ w.lat }}°N, {{ w.lon }}°E</p>
                <p><b>Elevation:</b> {{ w.elevation }} m a.s.l.</p>
            {% else %}
                <p style='color:red;'>Error fetching weather data.</p>
            {% endif %}
        </div>
    </div>
    """, w=weather_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)