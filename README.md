# jipubetapi
## Установка библиотеки
```python
  pip install --upgrade jipubetapi
```
### Библиотека полностью асинхронна
________
## Пример использования
```python
import jipubetapi
from jipubetapi import ApiError
import asyncio
api = jipubetapi.JipubetKey()
async def main():
  try:
    print(await api.toad())
   except ApiError:
    print('api error')
asyncio.run(main())
```
#### Подробнее можете прочитать в документации: _скоро_
