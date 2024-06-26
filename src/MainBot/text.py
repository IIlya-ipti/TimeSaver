greet1 = """
Привет, {name}! 
Бывают случаи, когда дорогие тебе люди пишут, а ты не можешь ответить, либо просто не видел сообщение. Мы не хотим, чтобы они волновались и расстраивались, поэтому я помогу тебе и отвечу за тебя! 
"""
greet2 = """
Чтобы я мог помочь тебе, нажми на кнопку ниже.
"""

menu = "Выбрать действие"

reg_text = """
Отлично, начнем! 
Тебе необходимо ввести через запятую api_id, api_hash.
Инструкцию, как получить их, можешь посмотреть здесь:
https://core.telegram.org/api/obtaining_api_id
"""
aut_text = """
Продолжим, сейчас введи через запятую свой номер телефона и пароль от телеграмма.
"""
code_text = """
Тебе от официального аккаунта Telegram должен был прийти код. Чтобы закончить регистрацию, введи его, ставя после каждой цифры '_'. 
Пример ввода: 1_1_1_1_1
"""
reg_text_correct = """
Ты большой молодец!
Осталось лишь добавить дорогих тебе людей через меню.
Вызови меню, нажав на кнопку. 
"""

error_text = """
Что-то пошло не так, попробуй еще раз!
"""

add_con_text = """
Чтобы добавить человека в важных, введите его tg_id. 
"""
add_con_text_correct = """
Успешно!
Теперь {name} не будет лишний раз волноваться.
"""

add_reg_text = """
Чтобы добавить регулярное сообщение, через запятую введите tg_id человека, само сообщение, начальную дату и период между сообщениями в секундах.
Дата вводится в формате: день/месяц/год час:минута:секунда.
Пример ответа боту: @tg_id, сообщение, 03/02/00 14:48:00, 10"""
add_reg_text_correct = """
Успешно!
Теперь {name} будет получать регулярные сообщения. 
"""

del_text = """
Чтобы убрать человека из важных, введите его tg_id.
"""
del_text_correct = """
Успешно!
Теперь {name} больше не важен тебе. 
"""
