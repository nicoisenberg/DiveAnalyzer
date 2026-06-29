import pandas as pd
import matplotlib.pyplot as plt

from src.loader import load_csv
from src.analysis import generate_dive_report
from src.plotting import save_plot

data = load_csv("data/dive_data.csv")

report = generate_dive_report(data)

print(report)

save_plot(
    data,
    "plots/dive_plot.png"
)

