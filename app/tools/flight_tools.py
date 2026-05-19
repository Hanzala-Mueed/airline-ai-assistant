# import json

# def get_ticket_price(destination):
#     with open("app/data/ticket_prices.json", "r") as file:
#         prices = json.load(file)

#     destination = destination.lower()

#     if destination in prices:
#         return prices[destination]

#     return "Destination not found"

import json


def get_ticket_price(destination):
    with open("app/data/ticket_prices.json", "r") as file:
        prices = json.load(file)

    destination = destination.lower()

    if destination in prices:
        return {
            "destination": destination,
            "price": prices[destination]
        }

    return {
        "error": "Destination not found"
    }