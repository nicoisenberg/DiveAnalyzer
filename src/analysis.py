def generate_dive_report(data):

    report = f"""
    ----- Dive Report -----
    Number of dives: {data.shape[0]}
    Average depth: {data['Depth'].mean():.1f} m
    Maximum depth: {data['Depth'].max():.1f} m
    Minimum depth: {data['Depth'].min():.1f} m
    Average temperature: {data['Temperature'].mean():.1f} °C
    """
    return report