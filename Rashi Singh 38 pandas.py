
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv("weather.csv")

# 2. Display weather data
print("WEATHER DATA")
print(df)

# 3. Calculate temperature statistics
print("\nTEMPERATURE STATISTICS")
print("Average Temperature:", df["Temperature"].mean())
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())

# 4. Find the hottest day
day = df.loc[df["Temperature"].idxmax(), "Day"]
print("Hottest Day:", day)

# 5. Line chart
plt.figure()
plt.plot(df["Day"], df["Temperature"], marker="o")
plt.title("Daily Temperature Changes")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()

# 6. Histogram
plt.figure()
plt.hist(df["Temperature"], bins=5, edgecolor="black")
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

# 7. Scatter plot
plt.figure()
plt.scatter(df["Humidity"], df["Temperature"])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
