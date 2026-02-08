def assign_team(description: str):
    desc = description.lower()

    if "login" in desc or "auth" in desc:
        return "Auth Team"
    elif "database" in desc or "db" in desc:
        return "Database Team"
    elif "payment" in desc:
        return "Finance Team"
    elif "ui" in desc or "button" in desc:
        return "Frontend Team"
    else:
        return "Support Team"
