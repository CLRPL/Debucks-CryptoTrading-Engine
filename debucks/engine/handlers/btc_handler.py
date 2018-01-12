#################################################################
#################   Automatically Generated   ###################

# @Owner:   Cohomology Labs Research Pvt Ltd
# @Owner's Website: https://cohomologylabs.tech
# @CreatedBy: ArvindSinc
# @Date:   10/01/2018

#################################################################

from .handler import handler
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging


logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

class btc_handler(handler):
	def __init(self):
		# rpc_user and rpc_password are set in the bitcoin.conf file
		rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))
		best_block_hash = rpc_connection.getbestblockhash()
		print(rpc_connection.getblock(best_block_hash))

		# batch support : print timestamps of blocks 0 to 99 in 2 RPC round-trips:
		commands = [ [ "getblockhash", height] for height in range(100) ]
		block_hashes = rpc_connection.batch_(commands)
		blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
		block_times = [ block["time"] for block in blocks ]
		print(block_times)

	def backupwallet(self): pass

	def dumpprivkey(self): pass

	def dumpwallet(self):pass

	def getaccount(self):pass

	def getaccountaddress(self):pass

	def getaddressbyaccount(self):pass

	def getbalance(self):pass

	def getnewaddress(self):pass

	def gettransaction(self):pass

	def sendfrom(self):pass

