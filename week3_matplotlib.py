import matplotlib.pyplot as plt

# Sample workout data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
calories = [200, 250, 180, 300, 270]

# Create a line graph
plt.plot(days, calories, marker="o")

# Add title and labels
plt.title("Calories Burned During the Week")
plt.xlabel("Days")
plt.ylabel("Calories")

# Display the graph
plt.show()