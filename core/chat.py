import requests
import json
import inquirer
import sys
from rich import print
from rich.prompt import Prompt
from glob import glob

def choose_tts_character():
    tts_characters = {} # Here we'll contain the character name an the path of this json config.
    tts_characters_name_list = [] # Here is the list containing all the characters avaiable in a interactive selector.

    for i in glob('characters/*.json'):
        if i.split("\\")[1] != "example.json":
            character_file = i.split("\\")[1]
            tts_characters[character_file.split(".")[0]] = i

    for voice in tts_characters.keys():
        tts_characters_name_list.append(voice.capitalize())
    tts_voices_selector = [
        inquirer.List('tts_selected_character',
                message="Select your desired TTS Character",
                choices=tts_characters_name_list,
            ),
    ]
    try:
        answers = inquirer.prompt(tts_voices_selector)
    except IndexError:
        print("Put some tts characters in the folder bro")
        sys.exit(0)
    print("You selected: [cyan]"+ answers['tts_selected_character']+"[/cyan]\n")

    # Now with the selected tts character we load all the model json config
    character_config = json.load(open(tts_characters[answers['tts_selected_character'].lower()]))
    return character_config.get(list(character_config.keys())[0])

# TODO for now only it works with the character tohru in the LLM, create extra functions to gather more data, improve all the logic and clean up.
def send_message_to_chat(history, url, user_name):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "mode": "chat",
        "character": "Tohru",
        "user_name": user_name,
        "messages": history
    }
    user_message = Prompt.ask("> "+data["user_name"])
    history.append({"role": "user", "content": user_message})

    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": assistant_message})
    print("[orchid]> "+data["character"]+": "+assistant_message+"\n")
    return history, assistant_message
