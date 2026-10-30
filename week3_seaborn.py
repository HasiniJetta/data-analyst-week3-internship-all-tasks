import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
df = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Calories": [200, 250, 180, 300, 270]
})

# Create a bar graph using Seaborn
sns.barplot(data=df, x="Day", y="Calories")

# Add a title and labels
plt.title("Daily Calories Burned")
plt.xlabel("Day")
plt.ylabel("Calories")

# Display the graph
plt.show()