# from django.http import request
#
# def notify(email_to):
#     email_send(email_to)
#     telegram_notify(email_to)
#
#
# def email_send(email_to):
#     pass
#
#
# def telegram_notify(email_to):
#     Telegram()
#     Telegram.notify()
#
#
# class Telegram:
#     def notefy(self, msg):
#         telegram_url = 'https://api.telegram.org/bot<Token>'
#         params = {'chat_id': 'hello', 'text': msg}
#         response = request.post(telegram_url + 'sendMessage', data=params)
#
#         return response