from flask import Flask, jsonify, request
from flask_smorest import Api, Blueprint
from database import get_events, add_event, delete_event, event_exists, save_registration, registration_exists
from validation import validate_event, validate_registration
from schemas import EventSchema, RegistrationSchema, LoginSchema
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# Configure Swagger
app.config["API_TITLE"] = "Event Registration API"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.spec.components.security_scheme(
    "bearerAuth",
    {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
)

# to group/container for related endpoints
blp = Blueprint(
    "events",
    "events",
    url_prefix="/events",
    description="Event operations"
)

@blp.get("/")
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
# create events
@blp.post("/")
@blp.arguments(EventSchema)
@blp.doc(security=[{"bearerAuth": []}])
@jwt_required()
def create_event(event):

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

@blp.delete("/<event_id>")
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

api.register_blueprint(blp) # to register the event Blueprint with the API


# create a separate blueprint for registrations
registration_blp = Blueprint(
    "registrations",
    "registrations",
    url_prefix="/registrations",
    description="Registration operations"
)

# Add the registration endpoint
@registration_blp.post("/")
@registration_blp.arguments(RegistrationSchema)
def create_registration(registration):

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

api.register_blueprint(registration_blp) # to register the registration Blueprint with the API

# Create a login endpoint

login_blp = Blueprint(
    "login",
    "login",
    url_prefix="/login",
    description="Authentication"
)

@login_blp.post("/")
@login_blp.arguments(LoginSchema)
def login(data):

    username = data.get("username")
    password = data.get("password")

    # Temporary user for testing
    if username == "admin" and password == "pw123":

        access_token = create_access_token(identity=username)

        return jsonify({
            "access_token": access_token
        }), 200

    return jsonify({
        "error": "Invalid username or password"
    }), 401


api.register_blueprint(login_blp) # to register the login Blueprint with the API

if __name__ == "__main__":
    app.run(debug=True)