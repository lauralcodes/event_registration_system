from flask import Flask, jsonify, request
from database import get_events, add_event, delete_event, event_exists
from datetime import datetime
import re
from validation import validate_event

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

    # To check whether the event ID already exists
    if event_exists(event["event_id"]):
        return jsonify({
             "error": "Event ID already exists"
         }), 400

    # add validation to make sure all the required fields are sent, and validate the price, date and time
    error = validate_event(event)
    if error:
        return jsonify({
            "error": error
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