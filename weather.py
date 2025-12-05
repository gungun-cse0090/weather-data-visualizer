import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# LOAD DATASET
# ------------------------------------------------------------
def load_dataset(path: str):
    print("\nLoading dataset...\n")
    df = pd.read_csv(path)
    print(df.head(), "\n")
    print(df.info(), "\n")
    return df

# ------------------------------------------------------------
# CLEAN DATASET
# ------------------------------------------------------------
def clean_dataset(df):
    print("\nCleaning data...\n")

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    # Fill missing numeric values
    numeric_cols = ["Temperature", "Rainfall", "Humidity"]
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    df = df[["Date", "Temperature", "Rainfall", "Humidity"]]
    print(df.head(), "\n")
    return df

# ------------------------------------------------------------
# STATISTICS
# ------------------------------------------------------------
def compute_statistics(df):
    print("\nComputing statistics...\n")

    daily_stats = {
        "mean": df["Temperature"].mean(),
        "min": df["Temperature"].min(),
        "max": df["Temperature"].max(),
        "std": df["Temperature"].std()
    }

    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year

    monthly_stats = df.groupby("Month").agg({
        "Temperature": ["mean", "min", "max"],
        "Rainfall": "sum"
    })

    yearly_stats = df.groupby("Year").agg({
        "Temperature": "mean",
        "Rainfall": "sum"
    })

    print("Daily:", daily_stats, "\n")
    print("Monthly Stats:\n", monthly_stats, "\n")
    print("Yearly Stats:\n", yearly_stats, "\n")

    return daily_stats, monthly_stats, yearly_stats

# ------------------------------------------------------------
# PLOTS
# ------------------------------------------------------------
def generate_plots(df):
    print("\nGenerating plots...\n")

    # Temperature trend
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Temperature"])
    plt.title("Daily Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.savefig("temperature_trend.png")
    plt.show()

    # Monthly rainfall
    monthly_rain = df.groupby("Month")["Rainfall"].sum()
    plt.figure(figsize=(10, 5))
    plt.bar(monthly_rain.index, monthly_rain.values)
    plt.title("Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall")
    plt.savefig("monthly_rainfall.png")
    plt.show()

    # Scatter
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Humidity"], df["Temperature"])
    plt.xlabel("Humidity")
    plt.ylabel("Temperature")
    plt.title("Humidity vs Temperature")
    plt.savefig("humidity_vs_temperature.png")
    plt.show()

# ------------------------------------------------------------
# SEASONAL ANALYSIS
# ------------------------------------------------------------
def seasonal_analysis(df):
    print("\nSeasonal analysis...\n")

    season_map = {
        12:"Winter", 1:"Winter", 2:"Winter",
        3:"Spring", 4:"Spring", 5:"Spring",
        6:"Summer", 7:"Summer", 8:"Summer",
        9:"Autumn", 10:"Autumn", 11:"Autumn"
    }

    df["Season"] = df["Month"].map(season_map)

    season_stats = df.groupby("Season").agg({
        "Temperature": "mean",
        "Rainfall": "sum",
        "Humidity": "mean"
    })

    print(season_stats, "\n")
    return season_stats

# ------------------------------------------------------------
# EXPORT RESULTS
# ------------------------------------------------------------
def export_results(df, daily, monthly, seasonal):
    print("\nExporting results...\n")

    df.to_csv("cleaned_weather.csv", index=False)

    with open("summary_report.txt", "w") as f:
        f.write("WEATHER DATA ANALYSIS REPORT\n")
        f.write("=============================================\n\n")

        f.write("Daily Temperature Stats:\n")
        f.write(str(daily) + "\n\n")

        f.write("Monthly Rainfall (Sum):\n")
        f.write(str(monthly["Rainfall"]["sum"]) + "\n\n")

        f.write("Seasonal Statistics:\n")
        f.write(str(seasonal) + "\n")

    print("✔ cleaned_weather.csv saved")
    print("✔ summary_report.txt saved\n")

# ------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------
def main():
    df = load_dataset("weather.csv")
    df = clean_dataset(df)
    daily, monthly, yearly = compute_statistics(df)
    generate_plots(df)
    seasonal = seasonal_analysis(df)
    export_results(df, daily, monthly, seasonal)

if __name__ == "__main__":
    main()
