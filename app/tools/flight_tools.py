import json


TICKET_PRICES_FILE = "app/data/ticket_prices.json"


def get_ticket_price(departure=None, destination=None, ticket_class="economy"):
    try:
        if not departure:
            return {
                "error": "Departure city is required."
            }

        if not destination:
            return {
                "error": "Destination city is required."
            }

        if not ticket_class:
            ticket_class = "economy"

        with open(TICKET_PRICES_FILE, "r") as file:
            prices = json.load(file)

        departure = departure.lower().replace(" ", "_")
        destination = destination.lower().replace(" ", "_")
        ticket_class = ticket_class.lower().replace(" ", "_")

        if departure not in prices:
            return {
                "error": f"Departure city '{departure}' not found."
            }

        if destination not in prices[departure]:
            return {
                "error": f"No route found from {departure} to {destination}."
            }

        route_prices = prices[departure][destination]

        if ticket_class not in route_prices:
            return {
                "error": f"Ticket class '{ticket_class}' not available."
            }

        return {
            "departure": departure,
            "destination": destination,
            "ticket_class": ticket_class,
            "price": route_prices[ticket_class]
        }

    except Exception as e:
        return {
            "error": f"Failed to get ticket price: {str(e)}"
        }