from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils import executor

api_key = ''
bot = Bot(token=api_key)
dsp = Dispatcher(bot=bot, storage=MemoryStorage())

@dsp.message_handler(commands=['start'])
async def start(message):
    print('Выведено сообщение: Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dsp.message_handler()
async def all_messages(message):
    print('Выведено сообщение: Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)