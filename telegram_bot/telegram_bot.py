from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.replykeyboardremove import ReplyKeyboardRemove
import json
import requests

updater = Updater('405494586:AAEV7gYsdcocDBeodO3h4yyos0RfEOkAFRg')

question_query_data = ''

ADMIN = 419849271
START = 'start'
EXIT = 'exit'
HELP = 'help'
CHOSE_CATEGORY = 'chose_category'
CUSTOMER_CATEGORY = 'customer_category'
CUSTOMER_QUESTION = 'customer_question'
PROVIDER_CATEGORY = 'provider_category'
PROVIDER_QUESTION = 'provider_question'
USER_BLOCKED = 'user_blocked'

user_help = 1
provider_contact = 2
customer_contact = 3
start_text = 4
end_text = 5
access = 6
callback_text = 7
access_help = 8
opinion_get_text = 11
ask_get_text = 12

state_home_page = "صفحه اصلی"
state_enter_customer_category = "ورود مشتریان"
state_enter_customer_question = "صفحه سوالات مشتريان"
state_enter_customer_question_answer = "سوال انتخاب شده مشتريان"
state_enter_provider_category = "ورود سرویس‌دهندگان"
state_enter_provider_question = "صفحه سوالات سرويس‌دهندگان"
state_enter_provider_question_answer = "سوال انتخاب شده سرويس‌دهندگان"
state_exit = "📴 خروج"
state_start = "شروع مجدد ربات استادکار"
state_protect = "مسدوديت"
state_help = "❓ آموزش کار با ربات استادکار"
state_back = "بازگشت"
state_activate = "فعال"
state_deactivate = "غیرفعال"
state_new = "جدید"
state_exist = "وجوددارد"
state_notExist = "وجودندارد"
state_chose = "لطفا انتخاب نماييد:"
state_opinion = "انتقادها و پیشنهادها"
state_try_again = "تلاش مجدد"
state_ask = 'از استادکار بپرس'
state_chose_ask_type = 'لطفا دسته مربوط به سوال را انتخاب نمایید:'
state_left = 'انصراف'
state_customer = 'مشتری'
state_provider = 'سرویس‌دهنده'
state_wrong_entered = 'عبارت وارد شده صحیح نمی‌باشد.لطفا عبارت صحیح را وارد نمایید.'
state_customer_ask = 'پرسیدن سوال مشتری'
state_provider_ask = 'پرسیدن سوال‌ سرویس‌دهنده'
state_add_question = '👤افزودن سوال'
state_add_questions = 'افزودن سوالات'
state_users_status = 'وضعیت کاربران'
state_deactivation = 'غیرفعال'
state_account_type_admin = 'ناظر'
state_users_list = 'لیست کاربران'
state_admin_home_page = 'صفحه اصلی ناظر'
state_account_type_normal = 'کاربر عادی'
state_add_customer_question = 'افزودن سوال مشتری'
state_add_provider_question = 'افزودن سوال سرویس‌دهنده'
state_get_customer_question = 'وارد کردن سوال و جواب مشتری'
state_get_provider_question = 'وارد کردن سوال و جواب سرویس‌دهنده'
state_customer_category = 'دسته‌بندی مشتریان'
state_provider_category = 'دسته‌بندی سرویس‌دهنده'
state_customer_question = 'سوالات مشتریان'
state_provider_question = 'سوالات سرویس‌دهنده'
state_add_category = '👤افزودن دسته'
state_sending_general_message = 'ارسال پیام عمومی'
state_sending_unique_message = 'ارسال پیام شخصی'


def set_user_state(user_id, state):
    requests.post('http://127.0.0.1:8000/setUserState/', json={"user_id": user_id, "state": state})


def get_user_state(user_id):
    data = requests.post('http://127.0.0.1:8000/getUserState/', json={"user_id": user_id})
    return data


def get_customer_question_list():
    data = json.loads(requests.get('http://127.0.0.1:8000/customerQuestionList/').text)
    return data


def get_provider_category_list():
    data = json.loads(requests.get('http://127.0.0.1:8000/providerCategoryList/').text)
    return data


def get_provider_question_list():
    data = json.loads(requests.get('http://127.0.0.1:8000/providerQuestionList/').text)
    return data


def get_customer_category_list():
    data = json.loads(requests.get('http://127.0.0.1:8000/customerCategoryList/').text)
    return data


def telegram_text_list(id_get):
    data_get = json.loads(requests.get('http://127.0.0.1:8000/telegramText/').text)
    for data in data_get:
        category_get = data.get('category_get', '')
        text_get = data.get('text_get', '')
        if id_get == category_get:
            return text_get
    return -1


def users_list_view(bot, update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_users_list)
    data_get = json.loads(requests.get('http://127.0.0.1:8000/usersAccount').text)
    list_get = ""
    for data in data_get:
        user_id_get = data.get('user_id', '')
        username_get = data.get('username', '')
        if username_get == '':
            username_get = 'ندارد'
        else:
            username_get = "@" + username_get
        first_name_get = data.get('first_name', '')
        if first_name_get == '':
            first_name_get = 'ندارد'
        last_name_get = data.get('last_name', '')
        if last_name_get == '':
            last_name_get = 'ندارد'
        account_type_get = data.get('account_type', '')
        state_get = data.get('state', '')
        status_get = data.get('status', '')
        list_get_1 = ("کد تلگرام: {0}\nکد کاربری: {1}\nنام: {2}\nنام خانوادگی: {3}\nنوع اکانت: {4}\n"
                      "موقعیت: {5}\nوضعیت: {6}").format(user_id_get, username_get, first_name_get, last_name_get,
                                                        account_type_get, state_get, status_get)
        list_get = list_get + "\n***\n" + list_get_1
    bot.send_message(chat_id, list_get)


def users_status(bot, update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_users_list)
    message = update.message.text
    if message == state_back:
        set_user_state(chat_id, state_admin_home_page)
    else:
        set_user_state(chat_id, state_users_status)
        data_get = json.loads(requests.get('http://127.0.0.1:8000/usersAccount').text)
        all_users = len(data_get)
        activate_users = 0
        deactivate_users = 0
        account_type_normal = 0
        account_type_admin = 0
        for data in data_get:
            account_type_get = data.get('account_type', '')
            status_get = data.get('status', '')
            if status_get == state_activate:
                activate_users = activate_users + 1
            elif status_get == state_deactivation:
                deactivate_users = deactivate_users + 1
            if account_type_get == state_account_type_normal:
                account_type_normal = account_type_normal + 1
            if account_type_get == state_account_type_admin:
                account_type_admin = account_type_admin + 1
        list_show = "👥 وضعیت کاربران:\n\n👤 تعداد کاربران: {0}\n" \
                    "✅ کاربران فعال:{1}\n❌ کاربران غیرفعال:{2}\n\nنوع اکانت:\n👨‍👨‍👧 عادی:{3}\n👨🏻‍💻 ناظر:{4}\n" \
            .format(all_users, activate_users, deactivate_users, account_type_normal, account_type_admin)
        keyboard = [["👥 " + state_users_list], ["👤🗣 " + state_sending_unique_message],
                    ["👥🗣 " + state_sending_general_message], [state_back]]
        bot.send_message(chat_id, list_show, reply_markup=ReplyKeyboardMarkup(keyboard))


def customer_category_change_name_id(message):
    data_get = get_customer_category_list()
    for data in data_get:
        id_get = data.get('id', '')
        name_get = data.get('category_name', '')
        if name_get == message:
            return id_get
    return -1


def customer_category_change_id_name(message):
    data_get = get_customer_category_list()
    for data in data_get:
        id_get = data.get('id', '')
        name_get = data.get('category_name', '')
        if id_get == message:
            return name_get
    return -1


def provider_category_change_name_id(message):
    data_get = get_provider_category_list()
    for data in data_get:
        id_get = data.get('id', '')
        name_get = data.get('category_name', '')
        if name_get == message:
            return id_get
    return -1


def provider_category_change_id_name(message):
    data_get = get_provider_category_list()
    for data in data_get:
        id_get = data.get('id', '')
        name_get = data.get('category_name', '')
        if id_get == message:
            return name_get
    return -1


def customer_question_answer(bot, update, message):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_enter_customer_question_answer)
    if message == state_back:
        set_user_state(chat_id, state_enter_customer_question)
    else:
        data_get = json.loads(requests.get('http://127.0.0.1:8000/customerQuestionList').text)
        for data in data_get:
            question_name_get = data.get('question_name')
            if message == question_name_get:
                bot.send_message(chat_id, data.get('question_answer', ''))


def provider_question_answer(bot, update, message):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_enter_provider_question_answer)
    if message == state_back:
        set_user_state(chat_id, state_enter_provider_question)
    else:
        data_get = json.loads(requests.get('http://127.0.0.1:8000/providerQuestionList').text)
        for data in data_get:
            question_name_get = data.get('question_name')
            if message == question_name_get:
                bot.send_message(chat_id, data.get('question_answer', ''))


def customer_question(bot, update, category_name_set):
    chat_id = update.message.chat_id
    message = update.message.text
    if message == state_back:
        set_user_state(chat_id, state_home_page)
    else:
        set_user_state(chat_id, state_enter_customer_question)
        data_get = json.loads(requests.get('http://127.0.0.1:8000/customerQuestionList').text)
        keyboard = []
        for data in data_get:
            category_name_get = data.get('category_name', '')
            if category_name_get == category_name_set:
                question_name_get = data.get('question_name', '')
                keyboard.append([question_name_get])
        keyboard.append([state_back])
        bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))


def provider_question(bot, update, category_name_set):
    chat_id = update.message.chat_id
    message = update.message.text
    if message == state_back:
        set_user_state(chat_id, state_home_page)
    else:
        set_user_state(chat_id, state_enter_provider_question)
        data_get = json.loads(requests.get('http://127.0.0.1:8000/providerQuestionList').text)
        keyboard = []
        for data in data_get:
            category_name_get = data.get('category_name', '')
            if category_name_get == category_name_set:
                question_name_get = data.get('question_name', '')
                keyboard.append([question_name_get])
        keyboard.append([state_back])
        bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))


def customer_category(bot, update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_enter_customer_category)
    data_get = json.loads(requests.get('http://127.0.0.1:8000/customerCategoryList').text)
    keyboard = []
    for data in data_get:
        category_name_get = data.get('category_name', '')
        keyboard.append([category_name_get])
    keyboard.append([state_back])
    bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))


def provider_category(bot, update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_enter_provider_category)
    data_get = json.loads(requests.get('http://127.0.0.1:8000/providerCategoryList').text)
    keyboard = []
    for data in data_get:
        category_name_get = data.get('category_name', '')
        keyboard.append([category_name_get])
    keyboard.append([state_back])
    bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))


def set_user_opinion(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text
    if message != state_left:
        username_get = update.message.chat.username
        first_name_get = update.message.chat.first_name
        last_name_get = update.message.chat.last_name
        bot.send_message(chat_id, "با سپاس نظر شما ثبت شد و در کوتاه‌ترین زمان رسیدگی می‌گردد.",
                         reply_markup=ReplyKeyboardRemove())
        requests.post('http://127.0.0.1:8000/userOpinion/',
                      json={"user_opinion_id": chat_id, "user_opinion_text": message, "username": username_get,
                            "first_name": first_name_get, "last_name": last_name_get})
        set_user_state(chat_id, state_home_page)
        send_start_menu(bot, update)


def set_user_ask(bot, update, ask_category):
    message = update.message.text
    chat_id = update.message.chat_id
    if message != state_left:
        username_get = update.message.chat.username
        first_name_get = update.message.chat.first_name
        last_name_get = update.message.chat.last_name
        bot.forward_message(chat_id=ADMIN, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        requests.post('http://127.0.0.1:8000/userAsk/',
                      json={"user_id": chat_id, "ask_text": message, "username": username_get,
                            "first_name": first_name_get, "last_name": last_name_get, "ask_category": ask_category})
        bot.send_message(chat_id, "با سپاس سوال شما ثبت شد و در سریع‌ترین زمان پاسخگوی شما هستیم.")
        set_user_state(chat_id, state_home_page)
        send_start_menu(bot, update)
    else:
        set_user_state(chat_id, state_home_page)


def admin_add_question(bot, update):
    message = update.message.text
    chat_id = update.message.chat_id
    if message == state_add_question:
        set_user_state(chat_id, state_add_question)
        get_admin_question(bot, update)
    else:
        bot.send_message(chat_id, "pass")


def get_admin_question(bot, update):
    chat_id = update.message.chat_id
    keyboard = [
        [state_customer_question, state_provider_question],
        [state_add_question],
        [state_customer_category, state_provider_category], [state_add_category], [state_back]
    ]
    bot.send_message(chat_id, text=state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))


def sending_unique_message(update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_sending_unique_message)


def sending_general_message(update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_sending_general_message)


def button(bot, update):
    global question_query_data
    query = update.callback_query
    chat_id = query.message.chat_id
    keyboard = []
    state = get_user_state(chat_id).json()['state']
    if state == state_add_customer_question:
        question_query_data = "{0}_{1}".format(question_query_data, query.data)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              text="مرحله 3:\n وارد کردن سوال و جواب برای '{0}': \nفرمت ارسالی بصورت زیر می باشد."
                                   "\nسوال\nجواب\nاولویت نمایش در لیست".format(query.data),
                              message_id=query.message.message_id, reply_markup=InlineKeyboardMarkup(keyboard))
        set_user_state(chat_id, state_get_customer_question)
    if state == state_add_provider_question:
        question_query_data = "{0}_{1}".format(question_query_data, query.data)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              text="مرحله 3:\n وارد کردن سوال و جواب برای '{0}': \nفرمت ارسالی بصورت زیر می باشد."
                                   "\nسوال\nجواب\nاولویت نمایش در لیست".format(query.data),
                              message_id=query.message.message_id, reply_markup=InlineKeyboardMarkup(keyboard))
        set_user_state(chat_id, state_get_provider_question)
    if query.data == state_back:
        if state == state_add_customer_question or state == state_add_provider_question:
            get_admin_question(bot, update)
    if query.data == state_customer:
        question_query_data = query.data
        data_get = get_customer_category_list()
        for data in data_get:
            name_get = data.get('category_name', '')
            keyboard.append([InlineKeyboardButton(str(name_get), callback_data=str(name_get))])
        bot.edit_message_text(chat_id=query.message.chat_id, text="مرحله 2:\n دسته سوال خود را مطرح نمایید:",
                              message_id=query.message.message_id, reply_markup=InlineKeyboardMarkup(keyboard))
        set_user_state(chat_id, state_add_customer_question)
    elif query.data == state_provider:
        data_get = get_provider_category_list()
        for data in data_get:
            name_get = data.get('category_name', '')
            keyboard.append([InlineKeyboardButton(str(name_get), callback_data=str(name_get))])
        bot.edit_message_text(chat_id=query.message.chat_id, text="مرحله 2:\n دسته سوال خود را مطرح نمایید:",
                              message_id=query.message.message_id, reply_markup=InlineKeyboardMarkup(keyboard))
        set_user_state(chat_id, state_add_provider_question)


def home_page_view(bot, update):
    message = update.message.text
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_home_page)
    if message == state_enter_customer_category:
        set_user_state(chat_id, state_enter_customer_category)
        data_get = get_customer_category_list()
        keyboard = []
        for data in data_get:
            category_name_get = data.get('category_name', '')
            keyboard.append([category_name_get])
        keyboard.append([state_back])
        bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))
    elif message == state_enter_provider_category:
        set_user_state(chat_id, state_enter_provider_category)
        data_get = get_provider_category_list()
        keyboard = []
        for data in data_get:
            category_name_get = data.get('category_name', '')
            keyboard.append([category_name_get])
        keyboard.append([state_back])
        bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))
    elif message == state_help:
        set_user_state(chat_id, state_help)
    elif message == state_exit:
        set_user_state(chat_id, state_exit)


def user_information(update):
    chat_id = update.message.chat_id
    user_id_get = update['message']['chat']['id']
    username_get = update['message']['chat']['username']
    first_name_get = update['message']['chat']['first_name']
    last_name_get = update['message']['chat']['last_name']
    param = requests.post('http://127.0.0.1:8000/setUserID/',
                          json={"user_id": user_id_get, "username": username_get, "first_name": first_name_get,
                                "last_name": last_name_get})
    if param.json()['user'] == state_exist and param.json()['status'] == state_deactivate:  # user: deactivate.
        set_user_state(chat_id, state_protect)
        return 1
    elif param.json()['user'] == state_exist and param.json()['status'] == state_activate:  # user: activate and is old.
        set_user_state(chat_id, state_home_page)
        return 2
    elif param.json()['user'] == state_new:  # user: activate and is new.
        set_user_state(chat_id, state_home_page)
        return 3
    return -1


def send_start_menu(bot, update):
    chat_id = update.message.chat_id
    data_get = json.loads(requests.get('http://127.0.0.1:8000/startMenu/').text)
    keyboard = ([" 👨🏻‍🔧 " + data_get[0].get('menu_name'), " 👨🏻‍💼 " + data_get[1].get('menu_name')],
                [" 🙋🏻‍♂️" + data_get[2].get('menu_name'), " 💁🏻‍♂️" + data_get[3].get('menu_name')],
                [" ❓ " + data_get[4].get('menu_name')],
                [" 📴 " + data_get[5].get('menu_name')])
    bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))


def login(bot, update):
    chat_id = update.message.chat_id
    param = user_information(update)
    message = update.message.text
    account_type = get_user_state(chat_id).json()['account_type']
    if message == state_back and account_type == state_account_type_normal:
        send_start_menu(bot, update)
    else:
        if param == 1:  # user:  deactivate.
            keyboard = [[state_try_again], [state_exit]]
            bot.send_message(chat_id, telegram_text_list(access), reply_markup=ReplyKeyboardMarkup(keyboard))
        elif param == 2:  # user: activate and is old.
            if account_type == state_account_type_admin:
                set_user_state(chat_id, state_admin_home_page)
                keyboard = [["👥 " + state_users_status, "✍ " + state_add_questions],
                            ["🙋🏻‍♂️" + state_opinion, "🔕 " + state_deactivation]]
                bot.send_message(chat_id, state_chose, reply_markup=ReplyKeyboardMarkup(keyboard))
            else:
                bot.send_message(chat_id, telegram_text_list(callback_text))
                send_start_menu(bot, update)
        elif param == 3:  # user:  activate and is new.
            text_get = telegram_text_list(start_text)
            bot.send_message(chat_id, text_get)
            send_start_menu(bot, update)


def admin_user_message_handler(bot, update, chat_id, message, state):
    if message == state_customer_question:
        data_get = get_customer_question_list()
        for data in data_get:
            category_name_get = customer_category_change_id_name(int(data.get('category_name', '')))
            question_name_get = data.get('question_name', '')
            question_answer_get = data.get('question_answer', '')
            question_priority_get = data.get('question_priority', '')
            list_get = "عنوان سوال: {0}\n متن سوال: {1}\n جواب سوال: {2}\n اولویت قرارگیری: {3}". \
                format(category_name_get, question_name_get, question_answer_get, question_priority_get)
            bot.send_message(chat_id, list_get)
    if message == state_provider_question:
        data_get = get_provider_question_list()
        for data in data_get:
            category_name_get = provider_category_change_id_name(int(data.get('category_name', '')))
            question_name_get = data.get('question_name', '')
            question_answer_get = data.get('question_answer', '')
            question_priority_get = data.get('question_priority', '')
            list_get = "عنوان سوال: {0}\n متن سوال: {1}\n جواب سوال:{2}\n اولویت قرارگیری: {3}". \
                format(category_name_get, question_name_get, question_answer_get, question_priority_get)
            bot.send_message(chat_id, list_get)
    if message == "✍ " + state_add_questions:
        get_admin_question(bot, update)
    if message == state_add_question:
        keyboard_2 = [
            [InlineKeyboardButton(state_customer, callback_data=state_customer)],
            [InlineKeyboardButton(state_provider, callback_data=state_provider)],
        ]
        bot.send_message(chat_id, "مرحله 1:\n دسته سوال را مشخص نمایید:", reply_markup=InlineKeyboardMarkup(keyboard_2))
    if message == state_customer_category:
        data_get = get_customer_category_list()
        for data in data_get:
            bot.send_message(chat_id, data)
    if message == state_provider_category:
        data_get = get_provider_category_list()
        for data in data_get:
            bot.send_message(chat_id, data)
    if message == "🙋🏻‍♂️" + state_opinion:
        set_user_state(chat_id, state_opinion)
    if message == "👥 " + state_users_status:
        users_status(bot, update)
    if message == "👤🗣 " + state_sending_unique_message:
        keyboard = [[state_left]]
        bot.send_message(chat_id, "لطفا کد تلگرام و متن را به فرمت زیر وارد نمایید:\nکد تلگرام\nمتن ارسالی",
                         reply_markup=ReplyKeyboardMarkup(keyboard))
        sending_unique_message(update)
    if message == "👥🗣 " + state_sending_general_message:
        keyboard = [[state_left]]
        bot.send_message(chat_id, "لطفاً متن عمومی مورد نظر را وارد نمایید:",
                         reply_markup=ReplyKeyboardMarkup(keyboard))
        sending_general_message(update)
    if message == "🔕 " + state_deactivation:
        set_user_state(chat_id, state_exit)
        keyboard = [["📳 " + state_start]]
        bot.send_message(chat_id, telegram_text_list(end_text), reply_markup=ReplyKeyboardMarkup(keyboard))
    if message == state_back or message == state_left:
        if state == state_sending_unique_message or state == state_sending_general_message:
            users_status(bot, update)
        else:
            set_user_state(chat_id, state_admin_home_page)
            login(bot, update)
    if message == "👥 " + state_users_list and state == state_users_status:
        users_list_view(bot, update)
    if state == state_sending_unique_message:
        if message != state_left:
            chat_id_get, text_get = message.split("\n")
            data_get = json.loads(requests.get('http://127.0.0.1:8000/usersAccount/').text)
            i = 0
            for data in data_get:
                user_id_get = data.get('user_id', '')
                if user_id_get == chat_id_get:
                    bot.send_message(chat_id_get, text_get)
                    i = 1
            if i == 0:
                bot.send_message(chat_id, "کاربر مورد نظر پیدا نشد.")
            elif i == 1:
                bot.send_message(chat_id, "متن مورد نظر برای کاربر ارسال شد.")
    if state == state_sending_general_message:
        if message != state_left:
            i = 0
            data_get = json.loads(requests.get('http://127.0.0.1:8000/usersAccount/').text)
            for data in data_get:
                user_id_get = data.get('user_id', '')
                try:
                    i = i + 1
                    bot.send_message(user_id_get, message)
                except ValueError:
                    print("1")
            bot.send_message(chat_id, "پیام عمومی برای {0} نفر ارسال شد.".format(i), reply_markup=ReplyKeyboardRemove())
    if state == state_opinion:
        bot.send_message(chat_id, "ورود به انتقادها و پیشنهادها")
    if state == state_get_customer_question or state == state_get_provider_question:
        data_1, data_2 = question_query_data.split("_")
        data_3, data_4, data_5 = message.split("\n")
        if state == state_get_customer_question:
            data_2_id = customer_category_change_name_id(data_2)
        else:
            data_2_id = provider_category_change_name_id(data_2)
        requests.post('http://127.0.0.1:8000/addQuestionAdmin/',
                      json={"question_type": data_1, "category_name": data_2_id, "question_name": data_3,
                            "question_answer": data_4, "question_priority": data_5})
        bot.send_message(chat_id, "اطلاعات '{0}' ذخیره شد.".format(data_2))
        set_user_state(chat_id, state_admin_home_page)
        login(bot, update)


def normal_user_message_handler(bot, update, chat_id, message, state, status):
    if message == "💁🏻‍♂️" + state_ask and state != state_ask:
        keyboard = [["👨🏻‍💼 " + state_customer, "👨🏻‍🔧 " + state_provider], [state_left]]
        bot.send_message(chat_id, state_chose_ask_type, reply_markup=ReplyKeyboardMarkup(keyboard))
        set_user_state(chat_id, state_ask)
    if message == "🙋🏻‍♂️" + state_opinion and state != state_opinion:
        keyboard = [[state_left]]
        bot.send_message(chat_id, telegram_text_list(opinion_get_text),
                         reply_markup=ReplyKeyboardMarkup(keyboard))
        set_user_state(chat_id, state_opinion)
    if message == state_help:
        help_bot(bot, update)
    if message == state_exit:
        exit_bot(bot, update)
    if message == state_back or message == state_left and state != state_home_page:
        if state == state_enter_customer_category or state == state_enter_provider_category:
            login(bot, update)
        elif state == state_enter_customer_question or state == state_enter_customer_question_answer:
            customer_category(bot, update)
        elif state == state_enter_provider_question or state == state_enter_provider_question_answer:
            provider_category(bot, update)
        elif state == state_customer_ask or state == state_provider_ask:
            set_user_state(chat_id, state_home_page)
            send_start_menu(bot, update)
        elif state == state_opinion or state == state_ask:
            set_user_state(chat_id, state_home_page)
            send_start_menu(bot, update)
    if status == state_deactivate:
        login(bot, update)
    if status == state_activate:
        if state == state_home_page:
            if message == "👨🏻‍💼 " + state_enter_customer_category:
                customer_category(bot, update)
            elif message == "👨🏻‍🔧 " + state_enter_provider_category:
                provider_category(bot, update)
        elif state == state_opinion:
            set_user_opinion(bot, update)
        elif state == state_enter_customer_category:
            customer_question(bot, update, customer_category_change_name_id(message))
        elif state == state_enter_provider_category:
            provider_question(bot, update, provider_category_change_name_id(message))
        elif state == state_enter_customer_question:
            customer_question_answer(bot, update, message)
        elif state == state_enter_provider_question:
            provider_question_answer(bot, update, message)
        elif state == state_ask:
            if message == "👨🏻‍💼 " + state_customer:
                keyboard = [[state_left]]
                set_user_state(chat_id, state_customer_ask)
                bot.send_message(chat_id, telegram_text_list(ask_get_text),
                                 reply_markup=ReplyKeyboardMarkup(keyboard))
            elif message == "👨🏻‍🔧 " + state_provider:
                keyboard = [[state_left]]
                set_user_state(chat_id, state_provider_ask)
                bot.send_message(chat_id, telegram_text_list(ask_get_text),
                                 reply_markup=ReplyKeyboardMarkup(keyboard))
        elif state == state_customer_ask:
            set_user_ask(bot, update, state_customer)
        elif state == state_provider_ask:
            set_user_ask(bot, update, state_provider)
        else:
            bot.send_message(chat_id, state_wrong_entered)


def message_handler(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text
    if message == "📳 " + state_start or message == "🔕 " + state_deactivation:
        login(bot, update)
    account_type = get_user_state(chat_id).json()['account_type']
    state = get_user_state(chat_id).json()['state']
    status = get_user_state(chat_id).json()['status']
    if account_type == state_account_type_admin:
        admin_user_message_handler(bot, update, chat_id, message, state)
    elif account_type == state_account_type_normal:
        normal_user_message_handler(bot, update, chat_id, message, state, status)


def start(bot, update):
    login(bot, update)


def exit_bot(bot, update):
    chat_id = update.message.chat_id
    set_user_state(chat_id, state_exit)
    keyboard = [["📳 " + state_start]]
    bot.send_message(update.message.chat_id, telegram_text_list(end_text), reply_markup=ReplyKeyboardMarkup(keyboard))


def help_bot(bot, update):
    message = update.message.text
    chat_id = update.message.chat_id
    status = get_user_state(chat_id).json()['status']
    if message == state_back or status == state_deactivate:
        text_get = telegram_text_list(access_help)
        set_user_state(chat_id, state_protect)
    else:
        text_get = telegram_text_list(user_help)
    set_user_state(chat_id, state_home_page)
    bot.send_message(update.message.chat_id, text_get)


def main():
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help_bot))
    updater.dispatcher.add_handler(CommandHandler('exit', exit_bot))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], message_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()


if __name__ == '__main__':
    main()
