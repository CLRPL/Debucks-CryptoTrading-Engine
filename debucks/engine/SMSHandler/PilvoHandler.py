#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################

"""
A file that contains functions to talk to the Pilvo API and to send SMS.
"""

from SubConfig import PILVO_AUTH_ID,PILVO_AUTH_TOKEN,PILVO_DEFAULT_SOURCE_NUMBER #import default values from the subconfig file
import plivo

def send_sms_via_pilvo(destination_number,text_body,source_number = PILVO_DEFAULT_SOURCE_NUMBER):
    """
    @params:
        source_number(String): The number provided by pilvo as your source number unless specified.
        destination_number(String): The destination phone number.
        text_body(String): The body of the SMS
    @return:
        null
    The function sends a text SMS from the provided source number to the destination number.

    """

    client = plivo.Client(PILVO_AUTH_ID, PILVO_AUTH_TOKEN)
    try:
        '''
        An example response
        {
            "message": "message(s) queued",
            "message_uuid": ["db3ce55a-7f1d-11e1-8ea7-1231380bc196"],
            "api_id": "db342550-7f1d-11e1-8ea7-1231380bc196"
        }
        '''
        response = client.messages.create(
            src=str(source_number),
            dst=str(destination_number),
            text=str(text_body),
        )
        print(response.__dict__)

    except plivo.exceptions.PlivoRestError as e:
        print(e)

def send_bulk_sms_via_pilvo(destination_numbers,text_body,source_number = PILVO_DEFAULT_SOURCE_NUMBER):
    """
    @params:
        source_number(String): The number provided by pilvo as your source number unless specified.
        destination_number(String): List of  destination phone numbers as string. (Example: ['1111111','121212424'])
        text_body(String): The body of the SMS
    @return:
        null
    The function sends a text SMS from the provided source number to the destination numbers.
    """
    client = plivo.Client(PILVO_AUTH_ID, PILVO_AUTH_TOKEN)
    try:
        '''
        An example response
        {
            "api_id": "984bc856-9231-11e7-b886-067c5485c240",
            "invalid_number": [
                "jsgf3dsjh28372"
            ],
            "message": "message(s) queued",
            "message_uuid": [
                "6da4afba-2bcf-4a87-9eff-d2f88577b0f1",
                "6da384ba-19js-aand-2h3g-r2f8ja0700f1"
            ]
        }
        '''
        response = client.messages.create(
            src=str(source_number),
            dst=[str(destination_number) for destination_number in destination_numbers],
            text=str(text_body),
        )
        print(response.__dict__)

    except plivo.exceptions.PlivoRestError as e:
        print(e)