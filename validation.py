from datetime import datetime
import re


def validate_event(event):

    required_fields = [
        "event_id",
        "name",
        "date",
        "time",
        "price"
    ]

    for field in required_fields:
        if field not in event:
            return f"Missing required field: {field}"

    if not isinstance(event["name"], str) or not event["name"].strip():
        return "Event name cannot be empty"

    if not isinstance(event["price"], (int, float)):
        return "Price must be a number"

    if event["price"] < 0:
        return "Price cannot be negative"

    try:
        datetime.strptime(event["date"], "%Y-%m-%d")
    except ValueError:
        return "Date must be in YYYY-MM-DD format"

    time_pattern = r"^\d{2}:\d{2}-\d{2}:\d{2}$"

    if not re.match(time_pattern, event["time"]):
        return "Time must be in HH:MM-HH:MM format"

    return None



def validate_registration(registration):

    required_fields = ["name", "email", "eventId"]

    for field in required_fields:
        if field not in registration:
            return f"Missing required field: {field}"

    if not registration["name"].strip():
        return "Name cannot be empty"

    if "@" not in registration["email"]:
        return "Invalid email address"

    if not registration["eventId"].strip():
        return "Event ID cannot be empty"

    return None