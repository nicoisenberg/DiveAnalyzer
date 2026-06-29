import pandas as pd
import matplotlib.pyplot as plt
import sys

from src.loader import load_csv
from src.analysis import generate_dive_report
from src.plotting import save_plot
from src.report import save_report

data = load_csv("data/dive_data.csv")

if data is None:
    print("Program terminated.")
    sys.exit(1)

report = generate_dive_report(data)

print(report)

save_plot(
    data,
    "plots/dive_plot.png"
)

save_report(
    report,
    "reports/dive_report.txt"
)

