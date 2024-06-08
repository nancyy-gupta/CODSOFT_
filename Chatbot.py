def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what can you do" in user_input:
        return "I can chat with you, answer some questions, and assist you with basic tasks."
    elif "what is the weather" in user_input:
        return "I can't check the weather right now, but you can look it up on a weather website or app."
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what is your favorite color" in user_input:
        return "I don't have preferences, but I've heard blue is quite popular!"
    elif "what is the capital of India" in user_input:
        return "The capital of India is New Delhi."
    elif "how old are you" in user_input:
        return "I don't have an age, but I was created in 2024."
    elif "who created you" in user_input:
        return "I was created by Nancy Gupta."
    elif "what is your purpose" in user_input:
        return "My purpose is to assist and chat with users like you."
    elif "Can you help me with programming" in user_input:
        return "Sure, I can try to help with programming questions. What do you need help with?"
    elif "what is your favorite food" in user_input:
        return "I don't eat, but I've heard pizza is a popular choice!"
    elif "tell me a fact" in user_input:
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible."
    elif "what time is it" in user_input:
        return "I don't have real-time capabilities to tell the current time. Please check your device's clock."
    elif "do you have any hobbies" in user_input:
        return "I don't have hobbies, but I enjoy helping people!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot: " + response)
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
