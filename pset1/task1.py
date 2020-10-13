import pandas as pd
import matplotlib.pyplot as plt

fname = "./data/fire_nrt_V1_96617.csv"

data = pd.read_csv(fname)
xlabel = "Longitude (°)"
ylabel = "Latitude (°)"
sampling_rate = 1000

fig, axs = plt.subplots(2, 2)

axs[0, 0].scatter(data.longitude, data.latitude)
axs[0, 1].scatter(data.longitude, data.latitude, s=2, alpha=0.01)
axs[1, 0].scatter(data.longitude[::sampling_rate], data.latitude[::sampling_rate])
hb = axs[1, 1].hexbin(data.longitude, data.latitude, bins="log")

for ax in axs.flat:
    ax.set(xlabel=xlabel, ylabel=ylabel)

axs[0, 0].set_title("Observed Fires")
axs[0, 1].set_title("Observed Fires")
axs[1, 0].set_title(
    "Observed Fires" "\n" f"(downsampled to {sampling_rate}" r"$^{-1}$)"
)
axs[1, 1].set_title("Observed Fire Count by Bin")

cb = fig.colorbar(hb, ax=axs[1, 1])
cb.set_label("count")

plt.tight_layout()
plt.show()
