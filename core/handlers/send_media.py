from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(path='media\SENS_-_Blue_Flower_(muzofond.website).mp3', filename='track.mp3')
    await bot.send_audio(message.chat.id, audio=audio)


async def get_document(message: Message, bot: Bot):
    document = FSInputFile(path='media\document.txt')
    await bot.send_document(message.chat.id, document=document, caption='Это документ')


async def get_media_group(message: Message, bot: Bot):
    photo_mg = InputMediaPhoto(
        type='photo', 
        media=FSInputFile('media\kartinki24_horses_0006-1.jpg'),
        caption='Это медиагруппа'
    )
    video_mg = InputMediaVideo(
        type='video',
        media=FSInputFile('media\Ботостроение Telegram. Отправка медиафайлов. Aiogram3 - полное руководство.mp4')
    )
    media = [photo_mg, video_mg]
    await bot.send_media_group(message.chat.id, media=media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(path='media\kartinki24_horses_0006-1.jpg')
    await bot.send_photo(message.chat.id, photo=photo, caption='Это фото')


async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile(path='media\pngwing.png')
    await bot.send_sticker(message.chat.id, sticker=sticker)


async def get_video(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=bot):
        video = FSInputFile(path='media\Ботостроение Telegram. Отправка медиафайлов. Aiogram3 - полное руководство.mp4')
        await bot.send_video(message.chat.id, video=video)


async def get_video_note(message: Message, bot: Bot): # Видео должно быть квадратным
    async with ChatActionSender.upload_video_note(chat_id=message.chat.id, bot=bot):
        video_note = FSInputFile(path='media\Ботостроение Telegram. Отправка медиафайлов. Aiogram3 - полное руководство.mp4')
        await bot.send_video(message.chat.id, video_note)


async def get_voice(message: Message, bot: Bot):
    async with ChatActionSender.record_voice(chat_id=message.chat.id, bot=bot):
        voice = FSInputFile('media\SENS_-_Blue_Flower_(muzofond.website).mp3')
        await bot.send_voice(message.chat.id, voice)