🌦️ Weather Data Visualizer

Mini Project | Programming for Problem Solving using Python

This project analyzes real-world weather data, performs statistical computations, and visualizes temperature, rainfall, and humidity trends using Pandas, NumPy, and Matplotlib.

The dataset used contains daily weather records from Jan–Jun 2024, including Temperature, Rainfall, and Humidity.

📌 Objectives of the Project

Load and clean weather data

Compute daily, monthly, yearly, and seasonal statistics

Generate meaningful visualizations

Automate reporting with CSV + text output

Gain experience with Pandas, NumPy, and Matplotlib

📁 Dataset Used
Date,Temperature,Rainfall,Humidity
2024-01-01,25,0,40
2024-01-02,26,1,42
2024-01-03,24,0,38
2024-01-04,27,3,48
2024-01-05,28,0,45
2024-02-01,22,5,52
2024-02-02,23,0,47
2024-02-03,24,2,49
2024-03-01,30,0,35
2024-03-02,31,1,33
2024-03-03,29,0,36
2024-04-01,32,0,30
2024-04-02,33,0,28
2024-04-03,34,0,27
2024-05-01,35,0,25
2024-05-02,36,0,26
2024-05-03,37,1,20
2024-06-01,34,10,60
2024-06-02,33,12,63
2024-06-03,32,8,58


Total records: 19
Months covered: Jan–Jun 2024

🗂️ Project Structure
weather-data-visualizer/
│
├── weather.py                   # Main program
├── weather.csv                  # Raw dataset
│
├── cleaned_weather.csv          # Processed dataset
├── summary_report.txt           # Auto-generated analysis report
│
├── temperature_trend.png        # Line chart
├── monthly_rainfall.png         # Bar chart
├── humidity_vs_temperature.png  # Scatter plot
│
└── README.md                    # Documentation

🔧 Technologies Used

Python 3

Pandas → data cleaning & processing

NumPy → numeric calculations

Matplotlib → plots & charts

📊 Features & Analysis Performed
🔹 1. Data Cleaning

Converted Date → datetime

Removed invalid rows

Filled missing numeric values with mean

Kept essential columns:

Date

Temperature

Rainfall

Humidity

🔹 2. Statistical Analysis
✅ Daily Temperature Statistics

Mean

Minimum

Maximum

Standard Deviation

✅ Monthly Analysis

Average Temperature

Min/Max Temperature

Total Rainfall per month

✅ Yearly Analysis

Mean Annual Temperature

Total Annual Rainfall

🔹 3. Seasonal Analysis

Seasons used:

Season	Months
Winter	Dec–Feb
Spring	Mar–May
Summer	Jun–Aug
Autumn	Sep–Nov

For each season, the program computes:

Average temperature

Total rainfall

Average humidity

🔹 4. Visualizations (Auto Generated)
Plot	Description
temperature_trend.png	Daily temperature line chart
monthly_rainfall.png	Bar chart of rainfall by month
humidity_vs_temperature.png	Scatter plot (Humidity vs Temperature)
▶️ How to Run the Project
Install dependencies
pip install pandas numpy matplotlib

Run the script
python weather.py


After running:

Cleaned CSV will be saved

Text report will be generated

All graphs will be saved automatically

📤 Generated Output Files

cleaned_weather.csv

summary_report.txt

temperature_trend.png

monthly_rainfall.png

humidity_vs_temperature.png



📘 Summary Report Contains

Daily temperature summary

Monthly rainfall totals

Seasonal averages

Key trends and patterns

💡 Key Insights 

✨ January–May shows almost no rainfall, except light showers
✨ Heavy rainfall starts in June (10–12 mm)
✨ Temperature gradually increases from Jan (24–28°C) → May (35–37°C)
✨ Humidity dips in summer (20–30%) and peaks again in June (58–63%)



👩‍💻 Author

Gungun
B.Tech CSE (Data Science)
K.R. Mangalam University
