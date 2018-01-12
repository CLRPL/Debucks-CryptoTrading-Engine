#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################



import logging
from pyxchange import utils
from pyxchange import engine

logging.basicConfig(level = logging.DEBUG)

class market():

	def __init__(self):
		self.matcher = engine.Matcher()
		self.traders = list()

	def add_trader(self,user_id):
		mdequeHandler = utils.DequeHandler()
		mtrader = engine.Trader(matcher, str(user_id), mdequeHandler)
		self.traders.append(mtrader)
		return traders

	def create_order(self,**kwargs):
		trader = self.traders[kwargs['trader_id']]
		trader.createOrder({ 'side': kwargs['side'], 'price': kwargs['price'], 'quantity': kwargs['quantity'], 'orderId': kwargs['orderId'] })

	