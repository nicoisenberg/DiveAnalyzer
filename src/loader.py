import pandas as pd

def load_csv(file_path):
    
    try:
        data = pd.read_csv(file_path)
        return data
        
    except FileNotFoundError:
        print(f"Error: Could not find file '{file_path}'.")
        print("Please check the file path.")
        return None