import mysql.connector

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

# Test the MySQL connection
# connection = connect_to_database()

# if connection.is_connected():
    #print("MySQL connection successful!")

# connection.close()