# Create templates
bot_template = "BOT : {0}"

# Import the random module
import random

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Start the conversation with the bot
print(bot_template.format("Hi!"))

# Loop until the user types "Bye"
while True:
    # Get the user input
    user_input = input("USER : ")
    
    # Check if the user types "Bye" (case-insensitive)
    if user_input.lower() == "bye":
        print(bot_template.format("Goodbye!"))
        break
    
    # Send the message to the bot
    send_message(user_input)