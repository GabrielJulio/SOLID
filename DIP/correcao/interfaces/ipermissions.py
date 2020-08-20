from .iauthetication_for_user import IAuthenticationForUser

class IPermissions()
	def __init__(self, auth: IAuthenticationForUser)
		self.auth = auth
		
	def has_permissions():
		pass
