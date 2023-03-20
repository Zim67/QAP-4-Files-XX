import matplotlib.pyplot as plt

# Create data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [10000, 15000, 12000, 18000, 20000, 16000, 22000, 25000, 30000, 28000, 32000, 35000]

# Create line graph
plt.plot(months, sales)

# Customize graph
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)

# Display graph
plt.show()
