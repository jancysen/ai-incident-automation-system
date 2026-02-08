def get_ai_suggestion(title, description, log, root_cause):

    # Fake AI suggestions (for demo without API key)

    if "database" in description.lower():
        return """
Possible Fixes:
- Restart the database server
- Check DB connection settings
- Verify credentials
- Increase connection pool size

Prevention Tips:
- Monitor DB load
- Set up auto-restart alerts
"""

    elif "login" in description.lower():
        return """
Possible Fixes:
- Check authentication service
- Reset user credentials
- Verify token expiry settings

Prevention Tips:
- Enable login monitoring
- Add fallback auth server
"""

    elif "payment" in description.lower():
        return """
Possible Fixes:
- Check payment gateway status
- Verify API keys
- Retry failed transactions

Prevention Tips:
- Add payment retry logic
- Monitor payment service uptime
"""

    else:
        return """
Possible Fixes:
- Restart the affected service
- Check logs for errors
- Verify system configuration

Prevention Tips:
- Enable monitoring alerts
- Perform regular system health checks
"""
