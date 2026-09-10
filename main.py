# event registration system where user can register for events
# user can register with name and email address
# user should see the event list,
# when user go to an event, be able to choose date and time
# user will get the confirmation of the booking

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

#function
def select_event():
    print("Select the event you want to register")

    while True:
        event = input("Select the event (AI solutions for programming, Python programming, Java programming: ").strip().capitalize()

        if event == "AI solutions for programming":
            print(event1)
            print("Registration successful")
            break


        elif event == "Python programming":
            print(event2)
            print("Registration successful")
            break


        elif event == "Java programming":
            print(event3)
            print("Registration successful")
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





