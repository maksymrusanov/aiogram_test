# создаём файл взаимодействия с клавой
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# создали reply-кнопки(2 ряда,в первом одна кнопка,во втором-2)
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='button1')],
    # это две кнопки в один ряд
    [KeyboardButton(text='button2'), KeyboardButton(text='button3')]],
    # изменили размер кнопок
    resize_keyboard=True,
    # добавили как бы строку-подсказку
    input_field_placeholder='choose option')

# inline-кнопки
inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='youtube', url='www.youtube.com')],
    [InlineKeyboardButton(text='twitch', url='www.twitch.com'),
     InlineKeyboardButton(text='inst', url='www.instagrm.com')]
])
