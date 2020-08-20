from .iconnector import IConnector


class IAuthenticationForUser():
    def __init__(self, connector: IConnector):
		self.connection = connector.connect()
	
	def authenticate(self, credentials):
		pass
	
	def is_authenticated(self):
		pass
	
	def last_login(self):
		pass
