class ApiError(BaseException):
	def __init__(self, message):
		self.message = message
		
	def __str__(self):
		return f'API status code {self.message}'
