from flask import Flask, jsonify, request
from database import get_events, add_event

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

if __name__ == "__main__":
    app.run(debug=True)