import matplotlib.pyplot as plt
import pandas as pd
import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 55.75,
    "longitude": 37.61,
    "hourly": "temperature_2m",
}


def create_dataframe(hours, temperatures):
    """Создаёт DataFrame и сортирует данные по времени."""
    df = pd.DataFrame(
        {
            "time": pd.to_datetime(hours),
            "temperature_c": temperatures,
        }
    )
    return df.sort_values("time").reset_index(drop=True)


def main():
    response = requests.get(URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    data = response.json()

    hours = data["hourly"]["time"][:24]
    temperatures = data["hourly"]["temperature_2m"][:24]

    df = create_dataframe(hours, temperatures)
    df.to_csv("temperature_24h.csv", index=False)

    fig, ax = plt.subplots()
    ax.plot(df["time"], df["temperature_c"], marker="o")
    ax.set_title("Температура в Москве (24 часа)")
    ax.set_xlabel("Время")
    ax.set_ylabel("°C")
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.savefig("temperature_24h.png", dpi=150)
    plt.close(fig)

    print("Сохранено в temperature_24h.csv")
    print("График сохранён в temperature_24h.png")


if __name__ == "__main__":
    main()
