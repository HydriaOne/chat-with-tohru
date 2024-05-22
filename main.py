import yaml
from gradio_client import Client
from rich import print

from core.applio import create_tts
from core.audio import play_file
from core.chat import send_message_to_chat, choose_tts_character

#TODO handle all the chat history in a json format.
chat_history = []

# load Config
with open('config.yaml', 'r') as file:
   try:
        config_file = yaml.safe_load(file)
        tts_client = Client(config_file['Applio']['base_url']+":"+str(config_file['Applio']['port']))
        llm_url = config_file['LLM']['base_url']+":"+str(config_file['LLM']['port'])+"/v1/chat/completions"
   except yaml.YAMLError as exc:
       print(exc)

#TODO all the logging

if __name__ == '__main__':
    print("\n[orchid]Chat with Tohru\n")
    tts_character_config = choose_tts_character()
    while True:
        try:
            history,assistant_message = send_message_to_chat(chat_history, llm_url, config_file['LLM']['user_name'])
            play_file(create_tts(tts_client,assistant_message,tts_character_config))
        except KeyboardInterrupt:
            break  # Allow graceful exit on Ctrl+C
