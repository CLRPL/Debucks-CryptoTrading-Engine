#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################


'''
All the handlers should be imported here;
'''
from handlers.btc_handler import btc_handler
from handlers.xmr_handler import xmr_handler
from markets.btc_xmr_market import btc_xmr_market


'''
Declare all the handlers here.
Note : All the handlers should be derived from the currency_handler class.
'''
BTC_Handler = btc_handler()
XMR_Handler = xmr_handler()

'''
Declare all the markets here.
NOTE: All the markets should be derived from the market class.
'''
BTC_XMR_MARKET = btc_xmr_market()

'''
All the currency supported by debucks goes here;
(symbol,name,handler)
The handler should be derived from the handler class.
'''
Currencies = (
	('BTC','Bitcoin',BTC_Handler),
	('XMR','Monero',XMR_Handler),
)

'''
All the markets supported by debucks goes here;
(from,to,market)
'''
Markets = (
	('BTC','XMR',BTC_XMR_MARKET),
)

#Pilvo 
PILVO_AUTH_ID = 'bla bla bla'
PILVO_AUTH_TOKEN = 'bla bla bla'
PILVO_DEFAULT_SOURCE_NUMBER = 'bla bla bla'

#Twilio
TWILIO_ACCOUNT_SID = 'ACxxxxxxxxxxx'
TWILIO_AUTH_TOKEN = 'bla bla'
TWILIO_DEFAULT_SOURCE_NUMBER ='bla bla bla'

SMS_ENGINE = 'PILVO'
#SMS_ENGINE = 'TWILIO'