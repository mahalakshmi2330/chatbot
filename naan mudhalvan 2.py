import nltk
from nltk.chat.util import Chat, reflections
import pandas as pd

# Load the CSV dataset into a DataFrame
df = pd.read_csv( "C:\\Users\\maham\\Downloads\\amazon_chatbot_dataset.csv")

# Convert the DataFrame to a list of pairs (patterns and responses)
pairs = []
for index, row in df.iterrows():
    pairs.append([
        row['pattern'],  # The pattern (user input)
        [row['response']]  # The response (chatbot reply)
    ])

# Initialize the chatbot using the CSV-loaded pairs
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your Amazon customer support bot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() in ["bye", "exit", "quit"]:  # If user wants to exit
            print("Chatbot: Thank you for contacting Amazon Customer Support. Have a great day!")
            break
        response = chatbot.respond(user_input)  # Generate chatbot response based on user input
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
