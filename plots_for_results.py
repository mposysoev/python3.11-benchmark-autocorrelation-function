from matplotlib import pyplot as plt
import numpy as np

file_sizes = np.array([1000, 10000, 100000])

macos_10 = np.array([30.2 * 10 ** (-3), 1.807, 179.238])
macos_11 = np.array([22.5 * 10 ** (-3), 1.050, 104.061])

linux_10 = np.array([95.2 * 10 ** (-3), 6.012, 611.790])
linux_11 = np.array([64.8 * 10 ** (-3), 4.158, 425.07])

win_10 = np.array([127.2 * 10 ** (-3), 7.993, 796.721])
win_11 = np.array([115.7 * 10 ** (-3), 5.971, 581.504])

file_1000 = np.array(
    [macos_10[0], macos_11[0], linux_10[0], linux_11[0], win_10[0], win_11[0]]
)
file_10000 = np.array(
    [macos_10[1], macos_11[1], linux_10[1], linux_11[1], win_10[1], win_11[1]]
)
file_100000 = np.array(
    [macos_10[2], macos_11[2], linux_10[2], linux_11[2], win_10[2], win_11[2]]
)


# plt.xlabel('Size of the file [lines]')
# plt.xscale('log')
# plt.xticks(file_sizes)

# names_of_bench = [
#     "Mac OS, Python 3.10",
#     "Mac OS, Python 3.11",
#     "Linux, Python 3.10",
#     "Linux, Python 3.11",
#     "Windows, Python 3.10",
#     "Windows, Python 3.11",
# ]
# plt.bar(
#     names_of_bench,
#     file_1000 / file_1000[1] * 100,
#     color=[
#         "deepskyblue",
#         "deepskyblue",
#         "dodgerblue",
#         "dodgerblue",
#         "steelblue",
#         "steelblue",
#     ],
# )
python_ver = ["Py 3.10", "Py 3.11"]
colors = ["teal", "teal"]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=False, figsize=(9, 7))
bars1 = ax1.bar(python_ver, file_1000[0:2] / file_1000[0], color=colors)
ax1.bar_label(bars1)
ax1.set_title("File 1000", fontsize=15)
bars2 = ax2.bar(python_ver, file_10000[0:2] / file_10000[0], color=colors)
ax2.bar_label(bars2)
ax2.set_title("File 10000", fontsize=15)
bars3 = ax3.bar(python_ver, file_100000[0:2] / file_100000[0], color=colors)
ax3.bar_label(bars3)
ax3.set_title("File 100000", fontsize=15)

f.suptitle("Mac OS", fontsize=20, fontweight="bold")


plt.savefig("macos.png")
# plt.show()


colors = ["steelblue", "steelblue"]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=False, figsize=(9, 7))
bars1 = ax1.bar(python_ver, file_1000[2:4] / file_1000[2], color=colors)
ax1.bar_label(bars1)
ax1.set_title("File 1000", fontsize=15)
bars2 = ax2.bar(python_ver, file_10000[2:4] / file_10000[2], color=colors)
ax2.bar_label(bars2)
ax2.set_title("File 10000", fontsize=15)
bars3 = ax3.bar(python_ver, file_100000[2:4] / file_100000[2], color=colors)
ax3.bar_label(bars3)
ax3.set_title("File 100000", fontsize=15)

f.suptitle("Linux", fontsize=20, fontweight="bold")


plt.savefig("linux.png")
# plt.show()

colors = ["seagreen", "seagreen"]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=False, figsize=(9, 7))
bars1 = ax1.bar(python_ver, file_1000[4:] / file_1000[4], color=colors)
ax1.bar_label(bars1)
ax1.set_title("File 1000", fontsize=15)
bars2 = ax2.bar(python_ver, file_10000[4:] / file_10000[4], color=colors)
ax2.bar_label(bars2)
ax2.set_title("File 10000", fontsize=15)
bars3 = ax3.bar(python_ver, file_100000[4:] / file_100000[4], color=colors)
ax3.bar_label(bars3)
ax3.set_title("File 100000", fontsize=15)

f.suptitle("Windows 10", fontsize=20, fontweight="bold")


plt.savefig("windows.png")
