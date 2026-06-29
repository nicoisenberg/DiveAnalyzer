import pandas as pd
import matplotlib.pyplot as plt

from src.loader import load_csv
from src.analysis import generate_dive_report

data = load_csv("data/dive_data.csv")
report = generate_dive_report(data)

print(report)

