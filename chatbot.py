# Advanced Fashion Chatbot by Mahlatse
# Demonstrates: conditionals, loops, data structures, randomization, and personalization

import time
import random

# Data structure: dictionary with lists
outfit_suggestions = {
    "casual": ["jeans and a white t-shirt", "a floral summer dress", "denim jacket with leggings"],
    "formal": ["a black blazer with trousers", "a classy dress and heels", "a suit with a silk blouse"],
    "street": ["oversized hoodie and sneakers", "baggy jeans with crop top", "leather jacket and boots"]
}

mood_suggestions = {
    "happy": ["bright colors like yellow or pink", "a playful jumpsuit", "patterned skirts or dresses"],
    "sad": ["comfortable sweatpants and a hoodie", "soft pastel tones", "cozy oversized sweaters"],
    "confident": ["a bold red outfit", "heels with a fitted outfit", "statement jewelry"],
    "relaxed": ["loose linen pants", "a soft t-shirt dress", "slides or flats"]
}

# Function for pink background (works best in VS Code/Terminal)
def pink_background():
    print("\033[45m" + " " * 60)
    print(" " * 17 + "💖 Welcome to FashionBot 2.0 💖")
    print(" " * 60 + "\033[0m")

# Start Chatbot
pink_background()
print("Hi there, gorgeous! I’m your fashion assistant 💅")

# Ask for user's name
user_name = input("\nWhat’s your name? ").title()
print(f"Lovely to meet you, {user_name}! Let’s find your perfect outfit ✨")

# Main chatbot loop
while True:
    time.sleep(1)
    user_input = input("\nWhat type of occasion are you dressing for? (casual/formal/street or 'exit'): ").lower()

    # Control statement: exit
    if user_input == "exit":
        print(f"\nGoodbye, {user_name}! Stay stylish and confident 💖")
        break

    # Respond with outfit ideas
    elif user_input in outfit_suggestions:
        print(f"\nHere are some {user_input} outfit ideas for you, {user_name}:")
        for outfit in outfit_suggestions[user_input]:
            print(f" 👗 - {outfit}")

        # Ask about mood for personalized touch
        mood = input("\nHow are you feeling today? (happy/sad/confident/relaxed): ").lower()

        if mood in mood_suggestions:
            print(f"\nSince you’re feeling {mood}, you might love these looks too:")
            for idea in mood_suggestions[mood]:
                print(f" 💕 - {idea}")
        else:
            print("Mood not recognized, but you’ll look fabulous either way! 💫")

        # Ask about accessories
        accessory = input("\nWould you like accessory ideas? (yes/no): ").lower()
        if accessory == "yes":
            accessories = ["statement earrings", "a pearl necklace", "a stylish handbag", "cool sunglasses"]
            suggestion = random.choice(accessories)
            print(f"\nTry pairing your outfit with {suggestion} 😍")
        else:
            print("Keeping it minimal? Classy choice 💎")

    else:
        print("Hmm, I don’t have suggestions for that yet. Try 'casual', 'formal', or 'street'.")
