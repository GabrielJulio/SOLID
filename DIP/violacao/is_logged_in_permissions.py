from .interfaces.ipermissions import IPermissions

class IsLoggedInPermissions (IPermissions):
	def last_login():
		return auth.last_login()
