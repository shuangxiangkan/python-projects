import matplotlib.pyplot as plt

values = list(range(1, 5000))
values_cube = [num**3 for num in values]

plt.scatter(values, values_cube, edgecolors="none", c=values_cube, cmap=plt.cm.Reds, s=40)

# Set chart title and label axes
plt.title("cube numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Cube of Value", fontsize=24)


# Set size of tick labels
plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()
