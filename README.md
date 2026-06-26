# ✈️ Airline AI Assistant

An AI-powered flight booking assistant built with **Python**, **Gradio**, **Google Gemini**, and **Function Calling**.

The assistant allows users to interact using natural language to check flight ticket prices, create bookings, view reservations, and cancel bookings.

---

## 🚀 Features

### Flight Fare Lookup
- Route-based ticket prices
- Departure → Destination pricing
- Multiple ticket classes
- AI-powered natural language interaction

### Flight Booking
- Passenger name
- Departure city
- Destination city
- Travel date
- Ticket class
- Number of passengers
- Automatic total price calculation
- Unique booking reference generation

### Booking Management
- View booking details
- Cancel bookings
- Booking status tracking

---

## 🛠 Tech Stack

- Python 3.12+
- Gradio 6
- Google Gemini 2.5 Flash
- OpenAI Compatible SDK
- JSON Database
- Function Calling
- dotenv

---

## 📂 Project Structure

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

# 🧠 How It Works

```text
User
   │
   ▼
Gradio UI
   │
   ▼
Gemini LLM
   │
   ▼
Function Calling
   │
   ├──────────────┐
   ▼              ▼
Flight Tool    Booking Tool
   │              │
   └──────┬───────┘
          ▼
      JSON Storage
```

---

# 💬 Example Prompts

### Check Ticket Price

```
What is the economy ticket price from Miami to Tokyo?
```

---

### Book Flight

```
Book a flight for John Smith from Miami to Tokyo on 2026-07-10.

Economy class for 2 passengers.
```

---

### View Booking

```
View my booking AIR-XXXXXXXX
```

---

### Cancel Booking

```
Cancel booking AIR-XXXXXXXX
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-flight-booking-assistant.git
```

Move into the project

```bash
cd ai-flight-booking-assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

```bash
python -m app.main
```

The application will start at

```
http://127.0.0.1:7860
```

---

# 📁 Data Storage

The project currently uses JSON files as a lightweight database.

```
bookings.json
```

Stores all flight bookings.

```
ticket_prices.json
```

Stores airline ticket prices.

```
chat_history.json
```

Stores conversation history.

---

# 🛣 Current Workflow

```text
User Message
      │
      ▼
Gemini
      │
      ▼
Tool Selection
      │
      ├───────────► Flight Price Tool
      │
      ├───────────► Booking Tool
      │
      ├───────────► View Booking Tool
      │
      └───────────► Cancel Booking Tool
      │
      ▼
Gemini Response
      │
      ▼
Gradio Interface
```

---

# 🎯 Current Features

- Route-based ticket pricing
- AI function calling
- Passenger booking
- Ticket classes
- Multiple passengers
- Booking reference generation
- Total fare calculation
- Booking status
- View booking
- Cancel booking
- Conversation history
- JSON data persistence

---

# 🚧 Future Improvements

- Airline selection
- Flight number generation
- Seat selection
- Flight schedules
- Airport lookup
- Return flights
- Multi-city booking
- User authentication
- SQLite/PostgreSQL database
- Booking modification
- Email confirmation
- PDF e-ticket
- Payment integration
- Admin dashboard
- Real airline APIs
- Flight availability
- Baggage options
- Meal selection
- Check-in support

---

# 📸 Preview

*(Add screenshots here)*

---

# 👨‍💻 Author

**Hanzala Mueed**

GitHub:
https://github.com/yourusername

LinkedIn:
https://linkedin.com/in/yourprofile
