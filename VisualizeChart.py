import matplotlib.pyplot as plt
import pandas as pd

# Load the data from CSV
data = pd.read_csv("rank_history.csv")

# Convert the 'Date' column to datetime with the correct format
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Convert 'Rank' column to integers, removing commas
data['Rank'] = data['Rank'].replace({',': ''}, regex=True).astype(int)

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Rank'], marker='o')
plt.title("LeetCode Rank Over Time")
plt.xlabel("Date")
plt.ylabel("Rank")
plt.gca().invert_yaxis()  # Rank 1 is the best!
plt.grid(True)
plt.tight_layout()
plt.show()
