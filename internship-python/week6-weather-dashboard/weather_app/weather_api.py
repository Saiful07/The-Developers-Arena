import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict

class WeatherAPI:
    def __init__(self, api_key: str, base_url: str = "http://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_duration = 600  # 10 minutes

    def _get_cached_data(self, cache_key: str) -> Optional[Dict]:
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            if time.time() - cache_file.stat().st_mtime < self.cache_duration:
                try:
                    with open(cache_file, "r") as f:
                        return json.load(f)
                except:
                    pass
        return None

    def _save_to_cache(self, cache_key: str, data: Dict):
        cache_file = self.cache_dir / f"{cache_key}.json"
        with open(cache_file, "w") as f:
            json.dump(data, f, indent=2)

    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params["appid"] = self.api_key
            params["units"] = "metric"
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_current_weather(self, city: str, country_code: str = None) -> Optional[Dict]:
        cache_key = f"current_{city}_{country_code}" if country_code else f"current_{city}"
        cached = self._get_cached_data(cache_key)
        if cached: return cached
        query = f"{city},{country_code}" if country_code else city
        data = self._make_request("weather", {"q": query})
        if data: self._save_to_cache(cache_key, data)
        return data

    def get_forecast(self, city: str, country_code: str = None) -> Optional[Dict]:
        cache_key = f"forecast_{city}_{country_code}" if country_code else f"forecast_{city}"
        cached = self._get_cached_data(cache_key)
        if cached: return cached
        query = f"{city},{country_code}" if country_code else city
        data = self._make_request("forecast", {"q": query})
        if data: self._save_to_cache(cache_key, data)
        return data
