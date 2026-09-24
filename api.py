from flask import Flask, jsonify, request
from database import get_events, add_event, delete_event

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