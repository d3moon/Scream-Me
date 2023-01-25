import os
import vonage
import time

filepath = input("Enter the filepath of the private_key: ")
app_id = input("Enter the filepath of the application id: ")

if not os.path.isfile(filepath):
    print("[ERROR] The file does not exist.")

with open(filepath, 'rb') as f:
    key = f.read()
    key = key.decode()


def progress_bar():
    print("Calling...")
    print("[", end="")
    for i in range(20):
        time.sleep(0.1)
        print("█", end="")
    print("]")
    print("Successful call")

client = vonage.Client(
    application_id=app_id,
    private_key=key
)


voice = vonage.Voice(client)

to = input("Enter the number you'll calling: ")
from_number = input("Enter the number from you'll calling: ")
message = input("Enter the message: ")

response = voice.create_call({
    'to': [{'type': 'phone', 'number': to}],
    'from': {'type': 'phone', 'number': from_number},
    'ncco': [{'action': 'talk', 'text': message}]
})

print(response)
progress_bar()
