import matplotlib.pyplot as plt

data = [[1, 2, 3, 4], [5, 6, 7, 8], [3, 10, 1, 12], [13, 3, 15, 3]]

plt.imshow(data, cmap="Blues", interpolation="nearest")
# plt.colorbar()
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Heatmap")
plt.show()
