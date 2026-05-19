# airline-ai-assistant
An AI-powered airline customer service agent built with gemini-2.5-flash, Python, and Gradio, featuring lightweight JSON storage for flight and user data.

# Airline AI Assistant (JSON-Based) – Project Structure

This project is inspired by the Day4 notebook, but instead of SQLite, all data will be stored in JSON files.

You will use:

* Python
* OpenAI SDK
* Gemini API Key
* Model: gemini-2.5-flash
* Gradio for UI
* JSON for storage

---

# Suggested Project Structure

```bash
airline_ai_assistant/
│
├── app/
│   ├── main.py                  # Entry point
│   ├── config.py                # API keys & model config
│   ├── prompts.py               # System prompts
│   ├── chatbot.py               # Chat logic
│   ├── tools/
│   │   ├── flight_tools.py      # Ticket price tools
│   │   ├── booking_tools.py     # Booking related tools
│   │   └── json_manager.py      # Read/write JSON files
│   │
│   ├── services/
│   │   ├── llm_service.py       # Gemini/OpenAI client setup
│   │   └── history_service.py   # Chat history management
│   │
│   ├── data/
│   │   ├── ticket_prices.json   # Ticket price data
│   │   ├── bookings.json        # User bookings
│   │   └── chat_history.json    # Stored conversations
│   │
│   └── utils/
│       ├── helpers.py
│       └── validators.py
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── run.py
```

---



# Final Architecture Flow

```text
User
   ↓
Gradio UI
   ↓
Chatbot Logic
   ↓
Gemini Model (gemini-2.5-flash)
   ↓
Tool Calling
   ↓
JSON Database
   ↓
Response Back To User
```

---


