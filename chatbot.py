print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How can I help you?")
    
    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")
    
    elif user == "your name":
        print("Bot: I am a simple AI chatbot.")
    
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand.")