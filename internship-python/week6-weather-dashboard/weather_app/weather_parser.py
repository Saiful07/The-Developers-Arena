from datetime import datetime

def parse_current_weather(data):
    if "error" in data: return data
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "condition": data["weather"][0]["description"]
    }

def parse_forecast(data):
    if "error" in data: return data
    forecast = []
    for entry in data["list"]:
        forecast.append({
            "datetime": datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%a %H:%M"),
            "temp": entry["main"]["temp"],
            "condition": entry["weather"][0]["description"]
        })
    return forecast
