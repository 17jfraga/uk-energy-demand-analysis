pip install requests
import requests
import pandas as pd
import time

all_data = []

for day in pd.date_range(
    "2025-01-01",
    "2025-12-31",
    freq="D"
):
    date = day.strftime("%Y-%m-%d")

    start = f"{date}T00:00Z"

    next_day = (
        day + pd.Timedelta(days=1)
    ).strftime("%Y-%m-%d")

    end = f"{next_day}T00:00Z"

    url = (
        "https://api.carbonintensity.org.uk/"
        f"intensity/{start}/{end}"
    )

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        observations = response.json()["data"]

        all_data.extend(observations)

        print(f"Downloaded: {date}")

        time.sleep(0.2)

    except requests.RequestException as error:
        print(f"Failed: {date} - {error}")

carbon_df = pd.json_normalize(all_data)

carbon_df = carbon_df[
    ["from", "to", "intensity.actual"]
]

carbon_df.columns = [
    "start_time",
    "end_time",
    "carbon_intensity"
]

carbon_df.to_csv(
    "data/carbon_intensity_2025.csv",
    index=False
)

print("\nTotal observations:", len(carbon_df))
print(carbon_df.head())

