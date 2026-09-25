from flask import Flask, jsonify, request
from database import get_events, add_event, delete_event, event_exists
from datetime import datetime
import re

app = Flask(__name__)


@app.get("/events")
def events():
    events = get_events()

    event_list = []

    for event in events:
        event_list.append({
            "event_id": event.eventId,
            "name": event.name,
            "date": str(event.date),
            "time": event.time,
            "price": float(event.price)
        })

    return jsonify(event_list)

@app.post("/events")
def create_event():
    event = request.get_json()

    # add validation to make sure JSON was actually sent
    if event is None:
        return jsonify({
            "error": "Request body must contain JSON"
        }), 400

    # add validation to make sure all the required fields are sent
    required_fields = ["event_id", "name", "date", "time", "price"]

    for field in required_fields:
        if field not in event:
            return jsonify({
                "error": f"Missing required field: {field}"
            }), 400


    # To check whether the event ID already exists
    if event_exists(event["event_id"]):
        return jsonify({
            "error": "Event ID already exists"
        }), 400

    # validate the price
    if not isinstance(event["price"], (int, float)):
        return jsonify({
            "error": "Price must be a number"
        }), 400

    if event["price"] < 0:
        return jsonify({
            "error": "Price cannot be negative"
        }), 400

    # Validate the event date
    try:
        datetime.strptime(event["date"], "%Y-%m-%d")
    except ValueError:
        return jsonify({
            "error": "Date must be in YYYY-MM-DD format"
        }), 400

# Validate the event name
    if not isinstance(event["name"], str) or not event["name"].strip(): #if the name is empty or contains only spaces.
        return jsonify({
            "error": "Event name cannot be empty"
        }), 400

# Validate the time
    time_pattern = r"^\d{2}:\d{2}-\d{2}:\d{2}$"

    if not re.match(time_pattern, event["time"]):
        return jsonify({
            "error": "Time must be in HH:MM-HH:MM format"
        }), 400


    add_event(event)

    return jsonify({
        "message": "Event created successfully",
        "event": event
    }), 201


@app.delete("/events/<event_id>")
def remove_event(event_id):
    delete_event(event_id)

    return jsonify({
        "message": "Event deleted successfully",
        "event_id": event_id
    }), 200


if __name__ == "__main__":
    app.run(debug=True)