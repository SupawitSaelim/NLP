import re
import random
rules = {
    'do you think (.*)': [
        'if {0}? Absolutely.', 
        'No chance'], 
    'do you remember (.*)': [
        'Did you think I would forget {0}', 
        "Why haven't you been able to forget {0}", 
        'What about {0}', 
        'Yes .. and?'], 
    'I want (.*)': [
        'What would it mean if you got {0}', 
        'Why do you want {0}', 
        "What's stopping you from getting {0}"], 
    'if (.*)': [
        "Do you really think it's likely that {0}", 
        'Do you wish that {0}', 
        'What do you think about {0}', 
        'Really--if {0}']
}
# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response.format(phrase)

# Test match_rule
#print(match_rule(rules, "do you remember your last birthday"))
# Start the conversation loop
while True:
    # Get user input
    user_input = input("USER : ")
    
    # Check if the user types "Bye" (case-insensitive)
    if user_input.lower() == "bye":
        print("BOT : Goodbye!")
        break
    
    # Get the bot's response using match_rule
    response = match_rule(rules, user_input)
    
    # Print the bot's response
    print(f"BOT : {response}")