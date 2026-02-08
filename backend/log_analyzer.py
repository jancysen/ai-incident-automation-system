import random

def generate_logs(description: str):
    desc = description.lower()

    if "database" in desc or "db" in desc:
        return "ERROR: DB connection timeout"
    elif "login" in desc:
        return "ERROR: Authentication failed"
    elif "payment" in desc:
        return "ERROR: Payment gateway not responding"
    elif "slow" in desc:
        return "WARNING: High memory usage"
    else:
        return "INFO: Unknown issue detected"


def find_root_cause(log_text: str):
    log = log_text.lower()

    if "db" in log:
        return "Database overload or connection issue"
    elif "authentication" in log:
        return "Invalid credentials or auth service down"
    elif "payment" in log:
        return "Payment service failure"
    elif "memory" in log:
        return "High system resource usage"
    else:
        return "General system issue"
