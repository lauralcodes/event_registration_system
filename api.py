from flask import Flask, jsonify, request
from database import get_events, add_event, delete_event, event_exists, save_registration, registration_exists
from validation import validate_event, validate_registration

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


    # add validation to make sure all the required fields are sent, and validate the price, date and time
    error = validate_event(event)
    if error:
        return jsonify({
            "error": error
        }), 400

    # To check whether the event ID already exists
    if event_exists(event["event_id"]):
        return jsonify({
            "error": "Event ID already exists"
        }), 400

    add_event(event)

    return jsonify({
        "message": "Event created successfully",
        "event": event
    }), 201


@app.delete("/events/<event_id>")
def remove_event(event_id):

    if not event_exists(event_id):
        return jsonify({
            "error": "Event does not exist"
        }), 404

    delete_event(event_id)

    return jsonify({
        "message": "Event deleted successfully",
        "event_id": event_id
    }), 200

# Add the registration endpoint
@app.post("/registrations")
def create_registration():
    registration = request.get_json()

    if registration is None:
        return jsonify({
            "error": "Request body must contain JSON"
        }), 400

    error = validate_registration(registration)

    if error:
        return jsonify({
            "error": error
        }), 400

    # check that the selected eventId actually exists before saving
    if not event_exists(registration["eventId"]):
        return jsonify({
            "error": "Event does not exist"
        }), 404

    # validation to prevent duplicate registrations
    if registration_exists(registration["email"], registration["eventId"]):
        return jsonify({
            "error": "User is already registered for this event"
        }), 400

    save_registration(registration)

    return jsonify({
        "message": "Registration created successfully",
        "registration": registration
    }), 201



if __name__ == "__main__":
    app.run(debug=True)