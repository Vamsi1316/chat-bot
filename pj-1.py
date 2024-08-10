""" 
In the below code i used pyttsx3 to convert text into speech.
You can interact with chatbot through the terminal and to end the chat just say "bye".
The chat bot can answer to basic questions like hi, hellow, bye but for other question it just reply's "I'm sorry, I don't understand that."
"""

import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I am a simple chatbot created by you."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    speak("Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            response = get_response(user_input)
            print(f"Chatbot: {response}")
            speak(response)
            break
        else:
            response = get_response(user_input)
            print(f"Chatbot: {response}")
            speak(response)

if __name__ == "__main__":
    main()

