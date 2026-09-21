# event registration system where user can register for events
# user can register with name and email address
# user should see the event list,
# when user go to an event, be able to choose date and time
# user will get the confirmation of the booking


from registration import Registration
from database import save_registration, get_events

events = get_events()


selected_event = "new_event"
#function
def select_event():
    print("Select the event you want to register")

    while True:
        selected_event = input("Select the event (AI solutions for programming, Python programming, Java programming: ").strip()

        for event in events:
            if selected_event == event.name:
                print("Event selected")
                print(
                    "- Event name: ", event.name, "\n"
                    "- Event date: ", event.date, "\n"
                    "- Event time: ", event.time, "\n"
                    "- Event price: ", event.price
                    )
                return event


        print("Event does not exist---------.")


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

        # Call the method from database.py and save the result to the mysql db
            save_registration(booking) # all above steps handles inside this function in database.py
            print("New event registered.")



        else:
            print(" No registered event saved")

    else:
        print("Enter a valid e mail address.")







