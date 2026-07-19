import sys
import argparse

from src.loader import load_csv
from src.analysis import generate_dive_report
from src.plotting import save_plot
from src.report import save_report
from src.validation import validate_required_columns, validate_not_empty

parser = argparse.ArgumentParser(
    description="Analyze dive data from a CSV file."
)

parser.add_argument(
    "csv_path",
    help="Path to the CSV file containing dive data."
)

args = parser.parse_args()

data = load_csv(args.csv_path)

if data is None:
    print("Program terminated.")
    sys.exit(1)

required_columns = [
    "Date",
    "Depth",
    "Temperature"
]

if not validate_not_empty(data):
    sys.exit(1)

if not validate_required_columns(data, required_columns):
    sys.exit(1)

report = generate_dive_report(data)

print(report)

save_plot(
    data=data,
    x_column="Date",
    y_columns=["Depth", "Temperature"],
    output_path="plots/dive_plot.png",
    title="Dive Depth and Temperature",
    y_label="Value"
)

save_report(
    report,
    "reports/dive_report.txt"
)

