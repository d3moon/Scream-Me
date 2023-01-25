import phonenumbers

def is_phishing(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return True
    except phonenumbers.phonenumberutil.NumberParseException:
        return True
    return False
