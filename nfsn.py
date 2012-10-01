from requests.auth import AuthBase
import hashlib
import random
import string
import time
from calendar import timegm
import urllib

class NFSNAuth(AuthBase):
	"""Signs the request to NFS.N"""
	api_key = None
	login = None

	def __init__(self, api_key=None, login=None):
		if api_key is None and self.api_key is None:
			raise KeyError("No Api key set.")
		elif self.api_key is None:
			self.api_key = api_key

		if login is None and self.login is None:
			raise KeyError("No login credentials specified")
		elif self.login is None:
			self.login = login

	def __call__(self, request):
		"""Generate a hash, and set the X-NFSN Header"""
		body = ""
		if isinstance(request.data, list) and request.data:
			body = urllib.urlencode(request.data)
		elif request.data:
			body = request.data

		body_hash = hashlib.sha1(body).hexdigest()
		salt = self._gen_salt()
		timestamp = self._gen_timestamp()
		hash_string = ";".join((self.login,
								timestamp,
						 		salt,
						 		self.api_key,
						 		request.path_url,
						 		body_hash))
		hash = hashlib.sha1(hash_string).hexdigest()
		request.headers["X-NFSN-Authentication"] = \
				";".join((self.login, timestamp, salt, hash))
		return request

	def _gen_salt(self):
		"""Generate a 16 character a-zA-Z0-9 Salt for signing"""
		chars = "".join((string.lowercase, string.uppercase, string.digits))
		return "".join([random.choice(chars) for x in xrange(16)])
	
	def _gen_timestamp(self):
		"""Get the current 32-bit UNIX timestamp"""
		return str(timegm(time.gmtime()))
