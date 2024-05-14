import requests
import json
from glob import glob

# TODO Elavorate the logic between chat character with audio TTS profile
# Export the character list and the file path of it.
def get_the_characters_list():
    characters = {}
    for i in glob('characters/*.json'):
        if i.split("\\")[1] != "example.json":
            character_file = i.split("\\")[1]
            characters[character_file.split(".")[0]] = i
    return characters

# TODO select the characters for the json files.
# TODO iterate and add logic if there is mutliple characters in the file.
def choose_the_character():
    character_list = get_the_characters_list()
    for character in character_list:
        character_config = json.load(open(character_list.get(character)))
        break
    return character_config.get(list(character_config.keys())[0])

# TODO for now only it works with the character tohru in the LLM, improve all the logic and clean up.
def send_message_to_chat(history, url):
    headers = {
        "Content-Type": "application/json"
    }

    user_message = input("> Mina: ")
    history.append({"role": "user", "content": user_message})
    data = {
        "mode": "chat",
        "character": "Tohru",
        "user_name": "Mina",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": assistant_message})
    print("> Fauna: "+assistant_message+"\n")
    return history, assistant_message
