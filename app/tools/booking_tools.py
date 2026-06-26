# import json
# import uuid


# BOOKINGS_FILE = "app/data/bookings.json"


# def create_booking(name, departure, destination, booking_date):

#     try:
#         with open(BOOKINGS_FILE, "r") as file:
#             bookings = json.load(file)

#     except:
#         bookings = []

#     booking = {
#         "id": str(uuid.uuid4()),
#         "name": name,
#         "departure": departure,
#         "destination": destination,
#         "booking_date": booking_date
#     }

#     bookings.append(booking)

#     with open(BOOKINGS_FILE, "w") as file:
#         json.dump(bookings, file, indent=4)

#     return {
#         "message": "Booking created successfully",
#         "booking": booking
#     }

import json
import uuid


BOOKINGS_FILE = "app/data/bookings.json"


def load_bookings():
    try:
        with open(BOOKINGS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_bookings(bookings):
    with open(BOOKINGS_FILE, "w") as file:
        json.dump(bookings, file, indent=4)


def create_booking(
    name,
    departure,
    destination,
    booking_date,
    ticket_class,
    number_of_passengers,
    price_per_passenger
):
    bookings = load_bookings()

    number_of_passengers = int(number_of_passengers)
    price_per_passenger = float(price_per_passenger)
    total_price = number_of_passengers * price_per_passenger

    booking_reference = "AIR-" + str(uuid.uuid4())[:8].upper()

    booking = {
        "booking_reference": booking_reference,
        "status": "confirmed",
        "name": name,
        "departure": departure,
        "destination": destination,
        "booking_date": booking_date,
        "ticket_class": ticket_class,
        "number_of_passengers": number_of_passengers,
        "price_per_passenger": price_per_passenger,
        "total_price": total_price
    }

    bookings.append(booking)
    save_bookings(bookings)

    return {
        "message": "Booking created successfully",
        "booking": booking
    }


def view_booking(booking_reference):
    bookings = load_bookings()

    booking_reference = booking_reference.upper()

    for booking in bookings:
        if booking.get("booking_reference") == booking_reference:
            return {
                "message": "Booking found",
                "booking": booking
            }

    return {
        "error": "Booking not found"
    }


def cancel_booking(booking_reference):
    bookings = load_bookings()

    booking_reference = booking_reference.upper()

    for booking in bookings:
        if booking.get("booking_reference") == booking_reference:
            if booking.get("status") == "cancelled":
                return {
                    "message": "Booking is already cancelled",
                    "booking": booking
                }

            booking["status"] = "cancelled"
            save_bookings(bookings)

            return {
                "message": "Booking cancelled successfully",
                "booking": booking
            }

    return {
        "error": "Booking not found"
    }