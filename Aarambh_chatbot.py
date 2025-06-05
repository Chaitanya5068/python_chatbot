import spacy
import requests
import wikipedia
import sympy
import dateparser
from datetime import datetime
import re

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# OpenWeatherMap API key
WEATHER_API_KEY = "86055c3f5c9c6a6b1e6e163c63ee7891"

# Intents and associated keywords
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "self_info": ["yourself", "who are you", "about you", "what is your name"],
    "time": ["time", "current time", "what time"],
    "date": ["today", "current date", "what date"],
    "weather": ["weather", "temperature", "forecast", "rain", "raining", "hot", "cold"],
    "math": ["calculate", "+", "-", "*", "/", "^", "solve"],
    "wikipedia": ["who is", "what is", "tell me about", "explain", "define", "history of", "when was", "date of"],
}

# Basic replies
responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "self_info": (
        "I am Aarambh — your AI assistant. I can help you with:\n"
        "- Weather updates\n"
        "- Math problems\n"
        "- Date and time\n"
        "- History and general knowledge\n"
        "Just ask me anything!"
    ),
    "unknown": "Sorry, I didn't understand that. Can you please rephrase?",
}

# Get weather from API
def get_weather(city):
    if not city:
        return "Please specify a city like 'weather in Delhi'."
    try:
        city_query = city.strip().replace(" ", "+")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_query}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("weather") and data.get("main"):
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            return f"The weather in {city.title()} is {weather} with a temperature of {temp}°C."
        else:
            return f"Couldn't fetch weather for {city.title()}. Reason: {data.get('message', 'unknown error')}."
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

# Get current time
def get_current_time():
    return f"The current time is {datetime.now().strftime('%I:%M %p')}"

# Get current date
def get_current_date():
    return f"Today's date is {datetime.now().strftime('%A, %B %d, %Y')}"

# Solve math expression
def solve_math(expression):
    try:
        expr = re.sub(r"[^\d\+\-\*/\.\(\)\^\s]", "", expression)
        parsed_expr = sympy.sympify(expr)
        return f"The answer is: {parsed_expr.evalf()}"
    except Exception:
        return "I couldn't solve that math expression. Try something else."

# Wikipedia info extraction
def search_wikipedia(query):
    try:
        cleaned_query = re.sub(r"^(who is|what is|tell me about|define|explain|when was|date of|history of)\s+", "", query, flags=re.I).strip()
        try:
            return wikipedia.summary(cleaned_query, sentences=3)
        except:
            return wikipedia.summary(query, sentences=3)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results. Did you mean: {', '.join(e.options[:3])}?"
    except Exception:
        return "I couldn't find anything on that. Try rephrasing."

# Intent detection
def get_intent(user_input):
    lower_input = user_input.lower()

    # Detect math explicitly by operators first
    if any(op in user_input for op in "+-*/^"):
        return "math"

    for intent, keywords in intents.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', lower_input):
                return intent

    return "unknown"

# Extract city name for weather
def extract_city(user_input):
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            return ent.text.strip().title()

    match = re.search(r"(?:in|at|for|of)\s+([a-zA-Z\s]+)", user_input)
    if match:
        return match.group(1).strip().title()

    return None

# Main chatbot logic — only weather logic fixed
def chatbot_response(user_input):
    user_input = user_input.strip()
    intent = get_intent(user_input)

    if intent == "greeting":
        return responses["greeting"]
    elif intent == "goodbye":
        return responses["goodbye"]
    elif intent == "thanks":
        return responses["thanks"]
    elif intent == "self_info":
        return responses["self_info"]
    elif intent == "time":
        return get_current_time()
    elif intent == "date":
        return get_current_date()
    elif intent == "weather":
        city = extract_city(user_input)
        return get_weather(city)
    elif intent == "math":
        return solve_math(user_input)
    elif intent == "wikipedia":
        return search_wikipedia(user_input)

    # fallback NER-based Wikipedia query
    doc = nlp(user_input)
    if any(ent.label_ in ["PERSON", "ORG", "GPE", "EVENT"] for ent in doc.ents):
        return search_wikipedia(user_input)

    return responses["unknown"]

# Chat loop
def chatbot():
    print("🤖 Aarambh: Hello! I am Aarambh, your AI assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🤖 Aarambh:", responses["goodbye"])
            break
        print("🤖 Aarambh:", chatbot_response(user_input))

# Start chatbot
if __name__ == "__main__":
    chatbot()
