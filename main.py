import os
import vonage
import time
from tqdm import tqdm

filepath = input("Enter the filepath of the private_key: ")
app_id = input("Enter the filepath of the application id: ")

if not os.path.isfile(filepath):
    print("[ERROR] The file does not exist.")

with open(filepath, 'rb') as f:
    key = f.read()
    key = key.decode()

client = vonage.Client(
    application_id=app_id,
    private_key=key
)

def progress_bar(text):
    for i in tqdm(range(100), text):
        time.sleep(0.01)
    print("Successful "+ text)

def make_call():
    to = input("Enter the number you'll calling: ")
    from_number = input("Enter the number from you'll calling: ")
    message = input("Enter the message you want to say during the call: ")
    voice = vonage.Voice(client)
    response = voice.create_call({
        'to': [{'type': 'phone', 'number': to}],
        'from': {'type': 'phone', 'number': from_number},
        'ncco': [{'action': 'talk', 'text': message}]
    })
    print(response)
    progress_bar("Calling...")

def send_sms():
    to = input("Enter the number you'll sending SMS: ")
    from_number = input("Enter the number from you'll sending SMS: ")
    message = input("Enter the message: ")
    language = input("Enter the language you want to use (default is 'en-US'): ") or 'en-US'
    effect = input("Enter the sound effect you want to add (default is 'robot'): ") or 'robot'
    sms = vonage.SMS(client)
    response = sms.create_sms({
        'to': to,
        'from': from_number,
        'text': message,
        'voice': {'language': language, 'effect': effect}
    })
    print(response)
    progress_bar("Sending SMS...")

def main():
    print("1. Make a call")
    print("2. Send an SMS")
    choice = input("Enter your choice: ")
    if choice == '1':
        make_call()
    elif choice == '2':
        send_sms()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
