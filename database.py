import mysql.connector
from event import Event

# MySQL connection code
def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ChariJAVA25S_DT",
        database="event_registration"
    )
    return connection

# save a booking into the registrations table.
def save_registration(booking):
    connection = connect_to_database()

    cursor = connection.cursor() # the thing Python uses to send SQL commands to MySQL

    # SQL command. Insert a new row into registrations, using a name, email and event ID. The %s values are placeholders
    sql = """ 
        INSERT INTO registrations (name, email, event_id)
        VALUES (%s, %s, %s)
    """

    # takes the information from booking dictionary
    values = (
            booking["name"],
            booking["email"],
            booking["eventId"]
    )

    cursor.execute(sql, values) # Execute this SQL command using these values

    connection.commit() # It tells MySQL: Save this change permanently. Without the commit, the INSERT may not actually be saved.

    # closes the cursor and database connection
    cursor.close()
    connection.close()

def get_events():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")

    rows = cursor.fetchall()

    events = []

    for row in rows:
        event = Event(
            eventId=row[0],
            name=row[1],
            date=row[2],
            time=row[3],
            price=row[4]
        )
        events.append(event)

    cursor.close()
    connection.close()

    return events

# To check whether the event ID already exists
def event_exists(event_id):
    connection = connect_to_database()

    cursor = connection.cursor()

    sql = """
        SELECT event_id
        FROM events
        WHERE event_id = %s
    """

    cursor.execute(sql, (event_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None

def add_event(event):
    connection = connect_to_database()

    cursor = connection.cursor()

    sql = """
        INSERT INTO events (event_id, name, date, time, price)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        event["event_id"],
        event["name"],
        event["date"],
        event["time"],
        event["price"]
    )

    cursor.execute(sql, values)

    connection.commit()

    cursor.close()
    connection.close()

def delete_event(event_id):
    connection = connect_to_database()

    cursor = connection.cursor()

    sql = """
        DELETE FROM events
        WHERE event_id = %s
    """

    cursor.execute(sql, (event_id,))

    connection.commit()

    cursor.close()
    connection.close()

# Test the MySQL connection
# connection = connect_to_database()

# if connection.is_connected():
    #print("MySQL connection successful!")

# connection.close()

# temporary test code totest delete event function
# if __name__ == "__main__":
    # delete_event("EV05")
    # print("Event deleted")