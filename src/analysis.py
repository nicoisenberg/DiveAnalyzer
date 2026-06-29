def generate_dive_report(data):

    report = (
    "-----Dive Report -----\n\n"
    f"Number of dives: {data.shape[0]}\n"
    f"Average depth: {data['Depth'].mean():.1f} m\n"
    f"Maximum depth: {data['Depth'].max():.1f} m\n"
    f"Minimum depth: {data['Depth'].min():.1f} m\n"
    f"Average temperature: {data['Temperature'].mean():.1f} °C"
    )

    return report