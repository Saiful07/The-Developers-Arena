🌦️ Week 6 Weather Dashboard
A command-line weather dashboard built in Python that integrates with the OpenWeatherMap API.
It fetches current weather and 5-day forecasts for any city worldwide, with caching, error handling, and a user-friendly CLI.

✨ Features
Fetch current weather for any city

Display 5-day forecast with daily summaries

Show details: temperature, humidity, wind speed, conditions

Temperature unit toggle (°C ↔ °F)

Autocomplete city search (via Geocoding API)

Favorites management (favorites.json)

Error handling for API failures

Caching to reduce API calls

Color-coded CLI output with ASCII icons

📂 Project Structure
Code
week6-weather-dashboard/
│── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│── data/
│   ├── cache/
│   └── favorites.json
│── tests/
│   ├── test_api.py
│   ├── test_parser.py
│   └── test_display.py
│── requirements.txt
│── README.md
└── .gitignore
⚙️ Installation
Clone the repository:

bash
git clone https://github.com/your-username/week6-weather-dashboard.git
cd week6-weather-dashboard
Install dependencies:

bash
pip install -r requirements.txt
Add your OpenWeatherMap API key in weather_app/config.py:

python
API_KEY = "your_actual_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5"
▶️ Usage
Run the app from the project root:

bash
python -m weather_app.main
Example interaction:

Code
Enter city name: Jamshedpur
🌡️ Temp: 32°C
💧 Humidity: 45%
🌬️ Wind: 3.5 m/s
☁️ Condition: clear sky

5-Day Forecast
Tue 12:00 → 33°C, scattered clouds
Wed 12:00 → 34°C, light rain
...
🧪 Testing
Run unit tests with:

bash
pytest tests/
📌 Notes
Free API keys may take 10–15 minutes to activate after creation.

Cached responses are stored in data/cache/.

Favorites are stored in data/favorites.json.

📜 License
This project is for educational purposes. You may adapt and extend it freely.