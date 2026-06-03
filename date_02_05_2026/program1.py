import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].plot([1, 2, 3], [1, 4, 9], color="blue")
axs[0, 0].set_title("Top-Left (0,0)")

axs[0, 1].bar(["A", "B", "C"], [5, 7, 3], color="green")
axs[0, 1].set_title("Top-Right (0,1)")

axs[1, 0].scatter([1, 2, 3], [3, 2, 1], color="red")
axs[1, 0].set_title("Bottom-Left(1,0)")

axs[1, 1].hist([1, 1, 2, 3, 3, 3, 4], bins=4, color="purple")
axs[1, 1].set_title("Bottom-Right(1,1)")

plt.tight_layout()

plt.show()
