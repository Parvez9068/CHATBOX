import spacy

nlp = spacy.load("en_core_web_sm")

def process_user_input(user_input):
    """
    Processes user input and generates a response.
    """
    doc = nlp(user_input.lower())

    if "hello" in user_input.lower():
        return "Hi there! How can I assist you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "your name" in user_input.lower():
        return "I am your friendly chatbot, ready to help you!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you rephrase?"
