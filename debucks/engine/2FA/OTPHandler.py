#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################

"""
This file is used to send and verify OTP's.
"""

import pyotp  # 'pyotp' is an open source package to generate and validate OTPs. Learn more about pyotp here - https://github.com/pyotp/pyotp.
import unicodedata
import datetime
import SubConfig
from SMSHandler.SMSHandler import *

# We shall use the Time-Based OTP (TOTP) generation algorithm.
totp = pyotp.TOTP(pyotp.random_base32())

def send_otp(destination_number):
	"""
	Send a OTP
	"""
	text_body = str(totp) + "is your Debucks OTP and is valid for 60 Seconds Only"
	SMSHandler.send_sms(destination_number,text_body)


def verify_otp(user_input):
    current_time = datetime.datetime.now()
    """
    Compare the user entered OTP against valid OTPs for the last 60 seconds.
    """
    for i in range(-60, 1):
        if strings_equal(str(user_input), str(totp.at(current_time, i))):
            return True
        return False

def strings_equal(s1, s2):
    """
    Timing-attack resistant string comparison.
    Normal comparison using == will short-circuit on the first mismatching
    character. This avoids that by scanning the whole string, though we
    still reveal to a timing attack whether the strings are the same
    length.
    """
    s1 = unicodedata.normalize('NFKC', s1)
    s2 = unicodedata.normalize('NFKC', s2)
    return compare_digest(s1, s2)