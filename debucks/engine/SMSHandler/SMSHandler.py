#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################

"""
The file contains all the basic function used to send SMS.
This file automatically chooses the appropiate SMS engine based on setting in config.py file.
"""

from SubConfig import SMS_ENGINE
import PilvoHandler
import TwilioHandler

def send_sms(destination_number,text_body):
    """
    @params:
        destination_number(String): The destination phone number.
        text_body(String): The body of the SMS
    @return:
        null
    The function sends a text SMS from the provided source number to the destination number.

    """
    if SMS_ENGINE == 'PILVO':
    	PilvoHandler.send_sms_via_pilvo(destination_number,text_body)
    elif SMS_ENGINE == 'TWILIO':
    	TwilioHandler.send_sms_via_twilio(destination_number,text_body)
    else:
    	raise Exception('UNKNOW SMS ENGINE')

def send_bulk_sms(destination_numbers,text_body):
    """
    @params:
        destination_number(String): List of  destination phone numbers as string. (Example: ['1111111','121212424'])
        text_body(String): The body of the SMS
    @return:
        null
    The function sends a text SMS from the provided source number to the destination numbers.
    """
    if SMS_ENGINE == 'PILVO':
    	PilvoHandler.send_bulk_sms_via_pilvo(destination_number,text_body)
    elif SMS_ENGINE == 'TWILIO':
    	TwilioHandler.send_bulk_sms_via_twilio(destination_number,text_body)
    else:
    	raise Exception('UNKNOW SMS ENGINE')