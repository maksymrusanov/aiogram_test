from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
# импортировали этот модуль
import app.keyboards as kb
# роутер чтобы не было ошибок при рутинге(меняем все dp на router)
router = Router()


@router.message(CommandStart())
# обработка команды старт
async def cmd_start(message: Message):
    await message.answer('hello', reply_markup=kb.main)

# вывод созданных reply-кнопок из функции
# test_list = ['q', 'w', 'e']
# async def test_inline_buttons():
#     keyboard = ReplyKeyboardBuilder()
#     for i in test_list
#     keyboard.add(KeyboardButton(text=i))
#     return keyboard.adjust(2).as_markup()


@router.message(Command('test_inline'))
async def test_inline(message: Message):
    await message.reply('here is example of inline buttons', reply_markup=await kb.test_inline_buttons())


@router.message(Command('test_reply'))
async def test_inline(message: Message):
    await message.reply('here is example of reply buttons', reply_markup=await kb.test_reply_buttons())


@router.message(Command('inline'))
# создали вывод inline-кнопок
async def show_inline_buttons(message: Message):
    await message.answer('hello with inline buttons', reply_markup=kb.inline_buttons)


@router.message(Command('id'))
# возврат id по запросу /id с методом reply(ответит на сообщение)
async def cmd_start(message: Message):
    await message.reply(f'your ID is: {message.from_user.id}')


@router.message(Command('help'))
# обработка команды help,ответ будет просто сообщением
async def get_help(message: Message):
    await message.answer('this is /help command')


@router.message(F.text == 'good?')
# F-magic filter(пока что хз что это)
# сравниваем текст пользователя для отлова сообщения,если есть-выводит ответ
async def how_r_u(message: Message):
    await message.answer('all good?')


@router.message(F.photo)
async def get_photo(message: Message):
    # отлов картинки и ответ с id этой картинки([-1]это указание качества)
    await message.answer(f'id of picture:{message.photo[-1].file_id}')


@router.message(Command('photo'))
# пример запроса: /photo
# возврат картинки по id(таким образом можно отправлять картинки без скачивания)
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMUaII8hvciNOkT3bxQIEpBvY9P7N0AAuP1MRv1GxFIWr3hsAdiVw8BAAMCAAN5AAM2BA', caption='this is black picture')


@router.message(Command('photo_1'))
# пример запроса: /photo_1
# возврат картинки по ссылке(таким образом можно отправлять картинки без скачивания)
async def get_photo(message: Message):
    await message.answer_photo(photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.n-_WWS8nyodVAXv4HiKxagHaEW%3Fpid%3DApi&f=1&ipt=45f62af95bb5c38aa69246a4697db38f92008b0091683c120584fcdc9aa4ec56&ipo=images',
                               caption='this is another picture')

# сделали логику что при нажатии на кнопку появляются другие кнопки(как будто подкнопки,хз)


@router.callback_query(F.data == 'q')
async def q(callback: CallbackQuery):
    await callback.message.answer('you pressed q button')
    await callback.message.edit_text('pick up', reply_markup=await kb.test_inline_buttons())


@router.callback_query(F.data == 'w')
async def q(callback: CallbackQuery):
    await callback.message.answer('you pressed w button')


@router.callback_query(F.data == 'e')
async def q(callback: CallbackQuery):
    await callback.message.answer('you pressed e button')


@router.message(Command('callback'))
# функция обработки callback-функции
# call_back = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='q', callback_data='q')],
#     [InlineKeyboardButton(text='w', callback_data='w')],
#     [InlineKeyboardButton(text='e', callback_data='e')],
# ])
async def show_callback(message: Message):
    await message.answer('this is callback func', reply_markup=kb.call_back)
