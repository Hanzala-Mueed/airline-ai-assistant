import json
from openai import OpenAI
from app.config import (GEMINI_API_KEY, MODEL_NAME, BASE_URL)
from app.tools.flight_tools import get_ticket_price
from app.services.history_service import (load_chat_history, save_chat_history)
from app.tools.booking_tools import create_booking, view_booking, cancel_booking


client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)



SYSTEM_PROMPT = """
You are a helpful airline AI ticket booking assistant.

You help users with:
- checking airline ticket prices
- checking route-based fares
- creating flight bookings
- viewing flight bookings
- cancelling flight bookings

Before checking a ticket price, you must collect:
- departure city
- destination city
- ticket class

Before creating a booking, you must collect:
- passenger name
- departure city
- destination city
- ticket class
- number of passengers
- booking date

Before creating a booking, first check the ticket price using the get_ticket_price tool.
Use the returned price as price_per_passenger.
Calculate total price using:
price_per_passenger * number_of_passengers

When a booking is created, clearly show:
- booking reference
- passenger name
- departure city
- destination city
- booking date
- ticket class
- number of passengers
- price per passenger
- total price
- booking status

To view or cancel a booking, ask for the booking reference number if the user has not provided it.

When needed, use the available tools.
"""

messages = load_chat_history()

if not messages:
    messages.append(
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    )


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_ticket_price",
            "description": "Get ticket price from departure city to destination city by ticket class",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure": {
                        "type": "string",
                        "description": "Departure city"
                    },
                    "destination": {
                        "type": "string",
                        "description": "Destination city"
                    },
                    "ticket_class": {
                        "type": "string",
                        "description": "Ticket class such as economy, business, or first_class"
                    }
                },
                "required": ["departure", "destination", "ticket_class"]
            }
        }
    },

    {
            "type": "function",
            "function": {
                "name": "create_booking",
                "description": "Create a flight booking for a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Customer name"
                        },
                        "departure": {
                            "type": "string",
                            "description": "Departure city"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination city"
                        },
                        "booking_date": {
                            "type": "string",
                            "description": "Date of the flight booking"
                        },
                        "ticket_class": {
                            "type": "string",
                            "description": "Ticket class such as economy, business, or first_class"
                        },
                        "number_of_passengers": {
                            "type": "integer",
                            "description": "Number of passengers"
                        },
                        "price_per_passenger": {
                            "type": "number",
                            "description": "Ticket price per passenger"
                        }
                    },
                    "required": [
                        "name",
                        "departure",
                        "destination",
                        "booking_date",
                        "ticket_class",
                        "number_of_passengers",
                        "price_per_passenger"
                    ]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "view_booking",
                "description": "View a booking by booking reference number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "booking_reference": {
                            "type": "string",
                            "description": "Booking reference number"
                        }
                    },
                    "required": ["booking_reference"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_booking",
                "description": "Cancel a booking by booking reference number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "booking_reference": {
                            "type": "string",
                            "description": "Booking reference number"
                        }
                    },
                    "required": ["booking_reference"]
                }
            }
        }
]


# available_functions = {
#     "get_ticket_price": get_ticket_price,
#     "create_booking": create_booking
# }

available_functions = {
    "get_ticket_price": get_ticket_price,
    "create_booking": create_booking,
    "view_booking": view_booking,
    "cancel_booking": cancel_booking
}


def ask_ai(user_message):
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )
    save_chat_history(messages)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools
        )
    except Exception as e:
        return "Sorry, something went wrong. Please try again later."

    response_message = response.choices[0].message

    tool_calls = response_message.tool_calls

    if tool_calls:
        # messages.append(response_message)
        # save_chat_history(messages)

        messages.append(
            {
                "role": response_message.role,
                "content": response_message.content,
                "tool_calls": [
                    {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    }
                    for tool_call in tool_calls
                ]
            }
        )

        save_chat_history(messages)

        for tool_call in tool_calls:
            function_name = tool_call.function.name

            function_to_call = available_functions[function_name]

            function_args = json.loads(
                tool_call.function.arguments
            )

            # if function_name == "create_booking":
            #     function_response = function_to_call(
            #         name=function_args.get("name"),
            #         destination=function_args.get("destination"),
            #         booking_date=function_args.get("booking_date")
            #     )
            # else:
            #     function_response = function_to_call(
            #         destination=function_args.get("destination")
            #     )

            function_response = function_to_call(
                **function_args
            )

            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(function_response)
                }
            )
            save_chat_history(messages)

        second_response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )

        final_reply = second_response.choices[0].message.content
        if final_reply is None:
            final_reply = "Done. The requested action has been completed."

        messages.append(
            {
                "role": "assistant",
                "content": final_reply
            }
        )

        save_chat_history(messages)

        return final_reply

    assistant_reply = response_message.content
    if assistant_reply is None:
        assistant_reply = "I processed your request, but no message was returned."

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    save_chat_history(messages)

    return assistant_reply