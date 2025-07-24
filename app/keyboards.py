# создаём файл взаимодействия с клавой
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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


test_list = ['q', 'w', 'e']


async def test_reply_buttons():
    # создали функцию которая последовательно выведет елементы из списка в виде reply-кнопок
    # adjust(2)-количество кнопок в строке
    keyboard = ReplyKeyboardBuilder()
    for i in test_list:
        keyboard.add(KeyboardButton(text=i))
    return keyboard.adjust(2).as_markup()


async def test_inline_buttons():
    # создали функцию которая последовательно выведет елементы из списка в виде inline-кнопок
    # в inline помимо текст должно быть ещё что-то,как например здесь url
    keyboard = InlineKeyboardBuilder()
    for i in test_list:
        keyboard.add(InlineKeyboardButton(text=i, url='www.google.com'))
    return keyboard.adjust(2).as_markup()
