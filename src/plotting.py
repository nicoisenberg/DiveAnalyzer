import matplotlib.pyplot as plt

def save_plot(data, output_path):

    plt.figure(figsize = (8, 5))

    plt.plot(
    data["Date"],
    data["Depth"],
    marker = "o",
    label = "Depth"
    )

    plt.plot(
    data["Date"],
    data["Temperature"],
    marker = "o",
    label = "Temperature"
    )

    plt.title("Dive Depth and Temperature")
    plt.ylabel("Value")
    plt.xlabel("Date")

    plt.legend()
    plt.grid()

    plt.savefig(output_path)

    plt.close()
