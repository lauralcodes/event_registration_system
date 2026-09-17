import json

# Save booking to JSON.
# Before saving, create an empty list to containe bookings
# Before add the new booking, we need to check whether registrations.json already exists and read the booking_event[] inside it.
# Then add new booking and save everything back

def load_registrations():
    booked_events = []
    try:
        with open("registrations.json","r") as file:  # check whether registrations.json already exists and read the booking_event[] inside it.
            booked_events = json.load(file)  # If the file does exist, read JSON
    except FileNotFoundError:  # when we run the  program first time, there might be no registrations.json file. so If the file doesn't exist yet, just start with an empty list.
        booked_events = []

    return booked_events



def save_registrations(booking  ):
    booked_events = load_registrations()

    booked_events.append (booking)  # add new booking

    with open("registrations.json", "w") as file:  # Save the whole list to JSON
        json.dump(booked_events, file, indent=4)


def get_all_registrations():
    return load_registrations()
