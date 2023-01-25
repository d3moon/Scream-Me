import os
import vonage
from progressbar import progress_bar, call_progress_bar
from phishing import is_phishing
from config import read_private_key

filepath = input("Enter the filepath of the private_key: ")
app_id = input("Enter the filepath of the application id: ")
key = read_private_key(filepath)

client = vonage.Client(
    application_id=app_id,
    private_key=key
)


def send_sms(client):
    sms = vonage.SMS(client)

    to = input("Enter the number you'll sending SMS: ")
    if is_phishing(to):
        choice = input(
            "The number is known for being used in phishing campaigns. Do you still want to proceed? (y/n): ")
        if choice.lower() != "y":
            print("Aborting SMS.")
            return
    from_number = input("Enter the number from you'll sending SMS: ")
    message = input("Enter the message: ")
    language = input("Enter the language of the message: ")

    response = sms.send_message({
        'from': from_number,
        'to': to,
        'text': message,
        'language': language
    })

    print(response)
    progress_bar()


def make_call(client):
    voice = vonage.Voice(client)

    to = input("Enter the number you'll calling (format: 1122345678990): ")
    if is_phishing(to):
        choice = input("The number is known for being used in phishing campaigns. Do you still want to proceed? (y/n): ")
        if choice.lower() != "y":
            print("Aborting call.")
            return
    from_number = input("Enter the number from you'll calling (format: 1122345678990): ")
    message = input("Enter the message: ")

    response = voice.create_call({
        'to': [{'type': 'phone', 'number': to}],
        'from': {'type': 'phone', 'number': from_number},
        'ncco': [{'action': 'talk', 'text': message}]
    })

    print(response)
    call_progress_bar()

while True:
    choice = input("Enter 1 to send an SMS, 2 to make a call, or 3 to exit: ")
    if choice == "1":
        send_sms(client)
    elif choice == "2":
        make_call(client)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
