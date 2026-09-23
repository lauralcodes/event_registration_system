from flask import Flask, jsonify
from database import get_events

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


if __name__ == "__main__":
    app.run(debug=True)