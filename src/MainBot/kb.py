from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu_greet = [
    [InlineKeyboardButton(text="📝 Предоставить доступ к аккаунту", callback_data="registration")]
]

menu_main = [
    [InlineKeyboardButton(text="📝 Добавить человека в важных", callback_data="add_contact")],
    [InlineKeyboardButton(text="🖼 Удалить человека из важных", callback_data="delete_contact")],
    [InlineKeyboardButton(text="💳 Добавить сообщение по расписанию", callback_data="add_regular_massage")],
]

menu_greet = InlineKeyboardMarkup(inline_keyboard=menu_greet)
menu_main = InlineKeyboardMarkup(inline_keyboard=menu_main)
exit_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню"),
     KeyboardButton(text="Начать работу")]
], resize_keyboard=True)
