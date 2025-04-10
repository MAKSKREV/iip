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

from aiogram import Router, types


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
    if message.from_user.id in [5176998143]:
        await message.answer('Привет админ')
        await message.answer('Выбери один из пунктов:', reply_markup=kb.modex)
    else:
        await message.answer(f'Привет {message.from_user.first_name}')
        await message.answer('Выбери один из пунктов:', reply_markup=kb.vibor)


@router.callback_query(F.data.startswith('modex'))
async def handle_category_selection(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    await callback.answer()
    await state.update_data(selected_category=category)
    
    if category == 'modex1':
        # Создаём InlineKeyboard с кнопкой, которая содержит URL
        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton("Открыть приложение", url="https://makskrev-iip-appapp-fgwefy.streamlit.app/")
        )
        await callback.message.answer('Запускаю приложение', reply_markup=keyboard)
    elif category == 'modex2':
        await callback.message.answer('Вывожу подарки')
    


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
    await callback.message.answer('9-ая парковая д52 корпус 1, возле 3 подьезда')
    with open("app/foto/ii.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('9-ая парковая дом 52 корпус 1, между 1 и 2 подьездами')
    with open("app/foto/pp.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('11-ая Парковая улица, дом 36 строение 3')
    with open("app/foto/bb.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
        await callback.message.answer('6я парковая 29А')
    with open("app/foto/ff.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Сиреневый бульвар, 23А. около входа в озон')
    with open("app/foto/fff.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('На перекрестке, на стороне возле дома 9-парковая 49к2')
    with open("app/foto/ppp.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    
    await callback.message.answer('5 парковая 64')
    with open("app/foto/bbuuu.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('3-я парковая улица. дом 39. корпус 1')
    with open("app/foto/yxx.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Щелковский шоссе 81')
    with open("app/foto/axx.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Измайловский проспект, 49')
    with open("app/foto/exx.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Щелковское шоссе 69 , Пятерочка')
    with open("app/foto/xexe.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('9 парковка улица 57(2) , за домом')
    with open("app/foto/xaxa.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Сиреневый бульвар дом 40 корпус 1')
    with open("app/foto/xsxs.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)

    await callback.message.answer('5-я Парковая улица, 57, обе автобусные остановки')
    await callback.message.answer('Видео или фото граффити выше нет')

    await callback.message.answer('Щелковское шоссе 47, Щелковское шоссе 45а. Подземный переход')
    with open("app/foto/vid.mp4", "rb") as file:
        video = BufferedInputFile(file.read(), filename="vid.mp4")
        await callback.message.answer_video(video)
    
    




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
