# event registration system where user can register for events
# user can register with name and email address
# user should see the event list,
# when user go to an event, be able to choose date and time
# user will get the confirmation of the booking

from registration import Registration
from event import Event

events_list = { "AI solutions for programming",
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

events = [event1, event2, event3]

#function
def select_event():
    print("Select the event you want to register")

    while True:
        print("Available events: ", events_list)
        selected_event = input("Select the event:  ").strip()

        if selected_event == "AI solutions for programming":
            print("Registration successful")
            print(
                "- Event name: ", event1.name,"\n"
                "- Event date: ", event1.date,"\n"
                "- Event time: ", event1.time,"\n"
                "- Event price: ", event1.price
            )
            break


        elif selected_event == "Python programming":
            print("Registration successful")
            print(
                "- Event name: ", event2.name,"\n"
                "- Event date: ", event2.date,"\n"
                "- Event time: ", event2.time,"\n"
                "- Event price: ", event2.price
            )
            break


        elif selected_event == "Java programming":
            print("Registration successful")
            print(
                "- Event name: ", event3.name,"\n"
                "- Event date: ", event3.date,"\n"
                "- Event time: ", event3.time,"\n"
                "- Event price: ", event3.price
            )
            break


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

        select_event()

    else:
        print("Enter a valid e mail address.")





