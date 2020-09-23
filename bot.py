from random import choice


#combine functions and conditionals to get a response from the bot
def get_food_bot_response(user):
    bot_response = {
        'breakfast': ['Eggs, simple classic staple breakfast', 'Ceareal, have a lazy morning and go this route.', 'Oatmeal, how have you already not made a bowl of it?', 'Omelette, eggs but we feelin fancy.'],
                  
        'lunch': ['Grilled Cheese, bread and cheese cant get simpler', 'Noodles, alfredo, tomato, buttered, the choices are endless.', 'Salad, Caesar with some french.', ],

        'dinner': ['Tacos, salsa cheese and everything nice.', 'Burgers, takes 3 years but is well well worth it!', 'Salad, healthy night cap.', 'Mac & Cheese, krafts anything else is a flop'],

    }

    if user == 'breakfast':
        return choice(bot_response['breakfast'])
    elif user == 'lunch':
        return choice(bot_response['lunch'])
    elif user == 'dinner':
        return choice(bot_response['dinner'])
    else:
        return "Granola bar is always smack"


print("Welcome to Food Bot")
print("Please enter which meal you're eating")

user_response1 = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
    user_response1 = input("Cookin' in the Kitchen!")


    # Quits program when user responds with 'done'
    if user_response1 == 'done':
        break

    bot_response = get_food_bot_response(user_response1)
    print(bot_response)
