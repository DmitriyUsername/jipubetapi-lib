##########################################################################################################
# На данный момент проходит ОБТ библиотеки,                                                              #
# а также API. Возможны ошибки, опечатки и тому подобное.                                                #
# Просьба сообщать обо всех найденых багах/ошибках на сервер поддержки (https://discord.gg/WtH6XeVKkh)   #
# Или в ЛС JIPUBET#5964, Kovirum#6492.                                                                   #
##########################################################################################################
import aiohttp
from typing import Optional
from jipubetapi.modules.errors import ApiError

class JipubetKey:
	"""
	This class is used to simplify the use of the API jipubet-api.ga

	Parameters
	----------
	key : :class: `str`
		This is the API key
	"""
	
	def __init__(self, key: Optional[str] = None):
		self.key = key
	
	@staticmethod
	async def toad():                                                                           
		"""
		This function accesses the method "toad"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/toad") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	async def key_check(self):
		key = self.key
		if key is None:
			return 'Вы не вводили ключа'
		else:
			return f'Вы ввели ключ «{key}»'
	
	@staticmethod
	async def token():
		"""
		This function accesses the method "token"


		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/token") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				
				raise ApiError(f'API status code {status}')
			
	@staticmethod
	async def cheer(user: str):
		"""
		This function accesses the method "toad"

		Parameters
		----------
		user : :class: `str`
			Username
		"""
		async with aiohttp.request("GET", url=f"https://www.jipubet-api.ga/cheer?user={user}") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
			
	@staticmethod
	async def captcha(count: int):
		"""
		This function accesses the method "captcha"

		Parameters
		----------
		count : :class: `int`
			This is the number of characters in the captcha
		"""
		if type(count) is not int:
			raise ValueError('Count not int')
		async with aiohttp.request("GET", url=f"https://www.jipubet-api.ga/captcha?count={count}") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
			
	@staticmethod
	async def cat():
		"""
		This function accesses the method "cat"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/cat") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	@staticmethod
	async def axolotl():
		"""
		This function accesses the method "axolotl"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/axolotl") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	@staticmethod
	async def capybara():
		"""
		This function accesses the method "capybara"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/capybara") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	@staticmethod
	async def fox():
		"""
		This function accesses the method "fox"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/fox") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	@staticmethod
	async def dog():
		"""
		This function accesses the method "dog"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/dog") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	@staticmethod
	async def wolf():
		"""
		This function accesses the method "wolf"

		"""
		async with aiohttp.request("GET", url="https://www.jipubet-api.ga/wolf") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
	
	@staticmethod
	async def server(ip: str = 'mc.hypixel.net'):
		"""
		This function accesses the method "fox"
		Parameters
		---------
		ip : :class: `str`
			The IP of the minecraft server
		"""
		async with aiohttp.request("GET", url=f"https://www.jipubet-api.ga/server?ip={ip}") as response:
			status = response.status
			if status == 200:
				data = await response.json(content_type=None)
				return data['message']
			elif 400 >= status <= 499:
				data = await response.json(content_type=None)
				return data['error']
			else:
				raise ApiError(f'API status code {status}')
