from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+18039982205 "

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+918329469206",]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("AC2bac814ea87d6ed31a1b0fd5a1e86874", "80a68e5f8c0b7ad2f11ce2f079a1b654")



def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)

