import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F
from update_question import new_quiz

dp = Dispatcher()

logging.basicConfig(level=logging.INFO)
API_TOKEN = ''
DB_NAME = 'quiz_bot.db'

with open('bot_token.txt') as f:
    API_TOKEN = f.read()

bot = Bot(token=API_TOKEN)

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Начать игру'))
    await message.answer("Начнем квиз!", reply_markup=builder.as_markup(resize_keyboard = True))


@dp.message(F.text =='Начать игру')
@dp.message(Command('qiuz'))
async def cmd_start(message: types.Message):
    await message.answer("Давайте начнем квиз!")
    await new_quiz(message)


@dp.message(Command('help'))
async def cmd_start(message: types.Message):
    await message.answer("Команды бота:\n\start - начать взаимодействие с ботом \n \quiz - начать игру \n \help - список команд")



async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        await db.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, user_score INTEGER)''')
        await db.commit()


# Запуск процесса поллинга новых апдейтов
async def main():
    await create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())