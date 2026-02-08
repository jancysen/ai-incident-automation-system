def predict_severity(description: str):
    desc = description.lower()

    if "down" in desc or "crash" in desc or "failure" in desc:
        return "Critical"
    elif "error" in desc:
        return "High"
    elif "slow" in desc:
        return "Medium"
    else:
        return "Low"
