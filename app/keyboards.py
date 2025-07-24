# создаём файл взаимодействия с клавой
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# создали кнопки(2 ряда,в первом одна кнопка,во втором-2)
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='button1')],
    # это один ряд
    [KeyboardButton(text='button2'), KeyboardButton(text='button3')]],
    resize_keyboard=True,
    input_field_placeholder='choose option')
