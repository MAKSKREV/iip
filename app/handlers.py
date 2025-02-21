from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram import Bot, Dispatcher, types


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import app.keyboards as kb

from aiogram.types import BufferedInputFile
from config import GROUP_ID,KAT2_GROUP_ID,KAT3_GROUP_ID

from datetime import datetime


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


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    print(f'ID:{message.from_user.id} Имя:{message.from_user.first_name}')
    await message.answer(f'Привет {message.from_user.first_name}')
    await message.answer('Выбери один из пунктов:', reply_markup=kb.vibor)

@router.callback_query(F.data.startswith('kat'))
async def handle_category_selection(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    await callback.answer()
    await state.update_data(selected_category=category)
    
    if category == 'kat0':
        await callback.message.answer('Выберите вариант:', reply_markup=kb.vopros1)
    elif category == 'kat1':
        await callback.message.answer('Отправьте текст с фото')
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
    from config import KAT3_GROUP_ID
    await bot.send_photo(
        chat_id=KAT3_GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Ваше сообщение успешно отправлено!")
    await state.clear()

@router.message(AuthState.waiting_for_kat1_content, F.text)
async def handle_kat1_text(message: Message, state: FSMContext, bot: Bot):
    from config import KAT3_GROUP_ID
    text = message.text
    await bot.send_message(
        chat_id=KAT3_GROUP_ID,
        text=f"Сообщение из предложки:{text}"
    )
    
    await message.answer("Ваше сообщение успешно отправлено!")
    await state.clear()


@router.callback_query(F.data == 'plus1')
async def handle_plus1(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Отправьте фото/видео и текст одним сообщением")
    await callback.message.answer("❗❗ПОСТЫ БУДУТ ПРИНИМАТЬСЯ , ТОЛЬКО С КООРДИНАТАМИ/АДРЕСОМ , ОСТАЛЬНОЕ ОТКЛОНИТЬСЯ❗❗")
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
    await callback.message.answer("❗❗ГРАФФИТИ БУДУТ ПРИНИМАТЬСЯ , ТОЛЬКО С КООРДИНАТАМИ/АДРЕСОМ , ОСТАЛЬНОЕ ОТКЛОНИТЬСЯ❗❗")
    await state.set_state(AuthState.waiting_for_plus3_content)

@router.message(AuthState.waiting_for_plus3_content, F.photo)
async def handle_plus3_content(message: Message, state: FSMContext, bot: Bot):
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
    
    await message.answer("Фото и текст успешно отправлены!")
    await state.clear()


    await bot.send_message(
        chat_id=GROUP_ID,
        text="Говорят что закрасили",
        
    )






@router.message(AuthState.waiting_for_kat2_content)
async def handle_kat2_content(message: Message, state: FSMContext, bot: Bot):
    text = message.text
    await bot.send_message(
        chat_id=KAT2_GROUP_ID,
        text=f"Запрос на разбан:\n{text}"
    )
    await message.answer("Ваш запрос успешно отправлен!")
    await state.clear()


@router.callback_query(F.data == 'plus2')
async def handle_plus2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Щёлковское шоссе, 85к1, подъезд 5 или 6')
    with open("app/foto/uu.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('4-ая парковая,дом 25')
    with open("app/foto/yy.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
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
    await callback.message.answer('Щелковское шоссе 47, Щелковское шоссе 45а. Подземный переход')
    with open("app/foto/vid.mp4", "rb") as file:
        video = BufferedInputFile(file.read(), filename="vid.mp4")
        await callback.message.answer_video(video)
    




@router.callback_query(F.data == 'plus222')
async def handle_plus222(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    # Send checkmark emoji
    await callback.message.answer("✅")

    await callback.message.edit_reply_markup(reply_markup=None)

@router.callback_query(F.data == 'plus111')
async def handle_plus222(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    # Send checkmark emoji
    await callback.message.answer("❌")

    await callback.message.edit_reply_markup(reply_markup=None)
