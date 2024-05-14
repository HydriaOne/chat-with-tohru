from gradio_client import Client

from core.applio import create_tts
from core.audio import play_file
from core.chat import send_message_to_chat, choose_the_character

#TODO load all the config from a file
gradio_client = Client("http://127.0.0.1:6969/")
llm_url = "http://127.0.0.1:5000/v1/chat/completions"

#TODO handle all the chat history in a json format.
chat_history = []

#TODO all the try catch logic
#TODO all the logging

if __name__ == '__main__':
    character_config = choose_the_character()
    while True:
        try:
            history,assistant_message = send_message_to_chat(chat_history, llm_url)
            play_file(create_tts(gradio_client,assistant_message,character_config))
        except KeyboardInterrupt:
            break  # Allow graceful exit on Ctrl+C
