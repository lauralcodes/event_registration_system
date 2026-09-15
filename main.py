# event registration system where user can register for events
# user can register with name and email address
# user should see the event list,
# when user go to an event, be able to choose date and time
# user will get the confirmation of the booking

import json

from event_registration_system import registration
from registration import Registration
from event import Event


events = { "AI solutions for programming",
           " Python programming",
           " Java programming"
}

event1 = Event(
    eventId="EV01",
    name="AI solutions for programming",
    date="27- 10-2026",
    time="09.00-16.00",
    price="1000 SEK"
)


event2 = Event(
    eventId="EV02",
    name="Python programming",
    date="17- 11-2026",
    time="09.00-16.00",
    price="1000 SEK"
)

event3 = Event(
    eventId="EV03",
    name="Java programming",
    date="27- 10-2026",
    time="09.00-16.00",
    price="1000 SEK"
)


selected_event = "new_event"
#function
def select_event():
    print("Select the event you want to register")

    while True:
        selected_event = input("Select the event (AI solutions for programming, Python programming, Java programming: ").strip()

        if selected_event == "AI solutions for programming":
            print("Registration successful")

            print(
                "- Event name: ", event1.name,"\n"
                "- Event date: ", event1.date,"\n"
                "- Event time: ", event1.time,"\n"
                "- Event price: ", event1.price
            )
            return event1


        elif selected_event == "Python programming":
            print("Registration successful")
            print(
                "- Event name: ", event2.name,"\n"
                "- Event date: ", event2.date,"\n"
                "- Event time: ", event2.time,"\n"
                "- Event price: ", event2.price
            )
            return event2


        elif selected_event == "Java programming":
            print("Registration successful")
            print(
                "- Event name: ", event3.name,"\n"
                "- Event date: ", event3.date,"\n"
                "- Event time: ", event3.time,"\n"
                "- Event price: ", event3.price
            )
            return event3



        else:
            print("Event does not exist.")


# main program
print(" --- Event registration system --- ")
print(" ----------------*------------------ ")

print("Enter your details")

name = input("Enter your name: ").strip().capitalize()
if not name:
    print("Name cannot be empty.")
else:
    email = input("Enter your email: ").strip()
    if "@" in email and "." in email.split("@")[-1]:
        print("Registration  processing...")

        registration = Registration (name, email)
        print("Name: ", (registration.name))
        print("Email: ", (registration.email))

        print(" ----------------------------------- ")

        selected_event = select_event()

        # create booking
        if selected_event is not None:
            booking = {
                "name": registration.name,
                "email": registration.email,
                "eventId": selected_event.eventId,
                "event": selected_event.name,
                "date": selected_event.date,
                "time": selected_event.time,
                "price": selected_event.price
            }

        # Save booking to JSON.
        # Before saving, create an empty list to containe bookings
        # Before add the new booking, we need to check whether registrations.json already exists and read the booking_event[] inside it.
        # Then add new booking and save everything back


        try:
            with open("registrations.json", "r") as file: #check whether registrations.json already exists and read the booking_event[] inside it.
                booked_events = json.load(file) # If the file does exist, read JSON
        except FileNotFoundError: # when we run the  program first time, there might be no registrations.json file. so If the file doesn't exist yet, just start with an empty list.
            booked_events = []

        booked_events.append(booking) # add new booking


        with open("registrations.json", "w") as file: # Save the whole list to JSON
            json.dump(booked_events, file, indent=4)

    else:
        print("Enter a valid e mail address.")







