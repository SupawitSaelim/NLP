# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that responds to a user's message
def respond(message):
    # Concatenate the user's message to the end of a standard bot response
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message

# Define a function that sends a message to the bot
def send_message():
    while True:
        # Get input from the user
        message = input("USER: ")
        # If the user types "bye", stop the chat
        if message.lower() == "bye":
            print("BOT: Goodbye!")
            break
        
        # Get the bot's response to the message
        response = respond(message)
        # Print the bot template including the bot's response
        print(bot_template.format(response))

# Start a conversation
send_message()
