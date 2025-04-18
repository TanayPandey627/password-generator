import random
import string

def transform_word(word):
    # Capitalize first letter, replace characters with lookalikes
    substitutions = {
        'a': '@', 's': '$', 'i': '1', 'o': '0', 'e': '3', 'l': '1'
    }
    word = word.capitalize()
    word = ''.join(substitutions.get(c, c) for c in word)
    return word

def generate_custom_password(words):
    if not words:
        return "No words provided."

    transformed_words = [transform_word(word) for word in words]
    
    # Add random symbol and number between words
    symbols = "!@#$%^&*"
    numbers = [str(random.randint(1, 99)) for _ in range(len(words) - 1)]

    # Build password
    password = ""
    for i in range(len(words)):
        password += transformed_words[i]
        if i < len(words) - 1:
            password += random.choice(symbols) + numbers[i]

    return password

# ---- Run the script ----
if __name__ == "__main__":
    user_input = input("Enter a few words (space-separated): ")
    word_list = user_input.strip().split()
    final_password = generate_custom_password(word_list)
    print("Generated Password:", final_password)
