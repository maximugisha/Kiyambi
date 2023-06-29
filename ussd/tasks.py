from django.db.models import Q
from django.db.utils import IntegrityError
from django.http import HttpResponse
import africastalking

# Create your credentials
username = "maximo"
api_key = "b6efe729707d4fc8a37e63f185e3a88ebe8f221a67b0b1a85a2f67cc8bb03998"

# Initialize the SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS


def send_sms_order(message):
    # Define some options that we will use to send the SMS
    ussd
    recipients = ["+256702431725", "+256775097505"]
    # sender = '14262'
    # Send the SMS
    try:
        # Once this is done, that's it! We'll handle the rest
        msg_response = sms.send(message, recipients)
        print(msg_response)
        print(message)
    except IntegrityError as e:
        print(f"Houston, we have a problem {e}")


def send_sms(message):
    # Define some options that we will use to send the SMS
    ussd
    recipients = [str(ussd.phone_number)]
    # sender = '14262'
    # Send the SMS
    try:
        # Once this is done, that's it! We'll handle the rest
        msg_response = sms.send(message, recipients)
        print(msg_response)
        print(message)
    except IntegrityError as e:
        print(f"Houston, we have a problem {e}")


# @shared_task
def ussd(request):
    session_id = request.POST.get("sessionId")
    serviceCode = request.POST.get("serviceCode")
    ussd.phone_number = request.POST.get("phoneNumber")
    text = request.POST.get("text", default="")

    response = ""
    if text == "":

        # elif text == "1":
        # message1 = "I want to make an order, My Phone Number is: " + str(
        #     ussd.phone_number
        # )
        # send_sms_order(message1)
        #
        # response = "END Your Request to order has been received"

        response = "CON Welcome to Kiyambi your PA.\n"
        response += "Choose PA for \n"
        response += "1. Sign Language Interpreters \n"
        response += "2. Guides \n"
        response += "3. Captioners \n"
        response += "4. Helpers"

    elif text == "1" or text == "2" or text == "3" or text == "4":
        response = "CON Choose Your location \n"
        response += "1. Rubaga Division \n"
        response += "2. Nakasero Division \n"
        response += "3. Kyaddondo Division"
        response += "4. Other Regions"

    elif text == "1*1" or text == "1*2" or text == "1*3":
        response = "CON Here are Sign language interpreters in your region \n"
        response += "1. Amon - 5 star \n"
        response += "2. Mercy 5 star \n"
        response += "3. Leticia 4 star"

    elif text == "2*1" or text == "2*2" or text == "2*3":
        response = " CON Here are Guides in your region \n"
        response += "1. Bruno 5 star \n"
        response += "2. Laila 5 star \n"
        response += "3. Kim 4 star"

    elif text == "3*1" or text == "3*2" or text == "3*3":
        response = " CON Here are Captioners in your region \n"
        response += "1. Bruno 5 star \n"
        response += "2. Laila 5 star \n"
        response += "3. Kim 4 star"

    elif text == "4*1" or text == "4*2" or text == "4*3":
        response = " CON Here are Helpers in your region \n"
        response += "1. Bruno 5 star \n"
        response += "2. Laila 5 star \n"
        response += "3. Kim 4 star"

    elif text == "1*1*1" or text == "2*1*1" or text == "3*1*1" or text == "4*1*1":
        message1 = "KIYAMBI P.A p Mr Maximo Mugisha located in Makererere, " \
                   "Kampala, has requested for your service. His Phone Number is: " + str(ussd.phone_number)
        send_sms_order(message1)

        response = " END Your Selected guide hase been notified. \n"
        response += " They will call you shortly. \n"

    else:
        response = "END Still under implementation"

    return HttpResponse(response)
