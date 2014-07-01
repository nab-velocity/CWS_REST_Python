class NabError(Exception):
	
	def __init__(self, reason, response=None):
		self.reason = str(reason)
		self.response = response
	
	def __str__(self):
		return self.reason

