import re
import random
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"(?i)hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?", "I'm good, how about yourself?", "I'm great! What about you?"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me BCPBA (Basic Chatbot Program by Anshuman).", "I'm BCPBA (Basic Chatbot Program by Anshuman), nice to meet you!"]
    ],
    [
        r"what can you do for me ?",
        ["I can chat with you and provide information. Just ask me anything!"]
    ],
    [
        r"(.*) (age|old) are you ?",
        ["I'm just a program, so I don't have an age."]
    ],
    [
        r"(.*) created you ?",
        ["I was created by a talented developer named Anshuman using Python."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am a virtual bot, so I don't have a physical location."]
    ],
    [
        r"(.*) (weather) in (.*)",
        ["The weather in %3 is usually nice!", "I'm not sure, but I can check online for you."]
    ],
    [
        r"(.*) (rain) in (.*)",
        ["Yes, it often rains in %3.", "I believe so, %3 gets quite a bit of rain."]
    ],
    [
        r"quit|bye|goodbye",
        ["Bye! Take care.", "Goodbye, have a great day!", "See you later!"]
    ],
    [
        r"(.*) (sorry|apologize) (.*)",
        ["It's okay, no need to apologize.", "No worries!", "Don't mention it."]
    ],
    [
        r"(.*) (happy|joyful) (.*)",
        ["That's wonderful to hear!", "I'm glad you're happy.", "It's always great to feel joyful."]
    ],
    [
        r"(.*) (sad|upset|depressed) (.*)",
        ["I'm sorry to hear that. Is there anything specific that's bothering you?", "Feeling down is tough. Is there something you'd like to talk about?", "I'm here for you. Would you like to share more about what's going on?"]
    ],
    [
        r"(.*) (thank you|thanks) (.*)",
        ["You're welcome!", "No problem!", "Glad I could assist."]
    ],
    [
        r"(.*) (help) (.*)",
        ["Of course! What do you need help with?", "I'm here to help. What's the issue?", "How can I assist you?"]
    ],
]

# Create a chatbot with the defined patterns
chatbot = Chat(pairs, reflections)

# Additional conversational prompts to encourage more interaction
conversation_prompts = [
    "Tell me more about yourself.",
    "What do you enjoy doing in your free time?",
    "Do you have any hobbies or interests?",
    "What's your favorite book/movie/TV show?",
    "How was your day today?",
    "Is there anything on your mind that you'd like to talk about?"
]

def main():
    print("Hi, I'm a conversational chatbot. How can I assist you today?")
    print("Feel free to ask me anything. Enter 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print(random.choice(chatbot.respond(user_input)))
            break
        else:
            response = chatbot.respond(user_input)
            if not response:
                tokens = nltk.word_tokenize(user_input)
                tagged_tokens = nltk.pos_tag(tokens)
                response = generate_response(tagged_tokens)
            print(response)

def generate_response(tagged_tokens):
    response = ""
    # Check for specific patterns and generate appropriate responses
    for (word, pos) in tagged_tokens:
        if pos in ['VB', 'VBP']:  # Verbs
            response = "Hmm, that's interesting. What else would you like to know?"
            break
        elif pos in ['NN', 'NNS']:  # Nouns
            response = "Could you tell me more about " + word + "?"
            break
        elif pos in ['JJ', 'JJR', 'JJS']:  # Adjectives
            response = "That sounds " + word + "! Tell me more."
            break
    if not response:
        response = random.choice(conversation_prompts)
    return response

if __name__ == "__main__":
    main()




#CODE BY ANSHUMAN