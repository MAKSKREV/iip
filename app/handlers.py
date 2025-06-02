from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import app.keyboards as kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import BufferedInputFile
from config import GROUP_ID,KAT2_GROUP_ID,KAT3_GROUP_ID,TOKEN
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aiogram.types import  LabeledPrice
from aiogram import Router, types
import random
from aiogram.utils.keyboard import InlineKeyboardBuilder
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import subprocess
from datetime import datetime

import logging



from aiogram import Bot, Dispatcher, types

import config
logging.basicConfig(level=logging.INFO)





router = Router()



# Dictionary to store temporary messages
user_messages = {}


class AuthState(StatesGroup):
    waiting_for_phone = State()
    waiting_for_code = State()
    waiting_for_plus1_content = State()
    waiting_for_plus3_content = State()
    waiting_for_kat1_content = State()
    waiting_for_kat2_content = State()
    waiting_for_plus22_content = State()
    waiting_for_plus222_content = State()

    waiting_for_username = State()
    waiting_for_tg_id = State()
    waiting_for_chat_link = State()
    waiting_for_violation_link = State()




@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    if message.from_user.id in [5176998143,8013867574]:
        await message.answer('Привет админ')
        await message.answer('Выбери один из пунктов:', reply_markup=kb.modex)
    else:
        await message.answer(f'Привет {message.from_user.first_name}')
        await message.answer('Выбери один из пунктов:', reply_markup=kb.vibor)



def payment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Заплатить⭐️", pay=True)
    return builder.as_markup()

@router.callback_query(F.data == 'cancel_payment')
async def cancel_payment_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer("Платеж отменен.")
    await callback_query.message.delete_reply_markup() # Удалить клавиатуру с инвойсом
    await state.clear() # Очистить состояние, если оно было активно

@router.callback_query(F.data == 'nft0')
async def send_invoice_handler_25_stars(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data({'stars_to_add': 5})
    prices = [LabeledPrice(label="XTR", amount=5)]
    await callback_query.answer()
    await callback_query.message.answer_invoice(
        title="Пополнить баланс",
        description="Заплатить 5 звёзд!",
        prices=prices,
        provider_token="вставьте ваш токен",  # вставьте ваш токен
        payload="channel_support_25",
        currency="XTR",
        reply_markup=payment_keyboard(),
    )

@router.callback_query(F.data == 'nft1')
async def send_invoice_handler_50_stars(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data({'stars_to_add': 15})
    prices = [LabeledPrice(label="XTR", amount=15)]
    await callback_query.answer()
    await callback_query.message.answer_invoice(
        title="Пополнить баланс",
        description="Заплатить 15 звёзд!",
        prices=prices,
        provider_token="вставьте ваш токен",
        payload="channel_support_50",
        currency="XTR",
        reply_markup=payment_keyboard(),
    )

@router.callback_query(F.data == 'nft2')
async def send_invoice_handler_100_stars(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data({'stars_to_add': 45})
    prices = [LabeledPrice(label="XTR", amount=45)]
    await callback_query.answer()
    await callback_query.message.answer_invoice(
        title="Пополнить баланс",
        description="Заплатить 45 звёзд!",
        prices=prices,
        provider_token="вставьте ваш токен",
        payload="channel_support_100",
        currency="XTR",
        reply_markup=payment_keyboard(),
    )

@router.callback_query(F.data == 'nft')
async def send_invoice_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
    '<b>💎 НФТ (0.75%)</b>\n'
    '— Любой (0.75%)\n\n'
    '<b>🪐 НФТ (2%)</b>\n'
    '— Любой (2%)\n\n'
    '<b>🎰 НФТ (15%)</b>\n'
    '— Любой (15%)',
    parse_mode='HTML',
    reply_markup=kb.vibor666
)

@router.pre_checkout_query()
async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)

@router.message(F.successful_payment)
async def successful_payment(message: types.Message, state: FSMContext):
    data = await state.get_data()
    stars_to_add = data.get('stars_to_add', 0)
    if not stars_to_add:
        await message.answer("Ошибка: количество звезд для добавления не установлено.")
        return

    # Определяем вероятность выигрыша/проигрыша в зависимости от суммы
    if stars_to_add == 5:
        win_probability = 0.0075  # 0.75%
        lose_probability = 0.9325  # 93.25%
    elif stars_to_add == 15:
        # Можно задать свои вероятности для этого варианта
        win_probability = 0.2  # например, 10%
        lose_probability = 0.85  # 85%
    elif stars_to_add == 45:
        # И так далее
        win_probability = 0.15
        lose_probability = 0.80
    else:
        # Значение по умолчанию
        win_probability = 0.05
        lose_probability = 0.90

    # Генерируем случайное число для определения результата
    rand_value = random.random()

    if rand_value <= win_probability:
        result = "выиграл"
        response_text = "Поздравляем! Вы выиграли!"
    else:
        result = "проиграл"
        response_text = "К сожалению, вы проиграли."

    # Ответ пользователю
    await message.answer(response_text)

    # Очистка состояния
    await state.clear()





    


@router.callback_query(F.data.startswith('kat'))
async def handle_category_selection(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    await callback.answer()
    await state.update_data(selected_category=category)
    
    if category == 'kat0':
        await callback.message.answer('Выберите вариант:', reply_markup=kb.vopros1)
    elif category == 'kat1':

        await callback.message.answer('Отправьте текст с фото/текст с видео')
        await callback.message.answer("❗❗В сообщении может присутствовать максимум 1 видео или 1 фото❗❗")
        await state.set_state(AuthState.waiting_for_kat1_content)


    elif category == 'kat2':
        await callback.message.answer('Напишите ваш тэг и причину разбана:')
        await state.set_state(AuthState.waiting_for_kat2_content)


@router.message(AuthState.waiting_for_kat1_content, F.photo)
async def handle_kat1_photo(message: Message, state: FSMContext, bot: Bot):
    photo = message.photo[-1]
    caption = message.caption or ""
    photo_file = await bot.get_file(photo.file_id)
    photo_bytes = await bot.download_file(photo_file.file_path)
    
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'photo': photo,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored photo message before forwarding to group with key {key}")

    # Send to group
    await bot.send_photo(
        chat_id=KAT3_GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )






    

@router.message(AuthState.waiting_for_kat1_content, F.video)
async def handle_kat1_video(message: Message, state: FSMContext, bot: Bot):
    video = message.video
    caption = message.caption or ""
    video_file = await bot.get_file(video.file_id)
    video_bytes = await bot.download_file(video_file.file_path)
    
    # Store the video in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'video': video,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored video message before forwarding to group with key {key}")

    # Send to group
    await bot.send_video(
        chat_id=KAT3_GROUP_ID,
        video=BufferedInputFile(video_bytes.read(), filename="video.mp4"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )


@router.message(AuthState.waiting_for_kat1_content, F.text)
async def handle_kat1_text(message: Message, state: FSMContext, bot: Bot):
    text = message.text
    
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'text': text,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored text message before forwarding to group with key {key}")

    await bot.send_message(
        chat_id=GROUP_ID,
        text=f"Текст сообщения:\n{text}"
    )
    
    await message.answer("Текст успешно отправлен!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )




@router.callback_query(F.data == 'plus1')
async def handle_plus1(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Отправьте фото/видео и текст одним сообщением")
    await callback.message.answer("❗❗ПОСТЫ БУДУТ ПРИНИМАТЬСЯ , ТОЛЬКО С КООРДИНАТАМИ/АДРЕСОМ , ОСТАЛЬНОЕ ОТКЛОНИТСЯ❗❗")
    await state.set_state(AuthState.waiting_for_plus1_content)


@router.message(AuthState.waiting_for_plus1_content, F.photo)
async def handle_plus1_photo(message: Message, state: FSMContext, bot: Bot):
    photo = message.photo[-1]
    caption = message.caption or ""
    photo_file = await bot.get_file(photo.file_id)
    photo_bytes = await bot.download_file(photo_file.file_path)
    
    # Store the photo in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'photo': photo,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored photo message before forwarding to group with key {key}")

    # Send to group
    await bot.send_photo(
        chat_id=GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        text="Добавить в незакрашенные граффити?",
        reply_markup=kb.vopros3
    )

@router.message(AuthState.waiting_for_plus1_content, F.video)
async def handle_plus1_video(message: Message, state: FSMContext, bot: Bot):
    video = message.video
    caption = message.caption or ""
    video_file = await bot.get_file(video.file_id)
    video_bytes = await bot.download_file(video_file.file_path)
    
    # Store the video in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored video message before forwarding to group with key {key}")

    # Send to group
    await bot.send_video(
        chat_id=GROUP_ID,
        video=BufferedInputFile(video_bytes.read(), filename="video.mp4"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        text="Добавить в незакрашенные граффити?",
        reply_markup=kb.vopros3
    )

@router.message(AuthState.waiting_for_plus1_content, F.text)
async def handle_plus1_text(message: Message, state: FSMContext, bot: Bot):
    text = message.text
    
    # Store the text in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'text': text,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored text message before forwarding to group with key {key}")

    # Send to group
    await bot.send_message(
        chat_id=GROUP_ID,
        text=f"Текст сообщения:\n{text}"
    )
    
    await message.answer("Текст успешно отправлен!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        text="Добавить в незакрашенные граффити?",
        reply_markup=kb.vopros3
    )





@router.callback_query(F.data == 'plus3')
async def handle_plus3(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Отправьте фото и текст одним сообщением")
    await callback.message.answer("❗❗ГРАФФИТИ БУДУТ ПРИНИМАТЬСЯ , ТОЛЬКО С КООРДИНАТАМИ/АДРЕСОМ , ОСТАЛЬНОЕ ОТКЛОНИТСЯ❗❗")
    await state.set_state(AuthState.waiting_for_plus3_content)

@router.message(AuthState.waiting_for_plus3_content, F.photo)
async def handle_plus3_content(message: Message, state: FSMContext, bot: Bot):
    photo = message.photo[-1]
    caption = message.caption or ""
    photo_file = await bot.get_file(photo.file_id)
    photo_bytes = await bot.download_file(photo_file.file_path)
    

    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'photo': photo,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored photo message before forwarding to group with key {key}")

    
    # Send to group
    await bot.send_photo(
        chat_id=GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Фото и текст успешно отправлены!")
    await state.clear()


    await bot.send_message(
        chat_id=GROUP_ID,
        text="Говорят что закрасили",
        
    )




@router.callback_query(F.data == 'plus2')
async def handle_plus2(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Граффити нет!')
    
    




@router.callback_query(F.data == 'plus222')
async def handle_plus222(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    await callback.message.answer("✅")

    await callback.message.edit_reply_markup(reply_markup=None)

@router.callback_query(F.data == 'plus111')
async def handle_plus222(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    await callback.message.answer("❌")

    await callback.message.edit_reply_markup(reply_markup=None)
