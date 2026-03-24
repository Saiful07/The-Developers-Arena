from rich.console import Console
console = Console()

def show_current_weather(weather):
    if "error" in weather:
        console.print(f"[red]Error: {weather['error']}[/red]")
        return
    console.print(f"[bold cyan]{weather['city']}[/bold cyan]")
    console.print(f"🌡️ Temp: {weather['temp']}°C")
    console.print(f"💧 Humidity: {weather['humidity']}%")
    console.print(f"🌬️ Wind: {weather['wind']} m/s")
    console.print(f"☁️ Condition: {weather['condition']}")

def show_forecast(forecast):
    if "error" in forecast:
        console.print(f"[red]Error: {forecast['error']}[/red]")
        return
    console.print("\n[bold green]5-Day Forecast[/bold green]")
    for entry in forecast[:5]:
        console.print(f"{entry['datetime']} → {entry['temp']}°C, {entry['condition']}")
