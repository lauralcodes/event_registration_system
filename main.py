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
    print("\nAvailable events:")

    for index, event in enumerate(events, start=1):
        print(
            f"{index}. {event.name} | "
            f"Date: {event.date} | "
            f"Time: {event.time} | "
            f"Price: {event.price} SEK"
        )

    while True:
        choice = input("\nSelect an event number: ").strip()
        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(events):
                selected_event = events[choice - 1]

                print("\nEvent selected")
                print("- Event name:", selected_event.name)
                print("- Event date:", selected_event.date)
                print("- Event time:", selected_event.time)
                print("- Event price:", selected_event.price)

                return selected_event



print("Invalid event selection. Please choose a valid event number.")


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
            print("Event registered.")



        else:
            print(" No registered event saved")

    else:
        print("Enter a valid e mail address.")







