def validate_required_columns(data, required_columns):
 
    for column in required_columns:
        if column not in data.columns:
            print(f"Column '{column}'is missing.")
            return False
        
    return True

def validate_not_empty(data):
    if data.empty:
        print(f"The dataset is empty.")
        return False
    
    return True

