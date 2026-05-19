import json
import uuid


BOOKINGS_FILE = "app/data/bookings.json"


def create_booking(name, destination,booking_date):

    try:
        with open(BOOKINGS_FILE, "r") as file:
            bookings = json.load(file)

    except:
        bookings = []

    booking = {
        "id": str(uuid.uuid4()),
        "name": name,
        "destination": destination,
        "booking_date": booking_date
    }

    bookings.append(booking)

    with open(BOOKINGS_FILE, "w") as file:
        json.dump(bookings, file, indent=4)

    return {
        "message": "Booking created successfully",
        "booking": booking
    }