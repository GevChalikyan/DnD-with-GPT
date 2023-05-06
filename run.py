import os
import platform
from pathlib import Path
import openai

def collectAPIKey():
    APIKey = input('Insert your API Key: ')
    with open('API Key.txt', 'w') as f:
        f.write(APIKey)



#	Checks if the user has given an API key yet
#	Collects one if there isn't one
try:
    my_abs_path = Path("./API Key.txt").resolve(strict=True)
except FileNotFoundError:
    collectAPIKey()
with open ('API Key.txt') as f:
    openai.api_key = f.readline()
if (platform.system() == 'Darwin'):
    os.system('clear')
elif (platform.system() == 'Windows'):
    os.system('cls')



#   Changed temporarily for testing
prompt = "You're a good helper!" # "You're the dungeon master of an epic dungeons and dragons campaign! Lead your player through an epic adventure and make sure that there is a plot with a climax and an ending!"
messages = [
    {
        "role": "system", 
        "content": prompt
    }
]



while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'\nDM: {chat_response}\n')