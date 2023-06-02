# Chatbot
Here i have made a simple chatbot for a school task that i had. The Chatbot that i have made uses a dictionary to pair responses with the users input.

> User: Hello
> 
> Chatbot: Hi, how can I assist you?
> 
> User: How are you?
> 
> Chatbot: I'm good, thank you!

## Installation
To be able to use this chatbot you first need to have installed python correctly on your computer and then you just need to folow the steps below in the "how it works" section.

## How it works
The first thing i do in the script is to import the python library time that i am going to use multiple times in the script.
```
import time
```
The next thing i do is create a dictionary with responses to certain key words and phrases.
```
responses = {
    "hello": "Hi, how can I assist you?",
    "how are you?": "I'm good, thank you!",
    "bye": "Goodbye! Have a nice day!",
    "default": "I'm sorry, I didn't understand that."
}
```
Then i create the chatbot function that handles the input from the user and the responses from the chatbot and adds a delay at the end.
```
def chatbot(): 
    while True:
        user_input = input("User: ")
        user_input = user_input.lower()

        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot:", responses["default"])
        time.sleep(1)  # Adds a delay to the chatbots response.
```
Then all we need to do is call the chatbot function for the script to work.
```
chatbot()
```
## Sources
For more information i have some sources here that utilizes the OpenAI API to create a Chatbot that generates a response based on the users input.
  - https://beebom.com/how-build-own-ai-chatbot-with-chatgpt-api/
  - https://platform.openai.com/docs/introduction/key-concepts
  - https://chat.openai.com/?model=text-davinci-002-render-sha
  - https://vikenfk.sharepoint.com/sites/1IMC2022-23forelever-VGAASI/Student%20Work/Forms/AllItems.aspx?id=%2Fsites%2F1IMC2022-23forelever-VGAASI%2FStudent%20Work%2FWorking%20files%2FOliver%20Richardsen%20%28Elev%29%2FOpenAI%20custom%20chatbot%2FRapport%20om%20hvordan%20du%20kan%20lage%20en%20custom%20chatbot%2Epdf&parent=%2Fsites%2F1IMC2022-23forelever-VGAASI%2FStudent%20Work%2FWorking%20files%2FOliver%20Richardsen%20%28Elev%29%2FOpenAI%20custom%20chatbot
