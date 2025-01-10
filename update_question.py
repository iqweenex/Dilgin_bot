import aiosqlite
from aiogram import F
from gen_opt_kb import generate_options_keyboard
from quiz_data import quiz_data



DB_NAME = 'quiz_bot.db'

async def get_question(message, user_id):
    current_question_index = await get_quiz_index(user_id)
    correct_index = quiz_data[current_question_index]['correct_option']
    opts = quiz_data[current_question_index]['options']
    kb = generate_options_keyboard(opts, opts[correct_index])
    await message.answer(f"{quiz_data[current_question_index]['question']}", reply_markup=kb)


async def new_quiz(message):
    user_id = message.from_user.id
    current_question_index = 0
    new_score = 0
    await update_quiz_index(user_id, current_question_index)
    await update_user_score(user_id, new_score)
    await get_question(message, user_id)


async def get_user_score(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT user_score FROM users WHERE user_id = (?)', (user_id, )) as cursor:
            result = await cursor.fetchone()
            if result is not None:
                return result[0]
            else:
                return 0


async def get_quiz_index(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = (?)', (user_id, )) as cursor:
            result = await cursor.fetchone()
            if result is not None:
                return result[0]
            else:
                return 0


async def update_quiz_index(user_id, index):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('INSERT OR REPLACE INTO quiz_state (user_id, question_index) VALUES (?, ?)', (user_id, index))
        await db.commit()


async def update_user_score(user_id, user_score):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('INSERT INTO users (user_id, user_score) VALUES (?, ?) ON CONFLICT(user_id) DO UPDATE SET user_score = excluded.user_score', (user_id, user_score))
        await db.commit()