# Simple Chatbot
# Description: A Python-based chatbot that responds to user inputs with predefined rules using if-else statements and randomization for varied responses.
# Features: Handles greetings,farewells,small talk,weather,dialogues,provides information, and shares favorite choices, enhancing interaction through natural language processing techniques.

import random
# Define chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello! How can I help you today?", "Hi there! What can I do for you?"])
    elif "how are you" in user_input:
        return random.choice(["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thank you! How are you?"])
    
    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(["Goodbye! Have a great day!", "See you later!"])
    
    # Information responses
    elif "your name" in user_input:
        return random.choice(["I am Chatbot, your virtual assistant.", "You can call me Chatbot."])
    elif "help" in user_input:
        return random.choice(["Sure, I'm here to help! What do you need assistance with?", "How can I assist you today?"])

    # Weather responses
    elif "weather" in user_input:
        return random.choice(["I can't check the weather for you right now, but you can use a weather app or website for up-to-date information.",
                              "For the latest weather updates, please check a weather website https://www.accuweather.com."])

    # Small talk
    elif "what are you doing" in user_input:
        return random.choice(["I'm here, ready to chat with you!", "Just waiting to assist you!"])
    elif "what's up" in user_input:
        return random.choice(["Not much, just chatting with you! How can I assist you?", "I'm here to help you!"])

    # Favorites
    elif "favorite color" in user_input:
        return random.choice(["I like all colors, but I think blue is pretty cool!", "Colors are fascinating! I like blue."])
    elif "favorite food" in user_input:
        return random.choice(["As a bot, I don't eat, but I like tirumala parasadam is a popular choice.", ])
    elif "favorite movie" in user_input:
        return random.choice(["I don't watch movies, but I've heard 'ssmb29' is quite interesting!"])

    # dialogues
    elif "tell me dialogues" in user_input:
        dialogues = [
            "Never forget what you are. The rest of the world will not. Wear it like armor, and it can never be used to hurt you.",
        ]
        return random.choice(dialogues)
    
    # Default response
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
