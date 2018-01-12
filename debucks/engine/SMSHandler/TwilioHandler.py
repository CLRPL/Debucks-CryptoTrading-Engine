#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################

"""
A file that contains functions to talk to the Twilio API and to send SMS.
"""

from SubConfig import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,TWILIO_DEFAULT_SOURCE_NUMBER #import default values from the subconfig file
from twilio.rest import Client

def send_sms_via_twilio(destination_number,text_body,source_number = TWILIO_DEFAULT_SOURCE_NUMBER):
    """
    @params:
        source_number(String): The number provided by pilvo as your source number unless specified.
        destination_number(String): The destination phone number.
        text_body(String): The body of the SMS
    @return:
        null
    The function sends a text SMS from the provided source number to the destination number.

    """
    try:
       client = Client(account_sid, auth_token)
       message = client.messages.create(
           to=str(destination_number), 
           from_=str(source_number),
           body=str(text_body)
           )
       print(message.sid)
    except:
        print("error")


def send_bulk_sms_via_twilio(destination_numbers,text_body,source_number = TWILIO_DEFAULT_SOURCE_NUMBER):
    """
    @params:
        source_number(String): The number provided by pilvo as your source number unless specified.
        destination_number(String): List of  destination phone numbers as string. (Example: ['1111111','121212424'])
        text_body(String): The body of the SMS
    @return:
        null
    The function sends a text SMS from the provided source number to the destination numbers.
    """
    pass