import matplotlib.pyplot as plt

def save_plot(data, x_column, y_columns, output_path, title, y_label):

    plt.figure(figsize = (8, 5))

    for y_column in y_columns:
        plt.plot(
            data[x_column],
            data[y_column],
            marker = "o",
            label = y_column
        )

    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_column)

    plt.legend()
    plt.grid()
    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()
