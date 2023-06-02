import time
import random

# Creates a dictionary with responses from the chatbot.
responses = {
    "hello": "Hi, how can I assist you?",
    "how are you?": "I'm good, thank you!",
    "bye": "Goodbye! Have a nice day!",
    "default": "I'm sorry, I didn't understand that."
}

def chatbot():  # Defines the chatbot function that runs a while loop that checks for the users input and picks the appropriate response from the dictionary.
    while True:
        user_input = input("User: ")
        user_input = user_input.lower()

        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot:", responses["default"])
        time.sleep(1)  # Adds a delay to the chatbots response.


# Runs the chatbot function
chatbot()
