import random
from aiogram import types
from aiogram.dispatcher import Dispatcher

# Максимальное число попыток
MAX_ATTEMPTS = 5

# Функция-обработчик для команды /start
async def start_command(message: types.Message):
    global secret_number, attempts_left
    secret_number = random.randint(1, 100)
    attempts_left = MAX_ATTEMPTS
    await message.reply(f"Привет! Я загадал число от 1 до 100. У тебя есть {MAX_ATTEMPTS} попыток. Попробуй угадать!")

# Функция-обработчик для текстовых сообщений
async def guess_number(message: types.Message):
    global attempts_left
    user_number = int(message.text)

    if user_number == secret_number:
        await message.reply("Поздравляю, ты угадал число!")
        return
    elif user_number < secret_number:
        await message.reply("Загаданное число больше.")
    else:
        await message.reply("Загаданное число меньше.")

    attempts_left -= 1
    if attempts_left > 0:
        await message.reply(f"Осталось {attempts_left} попыток.")
    else:
        await message.reply("У тебя закончились попытки. Загаданное число было " + str(secret_number))

# Функция для настройки обработчиков команды /start
def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(guess_number)

